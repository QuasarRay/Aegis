# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 195. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_records.py::module::root::Module

Source: `infra/agentinfra/roadmap_records.py:1`; AST `1e09c67d9335cf491a99172e7e779fb4d11c68ad6932a47786b6614978bc25de`.

Rust module: `infra::agentinfra::roadmap_records`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Any, ContractError, KEYWORDS, KeyError, OSError, Path, TypeError, ValueError, _pairs, all, any, at, b, bad_constant, bindings, bool, bytes, canonical, condition, confined_path, dict, digest, enumerate, exc, expected, failures, file_binding, hashlib, i, int, isinstance, item, json, key, len, list, loads, message, name, option, pairs, path, properties, re, read_json, ref, relative, require, result, root, schema, schemas, set, str, text, tuple, type, types, v, validate, value, x. Outputs/bindings: KEYWORDS, b, expected, failures, i, item, key, name, option, path, properties, ref, result, root, schemas, types, v, value, x.
Calls/effect boundaries: ContractError, all, any, canonical, confined_path, digest, enumerate, failures.append, file_binding, hashlib.sha256, hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest, isinstance, json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode, json.loads, len, loads, path.is_file, path.read_bytes, path.read_text, path.relative_to, path.relative_to(root).as_posix, re.search, read_json, ref.removeprefix, ref.startswith, require, root.get, schema.get, set, str, type, validate, value.items.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:1`; AST `7f73fb6c661ff18bee763f867a5385064a797d781f494c04c0ecc994d69bba7c`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_records.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_records.py:8`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_records.py:9`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[4]::Import

Source: `infra/agentinfra/roadmap_records.py:10`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_records.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_records.py:12`; AST `68c3503c96524a291ba3f175e383b38269e898b6c29bd9965c11d7e1d2ae8ae9`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_records.py:14`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::ContractError::root.body[8]::ClassDef

Source: `infra/agentinfra/roadmap_records.py:17`; AST `20ae71d452c076a448e2abd03254a17e5d196bb532756531049d3642b96038f2`.

Rust module: `infra::agentinfra::roadmap_records`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ClassDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::ContractError::root.body[8].body[0]::Pass

Source: `infra/agentinfra/roadmap_records.py:18`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Pass evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::require::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:21`; AST `f06fd0d93ca118a7afa91469826eb8c1e01262072ae28637c1bc8e9b87feee8b`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, bool, condition, message, str. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::require::root.body[9].body[0]::If

Source: `infra/agentinfra/roadmap_records.py:22`; AST `7eeeae7604dac282df7e6c5c3a98abf8a50bed3c6994b82bc3846c9f1c20c36e`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ContractError, condition, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[9].body[0]; no call, error or mutation may be omitted. Condition: not condition
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::require::root.body[9].body[0].body[0]::Raise

Source: `infra/agentinfra/roadmap_records.py:23`; AST `af6adc52e897a2e8a94f8a9b57898f3ff891bc1661ec52b6f5436d3300880f88`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::require::root.body[9].body[0].body[0].exc::Call

Source: `infra/agentinfra/roadmap_records.py:23`; AST `31cc39de2cb7708f97fb63a897e031342373423f025a4b3beea3b38042ba6887`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::canonical::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:26`; AST `317e7b5796d970670e2511b5d8bbf22df0062ff15bf15b6f81d6a476eeeda964`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Any, bytes, json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::canonical::root.body[10].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:27`; AST `30d1f018341dfe4d5caf9c699c861252c3ac47f8d45d4b1120258e4c0b741cb5`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::canonical::root.body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:27`; AST `808fd8fbe5cdede06cb4d04d4f080989bbd214a0d0c212a6eccacd28e7b66532`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::canonical::root.body[10].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_records.py:27`; AST `b842cdeebeb356f3d512440dd4e80298d235782025de21f2edd5d2317db38128`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::digest::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:31`; AST `f5d0cf61c480ecc5a8ec7bb1256ee870891554919ea902a4b9b49d115b8604e3`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Any, bytes, canonical, hashlib, isinstance, str, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, hashlib.sha256, hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest, isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::digest::root.body[11].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:32`; AST `0e8932784bc72e3897530ed78eb99dba2939e7334d942c16a79b0d9ec860daee`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes, canonical, hashlib, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, hashlib.sha256, hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest, isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::digest::root.body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:32`; AST `c63088eef2befe37d5d79be63dedef93fe6deb9edb696379bf57952f92687001`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, canonical, hashlib, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, hashlib.sha256, hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest, isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::digest::root.body[11].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_records.py:32`; AST `65b3c461596b09c292c1147a0d3f17f74ef119fef028e6bbec013e30e6ac9b3a`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, canonical, hashlib, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, hashlib.sha256, isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::digest::root.body[11].body[0].value.func.value.args[0].test::Call

Source: `infra/agentinfra/roadmap_records.py:32`; AST `952dcdc341aac4b7e1e87d815b76208592c95357e11ef0b8e2924bfc076856be`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.func.value.args[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::digest::root.body[11].body[0].value.func.value.args[0].orelse::Call

Source: `infra/agentinfra/roadmap_records.py:32`; AST `1a07bd0abe50598ca6ed04aec23bd487f4b47a0fab4fc87670427f80c2369336`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.func.value.args[0].orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:35`; AST `f326a07977b06c839ff33d83c32de37c221964ad2a501be65de0aea93e7cada5`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Any, dict, key, list, pairs, require, result, str, tuple, value. Outputs/bindings: key, result, value.
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:36`; AST `2c435ecac12c985901bb8025f4efe5e5ad7e200542d8b36f3e0370612550a391`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12].body[1]::For

Source: `infra/agentinfra/roadmap_records.py:37`; AST `e2881152f4b3eca334122a094ddda0c2e12b6f761430af692276ec7ec149e87d`.

Rust module: `infra::agentinfra::roadmap_records`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: key, pairs, require, result, value. Outputs/bindings: key, value.
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered For evaluation at root.body[12].body[1]; no call, error or mutation may be omitted. Iteration: (key, value) in pairs
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:38`; AST `a99a8ad8ea40684cda56be1530e430e10615e17882855e701dd5f2ca7168fc38`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:38`; AST `d61186809d6dd2bdc721a6c78ffb6e0c0570cd53bd4a55b00c6742f3a9bd6798`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_records.py:39`; AST `cce37ca285c93f048b08b90881688ef99f392a137c639b91d83d4cdb72fb564d`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, result, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::_pairs::root.body[12].body[2]::Return

Source: `infra/agentinfra/roadmap_records.py:40`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:43`; AST `f8c5e5547e6cc7101c0395955b1d846e15b71c0debb17096d60622b62930f2c5`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Any, ContractError, TypeError, ValueError, _pairs, bad_constant, exc, json, str, text, value. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, json.loads, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::bad_constant::root.body[13].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:44`; AST `6ce67238b517c065dafe0dc4e50a976cd4e0487b72b6fcf2876958069fa79c0f`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, str, value. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::bad_constant::root.body[13].body[0].body[0]::Raise

Source: `infra/agentinfra/roadmap_records.py:45`; AST `3ee16c41bf88669394fa470de6cf3e3c6ca5055ea23eafb0b915e6956dd84c2c`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, value. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::bad_constant::root.body[13].body[0].body[0].exc::Call

Source: `infra/agentinfra/roadmap_records.py:45`; AST `cb12a400b0498e78314d106d8ee6ec21a6ce15f001dc10d787f09036e6213079`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, value. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1]::Try

Source: `infra/agentinfra/roadmap_records.py:46`; AST `1ed4cfbe7247d4ab5df5190f82067f4a3e7d385e866d9f64026d596da03d6682`.

Rust module: `infra::agentinfra::roadmap_records`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ContractError, TypeError, ValueError, _pairs, bad_constant, exc, json, str, text. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, json.loads, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:47`; AST `a089dc81ddbbd18d02f503572ff5ab7fe61d0bce5522056e8261eeac54b718ec`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pairs, bad_constant, json, text. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[13].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:47`; AST `60d6d1e766964d2bd0bbb51ecb6f444e2cae5b18b1ea92abbf20ea031d74ac51`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pairs, bad_constant, json, text. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_records.py:48`; AST `0f8d605b35ffc6f797162cc4e8ce270207acb217964b3c834da5405ffff8a57e`.

Rust module: `infra::agentinfra::roadmap_records`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ContractError, TypeError, ValueError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[13].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1].handlers[0].body[0]::Raise

Source: `infra/agentinfra/roadmap_records.py:49`; AST `991709735578a78161b84218a93cc8c1572e00c88cc02885b9c542a7371adcfd`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/roadmap_records.py:49`; AST `67d88c9b2c638c8f4825def61dc2340420bd9582ba29453c0b0a40df88f8bb4c`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::loads::root.body[13].body[1].handlers[0].body[0].exc.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:49`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].handlers[0].body[0].exc.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::read_json::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:52`; AST `3d1da0559cebf622c1bafc5ac550d4c8f41bde7bf189a7f0fa42b5a6ef142e60`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Any, Path, loads, path. Outputs/bindings: (none).
Calls/effect boundaries: loads, path.read_text.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::read_json::root.body[14].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:53`; AST `b073c7bb6447f5cc6def50dbb6ae2dd14e506d27c66daac6d05e38429a476385`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, path. Outputs/bindings: (none).
Calls/effect boundaries: loads, path.read_text.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::read_json::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:53`; AST `694753b0636ccfa94fc5021ea0e201b720d225d3a26371bdf80dfcfbed364e58`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, path. Outputs/bindings: (none).
Calls/effect boundaries: loads, path.read_text.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::read_json::root.body[14].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:53`; AST `d7d2b1d3f5b3313cd24906b00f77863075a83ccc502a11ff12b073fd43d10854`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::root.body[15]::Assign

Source: `infra/agentinfra/roadmap_records.py:56`; AST `b2020d9b1196238883a0f0d973ca12c93ca996e0e7df240782ccd9cfb4c6366b`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: KEYWORDS.
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:62`; AST `c495db17e07ed43a4b6c6a97d1afda20ab382657d59b553ef04036e4d88a0802`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Any, ContractError, KEYWORDS, any, at, bool, canonical, dict, enumerate, exc, expected, failures, i, int, isinstance, item, key, len, list, name, option, properties, re, ref, require, root, schema, set, str, type, types, v, validate, value, x. Outputs/bindings: expected, failures, i, item, key, name, option, properties, ref, root, types, v, x.
Calls/effect boundaries: ContractError, any, canonical, enumerate, failures.append, isinstance, len, re.search, ref.removeprefix, ref.startswith, require, root.get, schema.get, set, str, type, validate, value.items.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:63`; AST `4978d8338113c25fd58fdc22e511044a72236d7f45bca73e6e07adda1af67d62`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, schema. Outputs/bindings: root.
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:64`; AST `082468e30a83408db1b2c216baab505d45df6bd237f0b945bf398ab78ba03859`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, dict, isinstance, require, schema. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:64`; AST `9361945f22592fe50a53727b041d0f0d583c4b9ba4713e9bbf56c36812bc5c82`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, dict, isinstance, require, schema. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:64`; AST `04e64341579f7fca914b718d486fcf5fc891c39bd528362ab24831c79013f26f`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, schema. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[2]::Expr

Source: `infra/agentinfra/roadmap_records.py:65`; AST `f06d431c8c4323eac7fce2470820f58f70960c40fec300a87389755d09a3be7f`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: KEYWORDS, at, require, schema, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[2].value::Call

Source: `infra/agentinfra/roadmap_records.py:65`; AST `7221d47fe5135897632069995f3f489db4bc9948986f5b13e309a1c902283747`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: KEYWORDS, at, require, schema, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[2].value.args[0].operand.left::Call

Source: `infra/agentinfra/roadmap_records.py:65`; AST `2d5d33452a2343dcf62f2dcf8a264edd4845200678e47e005aa0c13516fa9b65`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.args[0].operand.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[2].value.args[1].values[2].value.left::Call

Source: `infra/agentinfra/roadmap_records.py:65`; AST `2d5d33452a2343dcf62f2dcf8a264edd4845200678e47e005aa0c13516fa9b65`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.args[1].values[2].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3]::If

Source: `infra/agentinfra/roadmap_records.py:66`; AST `19c21fbfc9bb14352d167d26f8985298ec4f1ca39a206d3b6a416a0b6ef68b5d`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, isinstance, name, ref, require, root, schema, str, validate, value. Outputs/bindings: name, ref.
Calls/effect boundaries: isinstance, ref.removeprefix, ref.startswith, require, root.get, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[3]; no call, error or mutation may be omitted. Condition: '$ref' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:67`; AST `e45b33a2f1b00df89f6d38de9faf11acc044b5fc5cf21bb6b6c9bb483c892601`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: schema. Outputs/bindings: ref.
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:68`; AST `f3016ebf74493cdecc4f3f70d08d4f20d717d3a1a0b92cd13ed664061ae0745c`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, ref, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, ref.startswith, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:68`; AST `bf1fdff882b87f449f49fca344079133035eae8533e9a2a3450ca0b43353d4c7`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, ref, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, ref.startswith, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[1].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_records.py:68`; AST `3909f8a7b1dd6dad6752a94692f2f6ca0f8a5e181c67500bce83c87900bee78f`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, ref, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[1].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_records.py:68`; AST `91c3afd5a3a2544386562f413f9317423a2ca1a29794a7d95bf6008558107a9a`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ref. Outputs/bindings: (none).
Calls/effect boundaries: ref.startswith.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[2]::Assign

Source: `infra/agentinfra/roadmap_records.py:69`; AST `27538122cdd188c4796898c9712b7ea8d5453de11bcdae74a7d4b3b5e80854a0`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ref. Outputs/bindings: name.
Calls/effect boundaries: ref.removeprefix.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_records.py:69`; AST `1d4a5722e288c13cf65df4a38f80b0d20e063377a43adcc2fc3797e7f1859760`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ref. Outputs/bindings: (none).
Calls/effect boundaries: ref.removeprefix.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_records.py:70`; AST `207363dc736b7eb69894ef5db2261360ffd226382adaf9db4afe4e1aa76138fb`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, require, root. Outputs/bindings: (none).
Calls/effect boundaries: require, root.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_records.py:70`; AST `8460fefbc55a4a51f365234dfde87b7590ead5fafbba863e952f7df694d4dbea`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, require, root. Outputs/bindings: (none).
Calls/effect boundaries: require, root.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[3].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:70`; AST `542cc5f0d55a3924daab5c7b343e784eda3cb364016946eaf44ac1d19aa653f2`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_records.py:71`; AST `bbb478234393e15f8cbeb3046732fc62630db1a46541c0c555dcf6b0ab7e8add`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, name, root, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_records.py:71`; AST `de5fe85361c51f5d6416a3e33dbfdfb60434f0de67796d065d6361fa726d431d`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, name, root, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4]::If

Source: `infra/agentinfra/roadmap_records.py:72`; AST `4e6de8a773859fab1aff559e33abd7bd1898bac65902bbba58d806b0a5fcbf15`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ContractError, at, exc, failures, option, root, schema, str, validate, value. Outputs/bindings: failures, option.
Calls/effect boundaries: ContractError, failures.append, str, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[4]; no call, error or mutation may be omitted. Condition: 'anyOf' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:73`; AST `514ee02ae8a4214aa03f091ddbf949fab064cf09c6dd4c9dba9c189341586579`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: failures.
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1]::For

Source: `infra/agentinfra/roadmap_records.py:74`; AST `e959fc1410f444487ffafbccb3f07707d35c12c10b24f9aec1e21635698dd034`.

Rust module: `infra::agentinfra::roadmap_records`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, at, exc, failures, option, root, schema, str, validate, value. Outputs/bindings: option.
Calls/effect boundaries: ContractError, failures.append, str, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered For evaluation at root.body[16].body[4].body[1]; no call, error or mutation may be omitted. Iteration: option in schema['anyOf']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0]::Try

Source: `infra/agentinfra/roadmap_records.py:75`; AST `31fcf1b4c238cc8386b2a6f5255abe363bce30003534735b163f1d43d7f48014`.

Rust module: `infra::agentinfra::roadmap_records`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ContractError, at, exc, failures, option, root, str, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: failures.append, str, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[16].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:76`; AST `8ed256f4e92be34f1f2e206e437daa6f0b20f8e34dd9b141397406a9aa28a1f1`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, option, root, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:76`; AST `ed187d6b2744feca82fd9aae155b9a2fa17d9cd1f02114a2de46076c80e5c02e`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, option, root, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].body[1]::Break

Source: `infra/agentinfra/roadmap_records.py:77`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Break evaluation at root.body[16].body[4].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_records.py:78`; AST `aa1a144b914f4fad5c0e6b8bb86014e1d73ec06ca66ca9a91a2ed9f7ea679cff`.

Rust module: `infra::agentinfra::roadmap_records`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ContractError, exc, failures, str. Outputs/bindings: (none).
Calls/effect boundaries: failures.append, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[4].body[1].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:79`; AST `f848e50500f05c48fa430d3098ad2fb4af23c54902eb4a284892843bd3f3a64f`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, failures, str. Outputs/bindings: (none).
Calls/effect boundaries: failures.append, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:79`; AST `c8765da3ee4538fce8fb48f50bd3f444cd33e4ad15c98c63242fb1c200b25426`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, failures, str. Outputs/bindings: (none).
Calls/effect boundaries: failures.append, str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[0].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].body[0].handlers[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:79`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[0].handlers[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].orelse[0]::Raise

Source: `infra/agentinfra/roadmap_records.py:81`; AST `a34636308210369f837bd3c573cd2d41087cec5733fe4549de847be063c7e45a`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, at, failures. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[4].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[4].body[1].orelse[0].exc::Call

Source: `infra/agentinfra/roadmap_records.py:81`; AST `a6857a8148160c2307c237aaeefae06430db39f412f2601020451bf99e403fba`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, at, failures. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].orelse[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[5]::Assign

Source: `infra/agentinfra/roadmap_records.py:82`; AST `55b434f02d5cb5bd43950c367ab083df96f2a2f6291db2447c358be389dbc11e`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, dict, int, list, str, type. Outputs/bindings: types.
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[5].value.values[5]::Call

Source: `infra/agentinfra/roadmap_records.py:83`; AST `79991ae1422a386a1c2f607dfc175991cd30f3a6ee055324902f6efd004a81bb`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6]::If

Source: `infra/agentinfra/roadmap_records.py:84`; AST `2c36f1a7bff9fd599430d62390cdb0d5d3cd84e268d32ab1ab9995986e0632e4`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, expected, require, schema, type, types, value. Outputs/bindings: expected.
Calls/effect boundaries: require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[6]; no call, error or mutation may be omitted. Condition: 'type' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:85`; AST `ce36e51c0f2d179c54270a4a646cff64350bffc773013b47769e587343fb8630`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: schema. Outputs/bindings: expected.
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:86`; AST `1a415fc23466c0e629aa9fc7aedaf0733ef97ccc9bc12490fcdec7877f397c62`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, require, types. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:86`; AST `d3a3fbcf4eb2a2a7c9948908d626ba0850234a861bcec6a06c3ecadf5dda9950`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, require, types. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6].body[2]::Expr

Source: `infra/agentinfra/roadmap_records.py:87`; AST `a415ca62dd12f05a10672062cec53ea1fd18f5c544862d0df1929f76c2752e67`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, expected, require, type, types, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_records.py:87`; AST `12751ec3308a4df2ec786c3f0c58c891e0691a52b567c6bdfa7112e32f7d54cc`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, expected, require, type, types, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[6].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:87`; AST `a17a6931ac954db8619d8e0a6240ead3e757fcdb6647e625e925b7f462437b71`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, value. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[7]::If

Source: `infra/agentinfra/roadmap_records.py:88`; AST `035b8b5e3b0ee576a861dd3f085cdb72618e996a0cdd9f254cdffc10c01b64d2`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, require, schema, type, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[7]; no call, error or mutation may be omitted. Condition: 'const' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:89`; AST `0717cacddd515e7a44421de1862c553e0ba2c2c437e24586914474b6abc12b40`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, require, schema, type, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:89`; AST `a3b3029fefea8e6cb5ef6507eee69aab60432495d2e534eac9f71e3bcacce984`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, require, schema, type, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[7].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:89`; AST `a17a6931ac954db8619d8e0a6240ead3e757fcdb6647e625e925b7f462437b71`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, value. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[7].body[0].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:89`; AST `3fc7e8b18fb43fe1eec36129fc651cc079a41ca2f343e0f738eb21e64c2f1130`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8]::If

Source: `infra/agentinfra/roadmap_records.py:90`; AST `0a0c8d17c6b613e141ff040060e608fb474f7b0200cec7ae3e91b69412817c6a`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, at, require, schema, type, v, value. Outputs/bindings: v.
Calls/effect boundaries: any, require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[8]; no call, error or mutation may be omitted. Condition: 'enum' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:91`; AST `7156cc17a07aa6def24b7c29d6a5759f488772b104767856ff01ba0848c70b3a`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, at, require, schema, type, v, value. Outputs/bindings: v.
Calls/effect boundaries: any, require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:91`; AST `8f6e9285588563139a83a86289e204c88a3f5b0bb5de10c92432bb528c4d52ac`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, at, require, schema, type, v, value. Outputs/bindings: v.
Calls/effect boundaries: any, require, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:91`; AST `319744c102d7bed95a8f499cb93edeb46c1eabacfba3124e2e5c90a061e378ae`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, schema, type, v, value. Outputs/bindings: v.
Calls/effect boundaries: any, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8].body[0].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_records.py:91`; AST `dc1949c234d8a411048134e7f40e2931ee76d6b667cc73635032465a3c917d88`.

Rust module: `infra::agentinfra::roadmap_records`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: schema, type, v, value. Outputs/bindings: v.
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[16].body[8].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8].body[0].value.args[0].args[0].elt.values[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:91`; AST `a17a6931ac954db8619d8e0a6240ead3e757fcdb6647e625e925b7f462437b71`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, value. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[0].value.args[0].args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[8].body[0].value.args[0].args[0].elt.values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:91`; AST `e048786d0fd27242ac9513214da043edf756617a572829e1cb9725342ed3dd2b`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, v. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[0].value.args[0].args[0].elt.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9]::If

Source: `infra/agentinfra/roadmap_records.py:92`; AST `4c760fc6a151dd0abf11a5b0ab1273d515ac5844efae42e6f5d2d83af8377675`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ContractError, at, dict, isinstance, item, key, properties, require, root, schema, set, validate, value. Outputs/bindings: item, key, properties.
Calls/effect boundaries: ContractError, isinstance, require, schema.get, set, validate, value.items.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[9]; no call, error or mutation may be omitted. Condition: isinstance(value, dict)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].test::Call

Source: `infra/agentinfra/roadmap_records.py:92`; AST `a0df6caeebecae97cf305403969f3b48f16842ceba977c5f53441f25fd65637d`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:93`; AST `b944613f9fb47e6ebcbfde455ab3de35ba63e6204869f4d22d29e5004671f690`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: schema. Outputs/bindings: properties.
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:93`; AST `6d34cf7c372e308ffb42f5416cd6c3649094be00db310b8dca6c0ffedfbf7e35`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:94`; AST `b7ce90847cd89e50b462273b8cf68e3feb100aefa5f9d4810c62ffbcba07da08`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, require, schema, set, value. Outputs/bindings: (none).
Calls/effect boundaries: require, schema.get, set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:94`; AST `bdbb90546c5797528fe819abc7fc5439cac1eb246df7d44792f1b7825afdcac2`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, require, schema, set, value. Outputs/bindings: (none).
Calls/effect boundaries: require, schema.get, set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[1].value.args[0].operand.left::Call

Source: `infra/agentinfra/roadmap_records.py:94`; AST `84c7042027f65761126b124b04117a2a1b4aa1db1df8430caee017b81de4573d`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, set. Outputs/bindings: (none).
Calls/effect boundaries: schema.get, set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.args[0].operand.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[1].value.args[0].operand.left.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:94`; AST `d6f522e385b4175a192efaecf02aff0172d00cb5f11d416b80f6378d8fe8d2fe`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.args[0].operand.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[1].value.args[0].operand.right::Call

Source: `infra/agentinfra/roadmap_records.py:94`; AST `12efbf9fce61bc80e437c8e389d41cc76d03d0f1e31821a06fb8182388df6c99`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, value. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.args[0].operand.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2]::For

Source: `infra/agentinfra/roadmap_records.py:95`; AST `8f5b8219c1372b9af876e298acd92f4f0d8d31ddaa5b778c0aa4579b4ba8348d`.

Rust module: `infra::agentinfra::roadmap_records`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, at, dict, isinstance, item, key, properties, root, schema, validate, value. Outputs/bindings: item, key.
Calls/effect boundaries: ContractError, isinstance, schema.get, validate, value.items.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered For evaluation at root.body[16].body[9].body[2]; no call, error or mutation may be omitted. Iteration: (key, item) in value.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].iter::Call

Source: `infra/agentinfra/roadmap_records.py:95`; AST `4362ffa40c28dd58aa5a3210414f80f1c71cbc012fa66ab87790098fcb0edb14`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value.items.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_records.py:96`; AST `29c34290634811f1814caa650875ffc0e614bb613e8b8d8dcb6666bf1c2025bb`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ContractError, at, dict, isinstance, item, key, properties, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, isinstance, schema.get, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[9].body[2].body[0]; no call, error or mutation may be omitted. Condition: key in properties
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:97`; AST `60fac974437ed0612bd8501baa130eb5f5de04e5cd14fa2b822be5c2ec262483`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, item, key, properties, root, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:97`; AST `21fdf7ee37799c6eb0be43195b4eae50582a63c81739758087bcd4734362f737`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, item, key, properties, root, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_records.py:98`; AST `63921a4366703f747dc3abc64a03c364b6efdc1d0d56e080eccfa3fa1d882661`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ContractError, at, dict, isinstance, item, key, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, isinstance, schema.get, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[9].body[2].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: schema.get('additionalProperties') is False
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].test.left::Call

Source: `infra/agentinfra/roadmap_records.py:98`; AST `238cf6f96b4d240887e7a4b0a01656016ead83b5563476ef0ca3e41463e85b72`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].orelse[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].body[0]::Raise

Source: `infra/agentinfra/roadmap_records.py:99`; AST `7d379b0633d7e3be5d9fd9b6249828cfc61e6e76158422dca97ead8032751b95`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, at, key. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[9].body[2].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].body[0].exc::Call

Source: `infra/agentinfra/roadmap_records.py:99`; AST `eda1f80fca6da71a8162f81bd78a8df9f801fd7bbfe1d4aa4ff7528ca2f089b5`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, at, key. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].orelse[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_records.py:100`; AST `0ed684a4447cb4e74e0b88e2b76036a9fc2626535f2707b33c0df5730729ae9f`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, dict, isinstance, item, key, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, schema.get, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[9].body[2].body[0].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(schema.get('additionalProperties'), dict)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_records.py:100`; AST `83774711204c56e8135b51a5c9719a0538ffe31025148eab2b91a3e1fc0df601`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, schema. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].test.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:100`; AST `238cf6f96b4d240887e7a4b0a01656016ead83b5563476ef0ca3e41463e85b72`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:101`; AST `0a6af7a8df2017cca2289373b5b16e274305c0d5fe1d8e91c88fcb22a1f8d7b0`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, item, key, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:101`; AST `2c20c46710326e34fa08f65ecfe74d35c76c9c15026c14eb510effd64a419b87`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, item, key, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10]::If

Source: `infra/agentinfra/roadmap_records.py:102`; AST `7ccf741453d9058356cc8d82a5f39a3dd1482d4717ca5e991d906574a210a8ae`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, canonical, enumerate, i, isinstance, item, len, list, require, root, schema, validate, value, x. Outputs/bindings: i, item, x.
Calls/effect boundaries: canonical, enumerate, isinstance, len, require, schema.get, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[10]; no call, error or mutation may be omitted. Condition: isinstance(value, list)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].test::Call

Source: `infra/agentinfra/roadmap_records.py:102`; AST `f5635b2e334fb6e97f358f32dbb2b0086496303066699278ebd49fcf85562492`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:103`; AST `02ee47522d49858ed1877393164313bab46fa9db166f37700d4d4982708b7ebf`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, len, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:103`; AST `f67a7e2d463f0c1ea33ec62f048379e3a7f8191c575b1df31d23ee8ce3b02b72`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, len, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:103`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:103`; AST `b85864c5ccdd056ed7bef3980365e1e79f9bed825844e698678c51068e73e956`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1]::If

Source: `infra/agentinfra/roadmap_records.py:104`; AST `4b482512e8ccc6a7908c0194e4febb5c91a570e63a0dc6bb7f30c7c6b7275b86`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, canonical, len, require, schema, value, x. Outputs/bindings: x.
Calls/effect boundaries: canonical, len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[10].body[1]; no call, error or mutation may be omitted. Condition: schema.get('uniqueItems')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].test::Call

Source: `infra/agentinfra/roadmap_records.py:104`; AST `e4fd400a8d7758791ff2487a93a8941e74fa3aba67492ae651d918e5816aa8a1`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:105`; AST `bd091d7768a5b0b025a353caed7307ec4ebb69f6cbb31581e971e28e6c67754b`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, canonical, len, require, value, x. Outputs/bindings: x.
Calls/effect boundaries: canonical, len, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:105`; AST `940e4a50e25980c0919d9e2184467c902290c142e6c07a35b3ddae2f2ccb7ea4`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, canonical, len, require, value, x. Outputs/bindings: x.
Calls/effect boundaries: canonical, len, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:105`; AST `5682f77c8331b3233a1274664bede592e739491851048275765ab1c588cca7c3`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, value, x. Outputs/bindings: x.
Calls/effect boundaries: canonical, len.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].body[0].value.args[0].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_records.py:105`; AST `9d1190061356bf7ff49da0a52b7a38e044330d2af591248a2e58c2d82d4d3431`.

Rust module: `infra::agentinfra::roadmap_records`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: canonical, value, x. Outputs/bindings: x.
Calls/effect boundaries: canonical.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered SetComp evaluation at root.body[16].body[10].body[1].body[0].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].body[0].value.args[0].left.args[0].elt::Call

Source: `infra/agentinfra/roadmap_records.py:105`; AST `c7e9b54c25c23ab421855a3ed4bb8e19e18b6bc390f3236b960e414adf8c6b75`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, x. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].body[0].value.args[0].left.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[1].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:105`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[2]::For

Source: `infra/agentinfra/roadmap_records.py:106`; AST `1ce52649e32938884e5f3f5dd5d4e5e92a4e50770d5036082506af2346282014`.

Rust module: `infra::agentinfra::roadmap_records`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: at, enumerate, i, item, root, schema, validate, value. Outputs/bindings: i, item.
Calls/effect boundaries: enumerate, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered For evaluation at root.body[16].body[10].body[2]; no call, error or mutation may be omitted. Iteration: (i, item) in enumerate(value)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[2].iter::Call

Source: `infra/agentinfra/roadmap_records.py:106`; AST `7319a75af29aa16ce29cee5b47f4824c2eea50c99daf127db96a63b65622d4e7`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, value. Outputs/bindings: (none).
Calls/effect boundaries: enumerate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_records.py:107`; AST `e16b4038faf34d36bb5d7880fd2995df088fc68e521606256350487196746471`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, i, item, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[10].body[2].body[0]; no call, error or mutation may be omitted. Condition: 'items' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:108`; AST `0c230cf18e29b51ccf362798f05c0ee8fc0f2b08d438e9f8ee46526ebe511e52`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, i, item, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[10].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:108`; AST `55948b95a944a5671cdcd4303cde66bfc402144afed84731c53698da806cede1`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, i, item, root, schema, validate. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11]::If

Source: `infra/agentinfra/roadmap_records.py:109`; AST `5c2641d5d97f31eae819527cef751ffd98c28a257db6bd86f2dcc52cf2b33a58`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, isinstance, len, re, require, schema, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, re.search, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[11]; no call, error or mutation may be omitted. Condition: isinstance(value, str)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].test::Call

Source: `infra/agentinfra/roadmap_records.py:109`; AST `f0937843eac35cb846ed896776839197deebad579475d870c722a45446739540`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:110`; AST `5364b66b2739a9ce46cfc5ceb7241d491a79c9724cda26eb6f963d17e06737c9`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, len, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:110`; AST `0473600b78efea82f393817e9b4a6911a462a52808f7540898b02d9bf629748c`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, len, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:110`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:110`; AST `c477999af935b85f4f1f887b14a04b2b7ead45f7efd11cea989cea57fb497b88`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:111`; AST `fc192be0d1bb9d5125a007d9fb8f24682b31b7337a4d1a0a9a6315a38bf104dc`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, len, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:111`; AST `72549d454d6dff20d0a33cea50e03031caf74cb6d7ea674b8f137ed42ac612bc`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, len, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:111`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[1].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_records.py:111`; AST `d554a5c771cb372cf40536652ed47b183da19f8707787cf456df11b7af6ab3cd`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: len, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[1].value.args[0].comparators[0].args[1]::Call

Source: `infra/agentinfra/roadmap_records.py:111`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].value.args[0].comparators[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[2]::If

Source: `infra/agentinfra/roadmap_records.py:112`; AST `2d8dc5995cd7c57f8b5f873b145b2d5cc525ea933d3fee200265e0cfeae13c68`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, re, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[11].body[2]; no call, error or mutation may be omitted. Condition: 'pattern' in schema
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:113`; AST `33dd8ebe6d94b19fec5df3953a0f7c9c2ebb94fa088d64cd16577b7def02e4f0`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, re, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:113`; AST `84405121338180280c560b9b5e62ad0fe61dc6afc3659b4f3f522c4aa6055738`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, re, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[11].body[2].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:113`; AST `27b806a97500fdfa2237d049efb4141dbe7ba7b7ce11a419a89d518d5d6c669d`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[2].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[12]::If

Source: `infra/agentinfra/roadmap_records.py:114`; AST `dda6b865008f0d54903b7b95a08e4173edacaabf342bea03bfdf7f9598811727`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: at, int, require, schema, type, value. Outputs/bindings: (none).
Calls/effect boundaries: require, schema.get, type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[12]; no call, error or mutation may be omitted. Condition: type(value) is int
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[12].test.left::Call

Source: `infra/agentinfra/roadmap_records.py:114`; AST `a17a6931ac954db8619d8e0a6240ead3e757fcdb6647e625e925b7f462437b71`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, value. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_records.py:115`; AST `c7dfe54dcc400415b3e853bfed1d21b06bf93ed9a6302f61fd2e78d0d0a18187`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: at, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:115`; AST `fc520f997839fd31b031887dd6e4597d6b153bc1652c2df31ff3a4d03d8ca2a2`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: at, require, schema, value. Outputs/bindings: (none).
Calls/effect boundaries: require, schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[12].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_records.py:115`; AST `e4931cfc61d6afbadfe622b87bffbf9b260e8ceee4cab01c479ca18e59835410`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, value. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate::root.body[16].body[12].body[0].value.args[0].comparators[1]::Call

Source: `infra/agentinfra/roadmap_records.py:115`; AST `c2e3d246160de646723fabb7fcb12ecd4be4593d5bf60e48ae10ba8ccf9b77e4`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, value. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[0].value.args[0].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:118`; AST `96c9d66eebbb893c2ddc31f67514cd3b8d3b65416fa024d6b48f1338b79307ad`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, dict, name, read_json, require, root, schemas, str, validate, value. Outputs/bindings: schemas.
Calls/effect boundaries: read_json, require, validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:119`; AST `d6465099cc576dac85b719d3ce35820be321a1bcc685887a2cfa879cbd4bd0ec`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: schemas.
Calls/effect boundaries: read_json.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:119`; AST `6f2c55d17b7369e826d8713c0fc8e4bbc3af424cc3167b3e99b60e706f713cd5`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:120`; AST `80233a6835f4dccb7521e7c193065eaf735734049777417fb39acc64a8a527d4`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, require, schemas. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:120`; AST `6a3eda45ecb10a134631d01a335904367d925244a765c0bd7d972a41d1ab4eeb`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, require, schemas. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17].body[2]::Expr

Source: `infra/agentinfra/roadmap_records.py:121`; AST `a5f0d6c2155c640e8ab16417e90760e38f2240257352745dd68c13fd53701f3c`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, schemas, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::validate_record::root.body[17].body[2].value::Call

Source: `infra/agentinfra/roadmap_records.py:121`; AST `d2dff941d6b7ebd518330528464deef8a0483dd90612e7131065be1973f23f80`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, schemas, validate, value. Outputs/bindings: (none).
Calls/effect boundaries: validate.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:124`; AST `03ecfaa44198c19f438054618d5a14a4e0d19597ae1e1a13f3c473be41779f03`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, confined_path, dict, digest, path, relative, require, root, str. Outputs/bindings: path.
Calls/effect boundaries: confined_path, digest, path.is_file, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_records.py:125`; AST `e46824fd830d49aa0997b5da19da993dd7e9cb85a0ba53ccab360b6a9a0037b9`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:125`; AST `63c9acf4cfde20a50eacc658154bbb4ec3954f19236b82666a93c852e8d25e5a`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[1]::Expr

Source: `infra/agentinfra/roadmap_records.py:126`; AST `12ca069f3f270e6b797142c38d232b45ef73834c631131ef55d2f5e78f2439a7`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[1].value::Call

Source: `infra/agentinfra/roadmap_records.py:126`; AST `7b41db3b1aad76b077ec7906720848adfdc5e48c6f667d339b66181f641fd517`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file, require.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:126`; AST `d2081c59f0765455ac12b468dbfc8371bdf81a7d49d474e10d779496c1e121ac`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[2]::Return

Source: `infra/agentinfra/roadmap_records.py:127`; AST `8b9ab4c075ebcfbc3d5af796cd426b75a59f4b5dfc47bfe090364bcdc9e57e63`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, path, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[2].value.values[0]::Call

Source: `infra/agentinfra/roadmap_records.py:127`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[2].value.values[0].func.value::Call

Source: `infra/agentinfra/roadmap_records.py:127`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[2].value.values[1]::Call

Source: `infra/agentinfra/roadmap_records.py:127`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::file_binding::root.body[18].body[2].value.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_records.py:127`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19]::FunctionDef

Source: `infra/agentinfra/roadmap_records.py:130`; AST `aceeae3fe5e195567f8e9d6560f95e9080c8c426a5d2295666a7f1eaf3ffb5e9`.

Rust module: `infra::agentinfra::roadmap_records`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: KeyError, OSError, Path, ValueError, all, b, bindings, bool, dict, file_binding, list, root. Outputs/bindings: b.
Calls/effect boundaries: all, file_binding.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[0]::If

Source: `infra/agentinfra/roadmap_records.py:131`; AST `971699970f6f6af17862e6b5a1fde86576751dc9f258060fd74b5fe4e9ea1664`.

Rust module: `infra::agentinfra::roadmap_records`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bindings. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[0]; no call, error or mutation may be omitted. Condition: not bindings
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:132`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1]::Try

Source: `infra/agentinfra/roadmap_records.py:133`; AST `b088c3888802fe436c4de2bcb911f6405b32b99f1e4544d4959861c51dfbdaed`.

Rust module: `infra::agentinfra::roadmap_records`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, ValueError, all, b, bindings, file_binding, root. Outputs/bindings: b.
Calls/effect boundaries: all, file_binding.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:134`; AST `2f8d72431985ee26c342a992c2ad43a9338087c09892c8fdc171ee1342c83b93`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, b, bindings, file_binding, root. Outputs/bindings: b.
Calls/effect boundaries: all, file_binding.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_records.py:134`; AST `276fb8f27b663feb3d7311585d15434b435668dad40c0942ddef2714abfb5ea5`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, b, bindings, file_binding, root. Outputs/bindings: b.
Calls/effect boundaries: all, file_binding.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_records.py:134`; AST `d2ad5d4f10f7ccce90cff873307f0a021de78cdebd5320d116687e546b4e7384`.

Rust module: `infra::agentinfra::roadmap_records`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: b, bindings, file_binding, root. Outputs/bindings: b.
Calls/effect boundaries: file_binding.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[19].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1].body[0].value.args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_records.py:134`; AST `4cfc6678b50dce638ff1529d2624af626563fda6a1a0d081f58b7e45088eba6f`.

Rust module: `infra::agentinfra::roadmap_records`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[0].value.args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_records.py:135`; AST `38325b7f039539ac562884357d9d5cb801c7bcef921f6358d40703e278a591be`.

Rust module: `infra::agentinfra::roadmap_records`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: KeyError, OSError, ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[19].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_records.py::module::bindings_current::root.body[19].body[1].handlers[0].body[0]::Return

Source: `infra/agentinfra/roadmap_records.py:136`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_records`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, hashlib, json, pathlib, re, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
