# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 495. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/formal.py::module::root::Module

Source: `infra/agentinfra/formal.py:1`; AST `1576ae07809831a6ca4fd0f1074590361141a1c231207eb9f4a87d120af3adcc`.

Rust module: `infra::agentinfra::formal`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AUTHORITY, FRAMEWORK, FileLock, IDENT, KeyError, Namespace, OSError, Path, RUST_PATH, RuntimeError, SimpleNamespace, ValueError, __file__, a, active, all, any, args, assertion_locations, assurance, atomic_write_json, audit, binding, binding_key, blocker, blockers, bool, c, cases, classified, command, confined_path, contract, current_identity, current_receipt, data, dict, digest, entries, exact_keys, exc, expected, field, fields, found, framework_identity, identity, ids, int, isinstance, k, kani_properties, key, label, len, list, load_json, location, lock, manifest, name, o, obj, obligations, observation, optional, original_ids, p, path, paths, permitted, pointer, profile, proof, proof_identity, proof_key, proof_output, properties, property_location, property_name, props, prose, qualified_index, r, re, read, receipt, record, relative_path, require, result, reuse, root, rows, run_args, run_check, scope, seal, set, sha, sorted, source, source_snapshot, state_path, status, str, type, unseal, validate_plan, value, w, witness, witnesses. Outputs/bindings: AUTHORITY, FRAMEWORK, IDENT, RUST_PATH, a, assertion_locations, assurance, binding, blocker, blockers, c, cases, command, contract, data, entries, expected, field, found, identity, ids, k, key, location, lock, manifest, name, o, obligations, observation, optional, original_ids, p, path, paths, permitted, pointer, proof, proof_key, properties, props, r, receipt, record, result, reuse, rows, run_args, scope, sha, source, status, w, witness, witnesses.
Calls/effect boundaries: ' '.join, (FRAMEWORK / 'infra/agentinfra').glob, (record or {}).get, (record or {}).get('result', {}).get, AUTHORITY.read_bytes, FileLock, IDENT.fullmatch, Namespace, Path, Path(__file__).resolve, RUST_PATH.fullmatch, SimpleNamespace, active, all, any, assertion_locations.values, atomic_write_json, audit, blocker.startswith, blockers.append, bool, classified, confined_path, confined_path(root, manifest, must_exist=True).is_file, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, current_identity, current_receipt, data.pop, digest, entries.add, exact_keys, fields.split, framework_identity, ids.add, isinstance, kani_properties, len, load_json, lock.acquire, lock.release, o.get, o.get('evidence', {}).get, p.is_file, p.read_bytes, p.relative_to, p.relative_to(FRAMEWORK).as_posix, path.exists, path.read_bytes, path.read_text, path.relative_to, path.relative_to(root).as_posix, path.stat, paths.add, paths.append, paths.extend, pointer.get, proof_identity, proof_output, property_location, property_name, prose, qualified_index, re.compile, re.fullmatch, re.search, read, record.get, relative_path, require, result.get, rows.append, rows.extend, run_check, seal, set, sorted, source_snapshot, state_path, state_path(root, 'bindings').glob, str, type, unseal, validate_plan, value.strip, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[0]::Expr

Source: `infra/agentinfra/formal.py:1`; AST `d18ffceb4111f7596ceafaaf3e3d008d4867929245e1564a4191d010549fb774`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/formal.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/formal.py:8`; AST `b7d6bcdca8b664f6f9b11b53c3698446d9319e67139aff16db27b97fbdc0b6da`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/formal.py:9`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[4]::Import

Source: `infra/agentinfra/formal.py:10`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/formal.py:12`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/formal.py:13`; AST `1ed49ab5c99843fd698d802edccf90035469b9b5209ce77d25214cda45479c4b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/formal.py:14`; AST `f49eec2be7586a81b0fa34570d7cbaa58bc5eeaa5e471a05fac611f36b0ee7bd`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/formal.py:15`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[9]::Assign

Source: `infra/agentinfra/formal.py:17`; AST `97bf173db25f481e4314056dd3ee1eb26446998cbaa1e3bd9eff18be6583a592`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: FRAMEWORK.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[9].value.value.value::Call

Source: `infra/agentinfra/formal.py:17`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[9].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[9].value.value.value.func.value::Call

Source: `infra/agentinfra/formal.py:17`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[9].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[10]::Assign

Source: `infra/agentinfra/formal.py:18`; AST `75dae1949954255ed773f2a277cfb8920c3c37a9ca7fd8ac60082e4361fa66ce`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FRAMEWORK. Outputs/bindings: AUTHORITY.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[11]::Assign

Source: `infra/agentinfra/formal.py:19`; AST `5fa52efe580feec14ccf6a1ce44ad331103edeca3e3f74cb5591184d1fdb1390`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re. Outputs/bindings: IDENT.
Calls/effect boundaries: re.compile.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[11].value::Call

Source: `infra/agentinfra/formal.py:19`; AST `27c29ecbafe85ef988e57409ad353f136dc3784299e3cbb8fcf0506aaab6a6b0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[12]::Assign

Source: `infra/agentinfra/formal.py:20`; AST `5c00dd3bdc428c90198519f45b4c5c9e93ace9fe1f59132791a4142a40c0ecab`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re. Outputs/bindings: RUST_PATH.
Calls/effect boundaries: re.compile.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::root.body[12].value::Call

Source: `infra/agentinfra/formal.py:20`; AST `9898da04470e750742f695c411f2d001dda7117960e879bc807040b6314d10df`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13]::FunctionDef

Source: `infra/agentinfra/formal.py:23`; AST `93391b75caae7d7ae5c469d204186d1d148430e094a2de9ebc3a1f27bd4698ea`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: load_json, path, require. Outputs/bindings: (none).
Calls/effect boundaries: load_json, path.read_text, path.stat, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13].body[0]::Expr

Source: `infra/agentinfra/formal.py:25`; AST `fd91f05f5dcb26a10591276e67fc7c5a30ab0b9ec17ad30308fc305e7ded2875`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13].body[0].value::Call

Source: `infra/agentinfra/formal.py:25`; AST `68ac89ed076faaffe0e53fd397e59feb93793c651848f938bd2c5bb6adc433e8`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13].body[0].value.args[0].left.value::Call

Source: `infra/agentinfra/formal.py:25`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13].body[1]::Return

Source: `infra/agentinfra/formal.py:26`; AST `3845fc6fcb6586e1b6fe1650cfe39a836e6b7f5d5da87b7ff6886ec1275c2a49`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: load_json, path. Outputs/bindings: (none).
Calls/effect boundaries: load_json, path.read_text.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13].body[1].value::Call

Source: `infra/agentinfra/formal.py:26`; AST `5e5a5352fc8a5c5208a0fc921d409f794af5ae7b068df874f8c337379767c860`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_json, path. Outputs/bindings: (none).
Calls/effect boundaries: load_json, path.read_text.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::read::root.body[13].body[1].value.args[0]::Call

Source: `infra/agentinfra/formal.py:26`; AST `d7d2b1d3f5b3313cd24906b00f77863075a83ccc502a11ff12b073fd43d10854`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14]::FunctionDef

Source: `infra/agentinfra/formal.py:29`; AST `da39c2e7cd133c29ff656e1bedaa165fb6f80153997d112b3128f7ae92c17f0b`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, fields, label, obj, require, set, type. Outputs/bindings: (none).
Calls/effect boundaries: fields.split, require, set, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14].body[0]::Expr

Source: `infra/agentinfra/formal.py:30`; AST `07ba303d143f5630ca1aaf4c719de62ab1afc2cb7b2d022949264706e205e801`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, fields, label, obj, require, set, type. Outputs/bindings: (none).
Calls/effect boundaries: fields.split, require, set, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14].body[0].value::Call

Source: `infra/agentinfra/formal.py:30`; AST `043673c1bd9310303594fe0f53f1ea794ec58706f89bb4277fde425208e01a6d`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, fields, label, obj, require, set, type. Outputs/bindings: (none).
Calls/effect boundaries: fields.split, require, set, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:30`; AST `184a37ca46d14a62e42e99c3f12c0b9e175b2ab19354a6c3849c2c25c9f9fd96`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obj, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/formal.py:30`; AST `f4b8d3f879aa7b78b84e1139de6596da4208eb5036f935f8974bada596154049`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obj, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14].body[0].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:30`; AST `1a555dadd636ebfa5084385a9fe0d843ae11103b8f7eed6a5826888e2988ff02`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, set. Outputs/bindings: (none).
Calls/effect boundaries: fields.split, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::exact_keys::root.body[14].body[0].value.args[0].values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/formal.py:30`; AST `cc6af2ae706f1c00dcb9967ad8493f197a6f9c2c567f36609149c7fcfca06f1f`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields. Outputs/bindings: (none).
Calls/effect boundaries: fields.split.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15]::FunctionDef

Source: `infra/agentinfra/formal.py:33`; AST `9beb2a153884d1085efa0ab24775d86d4ff99bf23fbbffe03fef8ad417427f4a`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: isinstance, label, len, re, require, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, re.search, require, value.strip.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[0]::Expr

Source: `infra/agentinfra/formal.py:34`; AST `18cc6c784847115edf81f2e3424c3527d1f6da409b3e29ca3173664af4b1311c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, label, len, require, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, require, value.strip.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[0].value::Call

Source: `infra/agentinfra/formal.py:34`; AST `7ba832a18d0fb36b16b3f5ccbb659ec815e7bba495567422c11af37051c9fedb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, label, len, require, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, require, value.strip.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/formal.py:34`; AST `f0937843eac35cb846ed896776839197deebad579475d870c722a45446739540`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[0].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:34`; AST `4746191e84cae7472cc262de886a77b4a3158696f6bfce73db3516eb8062a418`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len, value.strip.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[0].value.args[0].values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/formal.py:34`; AST `7d389057b81f97945d507ad29556bbeb4cd0d442c311a6de949b3a4d38e1cedd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value.strip.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[1]::Expr

Source: `infra/agentinfra/formal.py:35`; AST `e5136e80b62a960d40ea11775e5fc1e30438701e0a638df8dd5e0674f2cd59d9`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: label, re, require, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[1].value::Call

Source: `infra/agentinfra/formal.py:35`; AST `fba536875161295e5f5ca6487acd486ad395dc302bf7aba79ce4bfbea389f34e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: label, re, require, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::prose::root.body[15].body[1].value.args[0].operand::Call

Source: `infra/agentinfra/formal.py:35`; AST `e427ad636dba207ef83c59b7c1a7337fcdedee3f17fae2e5f59962ff9958d9be`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, value. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16]::FunctionDef

Source: `infra/agentinfra/formal.py:38`; AST `4c04a35c94be3fbb6c52ab3140683d4af431da8cb42cab62aa5bcba312878c84`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AUTHORITY, FRAMEWORK, digest, p, paths, sorted. Outputs/bindings: p, paths.
Calls/effect boundaries: (FRAMEWORK / 'infra/agentinfra').glob, digest, p.read_bytes, p.relative_to, p.relative_to(FRAMEWORK).as_posix, sorted.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[0]::Assign

Source: `infra/agentinfra/formal.py:39`; AST `65080b379d3b8a1b2afd53de46decfadf4b3b4ab49707f091aa5d081f3f304db`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AUTHORITY, FRAMEWORK, sorted. Outputs/bindings: paths.
Calls/effect boundaries: (FRAMEWORK / 'infra/agentinfra').glob, sorted.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[0].value.elts[0].value::Call

Source: `infra/agentinfra/formal.py:39`; AST `fe4a7e258f352924efbf7182148cba249a7fee9503313982652774461de8eff0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'infra/agentinfra').glob, sorted.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.elts[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[0].value.elts[0].value.args[0]::Call

Source: `infra/agentinfra/formal.py:39`; AST `379e42e646e4c1639253efa652d103d91964c79914abeae041af26b822a93c99`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'infra/agentinfra').glob.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.elts[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1]::Return

Source: `infra/agentinfra/formal.py:41`; AST `1bdef19bb6e10dc2cea3ecb4062ef0ae52af8ab4f1cfcb104eaa0005f9cc8750`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FRAMEWORK, digest, p, paths. Outputs/bindings: p.
Calls/effect boundaries: digest, p.read_bytes, p.relative_to, p.relative_to(FRAMEWORK).as_posix.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1].value::Call

Source: `infra/agentinfra/formal.py:41`; AST `4deac1c247c59070e1dd1623178fc0821874bc1e64a5eaf0a57daa3191c9475c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, digest, p, paths. Outputs/bindings: p.
Calls/effect boundaries: digest, p.read_bytes, p.relative_to, p.relative_to(FRAMEWORK).as_posix.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1].value.args[0]::DictComp

Source: `infra/agentinfra/formal.py:41`; AST `bb70b3ea8e2f30019e6ea06e2845e945fa92c7991b062a3b88cce4582365ea1d`.

Rust module: `infra::agentinfra::formal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: FRAMEWORK, digest, p, paths. Outputs/bindings: p.
Calls/effect boundaries: digest, p.read_bytes, p.relative_to, p.relative_to(FRAMEWORK).as_posix.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered DictComp evaluation at root.body[16].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1].value.args[0].key::Call

Source: `infra/agentinfra/formal.py:41`; AST `6a85f0d171cb350ae577a7b393de9418d55d3bc71509c4c8ff9f7a362211bcf4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, p. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(FRAMEWORK).as_posix.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0].key; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1].value.args[0].key.func.value::Call

Source: `infra/agentinfra/formal.py:41`; AST `6ea13ae8977df06d575a9a24e7a185c439a28c324e725e45db35ee34429b058d`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, p. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0].key.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1].value.args[0].value::Call

Source: `infra/agentinfra/formal.py:41`; AST `247c4ea4944e51a5399ac9c52bb270562af25ad934c7555758845759b7d3c1e2`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, p. Outputs/bindings: (none).
Calls/effect boundaries: digest, p.read_bytes.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::framework_identity::root.body[16].body[1].value.args[0].value.args[0]::Call

Source: `infra/agentinfra/formal.py:41`; AST `6b83dca35b721a6480711503aa48f3d020a7a02c07f5371d07b93bdc3b0800e8`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.read_bytes.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17]::FunctionDef

Source: `infra/agentinfra/formal.py:44`; AST `6a0055975d089dca72ac37febfa495df02dc50665147eb366201b4c2e6f2d02c`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AUTHORITY, IDENT, Path, RUST_PATH, a, all, any, c, cases, command, confined_path, digest, entries, exact_keys, field, ids, int, isinstance, k, len, list, manifest, name, o, obligations, optional, original_ids, p, paths, permitted, profile, proof_key, property_name, props, prose, qualified_index, r, relative_path, require, reuse, root, scope, set, sorted, source, str, type, value, w, witness, witnesses. Outputs/bindings: a, c, cases, command, entries, field, ids, k, manifest, name, o, obligations, optional, original_ids, p, paths, permitted, proof_key, props, r, reuse, scope, source, w, witness, witnesses.
Calls/effect boundaries: ' '.join, AUTHORITY.read_bytes, IDENT.fullmatch, Path, RUST_PATH.fullmatch, all, any, confined_path, confined_path(root, manifest, must_exist=True).is_file, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, digest, entries.add, exact_keys, ids.add, isinstance, len, o.get, p.is_file, paths.add, property_name, prose, qualified_index, relative_path, require, set, sorted, type, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:45`; AST `19472c2814467e50afb83d05ae59a9a5dbe0a3bc693464f527f061af9b622231`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[1]::Expr

Source: `infra/agentinfra/formal.py:46`; AST `6a2dcc28b9fe30dd41dc9bcfaa10b05ed12d2e7d9a1b8236bbe46a8c1d1eefe3`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, value. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[1].value::Call

Source: `infra/agentinfra/formal.py:46`; AST `8cc0cd13b698e29f59c2d73c7a5199641bcbff7c425a591d1e2a7e1583a4ed81`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, value. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[2]::Expr

Source: `infra/agentinfra/formal.py:47`; AST `47f64447e99e9ce18b0b46f96967dd42a91545992e5be28687459b9b576e58d2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, type, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[2].value::Call

Source: `infra/agentinfra/formal.py:47`; AST `32c918e00b660982b9c05ad99e7edde6c73430016529c9d913b12026342ba016`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, type, value. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:47`; AST `76bff5d3a26f91fdcc33c90824fbbc1b016e5ef2731fc64b16e819abf4296eb5`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, value. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[3]::Expr

Source: `infra/agentinfra/formal.py:48`; AST `1cb949b9475c7a087dee805e554d4d9082abc89211e2ee6367f34f6202a56d4e`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AUTHORITY, digest, require, value. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes, digest, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[3].value::Call

Source: `infra/agentinfra/formal.py:48`; AST `dc535390c56c8ffe663de6dc06dc0f67e512790173ee162b67909db52dbfed31`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AUTHORITY, digest, require, value. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes, digest, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[3].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/formal.py:48`; AST `6e82c214c870a2d99c759bc7f0f9ca53a1cf98bccb7c7a8429fe6b380861b9ea`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AUTHORITY, digest. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes, digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[3].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/formal.py:48`; AST `357d0bc218c0b02201bc2aff9908fb9de431cd99cfa3beeb2659a5edfb327eec`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AUTHORITY. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[4]::Expr

Source: `infra/agentinfra/formal.py:49`; AST `a7e10cae5ba015f2f1d9c1611f2f1484fb0af85b6fb8af42459d541e1588c029`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prose, value. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[4].value::Call

Source: `infra/agentinfra/formal.py:49`; AST `d7a932ed2241fddd761e368eeb77f89d4de6ac35b54100e207190a58016d7a0a`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prose, value. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[5]::Expr

Source: `infra/agentinfra/formal.py:50`; AST `77ed6afdaff626fc1801d539e73cb0c1ecfa320516dc2b5b75f66cf4ac7705c7`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prose, value. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[5].value::Call

Source: `infra/agentinfra/formal.py:50`; AST `ea8459f524fae51ff894ac3bc258eedcaac97eeac2c7ed1fd08bf01f94f3d23d`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prose, value. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[6]::Assign

Source: `infra/agentinfra/formal.py:51`; AST `726827a51b424f868c1512d2ad3db778b02c125bf21ef529eaa9bac2a34ab6f2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: reuse.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[7]::Expr

Source: `infra/agentinfra/formal.py:52`; AST `8bde3a901079cc740d1cc78788f5416a37fb54ed9fc80768a902a4b0dd182fae`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, reuse. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[7].value::Call

Source: `infra/agentinfra/formal.py:52`; AST `a918a89bb98c25b9a70825ffd5b0f5ab1c4d05166668babf41c0ac6af0055801`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, reuse. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[8]::Expr

Source: `infra/agentinfra/formal.py:53`; AST `9e1b41c71cf9c5e4b83680db7d610f20f8c4dac6829b8c4d9fabb9339d62d659`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, reuse. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[8].value::Call

Source: `infra/agentinfra/formal.py:53`; AST `c9bcd558d5f1726282d3fd90d92f645d72741dab08507cc4de3e15c2b35738de`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, reuse. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[9]::For

Source: `infra/agentinfra/formal.py:54`; AST `4fa00dc64533a2d470c7a109099f2d78382c6dbb32366543a1cad857315a85af`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, prose, reuse. Outputs/bindings: field.
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[9]; no call, error or mutation may be omitted. Iteration: field in ('license', 'reason')
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[9].body[0]::Expr

Source: `infra/agentinfra/formal.py:55`; AST `ee7031b5b2300da6e07dd3349dbdb6ee272badb21a478aa42f90190e6e62471a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, prose, reuse. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[9].body[0].value::Call

Source: `infra/agentinfra/formal.py:55`; AST `abf90f168d155d4c27b65cb15599032f21e1e03be215809d8273faf0f98923a0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, prose, reuse. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[10]::Expr

Source: `infra/agentinfra/formal.py:56`; AST `5a925005f658ed60f8bf527fa272eb83450bbd4b0bcd3644ba42a071a5158aff`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, list, require, reuse, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[10].value::Call

Source: `infra/agentinfra/formal.py:56`; AST `169b60fd5480e7788debddfbd10b6329e8eafb243187af441661eb0368fa5e67`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, list, require, reuse, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[10].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:56`; AST `ab5d9d5ac6a4f776c12fcd774b6f8ffda27246e61235d6922331be0b96556397`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reuse, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[10].value.args[0].values[1].left::Call

Source: `infra/agentinfra/formal.py:56`; AST `0e493a7598b1162df0ea5c0113b86e97f6c9ea943db55f500c0bc825f671b751`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, reuse. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[11]::For

Source: `infra/agentinfra/formal.py:57`; AST `d38b07c9a639fb1c424f6744f2467b3d1f699181544214356a5d643683ae1fdb`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: prose, reuse, source. Outputs/bindings: source.
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[11]; no call, error or mutation may be omitted. Iteration: source in reuse['sources']
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[11].body[0]::Expr

Source: `infra/agentinfra/formal.py:58`; AST `dcd2c6ac9c0c330b3d83e5902ab48f61084a077094d3dfa21554a87b15033288`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prose, source. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[11].body[0].value::Call

Source: `infra/agentinfra/formal.py:58`; AST `14f5d41254aae487115f77f76c8f4d98de8168922b2463f23ff0bc527be3bac0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prose, source. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[12]::Expr

Source: `infra/agentinfra/formal.py:59`; AST `8769787d3fa433d03e0dcd75dbad99d15421176a2598851dc0e9562a65a0928b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, reuse. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[12].value::Call

Source: `infra/agentinfra/formal.py:59`; AST `e74dc967e9dc76656248aef1d3b7a635a9fe5c63c6ba05b2cfe844adc0b50b0c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, reuse. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[13]::Expr

Source: `infra/agentinfra/formal.py:60`; AST `502108317fdc4bba7a19b2e78f3d19908661ce6f6391b8d936562a273f9de768`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, all, isinstance, list, require, reuse, str, type. Outputs/bindings: a.
Calls/effect boundaries: all, isinstance, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[13].value::Call

Source: `infra/agentinfra/formal.py:60`; AST `d7277125589567203fc8b23d091d01901b088eca17c1523d33b7f1f00bf1146e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, isinstance, list, require, reuse, str, type. Outputs/bindings: a.
Calls/effect boundaries: all, isinstance, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[13].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:60`; AST `0ea0ad28ca784b17c1af239ab5177ccbf69e8736cf551c20f42208d4056f58af`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reuse, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[13].value.args[0].values[1]::Call

Source: `infra/agentinfra/formal.py:60`; AST `bf987fe8f480bb8ea957fed5b327583794d0665ee3f8b699efdb75cb9551523e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, isinstance, reuse, str. Outputs/bindings: a.
Calls/effect boundaries: all, isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[13].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:60`; AST `3cccce609189bbd92899d5b4edc880fe35a0b6867ff9f976d1de3dc60061f08e`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, isinstance, reuse, str. Outputs/bindings: a.
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[13].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[13].value.args[0].values[1].args[0].elt.values[0]::Call

Source: `infra/agentinfra/formal.py:60`; AST `839b13937f05bda9b701a3259fbd7443e8dbc925be78a97c2678d4e755705dd9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value.args[0].values[1].args[0].elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[14]::Expr

Source: `infra/agentinfra/formal.py:61`; AST `7f20e9312b95e6d9db1da83c4f5a2703eac42e91d6b55c0df5aa280fef1a5362`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, reuse. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[14].value::Call

Source: `infra/agentinfra/formal.py:61`; AST `e91d6de07742e976069b1decbbe63ce4fe84356b23217417caea3cb9fb25b45b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, reuse. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[15]::Assign

Source: `infra/agentinfra/formal.py:62`; AST `5207b83b8a2abbce7d2b528b51d2739086b4a1bf9161a60a51b54f95d5f38a1e`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: obligations.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[16]::Expr

Source: `infra/agentinfra/formal.py:63`; AST `1d888a4cc03f92e0f32e5b164422bdedf0dfa4d89153e3d5a0a34c04217292b4`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, list, obligations, require, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[16].value::Call

Source: `infra/agentinfra/formal.py:63`; AST `de1044b384b587ced6fe822252847959904b1f98f458ac15d797b2ca4841d217`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, list, obligations, require, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[16].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:63`; AST `22fe4300495791f5fb680a9f1cfb6133f867d2dba8c3afa1fadebfa724476194`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligations, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[16].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[16].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:63`; AST `aa832eaca9b8ad712344696fda175a5d53b6e55b2bda9c89270711d081b70dab`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, obligations. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[16].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[17]::Assign

Source: `infra/agentinfra/formal.py:64`; AST `40a34f795fd672ab4efc75ec6ec5424417e451bd20a34f5814d7a5431bca780f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: entries, ids, paths.
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[17].value.elts[0]::Call

Source: `infra/agentinfra/formal.py:64`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[17].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[17].value.elts[1]::Call

Source: `infra/agentinfra/formal.py:64`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[17].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[17].value.elts[2]::Call

Source: `infra/agentinfra/formal.py:64`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[17].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[18]::Assign

Source: `infra/agentinfra/formal.py:65`; AST `4d697b13d708809ee531b9e76d4cbcfacc2cc03daf5fbe92ffca0f677d4116d4`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: original_ids.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[19]::Assign

Source: `infra/agentinfra/formal.py:66`; AST `638d1ecb56a4affefaa39a79e176e91fbbd8338c41e530b091ff475ee2e11a2f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: command, profile. Outputs/bindings: command, permitted.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[19].value::SetComp

Source: `infra/agentinfra/formal.py:66`; AST `27c199d0c733165357f74f691f8ff4a279e39b3c65f301085484f58354b10638`.

Rust module: `infra::agentinfra::formal`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: command, profile. Outputs/bindings: command.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered SetComp evaluation at root.body[17].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20]::For

Source: `infra/agentinfra/formal.py:67`; AST `254f0acd5395088f613beed9af0d0e322098eb0a8b8096622e75a228e8c46e1b`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: IDENT, Path, RUST_PATH, all, any, c, cases, confined_path, entries, exact_keys, field, ids, int, isinstance, k, len, list, manifest, name, o, obligations, optional, original_ids, p, paths, permitted, proof_key, property_name, props, prose, qualified_index, r, relative_path, require, root, scope, set, str, type, w, witness, witnesses. Outputs/bindings: c, cases, field, k, manifest, name, o, optional, original_ids, p, proof_key, props, r, scope, w, witness, witnesses.
Calls/effect boundaries: ' '.join, IDENT.fullmatch, Path, RUST_PATH.fullmatch, all, any, confined_path, confined_path(root, manifest, must_exist=True).is_file, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, entries.add, exact_keys, ids.add, isinstance, len, o.get, p.is_file, paths.add, property_name, prose, qualified_index, relative_path, require, set, type, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[20]; no call, error or mutation may be omitted. Iteration: o in obligations
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[0]::Assign

Source: `infra/agentinfra/formal.py:68`; AST `0f1015a07267113c4350ab857704aa0adb4b13f9090102024724b0eafa3f2e0c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: k, o. Outputs/bindings: k, optional.
Calls/effect boundaries: ' '.join.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[0].value::Call

Source: `infra/agentinfra/formal.py:68`; AST `f13ffdd98ed055b441ae9f5d343627a49c7c30727b61581ea0b5a58d37bc5091`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, o. Outputs/bindings: k.
Calls/effect boundaries: ' '.join.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:68`; AST `fca9590725a43c7045eeaafdb7e96b8645f2ce6ccdce512d0e4fed16b1240b86`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: k, o. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[20].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[1]::Expr

Source: `infra/agentinfra/formal.py:69`; AST `33188b6f9928e4b0e6f7b0ef5547b1c659e3cdb9537e6d8137178f4669ae0e6c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, o, optional. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[1].value::Call

Source: `infra/agentinfra/formal.py:69`; AST `1c46597d0ed52eecdf2ab20109650906fe24b692416e08b6d071c6662cf5c3b9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, o, optional. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[2]::Expr

Source: `infra/agentinfra/formal.py:70`; AST `601bbb3e8c2d5a470947c9c48db3a9c5d42d513db45babc59d9a13e26494f0ea`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: IDENT, ids, isinstance, o, require, str. Outputs/bindings: (none).
Calls/effect boundaries: IDENT.fullmatch, isinstance, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[2].value::Call

Source: `infra/agentinfra/formal.py:70`; AST `082578f8ab086b782bdb5973015411dcf3f1974744c4fa597705866b8d306073`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: IDENT, ids, isinstance, o, require, str. Outputs/bindings: (none).
Calls/effect boundaries: IDENT.fullmatch, isinstance, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[2].value.args[0].values[0]::Call

Source: `infra/agentinfra/formal.py:70`; AST `53d718ab6293103215c571fa8b4f1aeafb7d2d4541972e9ded3eb2bec8de35ba`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, o, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[2].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/formal.py:70`; AST `09036a0214eb24d31ff46ba94c864ea5dbd3e5786fb009cf0970f8fcffb6a746`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: IDENT, o. Outputs/bindings: (none).
Calls/effect boundaries: IDENT.fullmatch.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[3]::Expr

Source: `infra/agentinfra/formal.py:71`; AST `545c7b5588ce0202b29fc4caa13f7a276d7eaa4f59c29a65f816b449c1953224`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, o. Outputs/bindings: (none).
Calls/effect boundaries: ids.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[3].value::Call

Source: `infra/agentinfra/formal.py:71`; AST `d8898ac276da2da1bf61edb9ba8c9d99fbfa005c7c8e29196b943332093a10c7`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, o. Outputs/bindings: (none).
Calls/effect boundaries: ids.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[4]::Expr

Source: `infra/agentinfra/formal.py:72`; AST `5e0dbf165757ec6962d33fe1d28371173645b631ea5d6ac555ba0e1df5ac0c6b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, o, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[4].value::Call

Source: `infra/agentinfra/formal.py:72`; AST `c95197764e421ec0ac4998462456fb5e311f3a4a950a2840c991ce749bb4df92`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, o, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[4].value.args[0].values[1]::Call

Source: `infra/agentinfra/formal.py:72`; AST `727e25942822871279d24fdda3784220b6f6cc4d2a62f50bf2913751db910aba`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, o, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[5]::Assign

Source: `infra/agentinfra/formal.py:73`; AST `34eb02de78c46cedc492d99e2cc92124c9acb9be018f7a0e6b4ee9f4176fc6ae`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o. Outputs/bindings: proof_key.
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[5].value.elts[1]::Call

Source: `infra/agentinfra/formal.py:73`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[5].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[6]::Expr

Source: `infra/agentinfra/formal.py:74`; AST `82f0f14a5c07facb6e772002772e4e29499ea512cb763b62a7ac35bf7877a130`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, proof_key, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[6].value::Call

Source: `infra/agentinfra/formal.py:74`; AST `9ff30a2d5ad074cb14d9d24482294e0c795ab3064351dde7ac2d97e604b2f312`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, proof_key, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[7]::Expr

Source: `infra/agentinfra/formal.py:75`; AST `c733f7b0291f377ad09117d86ea61acfae24392706cebdaca2f324e87d65f3ef`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, proof_key. Outputs/bindings: (none).
Calls/effect boundaries: entries.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[7].value::Call

Source: `infra/agentinfra/formal.py:75`; AST `0493b899c42f6a68e3122c04b3502f15bed5e7c0bdb39b1012a94afd40b01d0b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, proof_key. Outputs/bindings: (none).
Calls/effect boundaries: entries.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[8]::Expr

Source: `infra/agentinfra/formal.py:76`; AST `9ceb7adfed7caa078a03969ede46ef897f890cb36d52e5aa5aeb9b76166550cf`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, o, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[8].value::Call

Source: `infra/agentinfra/formal.py:76`; AST `4f405cedddd18b9d44b78681a764c2cf936dc0a32928a5c857d2f565b860a22b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, o, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[8].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:76`; AST `711b51df6a8be96f53f542f709d89a3d8576bdba9def17c0053015c2f82d7883`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[8].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9]::If

Source: `infra/agentinfra/formal.py:77`; AST `1fa41f5650b4d0ad3b299bfc90f8f0d70093e3446c870cf34c8a84763694bfe9`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: Path, RUST_PATH, confined_path, manifest, o, paths, permitted, relative_path, require, root. Outputs/bindings: manifest.
Calls/effect boundaries: Path, RUST_PATH.fullmatch, confined_path, confined_path(root, manifest, must_exist=True).is_file, o.get, paths.add, relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[17].body[20].body[9]; no call, error or mutation may be omitted. Condition: o['method'] == 'kani'
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[0]::Expr

Source: `infra/agentinfra/formal.py:78`; AST `4fa3d29c16dd695aee6fed582e5b0ac06494cc5ceb71e7e3bca114a65b92a4f4`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RUST_PATH, o, require. Outputs/bindings: (none).
Calls/effect boundaries: RUST_PATH.fullmatch, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[0].value::Call

Source: `infra/agentinfra/formal.py:78`; AST `24454f53a3727df5a73a13a2d995cb7f5970b50d6112305a78b2608a5e46ede5`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RUST_PATH, o, require. Outputs/bindings: (none).
Calls/effect boundaries: RUST_PATH.fullmatch, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/formal.py:78`; AST `ede56a9c77c592319f901931be2d3dc052b049d89c75f8250b68f0898346fc22`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RUST_PATH, o. Outputs/bindings: (none).
Calls/effect boundaries: RUST_PATH.fullmatch.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[1]::Assign

Source: `infra/agentinfra/formal.py:79`; AST `15bcd4cfefe61ec17b5a09bc4edc00b03b3b8f34478a313987caaf5dec40471c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o. Outputs/bindings: manifest.
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[1].value::Call

Source: `infra/agentinfra/formal.py:79`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[2]::Expr

Source: `infra/agentinfra/formal.py:80`; AST `91435249caf274bbea00318066c00ae56f0a7ddb32edeb271c90ca80123c9023`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, manifest, relative_path, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[2].value::Call

Source: `infra/agentinfra/formal.py:80`; AST `7544853701f2fb6054d10b0178a551c695a53fbcbc8300ecb260c4dbb9731ca0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, manifest, relative_path, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:80`; AST `70eff9e3aa5e53c3358a8c4bb74a686a9140ec20342592967ebdaf7c302b5b67`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest, relative_path. Outputs/bindings: (none).
Calls/effect boundaries: relative_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[2].value.args[0].values[1].left.value::Call

Source: `infra/agentinfra/formal.py:80`; AST `a3a7b0f552a1f0297f2a2185ddba50067d2701a986985a54d95fb6d527f3737e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, manifest. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[2].value.args[0].values[1].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[3]::Expr

Source: `infra/agentinfra/formal.py:81`; AST `5168af293f24b85bbd06dfc2618be6dd2d1d8b54740027f133db4de8cad4e376`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, manifest, require, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, manifest, must_exist=True).is_file, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[3].value::Call

Source: `infra/agentinfra/formal.py:81`; AST `9f5f0dd673cfddd25042d9f4b0ec294e902abe26a5b7f7a3a38d1b7041ea3040`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, manifest, require, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, manifest, must_exist=True).is_file, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:81`; AST `ac7e0ed32fcae68c9ab3841559a6c30c402eadc765658b4addf3df45ba79ca0c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, manifest, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, manifest, must_exist=True).is_file.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[3].value.args[0].func.value::Call

Source: `infra/agentinfra/formal.py:81`; AST `ad2e214a5b2c2cd30ce438762ddb010dff8704c7232cb5eb489dedb01b601e67`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, manifest, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[3].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[4]::Expr

Source: `infra/agentinfra/formal.py:82`; AST `fa2f2775fbd50139fa488d27831ee1bb1a23f56f50274285773e5a9e6d41cf7d`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: manifest, paths. Outputs/bindings: (none).
Calls/effect boundaries: paths.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].body[4].value::Call

Source: `infra/agentinfra/formal.py:82`; AST `cd03258fcc197b77274c7e2d0e366b07254c1e530d35075327c1213b972c21f5`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest, paths. Outputs/bindings: (none).
Calls/effect boundaries: paths.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].orelse[0]::Expr

Source: `infra/agentinfra/formal.py:84`; AST `ab3a1a506855eb76e269e7a296a72dbf064736d212432cf7a0893a585f2511f6`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].orelse[0].value::Call

Source: `infra/agentinfra/formal.py:84`; AST `57aba373019b8c15583d07025a4b16003d7ad8f33719e81dbe36bb53c110468e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].orelse[1]::Expr

Source: `infra/agentinfra/formal.py:85`; AST `b982d5eb438aa53600573fffdce7b993fc1779d5571e46db7e0833d2def69ef8`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, permitted, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].orelse[1].value::Call

Source: `infra/agentinfra/formal.py:85`; AST `6b257a098ec39cf3a6513c20ae10f4f3b6811aad08dc2481aed1c550e2af4d93`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, permitted, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].orelse[2]::Expr

Source: `infra/agentinfra/formal.py:86`; AST `af0778b4be96fad6b34f66ea646d1c7b8df374164ff4093d56a86e9d0c65ac03`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[9].orelse[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[9].orelse[2].value::Call

Source: `infra/agentinfra/formal.py:86`; AST `c48174bd5423c325c09174918e2780ed1768df5899d665fe3a552860fbe40832`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[9].orelse[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[10]::For

Source: `infra/agentinfra/formal.py:87`; AST `84928e5de63326dcdb1ba6c923a22e66c765dc1c093871e04e8968918df8f531`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, o, prose. Outputs/bindings: field.
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[20].body[10]; no call, error or mutation may be omitted. Iteration: field in ('invariant', 'assumptions', 'limits')
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[10].body[0]::Expr

Source: `infra/agentinfra/formal.py:88`; AST `5be846cd6d3d9722f13b70c69482d4c32c0270b645f9432fb1cdfb66aa5052af`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, o, prose. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[10].body[0].value::Call

Source: `infra/agentinfra/formal.py:88`; AST `8edf25e3ccbf87a0b4a57439aa7c7e6416cce9141d6baef27afdb5d0f3206f6f`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, o, prose. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11]::For

Source: `infra/agentinfra/formal.py:89`; AST `7b4dd4b140e3ff60be64d0a45812df982bd47c0485f72f634fbcdefa98620c44`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: confined_path, field, isinstance, len, list, name, o, p, paths, relative_path, require, root, str, type. Outputs/bindings: field, name, p.
Calls/effect boundaries: confined_path, isinstance, len, p.is_file, paths.add, relative_path, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[20].body[11]; no call, error or mutation may be omitted. Iteration: field in ('specification', 'implementation', 'proof_inputs')
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[0]::Expr

Source: `infra/agentinfra/formal.py:90`; AST `12a15a7c3d9c768418f5996654cd4d1f1f653cf64d2a286c4bea98448d9cf8fa`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, len, list, o, require, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[0].value::Call

Source: `infra/agentinfra/formal.py:90`; AST `a345413ce985f958cc397df1a2e8f9eb2b76f1d63ba2a8b0199a1d85939462ae`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, len, list, o, require, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:90`; AST `4c552e5fe8a877ee1fb0d9f16b1002a4f186a3f1ae5a1c294504d7b82143cac6`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, o, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[0].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:90`; AST `450fb9d336daf8d0d6bbee0eab856816a35c597c5fe0de63fa97a04b7ce22397`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, len, o. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[0].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1]::For

Source: `infra/agentinfra/formal.py:91`; AST `273ea6a899788d3b2c6ba8e2318dfa43dd4cae96e9a38f2325f8ff2b6e66d4f4`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: confined_path, field, isinstance, name, o, p, paths, relative_path, require, root, str. Outputs/bindings: name, p.
Calls/effect boundaries: confined_path, isinstance, p.is_file, paths.add, relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[20].body[11].body[1]; no call, error or mutation may be omitted. Iteration: name in o[field]
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[0]::Expr

Source: `infra/agentinfra/formal.py:92`; AST `c9289d42c75634397b121c0cfc6c43344e485f9e2d743871871d614dfee7265a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, name, relative_path, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[0].value::Call

Source: `infra/agentinfra/formal.py:92`; AST `5de986a40c4835c94a27e12866f0396cb909633d44d968c7676cdcd81c76a059`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, name, relative_path, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/formal.py:92`; AST `ec1885a68f635e9b05e21bf549ce84222799f1b460b2e2b511d6c9a601fd0627`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, name, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/formal.py:92`; AST `b14f1612b45f55f69d3b8e65cd5d2208506afdae15dfaad0223607d916546597`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, relative_path. Outputs/bindings: (none).
Calls/effect boundaries: relative_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[1]::Assign

Source: `infra/agentinfra/formal.py:93`; AST `3c377e3d01b48b377acaa452eb165749d6f251978606722edc90d8558aec2eb3`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, name, root. Outputs/bindings: p.
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[11].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[1].value::Call

Source: `infra/agentinfra/formal.py:93`; AST `84ad204db26e498c59a40ccefeec068f82fca59b0dd091cc081652642986ed46`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[2]::Expr

Source: `infra/agentinfra/formal.py:94`; AST `54b6c9ea11b5c08391fb56596505da39ca7a017f63bd3c4d31018121a0628282`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, p, require. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[11].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[2].value::Call

Source: `infra/agentinfra/formal.py:94`; AST `e8d752fa5641e3e54f999c394246b2aafb492547deb7a24a5b8d05278e8ccdb5`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, p, require. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[2].value.args[0]::Call

Source: `infra/agentinfra/formal.py:94`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[3]::Expr

Source: `infra/agentinfra/formal.py:95`; AST `1783219cf1b862adbfc59d79f711c22f8f4545d06d75fb9b14b1d865f519dd75`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, paths. Outputs/bindings: (none).
Calls/effect boundaries: paths.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[11].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[11].body[1].body[3].value::Call

Source: `infra/agentinfra/formal.py:95`; AST `f3142dfbcb0a11a75545005f10092f13962f65478f34038d0ac1ec8173d79fdd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, paths. Outputs/bindings: (none).
Calls/effect boundaries: paths.add.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[11].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12]::If

Source: `infra/agentinfra/formal.py:96`; AST `10d785960a4c1d357eead88f6bb276c7728f6a23d0f3526f4e6ca0a77e2c720d`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: all, any, c, cases, confined_path, exact_keys, field, int, isinstance, len, list, o, original_ids, p, property_name, props, prose, qualified_index, r, require, root, scope, set, str, type, w, witness, witnesses. Outputs/bindings: c, cases, field, original_ids, p, props, r, scope, w, witness, witnesses.
Calls/effect boundaries: all, any, confined_path, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, exact_keys, isinstance, len, property_name, prose, qualified_index, require, set, type, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[17].body[20].body[12]; no call, error or mutation may be omitted. Condition: 'evidence' in o
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:97`; AST `11449d92da6d2af5a5eb39e5619b69aece452afe582df04330f1e0b8e9ac8ceb`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17].body[20].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[1]::If

Source: `infra/agentinfra/formal.py:98`; AST `3f629029c633ddf351a6656c0faefff6469d4e59bf59fc9adec4398e1d7e1fe3`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: original_ids, qualified_index, r, root. Outputs/bindings: original_ids, r.
Calls/effect boundaries: qualified_index.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[17].body[20].body[12].body[1]; no call, error or mutation may be omitted. Condition: original_ids is None
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[1].body[0]::Assign

Source: `infra/agentinfra/formal.py:99`; AST `e1745893dab2e0c492277fc5406ef49bba7a4452872f342df76e836aa7330d0d`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualified_index, r, root. Outputs/bindings: original_ids, r.
Calls/effect boundaries: qualified_index.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[1].body[0].value::SetComp

Source: `infra/agentinfra/formal.py:99`; AST `153bf511f3b792ad678851ad29ebb81686768818465f524477a55b2fbd25f687`.

Rust module: `infra::agentinfra::formal`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: qualified_index, r, root. Outputs/bindings: r.
Calls/effect boundaries: qualified_index.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered SetComp evaluation at root.body[17].body[20].body[12].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[1].body[0].value.generators[0].iter::Call

Source: `infra/agentinfra/formal.py:99`; AST `cf28a785fa5a79d89e058eeba219926071b4f602c246cf1af42949b910d53069`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualified_index, root. Outputs/bindings: (none).
Calls/effect boundaries: qualified_index.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[1].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[2]::Assign

Source: `infra/agentinfra/formal.py:100`; AST `aa099afdd53f80859dcf1f51e8d8d0ffcadb1c85663656d48f534acda2d888d8`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o. Outputs/bindings: scope.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[3]::Expr

Source: `infra/agentinfra/formal.py:101`; AST `9dbedef2b8639a900fbb7556391877de4eeab62141b795984dc1a3fb4c2019ae`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, scope. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[3].value::Call

Source: `infra/agentinfra/formal.py:101`; AST `7eeb1945f85d32935b44379a4c18fc88dcfb3d665244de0292483e9f3b46f3b4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, scope. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[4]::Expr

Source: `infra/agentinfra/formal.py:102`; AST `c36d1fcceb80475ae3a75e4e431c2a155aaa5942fc8acce447a23aa87998b40b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[4].value::Call

Source: `infra/agentinfra/formal.py:102`; AST `a4c79e6dcb5ab0ef6ec6fe76ea217267b9ff5c2bb308ca90f9f8fab2efe9cbb5`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[5]::Expr

Source: `infra/agentinfra/formal.py:103`; AST `5c9424171abdac2095e29334c3b6c4b1963b783ae60c5cedc26709dc8d5423e5`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, scope. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[5].value::Call

Source: `infra/agentinfra/formal.py:103`; AST `5647a5d8f5827601a9f39cd7bbba7c0ef68790ce4f5a0206b41022500350cfda`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, scope. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[6]::Assign

Source: `infra/agentinfra/formal.py:104`; AST `81c7ae678a555313f1ca6eb389ec4f81944d32404c78c35656840362b8130ca6`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: scope. Outputs/bindings: cases.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7]::Expr

Source: `infra/agentinfra/formal.py:105`; AST `56dc2d2607cfda371bebd3030cfcf50e71a57d3fd18b112020141a09b961096b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, c, cases, isinstance, len, list, original_ids, require, str, type. Outputs/bindings: c.
Calls/effect boundaries: all, isinstance, len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7].value::Call

Source: `infra/agentinfra/formal.py:105`; AST `b3647aab917ebbe705a51baa92807d8ed83ea2440e8c69aeeacc7276baa56f97`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, cases, isinstance, len, list, original_ids, require, str, type. Outputs/bindings: c.
Calls/effect boundaries: all, isinstance, len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:105`; AST `2bf72fad55f654db0d58de4b86e440f92be9a12db54cdba1a65db0ec9adae0d7`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:105`; AST `5ed86541eebb17836d103325d02cd9def3215bd652802b878ccbf286fcc75fb9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[7].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7].value.args[0].values[2]::Call

Source: `infra/agentinfra/formal.py:105`; AST `3921f85b39e50511f1193224e2317355b9fd7e65479a1f75d8518c6d3e8bca91`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, cases, isinstance, original_ids, str. Outputs/bindings: c.
Calls/effect boundaries: all, isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[7].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7].value.args[0].values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:105`; AST `29ed06848a558f129e64af77a76c7bd7d0da036eab78b06ed9b61692297ef0a4`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, cases, isinstance, original_ids, str. Outputs/bindings: c.
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[20].body[12].body[7].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[7].value.args[0].values[2].args[0].elt.values[0]::Call

Source: `infra/agentinfra/formal.py:105`; AST `e5b4109f8762ad1ebe07ae2d3068017b95a6f2cfefe5a8ae9740a3cc879cf114`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[7].value.args[0].values[2].args[0].elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[8]::Expr

Source: `infra/agentinfra/formal.py:106`; AST `ed37a6aa4f67033c4d191fff4b6ad12df6b90a9e3b822820837f37e6f5d80f67`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[8].value::Call

Source: `infra/agentinfra/formal.py:106`; AST `6c76e5c0eb2b94e2fb3ab4f46e8c6fbf307d6906c3a82e09a5509a93e016e8cb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[8].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:106`; AST `5ed86541eebb17836d103325d02cd9def3215bd652802b878ccbf286fcc75fb9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[8].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[8].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/formal.py:106`; AST `0fa304750520ecad11bb746ed310f046123c5c3b34092ae238d947d9b1af4c8c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[8].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[8].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/formal.py:106`; AST `2fd843387a4299763f634d4dfdb654d2faaf708d16f5cc8b1a36623545b03467`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[8].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[9]::Assign

Source: `infra/agentinfra/formal.py:107`; AST `d1092ec1bef7ae16cebfa1f9e71deecc7eff178ee5d8e6a2d902fa83863ba23d`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: scope. Outputs/bindings: props.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[10]::ImportFrom

Source: `infra/agentinfra/formal.py:108`; AST `6af63389e56de12581c260caf6303d1a9dc6fd9f1017e14e5b28653ebac1d166`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17].body[20].body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11]::Expr

Source: `infra/agentinfra/formal.py:109`; AST `ecb93eeca744caa2e2584e5746966be86872233c7c6563aa56670ee3c2971b0a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, len, list, p, property_name, props, require, type. Outputs/bindings: p.
Calls/effect boundaries: all, len, property_name, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11].value::Call

Source: `infra/agentinfra/formal.py:109`; AST `a239f25251135af55402782f34f05d7e1defd00eaf11fba8517a543da0b2f78e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, len, list, p, property_name, props, require, type. Outputs/bindings: p.
Calls/effect boundaries: all, len, property_name, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:109`; AST `25a4eaf5f482788f99e97437d2e6b3324f6ad1d046482c0d5a4ffd9dd2915423`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: props, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[11].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:109`; AST `534a0d82c7e0746f581e181aacbf8990efb88b75d41862bafe8a0a9740873e7c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, props. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[11].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11].value.args[0].values[2]::Call

Source: `infra/agentinfra/formal.py:109`; AST `1cd0ed4d65cdc60870d5660707271d5d947b15b2fba0b8ca8c7529ffcc8eb39f`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, p, property_name, props. Outputs/bindings: p.
Calls/effect boundaries: all, property_name.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[11].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11].value.args[0].values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:109`; AST `fb251ddf0490abc4ab295ff993477073162ba2f9a3152b58f205d11abffb2371`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: p, property_name, props. Outputs/bindings: p.
Calls/effect boundaries: property_name.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[20].body[12].body[11].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[11].value.args[0].values[2].args[0].elt::Call

Source: `infra/agentinfra/formal.py:109`; AST `c112d2f59cd487bae8118938514e330cde7bafd377f7b78537261a73b88b1ade`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, property_name. Outputs/bindings: (none).
Calls/effect boundaries: property_name.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[11].value.args[0].values[2].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[12]::Expr

Source: `infra/agentinfra/formal.py:110`; AST `62709c05722add04548ef829326728287e8ada0ddbee878b490c4178a3d23d0b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, props, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[12].value::Call

Source: `infra/agentinfra/formal.py:110`; AST `acc43bb4eafe275cbbc63e7a03221b02bd6b2775ef3c74c20909e7722fd06f45`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, props, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[12].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:110`; AST `534a0d82c7e0746f581e181aacbf8990efb88b75d41862bafe8a0a9740873e7c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, props. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[12].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[12].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/formal.py:110`; AST `fef15a4edc6da2a7a1b076609b36c4cdca901bf25da1451df96cf3b6812c6feb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, props, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[12].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[12].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/formal.py:110`; AST `0b1e20441a4dcb455a673c629d2e88140a813e3f70fec84d15b783a28a6b4788`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: props, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[12].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[13]::For

Source: `infra/agentinfra/formal.py:111`; AST `3fdf80fa4a7d7cb2e667fa248bf7f832c261052c153f224b99077ad7d2271b3d`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, prose, scope. Outputs/bindings: field.
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[20].body[12].body[13]; no call, error or mutation may be omitted. Iteration: field in ('relation', 'review')
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[13].body[0]::Expr

Source: `infra/agentinfra/formal.py:112`; AST `3ff4588d50f5c5f00e7617b17fb96cad19dc21697916793992844c261062603f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, prose, scope. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[13].body[0].value::Call

Source: `infra/agentinfra/formal.py:112`; AST `4544b64345547db7c2130ca78ff4e64cb610af9223181be33ad6ce35592199ac`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, prose, scope. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[14]::Assign

Source: `infra/agentinfra/formal.py:113`; AST `c230496033c413bc313f50b12805a59a63ebe566ac3434f1d468ed13527fc1d9`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: scope. Outputs/bindings: witnesses.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[20].body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[15]::Expr

Source: `infra/agentinfra/formal.py:114`; AST `b28151ca12af8ca22d75e17957245d2575557553396ce4c0ce77461274584430`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, list, require, type, witnesses. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[15].value::Call

Source: `infra/agentinfra/formal.py:114`; AST `02f0ce20b4bc71c5ea24a0c1c63a93eb78637b94e7221f247a850263e07ec4f0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, list, require, type, witnesses. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[15].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:114`; AST `bf46c6313e18bbd241fb539e427a1420710811bb1efb09cd30b41693364d6583`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, witnesses. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[15].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[15].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/formal.py:114`; AST `4f4b314bed43e32e26e2d61faf6de861038103b6f612d22a04a02143b7007ab0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, witnesses. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[15].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16]::For

Source: `infra/agentinfra/formal.py:115`; AST `c83586398064aa1a0de16a9444a46e015145f8d119512802d155973b9cd0ae9c`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: confined_path, exact_keys, int, len, o, property_name, require, root, type, witness, witnesses. Outputs/bindings: witness.
Calls/effect boundaries: confined_path, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, exact_keys, len, property_name, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[17].body[20].body[12].body[16]; no call, error or mutation may be omitted. Iteration: witness in witnesses
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[0]::Expr

Source: `infra/agentinfra/formal.py:116`; AST `d2b952b936482754d009da4f7dd848c977ac511d5372cf0dafa72efab92cc4ff`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, witness. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[0].value::Call

Source: `infra/agentinfra/formal.py:116`; AST `02e6127dfe76df3ede3e2e533c3f9ef8383b045eb2ce855487e4631c6cbc7b6f`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, witness. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[1]::Expr

Source: `infra/agentinfra/formal.py:117`; AST `095f7e86e93f122bbe74bf844463ab84448140d2c09336fdc75e8cb142d9e8c2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: property_name, require, witness. Outputs/bindings: (none).
Calls/effect boundaries: property_name, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[1].value::Call

Source: `infra/agentinfra/formal.py:117`; AST `f5472abdb55f54b60b0b17b5b29a179356cbfae00c94e8549a381a9966fd87c0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_name, require, witness. Outputs/bindings: (none).
Calls/effect boundaries: property_name, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[1].value.args[0]::Call

Source: `infra/agentinfra/formal.py:117`; AST `4049dba7c6f4a19c51a8592f2cad8fdcb55bf685ea9bfd488555ac59e86fb0cb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_name, witness. Outputs/bindings: (none).
Calls/effect boundaries: property_name.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[2]::Expr

Source: `infra/agentinfra/formal.py:118`; AST `802ac6319516ca1bca7cb5dcc2baf5f61f4a148f07a4bea5dd9d96a9d8afbf2a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, require, witness. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[2].value::Call

Source: `infra/agentinfra/formal.py:118`; AST `97a64dd40ec4fc0119a3c1577608ca353ce982de8dbc7a58825365789f810090`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, require, witness. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3]::Expr

Source: `infra/agentinfra/formal.py:119`; AST `88dda7f5322b2db20ec47a7f8cf59d7ad4f7aef72ec83cbbd59756f940d3d90a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, int, len, require, root, type, witness. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3].value::Call

Source: `infra/agentinfra/formal.py:119`; AST `ac65cf7c91617482d16183403d76e718012a54791ec6cbb52d156dca0ab2add1`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, int, len, require, root, type, witness. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, len, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:119`; AST `b1f45c55d6edf7bfcfe3033e265c9ba06b3e8f5b810097f80d4b8b0cce4c4440`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, witness. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1]::Call

Source: `infra/agentinfra/formal.py:119`; AST `097e7f7cfefcc5242ce01b581e014567aa354d66bf80f28e4c707a0a29b0681e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, len, root, witness. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines, len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1].args[0]::Call

Source: `infra/agentinfra/formal.py:119`; AST `f782a8993c667fc490da4202d7d5be6edd954f07cefc61565b67788a35910b08`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, witness. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, witness['file']).read_text, confined_path(root, witness['file']).read_text().splitlines.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1].args[0].func.value::Call

Source: `infra/agentinfra/formal.py:119`; AST `3f130695dc821748bc1be55ed7b94e333c43be9a6dc455e70158fcc29b28f2d3`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, witness. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, witness['file']).read_text.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1].args[0].func.value.func.value::Call

Source: `infra/agentinfra/formal.py:119`; AST `2d566f0b9cd0389d85b16bb86f4e45e21b83f2407814a8ac1a75a1b9184831ad`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, witness. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[16].body[3].value.args[0].values[1].comparators[1].args[0].func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[17]::If

Source: `infra/agentinfra/formal.py:120`; AST `39f6ea7424effcd70153535573c34767dae02c1661b3b67ef831b2a06dee36a2`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, o, require, scope, w, witnesses. Outputs/bindings: w.
Calls/effect boundaries: any, require, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[17].body[20].body[12].body[17]; no call, error or mutation may be omitted. Condition: scope['kind'] == 'production_rust_refinement_proved'
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[17].body[0]::Expr

Source: `infra/agentinfra/formal.py:121`; AST `5d461940f6efadbc1cf47f86066a9999fe65a2247fcb8eb1f9f3e30672c1db68`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, o, require, w, witnesses. Outputs/bindings: w.
Calls/effect boundaries: any, require, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20].body[12].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[17].body[0].value::Call

Source: `infra/agentinfra/formal.py:121`; AST `cc1a3a23e136e2523771e9c01283f5f5f4d90ab1a7ecb810d1c112ea0f2f59c6`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, o, require, w, witnesses. Outputs/bindings: w.
Calls/effect boundaries: any, require, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[17].body[0].value.args[0]::Call

Source: `infra/agentinfra/formal.py:121`; AST `89e8c942b1ae86730b7ff431d71d6b166dc9298f5585a1c81014f4ff2fca3dd0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, o, w, witnesses. Outputs/bindings: w.
Calls/effect boundaries: any, w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[17].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[17].body[0].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:121`; AST `eacd7b5cbe9de4a2bf92c3cfc2e63715c1a7a19de2fd5a55718b6f63e75f1dc5`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: o, w, witnesses. Outputs/bindings: w.
Calls/effect boundaries: w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[20].body[12].body[17].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[20].body[12].body[17].body[0].value.args[0].args[0].elt.values[1]::Call

Source: `infra/agentinfra/formal.py:121`; AST `08f7bda331c47795cf54de23943ba73e71d87c72067446ad21f5f761bc046b5a`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: w. Outputs/bindings: (none).
Calls/effect boundaries: w['file'].startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].body[12].body[17].body[0].value.args[0].args[0].elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[21]::Return

Source: `infra/agentinfra/formal.py:123`; AST `2896816ac328a1592bfa39e1a53f45dbb63f0e483efee6750e560664f3215c9f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: paths, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[17].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::validate_plan::root.body[17].body[21].value::Call

Source: `infra/agentinfra/formal.py:123`; AST `249bb69769b27f7324fd05d54a20c84c4a7c24f461f09392781414fab9e1e331`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: paths, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[17].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18]::FunctionDef

Source: `infra/agentinfra/formal.py:126`; AST `482bdb07df38ae4bdc8e48643d1c6996296b87c27cd1e2d1dbf6d3d36990f3c6`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: contract, digest, framework_identity, path, paths, profile, read, root, source_snapshot, validate_plan. Outputs/bindings: contract, paths.
Calls/effect boundaries: digest, framework_identity, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, paths.append, paths.extend, read, source_snapshot, validate_plan.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:127`; AST `9c94b215c091ae7259551ca94b8e51f69a18d73220a0649dadf23dfcd41c7b3e`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[1]::Assign

Source: `infra/agentinfra/formal.py:128`; AST `7b4ec202a85e627e3367163fe7b5de0a6500335e849f8ee8daf4b225aa3f28f0`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, read. Outputs/bindings: contract.
Calls/effect boundaries: read.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[1].value::Call

Source: `infra/agentinfra/formal.py:128`; AST `91c3d5a5c55109bb7973459de73203e5bd8e4e5495f77ef991ee808efd1b7914`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read. Outputs/bindings: (none).
Calls/effect boundaries: read.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[2]::Assign

Source: `infra/agentinfra/formal.py:129`; AST `603582833fe4b99444eed0505fd074c484505871a95bd44a63c36c4d81e263bb`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, profile, root, validate_plan. Outputs/bindings: paths.
Calls/effect boundaries: validate_plan.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[2].value::Call

Source: `infra/agentinfra/formal.py:129`; AST `0a180ca9c852f6e135e1a85bd8c1c58f669af66c36bd7aada97368dd3095d4c4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, profile, root, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: validate_plan.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[3]::Expr

Source: `infra/agentinfra/formal.py:130`; AST `d6b55d0c6049014b280001153161c441059392bc89bec7576dcb760265c30660`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, paths, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix, paths.append.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[3].value::Call

Source: `infra/agentinfra/formal.py:130`; AST `40d2416b6490705b45b44301c8972bf4d00acabec2c2821ffb8df884d0121f3e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, paths, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix, paths.append.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:130`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[3].value.args[0].func.value::Call

Source: `infra/agentinfra/formal.py:130`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[4]::Expr

Source: `infra/agentinfra/formal.py:132`; AST `ab183d97f233219738e2b4203c7a4458aa352479066fbba82bc39f72dc17640a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: paths, profile. Outputs/bindings: (none).
Calls/effect boundaries: paths.extend.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[4].value::Call

Source: `infra/agentinfra/formal.py:132`; AST `399d86bf8d902f0b550bc126ab0ebb5defc47265628819667dc9175721924f3e`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: paths, profile. Outputs/bindings: (none).
Calls/effect boundaries: paths.extend.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[5]::Return

Source: `infra/agentinfra/formal.py:133`; AST `a68888904a896be7b8f9db837ab7f88efac5e70b3a1fa92c6b52d67d62e37477`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, digest, framework_identity, path, paths, root, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: digest, framework_identity, path.read_bytes, source_snapshot.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[5].value.elts[0].values[0]::Call

Source: `infra/agentinfra/formal.py:133`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.elts[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[5].value.elts[0].values[0].args[0]::Call

Source: `infra/agentinfra/formal.py:133`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.elts[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[5].value.elts[0].values[1]::Call

Source: `infra/agentinfra/formal.py:133`; AST `223711a36bf7007646a036f120ef9bd931e73d1236969b01e03293c2cd971b82`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: framework_identity. Outputs/bindings: (none).
Calls/effect boundaries: framework_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.elts[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::current_identity::root.body[18].body[5].value.elts[0].values[2]::Call

Source: `infra/agentinfra/formal.py:134`; AST `9b6347edb49d0c9406694eb2c35aa6b5b3714372a63505494a833b418eb7f89b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: paths, root, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.elts[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::seal::root.body[19]::FunctionDef

Source: `infra/agentinfra/formal.py:137`; AST `e9b955c1b71316704be7a18a12f3998d33c0c630e0408ee34a2a2ea11a8f2157`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: data, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::seal::root.body[19].body[0]::Return

Source: `infra/agentinfra/formal.py:138`; AST `f886baf4e56ecb96c0874c85ee9822d50ab087095dd487d7a22d2e77770c17f8`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::seal::root.body[19].body[0].value.values[1]::Call

Source: `infra/agentinfra/formal.py:138`; AST `b0c503897caf703abe533bb0600d583443f37f6b77e693cbbe1f39a2936f5da9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20]::FunctionDef

Source: `infra/agentinfra/formal.py:141`; AST `4a2613c5a7acdf9497b1b86223eab765fc0e70404900cb755bb334b73cabb96f`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: data, dict, digest, path, read, require, sha, type. Outputs/bindings: data, sha.
Calls/effect boundaries: data.pop, digest, read, require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[0]::Assign

Source: `infra/agentinfra/formal.py:142`; AST `6d516f573bcf79b50140270fb9a0692a1b45b03eb5ea12dd15783b5cf7451457`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, read. Outputs/bindings: data.
Calls/effect boundaries: read.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[0].value::Call

Source: `infra/agentinfra/formal.py:142`; AST `91c3d5a5c55109bb7973459de73203e5bd8e4e5495f77ef991ee808efd1b7914`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read. Outputs/bindings: (none).
Calls/effect boundaries: read.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[1]::Expr

Source: `infra/agentinfra/formal.py:143`; AST `fdc322a41c3efad34f6f607d739eee7f30c311f0be40f32c74815f80c15eeb92`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, dict, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[1].value::Call

Source: `infra/agentinfra/formal.py:143`; AST `96c1e0d93b0f3623e2ad5ad7d45edc8a93fcd2833f4447f6ad3e3573876acbf9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, dict, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:143`; AST `8758fc05156f7bc226137ab99078e24f4d503cd1367495bb9600b1890e784a2d`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[2]::Assign

Source: `infra/agentinfra/formal.py:144`; AST `882a49530555125962d6cb7defab189f5587bf211884323e50b0de04b7b22a05`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: sha.
Calls/effect boundaries: data.pop.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[2].value::Call

Source: `infra/agentinfra/formal.py:144`; AST `eff7584753ef569fa181dad2575387a30448f78e08afcbb52c803cf04ed633f4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.pop.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[3]::Expr

Source: `infra/agentinfra/formal.py:145`; AST `110938f0bd8cefa714d1b4f85bb311a61f51826069b2f0bb3a63742c3fd091e5`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, digest, require, sha. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[3].value::Call

Source: `infra/agentinfra/formal.py:145`; AST `064cb5a4af3d9bc8160acd7a8776d1db453617c118a7083abe01b2dea76aa9dd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, digest, require, sha. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[3].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:145`; AST `b0c503897caf703abe533bb0600d583443f37f6b77e693cbbe1f39a2936f5da9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::unseal::root.body[20].body[4]::Return

Source: `infra/agentinfra/formal.py:146`; AST `a12e64fa3a041e609d3a25dc46c10c675ec5ec937a53909e14dc1d95d37a3c33`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21]::FunctionDef

Source: `infra/agentinfra/formal.py:149`; AST `55cd61721c29198b40804abfc9f7ca862bab7794c58c146f9dfa7cd781d46219`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, atomic_write_json, binding, confined_path, contract, current_identity, digest, identity, key, lock, name, o, path, profile, relative_path, require, root, seal, state_path. Outputs/bindings: binding, contract, identity, key, lock, o, path.
Calls/effect boundaries: FileLock, atomic_write_json, confined_path, current_identity, digest, lock.acquire, lock.release, relative_path, require, seal, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:150`; AST `68cbc4f1106689aed3b5639436c44387b8a237de7d3a0565b81eea5c3e75b320`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[1]::Expr

Source: `infra/agentinfra/formal.py:151`; AST `cef1b3c98a3bc481735231e7a1dda3e1c028cd0cd3faa43e03b628164ff8c23c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, relative_path, require. Outputs/bindings: (none).
Calls/effect boundaries: relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[1].value::Call

Source: `infra/agentinfra/formal.py:151`; AST `37d319eff59b7321ad5769af606e2ff3e53235af8f750d6d6a96b8fede0f0025`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, relative_path, require. Outputs/bindings: (none).
Calls/effect boundaries: relative_path, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[1].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:151`; AST `b14f1612b45f55f69d3b8e65cd5d2208506afdae15dfaad0223607d916546597`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, relative_path. Outputs/bindings: (none).
Calls/effect boundaries: relative_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[2]::Assign

Source: `infra/agentinfra/formal.py:152`; AST `358410bb143995a0ed42b0eea9917b1c3327250705f68486e6dedc5a2efeb48d`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, name, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[2].value::Call

Source: `infra/agentinfra/formal.py:152`; AST `84ad204db26e498c59a40ccefeec068f82fca59b0dd091cc081652642986ed46`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[3]::Assign

Source: `infra/agentinfra/formal.py:153`; AST `dd8bd58def53b060a435ac4eba5b22e2a600ac64cd333e27b0c39876fa78ef9b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root, state_path. Outputs/bindings: lock.
Calls/effect boundaries: FileLock, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[3].value::Call

Source: `infra/agentinfra/formal.py:153`; AST `5ca72ae4d893c36dcbe036cb0538739a5a686b0710a916ea8c57b6ffb40221fd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:153`; AST `b8f54753d02fe32a01066abb6c4fa58ca6fe6eff4e5905f1c34bcc033ef74ad3`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[4]::Expr

Source: `infra/agentinfra/formal.py:154`; AST `428763d06f915001746cebdf7dd12cafef877a86e9b481dec8ac0e4b0c995c09`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[4].value::Call

Source: `infra/agentinfra/formal.py:154`; AST `7b464e5c1137f26af8593e9de31970baaae7cd7f638e99176de038b1af8b46a2`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5]::Try

Source: `infra/agentinfra/formal.py:155`; AST `e2cbba1577bc9f2c36bde7c5afa68d9c84738ba4fcb060babeaae23a906909af`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: atomic_write_json, binding, contract, current_identity, digest, identity, key, lock, name, o, path, profile, root, seal, state_path. Outputs/bindings: binding, contract, identity, key, o.
Calls/effect boundaries: atomic_write_json, current_identity, digest, lock.release, seal, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[21].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[0]::Assign

Source: `infra/agentinfra/formal.py:156`; AST `794e8e186e8dc1d5b0f37ffdcf35dc8c670a74c6ced6d36a9de28cc2b1c14028`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_identity, path, profile, root. Outputs/bindings: contract, identity.
Calls/effect boundaries: current_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[0].value::Call

Source: `infra/agentinfra/formal.py:156`; AST `12660ee5e9b21225cb13a082ae12ee4a6161600c22aa59ba8c749fa4e72717ca`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_identity, path, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: current_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[1]::Assign

Source: `infra/agentinfra/formal.py:157`; AST `b96b1644ec5b8eb128d8c906128989c2b13a4e838601ff66a6f2fee4f83479a6`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, identity, name. Outputs/bindings: binding.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[2]::Assign

Source: `infra/agentinfra/formal.py:158`; AST `ec9a882c9557657873dcef4fad958794d2e7d8ce3f5faf314bbc9b8d53808be7`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, digest. Outputs/bindings: key.
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[2].value::Call

Source: `infra/agentinfra/formal.py:158`; AST `c7e2cfe9e2f6c8475b0f85e66e6a10d58191c017aefb441566c67f83ffaf1988`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[3]::Expr

Source: `infra/agentinfra/formal.py:159`; AST `426e77eb081faae50dec9e970efb799c5470aa92be174922eef33f50b8003218`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, binding, key, root, seal, state_path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, seal, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[3].value::Call

Source: `infra/agentinfra/formal.py:159`; AST `4e7f45e5472e237c252f82f93dbcf26bbef5628a384fdcab0aefd41d75c05000`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, binding, key, root, seal, state_path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, seal, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:159`; AST `5cab5a2beac5143ce67f6dcd2a1aa3b91bbe8a19eaef6124bf881699a2718dce`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[3].value.args[1]::Call

Source: `infra/agentinfra/formal.py:159`; AST `70e9259e93cf4ab35a95bd37f871b924e14c3938d675fad290cde1ed8e3cab9d`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, seal. Outputs/bindings: (none).
Calls/effect boundaries: seal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[4]::Expr

Source: `infra/agentinfra/formal.py:160`; AST `9adfb2ba34e8b651a1bc6ced48287429e825e45d5bee364ce65431744ce97ee9`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, key, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[4].value::Call

Source: `infra/agentinfra/formal.py:160`; AST `b35573149c69f040f89b8f2c30995dfb3c04e4af7ceeb4a231bede45578505d6`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, key, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[4].value.args[0]::Call

Source: `infra/agentinfra/formal.py:160`; AST `07872dc0d7456104c3dacac28183ccb83e9eafb9af38fc9e35a12f9bf347e699`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[5]::Return

Source: `infra/agentinfra/formal.py:161`; AST `d3019ff49701f38fa1b70cd90b6ce036e3face4975483e57f1bd308e211dcfd2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, key, o. Outputs/bindings: o.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[21].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].body[5].value.values[2]::ListComp

Source: `infra/agentinfra/formal.py:161`; AST `bc6c49dacde261cb544db8b1a58a946ff969f830360375d1180b9563c92f4765`.

Rust module: `infra::agentinfra::formal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: contract, o. Outputs/bindings: o.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ListComp evaluation at root.body[21].body[5].body[5].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/formal.py:164`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::bind::root.body[21].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/formal.py:164`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22]::FunctionDef

Source: `infra/agentinfra/formal.py:167`; AST `507860b0b2baf9697332a97b2d6aa718ff9968e4abe55080c83a2a5421bda45d`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: binding, confined_path, contract, current_identity, digest, identity, isinstance, key, pointer, profile, re, read, require, root, state_path, str, unseal. Outputs/bindings: binding, contract, identity, key, pointer.
Calls/effect boundaries: confined_path, current_identity, digest, isinstance, pointer.get, re.fullmatch, read, require, state_path, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:168`; AST `9b43f0d5264e996b21b07e0a8acc5a5a0f437b5928cac6813466c4cd9378bc4a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[22].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[1]::If

Source: `infra/agentinfra/formal.py:169`; AST `3d85096fd45fcd7bc21e5dde02eddccdfcf3fb88a689f97ebe59fa314e565d27`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: key, pointer, read, root, state_path. Outputs/bindings: key, pointer.
Calls/effect boundaries: pointer.get, read, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[22].body[1]; no call, error or mutation may be omitted. Condition: key is None
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[1].body[0]::Assign

Source: `infra/agentinfra/formal.py:170`; AST `cf37704be476d5e59ea549e5a2af18a21194063355a446641e861fda390115ad`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read, root, state_path. Outputs/bindings: pointer.
Calls/effect boundaries: read, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[1].body[0].value::Call

Source: `infra/agentinfra/formal.py:170`; AST `dbb8dd33ae3fe64045735cfb367d2ae5e355a45d72b41cf466748dea2dd0f165`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: read, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[1].body[0].value.args[0]::Call

Source: `infra/agentinfra/formal.py:170`; AST `07872dc0d7456104c3dacac28183ccb83e9eafb9af38fc9e35a12f9bf347e699`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[1].body[1]::Assign

Source: `infra/agentinfra/formal.py:171`; AST `3fe397a563c009f5bf8abddf2da6ce9579ef811264960ef0d9b6753ed97f8358`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pointer. Outputs/bindings: key.
Calls/effect boundaries: pointer.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[1].body[1].value::Call

Source: `infra/agentinfra/formal.py:171`; AST `9e720990d34a3ff499c37d7538975186e3189224963d9ec47be771e1159cb7cc`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pointer. Outputs/bindings: (none).
Calls/effect boundaries: pointer.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[2]::Expr

Source: `infra/agentinfra/formal.py:172`; AST `7139dba7348cc94e083799f70dda0544b14bd9a7a56cf1a070021fc04359166e`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, key, re, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, re.fullmatch, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[2].value::Call

Source: `infra/agentinfra/formal.py:172`; AST `f154659944cbac75fcfdb221dc134c6ead44cbd36739a19604e98560bfc36deb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, key, re, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, re.fullmatch, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[2].value.args[0].values[0]::Call

Source: `infra/agentinfra/formal.py:172`; AST `cacffec277269334f4a9162e0d5a17654327f612395602c8646ed68079c5452c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, key, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/formal.py:172`; AST `9d07c3af7f945bed30ca29407341a9dcd70560503d8d82d44763f0f08298d882`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, re. Outputs/bindings: (none).
Calls/effect boundaries: re.fullmatch.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[3]::Assign

Source: `infra/agentinfra/formal.py:173`; AST `d95f68f1ed34a17223b2f82ae51001b709a2eb15b1b8cf6707f875e1f9c4d6a6`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, root, state_path, unseal. Outputs/bindings: binding.
Calls/effect boundaries: state_path, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[3].value::Call

Source: `infra/agentinfra/formal.py:173`; AST `873422c36a3d7474acee0ff67ca146648ce30f5fc1c7c2898e57d14e72a3833c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, root, state_path, unseal. Outputs/bindings: (none).
Calls/effect boundaries: state_path, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:173`; AST `5cab5a2beac5143ce67f6dcd2a1aa3b91bbe8a19eaef6124bf881699a2718dce`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[4]::Expr

Source: `infra/agentinfra/formal.py:174`; AST `eafa8e5d4a060f4fd5abb54cb0614cf879d9e219fe3cb2c89ecf605a955bda3e`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, digest, key, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[4].value::Call

Source: `infra/agentinfra/formal.py:174`; AST `4dadf2f387a3125bd7c9c8b8047755f4e2bb3132d74c1121b3f9c57369ef40fd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, digest, key, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[4].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:174`; AST `c7e2cfe9e2f6c8475b0f85e66e6a10d58191c017aefb441566c67f83ffaf1988`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[5]::Assign

Source: `infra/agentinfra/formal.py:175`; AST `7bbe1f9390e89373ed1d30fe569326ef7a25edc033bf63a6c84a41e512b34181`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, confined_path, current_identity, profile, root. Outputs/bindings: contract, identity.
Calls/effect boundaries: confined_path, current_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[5].value::Call

Source: `infra/agentinfra/formal.py:175`; AST `2e72a021651b7b2a5e2607c9edfc5962cc17445d20599a0bf358000e9289b829`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, current_identity, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, current_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[5].value.args[2]::Call

Source: `infra/agentinfra/formal.py:175`; AST `e93e7f2e055f15c3c8a83d6679f6cba3cc79f2c763673a69522794ba24c465f4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[5].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[6]::Expr

Source: `infra/agentinfra/formal.py:176`; AST `44f49e924acb276acca2d4f7fab963447e01a048e6dca78837f237d543e1bc80`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, contract, identity, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[6].value::Call

Source: `infra/agentinfra/formal.py:176`; AST `84c7ee98e76733dd03ee99eedb7def23ffa6390455b19c19f48ad978946329aa`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, contract, identity, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::active::root.body[22].body[7]::Return

Source: `infra/agentinfra/formal.py:177`; AST `374c50a06d58e0a479ed72054e65fd28970953fc01b5b1f5f8206c17fe17a02b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, key. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[22].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23]::FunctionDef

Source: `infra/agentinfra/formal.py:180`; AST `805373303a8b74a88ed78a43fe78f45a9c9a31cde3b44ff16f05374032915a6b`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, KeyError, Namespace, OSError, ValueError, active, args, assurance, atomic_write_json, binding, blocker, bool, classified, current_receipt, exc, found, key, len, lock, o, observation, profile, proof, proof_identity, require, result, root, run_args, run_check, seal, state_path, status, str. Outputs/bindings: assurance, binding, blocker, found, key, lock, o, observation, proof, result, run_args, status.
Calls/effect boundaries: FileLock, Namespace, active, atomic_write_json, bool, classified, current_receipt, len, lock.acquire, lock.release, o.get, o.get('evidence', {}).get, proof_identity, require, result.get, run_check, seal, state_path, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:181`; AST `53e0871d9d0460b24438232424f6482afe0fe6d3e4b27429a77b0fa46d807cb6`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[23].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[1]::ImportFrom

Source: `infra/agentinfra/formal.py:182`; AST `4c69bade1ac40e732ef68ac776124b5276a1874d90f005bf6eb1a74fbc513643`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[23].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[2]::Assign

Source: `infra/agentinfra/formal.py:183`; AST `dd8bd58def53b060a435ac4eba5b22e2a600ac64cd333e27b0c39876fa78ef9b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root, state_path. Outputs/bindings: lock.
Calls/effect boundaries: FileLock, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[2].value::Call

Source: `infra/agentinfra/formal.py:183`; AST `5ca72ae4d893c36dcbe036cb0538739a5a686b0710a916ea8c57b6ffb40221fd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[2].value.args[0]::Call

Source: `infra/agentinfra/formal.py:183`; AST `b8f54753d02fe32a01066abb6c4fa58ca6fe6eff4e5905f1c34bcc033ef74ad3`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[3]::Expr

Source: `infra/agentinfra/formal.py:184`; AST `428763d06f915001746cebdf7dd12cafef877a86e9b481dec8ac0e4b0c995c09`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[3].value::Call

Source: `infra/agentinfra/formal.py:184`; AST `7b464e5c1137f26af8593e9de31970baaae7cd7f638e99176de038b1af8b46a2`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4]::Try

Source: `infra/agentinfra/formal.py:185`; AST `0233d49cc2ba1f5faeb99afb1c2eac2eec45089ce2049f8890b01eadf213039a`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, Namespace, OSError, ValueError, active, args, assurance, atomic_write_json, binding, blocker, bool, classified, current_receipt, exc, found, key, len, lock, o, observation, profile, proof, proof_identity, require, result, root, run_args, run_check, seal, state_path, status, str. Outputs/bindings: assurance, binding, blocker, found, key, o, observation, proof, result, run_args, status.
Calls/effect boundaries: Namespace, active, atomic_write_json, bool, classified, current_receipt, len, lock.release, o.get, o.get('evidence', {}).get, proof_identity, require, result.get, run_check, seal, state_path, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[23].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[0]::Assign

Source: `infra/agentinfra/formal.py:186`; AST `850e555bf144d1d621e719aa2efb04078540975a63ad2d353e56a8ea244317f5`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, profile, root. Outputs/bindings: binding, key.
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[0].value::Call

Source: `infra/agentinfra/formal.py:186`; AST `2ea43ca63e5b3694b839f14a3c538341f4f88ca97307c277fc3ee814b7ac2eef`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[1]::Assign

Source: `infra/agentinfra/formal.py:187`; AST `74b5522845bbccb2f3076be890b590763babccb0641c98ac58473631f0d95c68`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, binding, o. Outputs/bindings: found, o.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[1].value::ListComp

Source: `infra/agentinfra/formal.py:187`; AST `23d7f776cbcd2caa507fba76104cc15a15e58547cdb89ce572b9fcb8510eae0a`.

Rust module: `infra::agentinfra::formal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: args, binding, o. Outputs/bindings: o.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ListComp evaluation at root.body[23].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[2]::Expr

Source: `infra/agentinfra/formal.py:188`; AST `f34ff1d34e79dba4ba19951edcf71eb3e78af3a3f1d951238a2a827be3b7a9f9`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[2].value::Call

Source: `infra/agentinfra/formal.py:188`; AST `7a337d2a52612c31378e1a2343bcfb6e2b4b46115215e3564fad49d43948083c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: found, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[2].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:188`; AST `244363a48c07bc804849e1e3fab8f87a0778954985423a260ac19a807987865c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: found, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[3]::Assign

Source: `infra/agentinfra/formal.py:189`; AST `38c1714dbfea12dab63ec2e8b705f3333ab8c9cc514805ee2829290f638f5b23`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found. Outputs/bindings: o.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[4]::Assign

Source: `infra/agentinfra/formal.py:190`; AST `ef7273d72513e364bc50e98a66d9a3f76f667e0f0b72f566df6d9243185c1170`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, proof_identity, root. Outputs/bindings: proof.
Calls/effect boundaries: proof_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[4].value::Call

Source: `infra/agentinfra/formal.py:190`; AST `6672b93afdc4745907b3bea058011fe4a9a4a64c9c060b1acf9b8d25f95eb450`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, proof_identity, root. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[5]::Assign

Source: `infra/agentinfra/formal.py:191`; AST `154bd55a27bff804a9db882efdb3bc050da3181ee3e0de980194553855c8b783`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Namespace, args, bool, o. Outputs/bindings: run_args.
Calls/effect boundaries: Namespace, bool, o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[5].value::Call

Source: `infra/agentinfra/formal.py:191`; AST `818b6f4232be8d17151a0949e760570b9fb7d12465419530a649ad53317bebfc`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Namespace, args, bool, o. Outputs/bindings: (none).
Calls/effect boundaries: Namespace, bool, o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[5].value.keywords[5].value::Call

Source: `infra/agentinfra/formal.py:194`; AST `e63858ddd77b102be9f45b09423d3526903813387207101991b8af7ce0dfd165`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, bool. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[5].value.keywords[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[5].value.keywords[11].value::Call

Source: `infra/agentinfra/formal.py:196`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[5].value.keywords[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[6]::Assign

Source: `infra/agentinfra/formal.py:197`; AST `b123efce8348e34b0785a015f6b20b24287087f01df4984f791af5d2d40c6007`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, root, run_args, run_check. Outputs/bindings: result.
Calls/effect boundaries: run_check.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[6].value::Call

Source: `infra/agentinfra/formal.py:197`; AST `369a05db7981323d4d670b2bfc906f00effd5a178aef084582fd992da0af9ed3`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, root, run_args, run_check. Outputs/bindings: (none).
Calls/effect boundaries: run_check.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[7]::Expr

Source: `infra/agentinfra/formal.py:199`; AST `6366d5c1bf8d171babc0197273e6c8cae9e802c4542bce4a8b21b27484e0109f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[7].value::Call

Source: `infra/agentinfra/formal.py:199`; AST `2ea43ca63e5b3694b839f14a3c538341f4f88ca97307c277fc3ee814b7ac2eef`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[8]::Assign

Source: `infra/agentinfra/formal.py:200`; AST `748b8f5460a61f004edb36555f8b58e0bc9d140bd99087b9ac1a8910dbd3324c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: status.
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[8].value.test.values[0]::Call

Source: `infra/agentinfra/formal.py:200`; AST `7fbc6677b25779d824f697eaf55bf708b84de69b9d99ec78a3eb02b5e4b275ba`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[8].value.test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[9]::Assign

Source: `infra/agentinfra/formal.py:201`; AST `12d6131a09626d39a69e105d4d4b2a0d7bece9d7a37ffb3b90c45c5cb7df62e3`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: assurance, blocker.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10]::If

Source: `infra/agentinfra/formal.py:202`; AST `3571746ef94720dde54789c97a8f7888f3c2d32e38f0d2c27938b428a3dbf7bf`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: KeyError, OSError, ValueError, classified, current_receipt, exc, o, profile, result, root, status, str. Outputs/bindings: assurance, blocker, status.
Calls/effect boundaries: classified, current_receipt, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[23].body[4].body[10]; no call, error or mutation may be omitted. Condition: status == 'CHECKED_SCOPED'
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0]::Try

Source: `infra/agentinfra/formal.py:203`; AST `f48868492c6554579b71c6d488658bf72551160a2365d108ccb9140b76f234c7`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, ValueError, classified, current_receipt, exc, o, profile, result, root, str. Outputs/bindings: assurance, blocker, status.
Calls/effect boundaries: classified, current_receipt, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[23].body[4].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0].body[0]::Assign

Source: `infra/agentinfra/formal.py:204`; AST `cf07f301b29b8aa4c96614bfba5528044e51aeac1f812cec45eac5406095f106`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classified, current_receipt, o, profile, result, root. Outputs/bindings: assurance.
Calls/effect boundaries: classified, current_receipt.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0].body[0].value::Call

Source: `infra/agentinfra/formal.py:204`; AST `04465581c48e81f51b59795c8ae881e14b7478aeb1fcfb832be60270dd613de4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, current_receipt, o, profile, result, root. Outputs/bindings: (none).
Calls/effect boundaries: classified, current_receipt.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0].body[0].value.args[2]::Call

Source: `infra/agentinfra/formal.py:204`; AST `910b661c55310f805b3a3861429efe23d94fda159e5a6591f0ae6837f3d64aff`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_receipt, profile, result, root. Outputs/bindings: (none).
Calls/effect boundaries: current_receipt.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[10].body[0].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/formal.py:205`; AST `b105cae39c8ee49d78db101063e3e3cb83455a3fcb29af168d54a068e173655c`.

Rust module: `infra::agentinfra::formal`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: KeyError, OSError, ValueError, exc, str. Outputs/bindings: blocker, status.
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[23].body[4].body[10].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0].handlers[0].body[0]::Assign

Source: `infra/agentinfra/formal.py:206`; AST `ee66591de41747fef8a116d6e3e73d250ec2a86a1167318584fec00fbf04debf`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, str. Outputs/bindings: blocker, status.
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[10].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[10].body[0].handlers[0].body[0].value.elts[1]::Call

Source: `infra/agentinfra/formal.py:206`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[10].body[0].handlers[0].body[0].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[11]::Assign

Source: `infra/agentinfra/formal.py:207`; AST `de7911646e6aa28a120c809d197403da72198d920d844c9ae1b2039d0e6ff051`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, blocker, key, o, proof, result, status. Outputs/bindings: observation.
Calls/effect boundaries: o.get, o.get('evidence', {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[11].value.values[7]::Call

Source: `infra/agentinfra/formal.py:209`; AST `33bced0a41f276980480302d43b4fd8b8ddb91aead63b4b903b8168ee5bc49ce`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get, o.get('evidence', {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[11].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[11].value.values[7].func.value::Call

Source: `infra/agentinfra/formal.py:209`; AST `b0c5628a059ea6d452330eda006070cba6299808b7782c2737d8962bb298ff2b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[11].value.values[7].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[12]::Expr

Source: `infra/agentinfra/formal.py:211`; AST `6ace00993e37f99ceff3b57b9dcea377d84236b58c29183a1a24c0325dac7252`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, key, o, observation, root, seal, state_path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, seal, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[4].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[12].value::Call

Source: `infra/agentinfra/formal.py:211`; AST `e294d12a917ac9b7d4ea5643bd4ad2e030860490dddc52b7aff9af2aa8a79e2d`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, key, o, observation, root, seal, state_path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, seal, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[12].value.args[0]::Call

Source: `infra/agentinfra/formal.py:211`; AST `642eb4c0084ecd0c28382291fccea5280641c11ffef4b203233425093cb36e15`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, o, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[12].value.args[1]::Call

Source: `infra/agentinfra/formal.py:211`; AST `ffb3935e2cb814d6feec7d441449c6432101d04f5b7c3121e392c2820af7d902`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, seal. Outputs/bindings: (none).
Calls/effect boundaries: seal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].body[12].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].body[13]::Return

Source: `infra/agentinfra/formal.py:212`; AST `5987e36d9ed4a2a06ae6f66c5ab3f523a5aa2b1a4b9a2b4ea08b3d5fe7a7a7ae`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[23].body[4].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].finalbody[0]::Expr

Source: `infra/agentinfra/formal.py:214`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[4].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::verify::root.body[23].body[4].finalbody[0].value::Call

Source: `infra/agentinfra/formal.py:214`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24]::FunctionDef

Source: `infra/agentinfra/formal.py:217`; AST `47cb56622360ce2e7554ea4878aab5647d78639d2cccd9861413f89a2a559df8`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, KeyError, OSError, SimpleNamespace, ValueError, active, all, assertion_locations, assurance, binding, binding_key, blocker, classified, current_receipt, exc, expected, kani_properties, key, len, location, lock, name, o, path, profile, proof_identity, proof_output, properties, property_location, r, receipt, record, require, root, rows, state_path, status, str, unseal. Outputs/bindings: assertion_locations, assurance, binding, blocker, expected, key, location, lock, name, o, path, properties, r, receipt, record, rows, status.
Calls/effect boundaries: (record or {}).get, (record or {}).get('result', {}).get, FileLock, SimpleNamespace, active, all, assertion_locations.values, blocker.startswith, classified, current_receipt, kani_properties, len, lock.acquire, lock.release, o.get, o.get('evidence', {}).get, path.exists, proof_identity, proof_output, property_location, record.get, require, rows.append, state_path, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[0]::ImportFrom

Source: `infra/agentinfra/formal.py:218`; AST `9b43f0d5264e996b21b07e0a8acc5a5a0f437b5928cac6813466c4cd9378bc4a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[1]::ImportFrom

Source: `infra/agentinfra/formal.py:219`; AST `92cd554b1ff6e35d3e103a22c41915a02928b34df7fc6b5264321816e0d76839`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[24].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[2]::ImportFrom

Source: `infra/agentinfra/formal.py:220`; AST `271cd8a5819453f6952690fd43e9ce152386df249c8de9a1999907454b0006b7`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[24].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[3]::Assign

Source: `infra/agentinfra/formal.py:221`; AST `dd8bd58def53b060a435ac4eba5b22e2a600ac64cd333e27b0c39876fa78ef9b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root, state_path. Outputs/bindings: lock.
Calls/effect boundaries: FileLock, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[3].value::Call

Source: `infra/agentinfra/formal.py:221`; AST `5ca72ae4d893c36dcbe036cb0538739a5a686b0710a916ea8c57b6ffb40221fd`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:221`; AST `b8f54753d02fe32a01066abb6c4fa58ca6fe6eff4e5905f1c34bcc033ef74ad3`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[4]::Expr

Source: `infra/agentinfra/formal.py:222`; AST `428763d06f915001746cebdf7dd12cafef877a86e9b481dec8ac0e4b0c995c09`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[4].value::Call

Source: `infra/agentinfra/formal.py:222`; AST `7b464e5c1137f26af8593e9de31970baaae7cd7f638e99176de038b1af8b46a2`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5]::Try

Source: `infra/agentinfra/formal.py:223`; AST `8ae9bcac8b7d69a37e284a70bd9d3ead5e352890d5dd856535e4361c23d3e559`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, SimpleNamespace, ValueError, active, all, assertion_locations, assurance, binding, binding_key, blocker, classified, current_receipt, exc, expected, kani_properties, key, len, location, lock, name, o, path, profile, proof_identity, proof_output, properties, property_location, r, receipt, record, require, root, rows, state_path, status, str, unseal. Outputs/bindings: assertion_locations, assurance, binding, blocker, expected, key, location, name, o, path, properties, r, receipt, record, rows, status.
Calls/effect boundaries: (record or {}).get, (record or {}).get('result', {}).get, SimpleNamespace, active, all, assertion_locations.values, blocker.startswith, classified, current_receipt, kani_properties, len, lock.release, o.get, o.get('evidence', {}).get, path.exists, proof_identity, proof_output, property_location, record.get, require, rows.append, state_path, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[24].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[0]::Assign

Source: `infra/agentinfra/formal.py:224`; AST `84458d7a1f1f651cae094947daa8e07570a0a4d0399735a6d932fce3bb23a153`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, binding_key, profile, root. Outputs/bindings: binding, key.
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[0].value::Call

Source: `infra/agentinfra/formal.py:224`; AST `446c4429ca21a94319c9faf9f37bd20d6e9c4820199c13ffe52da465e525bc23`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, binding_key, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[1]::Assign

Source: `infra/agentinfra/formal.py:225`; AST `ac5dc778d890ac7d3fe32248966b866f064c4894b141595ccc25455eb29f5366`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2]::For

Source: `infra/agentinfra/formal.py:226`; AST `f8d2109c3b5d8eedb6711e1a7e83e8e7162c274841e5860b207236f7d9e0b9c0`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: KeyError, OSError, SimpleNamespace, ValueError, all, assertion_locations, assurance, binding, blocker, classified, current_receipt, exc, expected, kani_properties, key, len, location, name, o, path, profile, proof_identity, proof_output, properties, property_location, receipt, record, require, root, rows, state_path, status, str, unseal. Outputs/bindings: assertion_locations, assurance, blocker, expected, location, name, o, path, properties, receipt, record, status.
Calls/effect boundaries: (record or {}).get, (record or {}).get('result', {}).get, SimpleNamespace, all, assertion_locations.values, blocker.startswith, classified, current_receipt, kani_properties, len, o.get, o.get('evidence', {}).get, path.exists, proof_identity, proof_output, property_location, record.get, require, rows.append, state_path, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[24].body[5].body[2]; no call, error or mutation may be omitted. Iteration: o in binding['contract']['obligations']
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[0]::Assign

Source: `infra/agentinfra/formal.py:227`; AST `2e419e9498343d09221744e84461e0f0f4be3e4a81d71a53709400204e57d949`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, o, root, state_path. Outputs/bindings: path.
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[0].value::Call

Source: `infra/agentinfra/formal.py:227`; AST `642eb4c0084ecd0c28382291fccea5280641c11ffef4b203233425093cb36e15`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, o, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[1]::Assign

Source: `infra/agentinfra/formal.py:228`; AST `17feea6ccd0c7c430672a80251de8455240ed87acfd20e225ed8c5c36e901fff`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[2]::Assign

Source: `infra/agentinfra/formal.py:229`; AST `9e8043287e300e255bde20c2cbc1826554b0f9c81734cfd3915524e757b76ae7`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: assurance, blocker, record.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[3]::Assign

Source: `infra/agentinfra/formal.py:230`; AST `043a0fbcb0692cb6f891a3be5e339ad4a3ce3aeab192905803d6dcfbc7133a43`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: assertion_locations.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4]::If

Source: `infra/agentinfra/formal.py:231`; AST `2228f5f81f28d283fc8cdca95c9d71fd770a3deed5d16bdabd029dd9da733798`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: KeyError, OSError, SimpleNamespace, ValueError, all, assertion_locations, blocker, classified, current_receipt, exc, expected, kani_properties, key, len, location, name, o, path, profile, proof_identity, proof_output, properties, property_location, receipt, record, require, root, status, str, unseal. Outputs/bindings: assertion_locations, assurance, blocker, expected, location, name, properties, receipt, record, status.
Calls/effect boundaries: SimpleNamespace, all, assertion_locations.values, blocker.startswith, classified, current_receipt, kani_properties, len, o.get, path.exists, proof_identity, proof_output, property_location, record.get, require, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[24].body[5].body[2].body[4]; no call, error or mutation may be omitted. Condition: path.exists()
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].test::Call

Source: `infra/agentinfra/formal.py:231`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[0]::Assign

Source: `infra/agentinfra/formal.py:232`; AST `79cbe29dda4f022d2e1e8224f4e1081629ba878dc9753ba0849695b13125c4cf`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, unseal. Outputs/bindings: record.
Calls/effect boundaries: unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[0].value::Call

Source: `infra/agentinfra/formal.py:232`; AST `568af2bc89ce861a8a6a796d7b6f2a9db1fd6cf14ffbe1799810f22aa8706cf0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, unseal. Outputs/bindings: (none).
Calls/effect boundaries: unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[1]::Expr

Source: `infra/agentinfra/formal.py:233`; AST `03a98e2abe360e8021a403bb2f98b8117111ffaec307038b86851e9771700250`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, o, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[1].value::Call

Source: `infra/agentinfra/formal.py:233`; AST `f87f9ef9dee2c2fc958858712ca8a38550c064cb554570b53c50010e9f3018e1`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, o, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[2]::Assign

Source: `infra/agentinfra/formal.py:234`; AST `5899ea1e64da8e4b3a254830b0fbd8ff634620021f7a8a55c7b32dec291499a3`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3]::If

Source: `infra/agentinfra/formal.py:235`; AST `3f75d94abc6c8f18167e041dbdb0c240c62f577275182e1878948d8ec2e5e4b8`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: KeyError, OSError, SimpleNamespace, ValueError, all, assertion_locations, blocker, classified, current_receipt, exc, expected, kani_properties, len, location, name, o, profile, proof_identity, proof_output, properties, property_location, receipt, record, require, root, status, str. Outputs/bindings: assertion_locations, assurance, blocker, expected, location, name, properties, receipt, status.
Calls/effect boundaries: SimpleNamespace, all, assertion_locations.values, blocker.startswith, classified, current_receipt, kani_properties, len, o.get, proof_identity, proof_output, property_location, record.get, require, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[24].body[5].body[2].body[4].body[3]; no call, error or mutation may be omitted. Condition: status == 'CHECKED_SCOPED'
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0]::Try

Source: `infra/agentinfra/formal.py:236`; AST `5e84b4bd5c1af1298fbdbcb977207418e2ecafcf383b0b84b0a7ba6da0799804`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, SimpleNamespace, ValueError, all, assertion_locations, blocker, classified, current_receipt, exc, expected, kani_properties, len, location, name, o, profile, proof_identity, proof_output, properties, property_location, receipt, record, require, root, str. Outputs/bindings: assertion_locations, assurance, blocker, expected, location, name, properties, receipt, status.
Calls/effect boundaries: SimpleNamespace, all, assertion_locations.values, blocker.startswith, classified, current_receipt, kani_properties, len, o.get, proof_identity, proof_output, property_location, record.get, require, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/formal.py:237`; AST `dbefc3b4496040f9da8d0bf33fbd2c7b17a41d790f4f1c01b49278fda0c945f4`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, proof_identity, record, require, root. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity, record.get, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/formal.py:237`; AST `985784c9dcc2eb38e519e60d6c1df311296f696b8620b9735ed0a63a889b8538`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, proof_identity, record, require, root. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity, record.get, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[0].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:237`; AST `385175ff426beee97ee9ae80977abddd3860bed33e55f450b97d48151d9a6250`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/formal.py:237`; AST `6672b93afdc4745907b3bea058011fe4a9a4a64c9c060b1acf9b8d25f95eb450`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, proof_identity, root. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[1]::Assign

Source: `infra/agentinfra/formal.py:238`; AST `7ed588728a8c068208c85f21fef6af18886f70186d6f1e75fab9d349789a800b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_receipt, profile, record, root. Outputs/bindings: receipt.
Calls/effect boundaries: current_receipt.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[1].value::Call

Source: `infra/agentinfra/formal.py:238`; AST `1bb317820184e16271cccb1c79b69c15ac7ca1950cd3eff85023a85e970cb84a`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_receipt, profile, record, root. Outputs/bindings: (none).
Calls/effect boundaries: current_receipt.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[2]::Expr

Source: `infra/agentinfra/formal.py:239`; AST `ae3235b0f5b9852d97dd13f7862d56be42630d96949a516bf40a144c03e79e2d`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[2].value::Call

Source: `infra/agentinfra/formal.py:239`; AST `aabd9178b85ceb6bde9731a042af598f176206798184d697ea28e43318e5aee1`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[3]::Assign

Source: `infra/agentinfra/formal.py:240`; AST `13acf79a3e9506fafeb1d380af748f3fa0d4efda047513560df2c8b3f55c3b92`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o. Outputs/bindings: expected.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[4]::If

Source: `infra/agentinfra/formal.py:241`; AST `75343ae82ca53b093c5d45f77c29ccbbf932441cce8e1b3b767cee34b334612f`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: expected, o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[4]; no call, error or mutation may be omitted. Condition: o['method'] == 'kani'
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[4].body[0]::Assign

Source: `infra/agentinfra/formal.py:242`; AST `ae1602ce5af8b6df6a0a845d48c5f55c2c4d46eaf74c02a3abccc964e904590c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[4].body[0].value::Call

Source: `infra/agentinfra/formal.py:242`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[5]::Expr

Source: `infra/agentinfra/formal.py:243`; AST `38233d1ce02cab008a3d176e14eba7a848cc27b134e9d55249586cbac6f1b433`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[5].value::Call

Source: `infra/agentinfra/formal.py:243`; AST `e77d1c50cec7789fcd0a08764944965ccf7549d23665542da75d57977f5dc8fb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[6]::Expr

Source: `infra/agentinfra/formal.py:244`; AST `ddf77e9591432cb2df498efed93e3b68249405e7538cd4d1799005498cf0a7cb`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SimpleNamespace, expected, len, proof_output, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, len, proof_output, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value::Call

Source: `infra/agentinfra/formal.py:244`; AST `7e2cfe9194494c36fd2582e3a1a62db1472488ea09023ff0d5a269c1d8329744`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, expected, len, proof_output, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, len, proof_output, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/formal.py:244`; AST `73055efa44b0e420e6e94249b2bd2de089c21a8056c5601afe83e21e2f3977e7`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, receipt. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value.args[0].values[1]::Call

Source: `infra/agentinfra/formal.py:244`; AST `5eafa02c33ccaef83546d005bb6ef9c66f971e50fd456ff01e2bacf5bd9ff3fb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, expected, proof_output, receipt. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, proof_output.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value.args[0].values[1].args[1]::Call

Source: `infra/agentinfra/formal.py:244`; AST `0ab2c29cca03e583c1e9f21ef41e3616987f0bb1d53464b69865db4e6885bf99`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, receipt. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[6].value.args[0].values[1].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[7]::Assign

Source: `infra/agentinfra/formal.py:245`; AST `bb6d3d43e4b40232ea65dbcf1b3905384132295ddc1d2c4c2aaf5cc2ba7ee666`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classified, o, receipt, root. Outputs/bindings: assurance.
Calls/effect boundaries: classified.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[7].value::Call

Source: `infra/agentinfra/formal.py:245`; AST `971932321f495d1ebf90bfa57b0842a746315fcc428402da66a1ce1c54f2583a`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, o, receipt, root. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8]::If

Source: `infra/agentinfra/formal.py:246`; AST `225efb97e3dd6c75ca52080be42036b5fd02be64fe8d81d6046fcf7844ca570e`.

Rust module: `infra::agentinfra::formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: all, assertion_locations, kani_properties, location, name, o, properties, property_location, receipt, require, root. Outputs/bindings: assertion_locations, location, name, properties.
Calls/effect boundaries: all, assertion_locations.values, kani_properties, o.get, property_location, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered If evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8]; no call, error or mutation may be omitted. Condition: o['method'] == 'kani' and o.get('evidence')
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].test.values[1]::Call

Source: `infra/agentinfra/formal.py:246`; AST `061b4b29b4f1af1b4bf971ac7f21552c205941cc4efd01243f6c677d8b4fa3a9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[0]::Assign

Source: `infra/agentinfra/formal.py:247`; AST `c4969e66b34f21074055bf30843c5787bca095a242a6ea42961bf566c4dac3de`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kani_properties, receipt. Outputs/bindings: properties.
Calls/effect boundaries: kani_properties.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[0].value::Call

Source: `infra/agentinfra/formal.py:247`; AST `22233a24c3f0af40f005f2458248e4db61d55875498d285cfb39fa7dae7af8f4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kani_properties, receipt. Outputs/bindings: (none).
Calls/effect boundaries: kani_properties.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1]::Assign

Source: `infra/agentinfra/formal.py:248`; AST `f4accc86a233e21dd4bcfae1d4136830488c3322d88d1f908828f193fd5ae545`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, o, properties, property_location, root. Outputs/bindings: assertion_locations, name.
Calls/effect boundaries: o.get, property_location.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1].value::DictComp

Source: `infra/agentinfra/formal.py:248`; AST `17a63819f6f09b0bd1a97521c5a4e1f336c383db09035180fb9e09d25df05998`.

Rust module: `infra::agentinfra::formal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: name, o, properties, property_location, root. Outputs/bindings: name.
Calls/effect boundaries: o.get, property_location.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered DictComp evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1].value.value::Call

Source: `infra/agentinfra/formal.py:248`; AST `ff894a72b3c2051b9601f5944af27708610a16cec0f3e9f61c7feac81582cc1c`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, o, properties, property_location, root. Outputs/bindings: (none).
Calls/effect boundaries: o.get, property_location.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1].value.value.args[1]::Call

Source: `infra/agentinfra/formal.py:248`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[1].value.value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2]::Expr

Source: `infra/agentinfra/formal.py:250`; AST `9c812c3bbe6d5e9e835736d2e5c43de42af665e4f957846554a725205594ab1f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, assertion_locations, location, require. Outputs/bindings: location.
Calls/effect boundaries: all, assertion_locations.values, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value::Call

Source: `infra/agentinfra/formal.py:250`; AST `dd86054ec38c5a4a1582d11641190460931e6ba030b90bf993e1c969bf84ec8f`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, assertion_locations, location, require. Outputs/bindings: location.
Calls/effect boundaries: all, assertion_locations.values, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value.args[0]::Call

Source: `infra/agentinfra/formal.py:250`; AST `8740e79b949168c7cfcd6e86fb4be2699af0bfd68c9c9499fafe78d7a2ae3dfb`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, assertion_locations, location. Outputs/bindings: location.
Calls/effect boundaries: all, assertion_locations.values.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:250`; AST `387c9001afee6f9da85b1600bc708e0781333e4d8389fd3a7eb54551af810d2a`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: assertion_locations, location. Outputs/bindings: location.
Calls/effect boundaries: assertion_locations.values.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value.args[0].args[0].generators[0].iter::Call

Source: `infra/agentinfra/formal.py:250`; AST `cfbb252cb5941bb822d71b8d60b47022e2cad86ba91468c00ea47012f852252a`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion_locations. Outputs/bindings: (none).
Calls/effect boundaries: assertion_locations.values.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].body[8].body[2].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/formal.py:252`; AST `d92fd55dd098a9c307554b8fa613e1bbc6b47786d87a27f9873daf9c219e6ea4`.

Rust module: `infra::agentinfra::formal`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: KeyError, OSError, ValueError, blocker, exc, str. Outputs/bindings: blocker, status.
Calls/effect boundaries: blocker.startswith, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[0]::Assign

Source: `infra/agentinfra/formal.py:253`; AST `6d52e3b6813870453b847d26d6ed649eda49b6ca98f91b5447f3803dd00e127f`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, str. Outputs/bindings: blocker.
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[0].value::Call

Source: `infra/agentinfra/formal.py:253`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[1]::Assign

Source: `infra/agentinfra/formal.py:254`; AST `7c8fe5ea408f3de0ce8e7ba7cc88fa9f0802d9728eb57d70f79278c67baf6ae9`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: blocker. Outputs/bindings: status.
Calls/effect boundaries: blocker.startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[1].value.test::Call

Source: `infra/agentinfra/formal.py:254`; AST `d709084c810b810f258de23ea357b16ba038a94736d42cabd9860e0787886568`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blocker. Outputs/bindings: (none).
Calls/effect boundaries: blocker.startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[1].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[1].value.orelse.test::Call

Source: `infra/agentinfra/formal.py:254`; AST `a3b2d27affe6b51af018097215c90bc866027c39cee7a036daf74bb17c3ce2d4`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blocker. Outputs/bindings: (none).
Calls/effect boundaries: blocker.startswith.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[4].body[3].body[0].handlers[0].body[1].value.orelse.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5]::Expr

Source: `infra/agentinfra/formal.py:255`; AST `92e27dc7f3ef57a775c9166aa2715d7f625c7e84051fe7c9c1a30e44a4825688`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertion_locations, assurance, blocker, o, profile, proof_identity, record, root, rows, status. Outputs/bindings: (none).
Calls/effect boundaries: (record or {}).get, (record or {}).get('result', {}).get, o.get, o.get('evidence', {}).get, proof_identity, rows.append.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value::Call

Source: `infra/agentinfra/formal.py:255`; AST `f70e3553dd5199802f8ccde4940f17f659885cc5898cdc2df21ece0a9fe99fd9`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion_locations, assurance, blocker, o, profile, proof_identity, record, root, rows, status. Outputs/bindings: (none).
Calls/effect boundaries: (record or {}).get, (record or {}).get('result', {}).get, o.get, o.get('evidence', {}).get, proof_identity, rows.append.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[4]::Call

Source: `infra/agentinfra/formal.py:256`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[5]::Call

Source: `infra/agentinfra/formal.py:257`; AST `c88dcaa478561ef1dda13eb3752bb90b2c6b7b09530fe48d3fa24d2e84de6c0b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get, o.get('evidence', {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[5].func.value::Call

Source: `infra/agentinfra/formal.py:257`; AST `b0c5628a059ea6d452330eda006070cba6299808b7782c2737d8962bb298ff2b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[5].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[8].values[1]::Call

Source: `infra/agentinfra/formal.py:259`; AST `d6aca6f5bf8401b0ca60b38980f0271226b09c3d4b88302681efa14b7be60a38`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (record or {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[8].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[9]::Call

Source: `infra/agentinfra/formal.py:260`; AST `6672b93afdc4745907b3bea058011fe4a9a4a64c9c060b1acf9b8d25f95eb450`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, proof_identity, root. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[11]::Call

Source: `infra/agentinfra/formal.py:262`; AST `4d970d5f245e67a91e16f1a39fadd0855191bce7fb7bf3184da37ecb89afefee`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (record or {}).get, (record or {}).get('result', {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[11].func.value::Call

Source: `infra/agentinfra/formal.py:262`; AST `a8afe162deb4674b41a06d37e12cef65a14ca4040f68d17a773394a3fac607aa`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (record or {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[11].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[12]::Call

Source: `infra/agentinfra/formal.py:263`; AST `33bced0a41f276980480302d43b4fd8b8ddb91aead63b4b903b8168ee5bc49ce`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get, o.get('evidence', {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[2].body[5].value.args[0].values[12].func.value::Call

Source: `infra/agentinfra/formal.py:263`; AST `b0c5628a059ea6d452330eda006070cba6299808b7782c2737d8962bb298ff2b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].body[5].value.args[0].values[12].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[3]::Expr

Source: `infra/agentinfra/formal.py:266`; AST `3bd41227e4833e4a86d3a4b1df2608694bcc4bb862c974addcac4de9c97989c5`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, key, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[3].value::Call

Source: `infra/agentinfra/formal.py:266`; AST `26508957b303ac0512c7f22e8edf02954cbdee98ec4592277761d3e7967ad3f8`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, key, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: active.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[4]::Return

Source: `infra/agentinfra/formal.py:267`; AST `b2d38fe0990c29bb0e048385f62a0b78894f7b31d663774646a1a9a774ed352b`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, key, r, rows. Outputs/bindings: r.
Calls/effect boundaries: all.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[24].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[4].value.values[0].test::Call

Source: `infra/agentinfra/formal.py:267`; AST `abe9d6702487b87ecf03ecb6855549e162a242c95d3c9bed8e733a2198ba3a41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, r, rows. Outputs/bindings: r.
Calls/effect boundaries: all.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[4].value.values[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].body[4].value.values[0].test.args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:267`; AST `fd334b9cb3221fdc42f12ae7441cadc861fd3fabf6732428bd7f9c83ccccea9e`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[24].body[5].body[4].value.values[0].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/formal.py:271`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::audit::root.body[24].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/formal.py:271`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25]::FunctionDef

Source: `infra/agentinfra/formal.py:274`; AST `b98ded25009fa9b9878d001efe5dc8addf3e3c57cfefd42b3ee4b2d916b9d9a8`.

Rust module: `infra::agentinfra::formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: KeyError, OSError, RuntimeError, ValueError, audit, binding, blockers, exc, len, o, path, paths, profile, r, require, result, root, rows, sorted, state_path, str, unseal. Outputs/bindings: binding, blockers, o, path, paths, r, result, rows.
Calls/effect boundaries: audit, blockers.append, len, o.get, o.get('evidence', {}).get, require, rows.append, rows.extend, sorted, state_path, state_path(root, 'bindings').glob, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[0]::Expr

Source: `infra/agentinfra/formal.py:275`; AST `2af73781c6a69df6159594adc9ee6061b74e08111b9945d0ccc74619839ab4fd`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[1]::ImportFrom

Source: `infra/agentinfra/formal.py:276`; AST `9b43f0d5264e996b21b07e0a8acc5a5a0f437b5928cac6813466c4cd9378bc4a`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[25].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[2]::Assign

Source: `infra/agentinfra/formal.py:277`; AST `20995c722601ee47aa8b896dc15119a732914da25fed36c31fa6da78e2b85186`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: blockers, rows.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[3]::Assign

Source: `infra/agentinfra/formal.py:278`; AST `5714c56c2f1d0bc731cc0be3776baaf8c01611169993cdd6091dae54201b2c2e`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, sorted, state_path. Outputs/bindings: paths.
Calls/effect boundaries: sorted, state_path, state_path(root, 'bindings').glob.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[3].value::Call

Source: `infra/agentinfra/formal.py:278`; AST `af5a909d31a3968318a9ba69a56cb5117d612b70403b7bfca09d661079259ec3`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, sorted, state_path. Outputs/bindings: (none).
Calls/effect boundaries: sorted, state_path, state_path(root, 'bindings').glob.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[3].value.args[0]::Call

Source: `infra/agentinfra/formal.py:278`; AST `9399e3b4adfdb166ce328e68a2bf3bd627ad06731f2f37014ebeb8b888c6b3b2`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path, state_path(root, 'bindings').glob.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[3].value.args[0].func.value::Call

Source: `infra/agentinfra/formal.py:278`; AST `497433ce32c70f27b9dbbc616e0daf0d21892370abafb11341224b28b90aa888`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[3].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[4]::Expr

Source: `infra/agentinfra/formal.py:279`; AST `98729aa169ffda3add5eb4f5113eeb14cc7a5188ff4799ccb5b01bf54ef12896`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, paths, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[4].value::Call

Source: `infra/agentinfra/formal.py:279`; AST `1c549ff17c75215e164de2596e9b39badbb2e68f99949d5d13db868c970a0c51`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, paths, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[4].value.args[0].left::Call

Source: `infra/agentinfra/formal.py:279`; AST `f3a94d5a6b4b27987e5d6b89f94fd57d18ca3311ec9ced2a5262a2483df89046`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, paths. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5]::For

Source: `infra/agentinfra/formal.py:280`; AST `7ea43cf402186203fb37d58693978d9bdbf3184ea1637944a221978ceedc613b`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: KeyError, OSError, RuntimeError, ValueError, audit, binding, blockers, exc, o, path, paths, profile, r, result, root, rows, str, unseal. Outputs/bindings: binding, o, path, r, result.
Calls/effect boundaries: audit, blockers.append, o.get, o.get('evidence', {}).get, rows.append, rows.extend, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[25].body[5]; no call, error or mutation may be omitted. Iteration: path in paths
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0]::Try

Source: `infra/agentinfra/formal.py:281`; AST `12b4f1f0424f2929e90341b36c9af1f7a923ed58e9ec928c734aab459a03b600`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, RuntimeError, ValueError, audit, binding, blockers, exc, o, path, profile, r, result, root, rows, str, unseal. Outputs/bindings: binding, o, r, result.
Calls/effect boundaries: audit, blockers.append, o.get, o.get('evidence', {}).get, rows.append, rows.extend, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[25].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].body[0]::Assign

Source: `infra/agentinfra/formal.py:282`; AST `fb9200314b76d085fcf0c9a23fb1dd1b66b3080a8fce332bae9aa936e07603cd`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit, path, profile, root. Outputs/bindings: result.
Calls/effect boundaries: audit.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].body[0].value::Call

Source: `infra/agentinfra/formal.py:282`; AST `fbca174527821a57113822380f5ac188c90176f61524784998acdbb17bda8697`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit, path, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: audit.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].body[1]::Expr

Source: `infra/agentinfra/formal.py:283`; AST `1cbc1124e327de18961a679894a4a0937d9824d759c62231227950e802604dab`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, r, result, rows. Outputs/bindings: r.
Calls/effect boundaries: rows.extend.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].body[1].value::Call

Source: `infra/agentinfra/formal.py:283`; AST `51b6e01b3f22a2ae554762fd8db608862871753241260ca7fd199cdfc1ffe159`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, r, result, rows. Outputs/bindings: r.
Calls/effect boundaries: rows.extend.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].body[1].value.args[0]::GeneratorExp

Source: `infra/agentinfra/formal.py:283`; AST `4548d67932cce6e384717f00cc48229b455fea1d9140e81d83af66a812b71310`.

Rust module: `infra::agentinfra::formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: path, r, result. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[25].body[5].body[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/formal.py:284`; AST `63ccfdf02ef9139dd020b675c0dabe3d88fa0c08a42d23d8afceb30c3804584f`.

Rust module: `infra::agentinfra::formal`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: KeyError, OSError, RuntimeError, ValueError, binding, blockers, exc, o, path, rows, str, unseal. Outputs/bindings: binding, o.
Calls/effect boundaries: blockers.append, o.get, o.get('evidence', {}).get, rows.append, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[25].body[5].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[0]::Expr

Source: `infra/agentinfra/formal.py:285`; AST `94cbcf62b96b26d8f58559d71555a7f6f7f784077f2afb996d9428aa1276d266`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: blockers, exc, path, str. Outputs/bindings: (none).
Calls/effect boundaries: blockers.append, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[5].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[0].value::Call

Source: `infra/agentinfra/formal.py:285`; AST `57dc5e7bb2a9662da43e8404f4f49b8568f4a74c48fdfbe246eb5dc286ea574b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blockers, exc, path, str. Outputs/bindings: (none).
Calls/effect boundaries: blockers.append, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/formal.py:285`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1]::Try

Source: `infra/agentinfra/formal.py:286`; AST `a1a36dde42677811925a087e58c2d89eca724c7e636c2baa163f7aefdebc67c7`.

Rust module: `infra::agentinfra::formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, RuntimeError, ValueError, binding, exc, o, path, rows, str, unseal. Outputs/bindings: binding, o.
Calls/effect boundaries: o.get, o.get('evidence', {}).get, rows.append, str, unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Try evaluation at root.body[25].body[5].body[0].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[0]::Assign

Source: `infra/agentinfra/formal.py:287`; AST `55f7be9c49c0d82ddac0092f26a3c9ea11454a6c62f01c76caf91c4535c1e86d`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, unseal. Outputs/bindings: binding.
Calls/effect boundaries: unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[0].value::Call

Source: `infra/agentinfra/formal.py:287`; AST `568af2bc89ce861a8a6a796d7b6f2a9db1fd6cf14ffbe1799810f22aa8706cf0`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, unseal. Outputs/bindings: (none).
Calls/effect boundaries: unseal.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1]::For

Source: `infra/agentinfra/formal.py:288`; AST `696d6a74b111565cd5b1f77b9068057ddb388ffbcb0e2d48bc2295eb901a755d`.

Rust module: `infra::agentinfra::formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, exc, o, path, rows, str. Outputs/bindings: o.
Calls/effect boundaries: o.get, o.get('evidence', {}).get, rows.append, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered For evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1]; no call, error or mutation may be omitted. Iteration: o in binding['contract']['obligations']
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0]::Expr

Source: `infra/agentinfra/formal.py:289`; AST `5e592a08bab0a64d8ed3850c1ad7febf30c7883c4cb7f708789af4f034739102`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, o, path, rows, str. Outputs/bindings: (none).
Calls/effect boundaries: o.get, o.get('evidence', {}).get, rows.append, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/formal.py:289`; AST `060323277aa49d492433acd017c539ca7d083464ba891a1ba4b2f6a26c0cb7fc`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, o, path, rows, str. Outputs/bindings: (none).
Calls/effect boundaries: o.get, o.get('evidence', {}).get, rows.append, str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[3]::Call

Source: `infra/agentinfra/formal.py:290`; AST `43c1d1b7275704f0b776ab5eaba30cf3253caade160bb33ead05dc66f574ba41`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[4]::Call

Source: `infra/agentinfra/formal.py:291`; AST `33bced0a41f276980480302d43b4fd8b8ddb91aead63b4b903b8168ee5bc49ce`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get, o.get('evidence', {}).get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[4].func.value::Call

Source: `infra/agentinfra/formal.py:291`; AST `b0c5628a059ea6d452330eda006070cba6299808b7782c2737d8962bb298ff2b`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o. Outputs/bindings: (none).
Calls/effect boundaries: o.get.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[4].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[8]::Call

Source: `infra/agentinfra/formal.py:293`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].body[0].handlers[0].body[1].body[1].body[0].value.args[0].values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/formal.py:294`; AST `ee63dace1e65bb792a8cf406cb80440733db59d7a712c0621187189cab661912`.

Rust module: `infra::agentinfra::formal`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: KeyError, OSError, RuntimeError, ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[25].body[5].body[0].handlers[0].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[5].body[0].handlers[0].body[1].handlers[0].body[0]::Pass

Source: `infra/agentinfra/formal.py:295`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Pass evaluation at root.body[25].body[5].body[0].handlers[0].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/formal.py::module::proof_inventory::root.body[25].body[6]::Return

Source: `infra/agentinfra/formal.py:296`; AST `783b1ba6d52bfb1b28211cbd827af6d1f568b0605df42f1158fa382367644477`.

Rust module: `infra::agentinfra::formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: blockers, rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, catalog, destiny, destiny_reuse, evidence, locks, pathlib, re, security, types.

Invariants: Preserve ordered Return evaluation at root.body[25].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
