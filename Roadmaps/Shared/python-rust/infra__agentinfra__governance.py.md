# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 291. Inventory digest: `a88fa49b629ac9e29e41dd9557e612ce8d0e176e192d8ecaa18138a46fdc9518`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/governance.py::module::root::Module

Source: `infra/agentinfra/governance.py:1`; AST `9976f7f61caf4b041ebfac6accc118ac1d14dfb6ea9e2f3ef15cff97243e17a2`.

Rust module: `infra::agentinfra::governance`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContextVar, GovernanceViolation, OSError, Path, RuntimeError, ValueError, _GOVERNANCE_CREATION_ROOTS, _INSTRUCTION_UPDATE_TARGETS, _entry, _governing_file_identities, _identity, _instruction_files, _path_key, _relative_casefold, agents, base, body, candidate, capture_governance, contextmanager, current, data, dict, directory, entries, exc, excluded, expected, files, found, frozenset, governance_creation, governing_identities, hashlib, identities, identity, instruction_update, int, is_path_redirect, isinstance, item, json, len, list, name, names, normalized_resolved, operation, os, parent, part, parts, path, paths, project, raw, relative, relative_parts, resolved, resolved_relative, root, set, snapshot, sorted, stat_result, str, supplied, target, targets, token, tuple, unique, value. Outputs/bindings: _GOVERNANCE_CREATION_ROOTS, _INSTRUCTION_UPDATE_TARGETS, agents, base, body, candidate, current, data, directory, entries, excluded, expected, files, found, governance_creation, governing_identities, identities, identity, instruction_update, name, names, normalized_resolved, parent, part, parts, path, paths, project, raw, relative, relative_parts, resolved, resolved_relative, stat_result, supplied, target, token, unique, value.
Calls/effect boundaries: (project / '.agents').exists, ContextVar, GovernanceViolation, Path, Path(root).resolve, _GOVERNANCE_CREATION_ROOTS.get, _GOVERNANCE_CREATION_ROOTS.reset, _GOVERNANCE_CREATION_ROOTS.set, _INSTRUCTION_UPDATE_TARGETS.get, _INSTRUCTION_UPDATE_TARGETS.reset, _INSTRUCTION_UPDATE_TARGETS.set, _entry, _governing_file_identities, _identity, _instruction_files, _path_key, _relative_casefold, agents.is_dir, agents.rglob, candidate.absolute, candidate.is_absolute, candidate.parent.resolve, candidate.relative_to, capture_governance, current.get, current.resolve, found.append, frozenset, hashlib.sha256, hashlib.sha256(data).hexdigest, hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest, identities.add, int, is_path_redirect, isinstance, item.relative_to, item.relative_to(project).as_posix, item.relative_to(root).as_posix, json.dumps, json.dumps(body, sort_keys=True, separators=(',', ':')).encode, len, os.readlink, os.walk, part.casefold, path.is_dir, path.is_file, path.is_symlink, path.parent.resolve, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, path.stat, raw.is_absolute, resolved.relative_to, root.resolve, set, snapshot.get, sorted, str, tuple, value.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/governance.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[1]::Import

Source: `infra/agentinfra/governance.py:3`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[2]::Import

Source: `infra/agentinfra/governance.py:4`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[3]::Import

Source: `infra/agentinfra/governance.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/governance.py:6`; AST `a510406c1fa6f159ec004f4ead0d836747696bf4154e0a5daee8abdfbd9829f0`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/governance.py:7`; AST `6588e8300f9de11fc19a7338e73f5cba5e5264abe31bdc98aaca6ec078376a63`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/governance.py:8`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/governance.py:10`; AST `632a9db15162364f46041598eaf2830d63e78af499728e92644736ad18ec9e6d`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::GovernanceViolation::root.body[8]::ClassDef

Source: `infra/agentinfra/governance.py:13`; AST `ae459368478ffc17b1df3d4a39366ae47085227bd88941b9a6f8fa210352b2b9`.

Rust module: `infra::agentinfra::governance`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ClassDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::GovernanceViolation::root.body[8].body[0]::Expr

Source: `infra/agentinfra/governance.py:14`; AST `a4a41829c31eb3a5a2761e12852668a3bd4101a6e38f555359dffd94ea783972`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[9]::AnnAssign

Source: `infra/agentinfra/governance.py:17`; AST `d5c632bb5a06a07662766f1a40d171cc60a222eae5cd3d9b546799b373cc6cb8`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextVar, frozenset, str. Outputs/bindings: _GOVERNANCE_CREATION_ROOTS.
Calls/effect boundaries: ContextVar, frozenset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered AnnAssign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[9].value::Call

Source: `infra/agentinfra/governance.py:17`; AST `36debee3acab2d3c6e5e3a59db68d9f7ad8e4e2ef843cd2d0efd447a0cfdfca6`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextVar, frozenset. Outputs/bindings: (none).
Calls/effect boundaries: ContextVar, frozenset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[9].value.keywords[0].value::Call

Source: `infra/agentinfra/governance.py:18`; AST `d7d1e4f61c3646ac60443f6017b1d71e6211b8937dd95f8cf8e93bdb97f3a7e2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: frozenset. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[9].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[10]::AnnAssign

Source: `infra/agentinfra/governance.py:20`; AST `d4fc075b3f20e1c3f2f43daf39cb2e41ff33213105a01b2cdb71388916242ca0`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextVar, frozenset, str. Outputs/bindings: _INSTRUCTION_UPDATE_TARGETS.
Calls/effect boundaries: ContextVar, frozenset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[10].value::Call

Source: `infra/agentinfra/governance.py:20`; AST `e1967cd10fc27d0589834c227b15cb8ca65314e118afb6fb6d064c0d68250a6f`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextVar, frozenset. Outputs/bindings: (none).
Calls/effect boundaries: ContextVar, frozenset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::root.body[10].value.keywords[0].value::Call

Source: `infra/agentinfra/governance.py:21`; AST `d7d1e4f61c3646ac60443f6017b1d71e6211b8937dd95f8cf8e93bdb97f3a7e2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: frozenset. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[10].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11]::FunctionDef

Source: `infra/agentinfra/governance.py:25`; AST `f22eb3b15b94c4fb37c3be5b1b957b8f0b0717fa3ec23e126e8df28e0fbd2774`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, candidate, os, path, str, value. Outputs/bindings: candidate, value.
Calls/effect boundaries: Path, candidate.parent.resolve, str, value.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[0]::Assign

Source: `infra/agentinfra/governance.py:26`; AST `a98722e47fb111f451451469e963ca6d1f06dfbf194e453669fd1d4d657569a7`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, path. Outputs/bindings: candidate.
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[0].value::Call

Source: `infra/agentinfra/governance.py:26`; AST `c4b629495a6e643da3774e82f742688d4a24128b1ff8b4448236e96c64f51421`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, path. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[1]::Assign

Source: `infra/agentinfra/governance.py:27`; AST `16342c461310ce10918493872d5746f3d058a1c8760ef734f7591ac65fd2266d`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, str. Outputs/bindings: value.
Calls/effect boundaries: candidate.parent.resolve, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[1].value::Call

Source: `infra/agentinfra/governance.py:27`; AST `4c93987a71fc81f9472d6c6e62833035a3cfa347e3d2146d1dea7d206cd555fb`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, str. Outputs/bindings: (none).
Calls/effect boundaries: candidate.parent.resolve, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[1].value.args[0].left::Call

Source: `infra/agentinfra/governance.py:27`; AST `816865b7ac8fbb50b64c521dbb56b1a62b5348247859df0ba2968f97fbdcaaef`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.parent.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[2]::Return

Source: `infra/agentinfra/governance.py:28`; AST `4b9a25e97e4b5dea19239c9441e54e217d1836cca95bbe6d875ad4f3cb2622f2`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, value. Outputs/bindings: (none).
Calls/effect boundaries: value.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_path_key::root.body[11].body[2].value.body::Call

Source: `infra/agentinfra/governance.py:28`; AST `f803ff04d84cbbde05f2c87eb0479d3e45ec1764e332e956b09193c0eac316f2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12]::FunctionDef

Source: `infra/agentinfra/governance.py:32`; AST `5a2a7e96aa258dd398b68b99d2acae1782539ae2a0e3aa3e9ca983b8195bb94d`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GovernanceViolation, Path, _GOVERNANCE_CREATION_ROOTS, contextmanager, current, project, root, str, token. Outputs/bindings: current, project, token.
Calls/effect boundaries: (project / '.agents').exists, GovernanceViolation, Path, Path(root).resolve, _GOVERNANCE_CREATION_ROOTS.get, _GOVERNANCE_CREATION_ROOTS.reset, _GOVERNANCE_CREATION_ROOTS.set, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[0]::Expr

Source: `infra/agentinfra/governance.py:33`; AST `2b7d68177453a932dfd1291859c09444cc789c8c0bd64563f448fa1d66dcfbe6`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[1]::Assign

Source: `infra/agentinfra/governance.py:39`; AST `adfb3a18626509aca1dd4631e301fa61aea2a40280f64962fd9af645b4070072`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: project.
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[1].value::Call

Source: `infra/agentinfra/governance.py:39`; AST `c730489059afc3f4aef1c52b1968dce819ad8d18695e9c28c3f4518931ce9791`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[1].value.func.value::Call

Source: `infra/agentinfra/governance.py:39`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[2]::If

Source: `infra/agentinfra/governance.py:40`; AST `ad357dc6ab36e5bf4d2a3029c0eb745699e3d2b48f05828c26fd2dc6a8acbec3`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, project. Outputs/bindings: (none).
Calls/effect boundaries: (project / '.agents').exists, GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[12].body[2]; no call, error or mutation may be omitted. Condition: (project / '.agents').exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[2].test::Call

Source: `infra/agentinfra/governance.py:40`; AST `81cfc017c8b64fc5c06f27966203656350d4c4d0f23ac5a7215c25f9038ca231`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project. Outputs/bindings: (none).
Calls/effect boundaries: (project / '.agents').exists.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[2].body[0]::Raise

Source: `infra/agentinfra/governance.py:41`; AST `fb5fe69b3589f1be81d913a223eab2c8846927bf691ae08bbf708667d56f07f2`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[2].body[0].exc::Call

Source: `infra/agentinfra/governance.py:41`; AST `b8d7fef4e8dedfaf7872e9889e64229e982dfd971ecec458dfffec4e08dcc76b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[3]::Assign

Source: `infra/agentinfra/governance.py:42`; AST `ac8f2f6d33cc185774ba4ccd27472f021092a7135bfe6d8703c23877f4f183a6`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _GOVERNANCE_CREATION_ROOTS. Outputs/bindings: current.
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[3].value::Call

Source: `infra/agentinfra/governance.py:42`; AST `e9af4fa3b4058e9a0cfef4da48b6d2b6876917d8c2f4497f81c1b3059800fd8d`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _GOVERNANCE_CREATION_ROOTS. Outputs/bindings: (none).
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[4]::Assign

Source: `infra/agentinfra/governance.py:43`; AST `d819a4934a0b598f51d75c367f12c0fc748fa143edb0e849c009ef208e51c791`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _GOVERNANCE_CREATION_ROOTS, current, project, str. Outputs/bindings: token.
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.set, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[4].value::Call

Source: `infra/agentinfra/governance.py:43`; AST `c3bda5f151a1a10f455a8590f7425431bba132ffc9e4be0233572ef1302d587b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _GOVERNANCE_CREATION_ROOTS, current, project, str. Outputs/bindings: (none).
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.set, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[4].value.args[0].right.elts[0]::Call

Source: `infra/agentinfra/governance.py:43`; AST `1475de91c44ce4d417060101e8d7b6de913a11f823247a507fb52d4b35621200`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value.args[0].right.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[5]::Try

Source: `infra/agentinfra/governance.py:44`; AST `47d6cda7eb7e448cef8a6b091e19bcc7e62fbcf3696b1f3a3b6bd25eb44733fb`.

Rust module: `infra::agentinfra::governance`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: _GOVERNANCE_CREATION_ROOTS, token. Outputs/bindings: (none).
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.reset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Try evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[5].body[0]::Expr

Source: `infra/agentinfra/governance.py:45`; AST `4ef85b91bd2f837cbb619428370c77b4e8f23faa1461fa93120d8bde06a4c480`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/governance.py:47`; AST `ba88d03970268c7cff802d2cda518610e6f327afdccc3fee21f6ce8e2964ba64`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _GOVERNANCE_CREATION_ROOTS, token. Outputs/bindings: (none).
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.reset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governance_tree_creation::root.body[12].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/governance.py:47`; AST `0211a74e2ffcbe959bfa5f118cb372fd3d1c3e51718233ce24b85748542b3309`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _GOVERNANCE_CREATION_ROOTS, token. Outputs/bindings: (none).
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.reset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13]::FunctionDef

Source: `infra/agentinfra/governance.py:51`; AST `93a03277184fe1184f13bbe1ba59d92766767a6279d11319f501b394c97fa003`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GovernanceViolation, Path, _INSTRUCTION_UPDATE_TARGETS, _path_key, candidate, contextmanager, current, expected, is_path_redirect, project, root, target, token. Outputs/bindings: candidate, current, expected, project, token.
Calls/effect boundaries: GovernanceViolation, Path, Path(root).resolve, _INSTRUCTION_UPDATE_TARGETS.get, _INSTRUCTION_UPDATE_TARGETS.reset, _INSTRUCTION_UPDATE_TARGETS.set, _path_key, candidate.is_absolute, is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[0]::Expr

Source: `infra/agentinfra/governance.py:52`; AST `91802cb02bdeffab798e760e6593f81fc88e877533ae097b6a53955f665db9a5`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[1]::Assign

Source: `infra/agentinfra/governance.py:54`; AST `adfb3a18626509aca1dd4631e301fa61aea2a40280f64962fd9af645b4070072`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: project.
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[1].value::Call

Source: `infra/agentinfra/governance.py:54`; AST `c730489059afc3f4aef1c52b1968dce819ad8d18695e9c28c3f4518931ce9791`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[1].value.func.value::Call

Source: `infra/agentinfra/governance.py:54`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[2]::Assign

Source: `infra/agentinfra/governance.py:55`; AST `0d611481fed78f0cf4931fc3188883bdefa6e649d93f594b6688ec8b0f5bed03`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project. Outputs/bindings: expected.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[3]::Assign

Source: `infra/agentinfra/governance.py:56`; AST `c0700114d69efd1615c532b9c3d6f98a8d3c454d726833dc018b3338902e0663`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, target. Outputs/bindings: candidate.
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[3].value::Call

Source: `infra/agentinfra/governance.py:56`; AST `dc4b9ecf5fece6ccb04ac1e778aa663b6323574a715f60affed94b5b7aed3a9a`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, target. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[4]::Assign

Source: `infra/agentinfra/governance.py:57`; AST `1f26a440fbd4f227b960a780b1e3700ff98036ec3bfa61922d3b99bb5cca04ee`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, project. Outputs/bindings: candidate.
Calls/effect boundaries: candidate.is_absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[4].value.test::Call

Source: `infra/agentinfra/governance.py:57`; AST `3855ce7aab16f429e12c6a129ddcdb42354183a693b4691956b4d57cf2107215`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.is_absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[5]::If

Source: `infra/agentinfra/governance.py:58`; AST `815b5591aff7266487e5fee90d57559faa7665bc22c8bb7bc4b64adcc21d93ed`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, _path_key, candidate, expected. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[13].body[5]; no call, error or mutation may be omitted. Condition: _path_key(candidate) != _path_key(expected)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[5].test.left::Call

Source: `infra/agentinfra/governance.py:58`; AST `4dba725311222a0ff68b5e86faa120af3dfa834eb034d5eaf5c6ca5d51f24d74`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _path_key, candidate. Outputs/bindings: (none).
Calls/effect boundaries: _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[5].test.comparators[0]::Call

Source: `infra/agentinfra/governance.py:58`; AST `f2a5af0c215d2caa43298310558bc8f69446d5e5e4d813a837231151d2bbf256`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _path_key, expected. Outputs/bindings: (none).
Calls/effect boundaries: _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[5].body[0]::Raise

Source: `infra/agentinfra/governance.py:59`; AST `49dc6e70e02f112edba8603d4875507b8354d45481f36c2cb8a658bb562f9165`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[5].body[0].exc::Call

Source: `infra/agentinfra/governance.py:59`; AST `a65be3840e5d9239c5fe44b3dec7bc94e64f7a87fd69ab935fe476b556c09be7`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[6]::If

Source: `infra/agentinfra/governance.py:60`; AST `fffd6f61ac9ef757485a9f6db4e70df4f72820bba3911d81fce31ab0c7b3dd12`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, candidate, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[13].body[6]; no call, error or mutation may be omitted. Condition: is_path_redirect(candidate)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[6].test::Call

Source: `infra/agentinfra/governance.py:60`; AST `bb09cd99c4bc33592e4f4ce77ff83a36bc9ca1d71a98614c5ebba440f30d5963`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[6].body[0]::Raise

Source: `infra/agentinfra/governance.py:61`; AST `7a454fe31697a528c029796ac0f0496eb12fcfa54eac321aad0349f914bdbbad`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[6].body[0].exc::Call

Source: `infra/agentinfra/governance.py:61`; AST `14602fe97ede4f7ec55a86263bda65b37d46626b249b470ff02fa6e265b982ca`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[7]::Assign

Source: `infra/agentinfra/governance.py:62`; AST `793782cd3e5044d81bfd381ae4f7b9fec462934ef175cd8f8f25e9712ec12bc3`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _INSTRUCTION_UPDATE_TARGETS. Outputs/bindings: current.
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[7].value::Call

Source: `infra/agentinfra/governance.py:62`; AST `2682c1e92b30fef44b60f47633376f41aad3e3f5627b101b0608ddb6e0e6db4e`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _INSTRUCTION_UPDATE_TARGETS. Outputs/bindings: (none).
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[8]::Assign

Source: `infra/agentinfra/governance.py:63`; AST `425e04251a7b4d6e09b077ee275005caced96e34760ae9398b0bc4803d43cf28`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _INSTRUCTION_UPDATE_TARGETS, _path_key, current, expected. Outputs/bindings: token.
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.set, _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[8].value::Call

Source: `infra/agentinfra/governance.py:63`; AST `f40841c6fbced9f5de00760295bef078ad341e6dc1d9c518192415e15c2925ac`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _INSTRUCTION_UPDATE_TARGETS, _path_key, current, expected. Outputs/bindings: (none).
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.set, _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[8].value.args[0].right.elts[0]::Call

Source: `infra/agentinfra/governance.py:63`; AST `f2a5af0c215d2caa43298310558bc8f69446d5e5e4d813a837231151d2bbf256`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _path_key, expected. Outputs/bindings: (none).
Calls/effect boundaries: _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].right.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[9]::Try

Source: `infra/agentinfra/governance.py:64`; AST `4ba0225dc4833ac88f1dcb7131b02efb013715874e6e81058343aa329d31e663`.

Rust module: `infra::agentinfra::governance`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: _INSTRUCTION_UPDATE_TARGETS, token. Outputs/bindings: (none).
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.reset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Try evaluation at root.body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[9].body[0]::Expr

Source: `infra/agentinfra/governance.py:65`; AST `4ef85b91bd2f837cbb619428370c77b4e8f23faa1461fa93120d8bde06a4c480`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[9].finalbody[0]::Expr

Source: `infra/agentinfra/governance.py:67`; AST `ba5ab9f9d15259f3181f9b2d11d2f94fe17accb73057687097b5c1695617e49a`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _INSTRUCTION_UPDATE_TARGETS, token. Outputs/bindings: (none).
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.reset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_instruction_update::root.body[13].body[9].finalbody[0].value::Call

Source: `infra/agentinfra/governance.py:67`; AST `eb51f12725a23fd2bba82721661904021c1215e2b663967d5867d75c9c671634`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _INSTRUCTION_UPDATE_TARGETS, token. Outputs/bindings: (none).
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.reset.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14]::FunctionDef

Source: `infra/agentinfra/governance.py:70`; AST `f0155344efc4eed87e53ba4018a6f3558282d2097130da5e8e77afbb141491f6`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, int, path, stat_result, tuple. Outputs/bindings: stat_result.
Calls/effect boundaries: int, path.stat.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[0]::Try

Source: `infra/agentinfra/governance.py:71`; AST `e9229c3825b23c399022c571cbea77ea73deda06d57bb0d356562458ec77a102`.

Rust module: `infra::agentinfra::governance`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, path. Outputs/bindings: stat_result.
Calls/effect boundaries: path.stat.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Try evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[0].body[0]::Assign

Source: `infra/agentinfra/governance.py:72`; AST `2e6eadeacc3fe64edd18c261e5ed1c4cf6065128f58c4752cb0f19048b03ef12`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: stat_result.
Calls/effect boundaries: path.stat.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[0].body[0].value::Call

Source: `infra/agentinfra/governance.py:72`; AST `d0f2660d5c576e75c41493128e9ef73fd43d1401a0dd272c961864f7164b7698`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/governance.py:73`; AST `cd17fbe822b7dd0d0ad96d0eea9d32cbb7ab096b21d0884e7107fab89ea84bba`.

Rust module: `infra::agentinfra::governance`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[0].handlers[0].body[0]::Return

Source: `infra/agentinfra/governance.py:74`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[14].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[1]::Return

Source: `infra/agentinfra/governance.py:75`; AST `d51f9514ddad54ef484cbbd60e291b0b21f79b07d137999d46fcab681c4f310d`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, stat_result. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[1].value.elts[0]::Call

Source: `infra/agentinfra/governance.py:75`; AST `4ef40754f57582c2b5cf29b805ddd624a8339639d167e5c2480715bc51b45b94`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, stat_result. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_identity::root.body[14].body[1].value.elts[1]::Call

Source: `infra/agentinfra/governance.py:75`; AST `d5c322e219f93e58a14087014cb12ff8a9198deadef5fc5203e2a5c909ebbb92`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, stat_result. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15]::FunctionDef

Source: `infra/agentinfra/governance.py:78`; AST `a9225589fed40af18518d4291c28a12106516eedb2f10558f235ee71e25fbc60`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ValueError, candidate, os, part, parts, path, relative, root, str, tuple. Outputs/bindings: candidate, part, parts, relative.
Calls/effect boundaries: candidate.relative_to, part.casefold, path.parent.resolve, root.resolve, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[0]::Expr

Source: `infra/agentinfra/governance.py:79`; AST `3cd5e078bbc71de811f5ad25acc5eaa3c57863c360de223a5c8fcc730757536b`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1]::Try

Source: `infra/agentinfra/governance.py:81`; AST `9f2fa2150cf90dbf484a541b4dbbcdc2a1b96ac9101d743f8912d9abb6b5e7dd`.

Rust module: `infra::agentinfra::governance`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ValueError, candidate, path, root. Outputs/bindings: candidate, relative.
Calls/effect boundaries: candidate.relative_to, path.parent.resolve, root.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Try evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].body[0]::Assign

Source: `infra/agentinfra/governance.py:82`; AST `9494caf74d5f0f8d49528041305e1ff50ffc155b39ccb52d9cbf2c0f056b7f4c`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: candidate.
Calls/effect boundaries: path.parent.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].body[0].value.left::Call

Source: `infra/agentinfra/governance.py:82`; AST `6b8de31f5a96bde7404c3405554f559e745b683c7e0c3108269c10c749180333`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].body[1]::Assign

Source: `infra/agentinfra/governance.py:83`; AST `47fe221a496c0840f605c1d9d1d642f4bdee8988474c2505adbba64602e25543`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, root. Outputs/bindings: relative.
Calls/effect boundaries: candidate.relative_to, root.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].body[1].value::Call

Source: `infra/agentinfra/governance.py:83`; AST `9dbbf1a62fa20151380a96b205d3b2dc2599ecde38410b2749ccffd7d02a919f`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, root. Outputs/bindings: (none).
Calls/effect boundaries: candidate.relative_to, root.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].body[1].value.args[0]::Call

Source: `infra/agentinfra/governance.py:83`; AST `56ce091af63844ee93125714af2e994600b88740aa8b9bf3bb1ba7526dba15a7`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/governance.py:84`; AST `4492c71a8c3ef59f184c3c4673324d0b8d40d44547b536f031d4d925483f5b10`.

Rust module: `infra::agentinfra::governance`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[15].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[1].handlers[0].body[0]::Return

Source: `infra/agentinfra/governance.py:85`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[15].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[2]::Assign

Source: `infra/agentinfra/governance.py:86`; AST `48a1c58e604129ed993103ccee3b726396fb52c580f72bfd64fceb7611117ba6`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative. Outputs/bindings: parts.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[3]::If

Source: `infra/agentinfra/governance.py:87`; AST `b357f17470862f9e91770ed6c0d21ced4c92a1d7ce2c3b711590fb60b79954c4`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: os, part, parts, tuple. Outputs/bindings: part.
Calls/effect boundaries: part.casefold, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[15].body[3]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[3].body[0]::Return

Source: `infra/agentinfra/governance.py:88`; AST `21713cd82f7f3d1d348db9fee07bee2c341f2005a905e658db5636a71c08eed5`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: part, parts, tuple. Outputs/bindings: part.
Calls/effect boundaries: part.casefold, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[3].body[0].value::Call

Source: `infra/agentinfra/governance.py:88`; AST `feb94d6d15c359f3cde29047c13fd7397ae2eda3c6a19d786b44c0d7933c60eb`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: part, parts, tuple. Outputs/bindings: part.
Calls/effect boundaries: part.casefold, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[3].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/governance.py:88`; AST `96417819e52c36a56378a0df76b84ca996c7cc010a34783f5fb70e1a3bc5b6aa`.

Rust module: `infra::agentinfra::governance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: part, parts. Outputs/bindings: part.
Calls/effect boundaries: part.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[3].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[3].body[0].value.args[0].elt::Call

Source: `infra/agentinfra/governance.py:88`; AST `079800cd1ad1fe20aa29eb38543d80a675f545f21b9983ce42988e6d58c588c8`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: part. Outputs/bindings: (none).
Calls/effect boundaries: part.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[4]::Return

Source: `infra/agentinfra/governance.py:89`; AST `6573d7ec4e4bab08334b782f9273f23af402fc429fb635013524612f03908b6b`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parts, tuple. Outputs/bindings: (none).
Calls/effect boundaries: tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_relative_casefold::root.body[15].body[4].value::Call

Source: `infra/agentinfra/governance.py:89`; AST `d4413fc3ac2b31d036b08e0f86e25259fb56a62c84da73a8655aa133951794a2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts, tuple. Outputs/bindings: (none).
Calls/effect boundaries: tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16]::FunctionDef

Source: `infra/agentinfra/governance.py:92`; AST `4d1540c18a8edde10d82d726e3eb2bf99fe8348fcf30724d936b116707bbf59d`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _identity, _instruction_files, agents, identities, identity, int, is_path_redirect, path, root, set, tuple. Outputs/bindings: agents, identities, identity, path.
Calls/effect boundaries: _identity, _instruction_files, agents.is_dir, agents.rglob, identities.add, is_path_redirect, set.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[0]::AnnAssign

Source: `infra/agentinfra/governance.py:93`; AST `633c2ad746adcd928534ad5d953c112b3450cef477879dbbdbe3d950b13c84ef`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, set, tuple. Outputs/bindings: identities.
Calls/effect boundaries: set.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered AnnAssign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[0].value::Call

Source: `infra/agentinfra/governance.py:93`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[1]::Assign

Source: `infra/agentinfra/governance.py:94`; AST `74f649770d81273d236051e3c3ebfcade1d985f80e2dd675d4e5765bd0016f12`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: agents.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2]::If

Source: `infra/agentinfra/governance.py:95`; AST `fbb55294ce3c583d67ee5a1af243377d56e8a8247f7266e01aa5e3a5c75dc724`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _identity, agents, identities, identity, is_path_redirect, path. Outputs/bindings: identity, path.
Calls/effect boundaries: _identity, agents.is_dir, agents.rglob, identities.add, is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[16].body[2]; no call, error or mutation may be omitted. Condition: agents.is_dir() and (not is_path_redirect(agents))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].test.values[0]::Call

Source: `infra/agentinfra/governance.py:95`; AST `6bb36e65b55b7270e23868578ebc038ecf2ad2558aee096988cbdc5d987833bb`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: agents. Outputs/bindings: (none).
Calls/effect boundaries: agents.is_dir.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].test.values[1].operand::Call

Source: `infra/agentinfra/governance.py:95`; AST `216461f87647356d55ba4d082959ee1d6e91a5a080aa201016d24b02ad893a62`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: agents, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0]::For

Source: `infra/agentinfra/governance.py:96`; AST `4ac13d6aae08b1ec261b3b1c6c512da897f59c40d79866102d61b0f7eee2cc19`.

Rust module: `infra::agentinfra::governance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _identity, agents, identities, identity, path. Outputs/bindings: identity, path.
Calls/effect boundaries: _identity, agents.rglob, identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered For evaluation at root.body[16].body[2].body[0]; no call, error or mutation may be omitted. Iteration: path in agents.rglob('*')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0].iter::Call

Source: `infra/agentinfra/governance.py:96`; AST `d8cf2b503225ec576b825c5f0624b6ab01cf7994653ec8e648b7ad41e9c118f2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: agents. Outputs/bindings: (none).
Calls/effect boundaries: agents.rglob.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0].body[0]::Assign

Source: `infra/agentinfra/governance.py:97`; AST `691a852a48af3ae8a197594669b8016fe30f4e2c8d768e60432a82b1e5436935`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _identity, path. Outputs/bindings: identity.
Calls/effect boundaries: _identity.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/governance.py:97`; AST `f5fa651fc3e0f848363b35cf83f31a71fe17eabb14ec0d65b1cb60ee53fe25b9`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _identity, path. Outputs/bindings: (none).
Calls/effect boundaries: _identity.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0].body[1]::If

Source: `infra/agentinfra/governance.py:98`; AST `7070a08fda5bf9f08405ec42b47ded270d7f1feb0a1393ede3b653adaaf9bc86`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: identities, identity. Outputs/bindings: (none).
Calls/effect boundaries: identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[16].body[2].body[0].body[1]; no call, error or mutation may be omitted. Condition: identity is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0].body[1].body[0]::Expr

Source: `infra/agentinfra/governance.py:99`; AST `74fbc82ed26c5078eb5da6757cedf0b737153772f68c9f5417fd953544199018`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identities, identity. Outputs/bindings: (none).
Calls/effect boundaries: identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[2].body[0].body[1].body[0].value::Call

Source: `infra/agentinfra/governance.py:99`; AST `88c3282f0aeaf6f11d82b6cccfa49926b9aa57d77e69bb238859bbf8f9a4e54b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identities, identity. Outputs/bindings: (none).
Calls/effect boundaries: identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3]::For

Source: `infra/agentinfra/governance.py:100`; AST `f0b55fd81a2efdcd86722c267763a3a25fd91afdd413193a8998e93a94206d0b`.

Rust module: `infra::agentinfra::governance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _identity, _instruction_files, identities, identity, path, root. Outputs/bindings: identity, path.
Calls/effect boundaries: _identity, _instruction_files, identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered For evaluation at root.body[16].body[3]; no call, error or mutation may be omitted. Iteration: path in _instruction_files(root)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3].iter::Call

Source: `infra/agentinfra/governance.py:100`; AST `40efbcf9ffb54ba16dffbeae645683c26fa1deef89d7052a881ba40da96a8194`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _instruction_files, root. Outputs/bindings: (none).
Calls/effect boundaries: _instruction_files.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3].body[0]::Assign

Source: `infra/agentinfra/governance.py:101`; AST `691a852a48af3ae8a197594669b8016fe30f4e2c8d768e60432a82b1e5436935`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _identity, path. Outputs/bindings: identity.
Calls/effect boundaries: _identity.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3].body[0].value::Call

Source: `infra/agentinfra/governance.py:101`; AST `f5fa651fc3e0f848363b35cf83f31a71fe17eabb14ec0d65b1cb60ee53fe25b9`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _identity, path. Outputs/bindings: (none).
Calls/effect boundaries: _identity.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3].body[1]::If

Source: `infra/agentinfra/governance.py:102`; AST `7070a08fda5bf9f08405ec42b47ded270d7f1feb0a1393ede3b653adaaf9bc86`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: identities, identity. Outputs/bindings: (none).
Calls/effect boundaries: identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[16].body[3].body[1]; no call, error or mutation may be omitted. Condition: identity is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3].body[1].body[0]::Expr

Source: `infra/agentinfra/governance.py:103`; AST `74fbc82ed26c5078eb5da6757cedf0b737153772f68c9f5417fd953544199018`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identities, identity. Outputs/bindings: (none).
Calls/effect boundaries: identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/governance.py:103`; AST `88c3282f0aeaf6f11d82b6cccfa49926b9aa57d77e69bb238859bbf8f9a4e54b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identities, identity. Outputs/bindings: (none).
Calls/effect boundaries: identities.add.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_governing_file_identities::root.body[16].body[4]::Return

Source: `infra/agentinfra/governance.py:104`; AST `9bc402988dbeb54376003184733313d9dfe7949ae8427d9f2583b5f16cd5690c`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identities. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17]::FunctionDef

Source: `infra/agentinfra/governance.py:107`; AST `baadb09d5e42194b50d460932fd2cb25f4b905b9c49caa062e51eaeffe38bd35`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, base, directory, excluded, files, found, item, list, name, names, os, root, sorted. Outputs/bindings: base, directory, excluded, files, found, name, names.
Calls/effect boundaries: Path, found.append, item.relative_to, item.relative_to(root).as_posix, os.walk, sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[0]::AnnAssign

Source: `infra/agentinfra/governance.py:108`; AST `1a60aa15140a3b89948d0aae9698a8b7ab5ace9c582a69ab72baaf97026ae25e`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, list. Outputs/bindings: found.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered AnnAssign evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[1]::Assign

Source: `infra/agentinfra/governance.py:109`; AST `c4b09030e8442909931a56e7aaf3fd28bfa4b569cbc19707079636b48375a3fa`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: excluded.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2]::For

Source: `infra/agentinfra/governance.py:110`; AST `4f14902aed8bd009fd6b519d7c767a582f6500f780a66b47eff130d829f81b15`.

Rust module: `infra::agentinfra::governance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, base, directory, excluded, files, found, name, names, os, root, sorted. Outputs/bindings: base, directory, files, name, names.
Calls/effect boundaries: Path, found.append, os.walk, sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered For evaluation at root.body[17].body[2]; no call, error or mutation may be omitted. Iteration: (directory, names, files) in os.walk(root, topdown=True, followlinks=False)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].iter::Call

Source: `infra/agentinfra/governance.py:110`; AST `789bd6a49012ea608e40aef0f9bdb7497e4f8bc3b69f4cf511d243fe79e4aa22`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, root. Outputs/bindings: (none).
Calls/effect boundaries: os.walk.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[0]::Assign

Source: `infra/agentinfra/governance.py:111`; AST `b0114a1ccb3b4b9db9104e9406d1f8a1b0417df2ba1f4c2c303d508672b034f3`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: excluded, name, names, sorted. Outputs/bindings: name.
Calls/effect boundaries: sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[0].value::Call

Source: `infra/agentinfra/governance.py:111`; AST `349372b8a4d2c9bea10b7d266010b7055987cbb3f05308cd38b12b2860b5ffff`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: excluded, name, names, sorted. Outputs/bindings: name.
Calls/effect boundaries: sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/governance.py:111`; AST `f155d5fbc06a854fce2578515802764ca1d64f7671ba783f5a813d2e181ef09f`.

Rust module: `infra::agentinfra::governance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: excluded, name, names. Outputs/bindings: name.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[1]::Assign

Source: `infra/agentinfra/governance.py:112`; AST `0d86456db0fe2293e0ddc795815abb329c1349594f6b2ac97bcc7fdf99b25e91`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: base.
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[1].value::Call

Source: `infra/agentinfra/governance.py:112`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[2]::If

Source: `infra/agentinfra/governance.py:113`; AST `c6d5a97c653bd51c6fc1c8bcf05aaf8ad92e4cb2c293a32dc35a1c9ee6e314d3`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: base, files, found. Outputs/bindings: (none).
Calls/effect boundaries: found.append.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[17].body[2].body[2]; no call, error or mutation may be omitted. Condition: 'AGENTS.md' in files
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[2].body[0]::Expr

Source: `infra/agentinfra/governance.py:114`; AST `1d26b405cc2671227935ede57352dcb0bb643357c489aec53e6427ed9ae7bd51`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, found. Outputs/bindings: (none).
Calls/effect boundaries: found.append.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[2].body[2].body[0].value::Call

Source: `infra/agentinfra/governance.py:114`; AST `e82b98bf4b8cb34a4dc39d2bbba2d4168bfc6c44857b0bd8ba0512592a6d8302`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, found. Outputs/bindings: (none).
Calls/effect boundaries: found.append.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[3]::Return

Source: `infra/agentinfra/governance.py:115`; AST `f49d4c602a61ca64537e99b789d3c3122c06e3f148b1e38f976d6c59fadef16c`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found, item, root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(root).as_posix, sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[3].value::Call

Source: `infra/agentinfra/governance.py:115`; AST `da556351e2fa17d5e07d85e9087b20128b0978828a18ba001fd1a116b65cb684`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: found, item, root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(root).as_posix, sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[3].value.keywords[0].value::Lambda

Source: `infra/agentinfra/governance.py:115`; AST `2307708d94c730df69a9b905aedc654533687d082376abe04bb793bc769b9e76`.

Rust module: `infra::agentinfra::governance`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: item, root. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(root).as_posix.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Lambda evaluation at root.body[17].body[3].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[3].value.keywords[0].value.body::Call

Source: `infra/agentinfra/governance.py:115`; AST `86ac84980aa66c5c13e865616514d14bb73553cd0e407794941de8981a2f2f5f`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, root. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(root).as_posix.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.keywords[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_instruction_files::root.body[17].body[3].value.keywords[0].value.body.func.value::Call

Source: `infra/agentinfra/governance.py:115`; AST `365d1cfd9a8d046eae9b0a87e52903680a2469730a85a045dc71a36fede54f60`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, root. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.keywords[0].value.body.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18]::FunctionDef

Source: `infra/agentinfra/governance.py:118`; AST `8b350e264c10b62b6364a3dc22c36f6c2f38446cef067416b70e4c0cff40402a`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, data, dict, hashlib, is_path_redirect, len, os, path, relative, root, str, target. Outputs/bindings: data, relative, target.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest, is_path_redirect, len, os.readlink, path.is_dir, path.is_file, path.is_symlink, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[0]::Assign

Source: `infra/agentinfra/governance.py:119`; AST `c9a5d02444369221b50b662c72fded4efbbded9a1bf01f8bacecd9d7badf680c`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, root. Outputs/bindings: relative.
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[0].value::Call

Source: `infra/agentinfra/governance.py:119`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[0].value.func.value::Call

Source: `infra/agentinfra/governance.py:119`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1]::If

Source: `infra/agentinfra/governance.py:120`; AST `dd7ee4e7123e8a91f27fabae40034d35fcb4a02efe816ba8a246d49bf43d7abb`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: is_path_redirect, os, path, relative, str, target. Outputs/bindings: target.
Calls/effect boundaries: is_path_redirect, os.readlink, path.is_symlink, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1]; no call, error or mutation may be omitted. Condition: is_path_redirect(path)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1].test::Call

Source: `infra/agentinfra/governance.py:120`; AST `d9cac03fb65b00711ae1083fa305b5510d29827fd7fb7d268ae3ec96200e726a`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: is_path_redirect, path. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1].body[0]::Assign

Source: `infra/agentinfra/governance.py:121`; AST `69fbb65505f0ea831649a9b94b3fbda4ca0311de6acb292e8fb99bb0deba4171`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, path. Outputs/bindings: target.
Calls/effect boundaries: os.readlink, path.is_symlink.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1].body[0].value.test::Call

Source: `infra/agentinfra/governance.py:121`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1].body[0].value.body::Call

Source: `infra/agentinfra/governance.py:121`; AST `23c309da4cd59ccc8fbea7b975a3e62dfd69bda6bde87c6b3174f9fe653f2dee`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, path. Outputs/bindings: (none).
Calls/effect boundaries: os.readlink.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1].body[1]::Return

Source: `infra/agentinfra/governance.py:122`; AST `54fd90f53f3e478536cdb04362b4515261cf21b114c24e4d0edb8b71250f095c`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, str, target. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[1].body[1].value.values[2]::Call

Source: `infra/agentinfra/governance.py:122`; AST `d2e90325631fec2e51a1a89c12de552564847a205bd0f02a9e21633dd5830325`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, target. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[2]::If

Source: `infra/agentinfra/governance.py:123`; AST `70ffe830c94ec8a1e56315bc1b6a91b81007bd11be37e91b5bbd47cef2291feb`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path, relative. Outputs/bindings: (none).
Calls/effect boundaries: path.is_dir.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[2]; no call, error or mutation may be omitted. Condition: path.is_dir()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[2].test::Call

Source: `infra/agentinfra/governance.py:123`; AST `6819eb54369694522640db8bd92d541e88abcce62d8bf6b40d60b47c12339610`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_dir.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[2].body[0]::Return

Source: `infra/agentinfra/governance.py:124`; AST `b163e3d4eb6a4924ee6197c34df7a149007e6e7dc0f09d48c5c67773b3c23aae`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3]::If

Source: `infra/agentinfra/governance.py:125`; AST `bacfc9fb7d3f1a2e3041aa339db886c7953128263fdaec9d26158f34568431ea`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: data, hashlib, len, path, relative. Outputs/bindings: data.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest, len, path.is_file, path.read_bytes.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3]; no call, error or mutation may be omitted. Condition: path.is_file()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].test::Call

Source: `infra/agentinfra/governance.py:125`; AST `d2081c59f0765455ac12b468dbfc8371bdf81a7d49d474e10d779496c1e121ac`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].body[0]::Assign

Source: `infra/agentinfra/governance.py:126`; AST `32655bfcede15cf6fa34a0bb6d45b1d10710f55d48d31b55e186f0fe0d220512`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: data.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].body[0].value::Call

Source: `infra/agentinfra/governance.py:126`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].body[1]::Return

Source: `infra/agentinfra/governance.py:127`; AST `82114446a61a476b630257d34a51778cb8d947da029a3b18dd2ac816db91475d`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, hashlib, len, relative. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest, len.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].body[1].value.values[2]::Call

Source: `infra/agentinfra/governance.py:130`; AST `fc74103c13bf8d377d661458ea3a35fc1992328898312d6f40eb90c2671f2ed8`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].body[1].value.values[3]::Call

Source: `infra/agentinfra/governance.py:131`; AST `ec988457fe103b959d993a11b804009071d8c43f7cb3ec64f12df05099c74d63`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[3].body[1].value.values[3].func.value::Call

Source: `infra/agentinfra/governance.py:131`; AST `08f31cedb8064eb17f9167928d61fe53346b78450a1fe6d6c7076f027285d627`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].value.values[3].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::_entry::root.body[18].body[4]::Return

Source: `infra/agentinfra/governance.py:133`; AST `b601845da266a51859903ea352512864c9ce53d909867deac5c24c3269141e08`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19]::FunctionDef

Source: `infra/agentinfra/governance.py:136`; AST `584ab5fc8475d402634caf6e4373f3887031d838f75e166b90f66a4c578ca2be`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GovernanceViolation, Path, _entry, _instruction_files, agents, body, dict, entries, hashlib, is_path_redirect, item, json, path, paths, project, root, set, sorted, str, unique. Outputs/bindings: agents, body, entries, path, paths, project, unique.
Calls/effect boundaries: GovernanceViolation, Path, Path(root).resolve, _entry, _instruction_files, agents.is_dir, agents.rglob, hashlib.sha256, hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest, is_path_redirect, item.relative_to, item.relative_to(project).as_posix, json.dumps, json.dumps(body, sort_keys=True, separators=(',', ':')).encode, set, sorted, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[0]::Expr

Source: `infra/agentinfra/governance.py:137`; AST `4e7bcb6cfa0f8ee8894c1acb9730816bf8419ce91350d52f698e07b9d8793b9f`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[1]::Assign

Source: `infra/agentinfra/governance.py:139`; AST `adfb3a18626509aca1dd4631e301fa61aea2a40280f64962fd9af645b4070072`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: project.
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[1].value::Call

Source: `infra/agentinfra/governance.py:139`; AST `c730489059afc3f4aef1c52b1968dce819ad8d18695e9c28c3f4518931ce9791`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[1].value.func.value::Call

Source: `infra/agentinfra/governance.py:139`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[2]::Assign

Source: `infra/agentinfra/governance.py:140`; AST `edf5fcde52713c8827a56bd18202da6b67d4b217934b1ccf3865f99a2cd9d7bf`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project. Outputs/bindings: agents.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[3]::If

Source: `infra/agentinfra/governance.py:141`; AST `b295770e3a7d67266a2cb816dccb41b53e390745af702c112bfbc8c6cc795a4c`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, agents, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, agents.is_dir, is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[19].body[3]; no call, error or mutation may be omitted. Condition: not agents.is_dir() or is_path_redirect(agents)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[3].test.values[0].operand::Call

Source: `infra/agentinfra/governance.py:141`; AST `6bb36e65b55b7270e23868578ebc038ecf2ad2558aee096988cbdc5d987833bb`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: agents. Outputs/bindings: (none).
Calls/effect boundaries: agents.is_dir.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[3].test.values[1]::Call

Source: `infra/agentinfra/governance.py:141`; AST `216461f87647356d55ba4d082959ee1d6e91a5a080aa201016d24b02ad893a62`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: agents, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[3].body[0]::Raise

Source: `infra/agentinfra/governance.py:142`; AST `1cc4d7e596fae4abf33ac2cc66726d475bf5465940ebc81bd03db4b26f9f7e19`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[3].body[0].exc::Call

Source: `infra/agentinfra/governance.py:142`; AST `f2b325bf6bffa974db18e7bf036aa6d45a184b0376202ccde3ace75b04556335`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[4]::Assign

Source: `infra/agentinfra/governance.py:143`; AST `1d76a13a1476155bed5b39b45178795a782f661f8d1e65df37fe6353b0418203`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _instruction_files, agents, project. Outputs/bindings: paths.
Calls/effect boundaries: _instruction_files, agents.rglob.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[4].value.elts[1].value::Call

Source: `infra/agentinfra/governance.py:143`; AST `d8cf2b503225ec576b825c5f0624b6ab01cf7994653ec8e648b7ad41e9c118f2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: agents. Outputs/bindings: (none).
Calls/effect boundaries: agents.rglob.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].value.elts[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[4].value.elts[2].value::Call

Source: `infra/agentinfra/governance.py:143`; AST `078cd558708f7cacb92b1741f103d5cf2f58d5078c9bd02c7e11c2c960c742d4`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _instruction_files, project. Outputs/bindings: (none).
Calls/effect boundaries: _instruction_files.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].value.elts[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[5]::Assign

Source: `infra/agentinfra/governance.py:144`; AST `36fe0b49f7651536d7e0fd87eb5111584f165bab7ac0da17f49bd6ba3e214b9f`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item, paths, project, set, sorted. Outputs/bindings: unique.
Calls/effect boundaries: item.relative_to, item.relative_to(project).as_posix, set, sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[5].value::Call

Source: `infra/agentinfra/governance.py:144`; AST `697479eae4bfcaf359d3d9874dc6853c915b7b9abd359c0e731edaa75862205b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, paths, project, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(project).as_posix, set, sorted.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[5].value.args[0]::Call

Source: `infra/agentinfra/governance.py:144`; AST `0c0d541993708f3bebe9e652099180d52dd7d1310a565c71fce4cd14fe8fdf98`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: paths, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[5].value.keywords[0].value::Lambda

Source: `infra/agentinfra/governance.py:144`; AST `51c11bd021db9e345f2987fc547ac493ee06213c27cbae0d04943ad321ad0b29`.

Rust module: `infra::agentinfra::governance`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: item, project. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(project).as_posix.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Lambda evaluation at root.body[19].body[5].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[5].value.keywords[0].value.body::Call

Source: `infra/agentinfra/governance.py:144`; AST `ef05cf5492a20717d4f5da736317e871a6a2949ab8720a4ca1715aeeda2c548e`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, project. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to, item.relative_to(project).as_posix.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.keywords[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[5].value.keywords[0].value.body.func.value::Call

Source: `infra/agentinfra/governance.py:144`; AST `b3e1a76f7d17479024ca51cbef31933eb338f5cc0ea341c7e65d599f14e303e1`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, project. Outputs/bindings: (none).
Calls/effect boundaries: item.relative_to.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.keywords[0].value.body.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[6]::Assign

Source: `infra/agentinfra/governance.py:145`; AST `57228978eb99cb6bad700a8a7e80a07f27d1e5d8f821c336ccf541eb203547ac`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _entry, path, project, unique. Outputs/bindings: entries, path.
Calls/effect boundaries: _entry.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[6].value::ListComp

Source: `infra/agentinfra/governance.py:145`; AST `e04364ccb08d9f9d2e2fbafc41e17946aabefca4dd4368ba5b67bc57725dc286`.

Rust module: `infra::agentinfra::governance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _entry, path, project, unique. Outputs/bindings: path.
Calls/effect boundaries: _entry.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ListComp evaluation at root.body[19].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[6].value.elt::Call

Source: `infra/agentinfra/governance.py:145`; AST `3290291b0af17373d4062ba84000494a70c9ff003b6063fc20e63f04797ef170`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _entry, path, project. Outputs/bindings: (none).
Calls/effect boundaries: _entry.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[7]::Assign

Source: `infra/agentinfra/governance.py:146`; AST `f3f64c69fee55ba0e730aebacd625d727e497393e0b0e4c3fe99b548f5bc50e6`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, project, str. Outputs/bindings: body.
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[7].value.values[1]::Call

Source: `infra/agentinfra/governance.py:148`; AST `1475de91c44ce4d417060101e8d7b6de913a11f823247a507fb52d4b35621200`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[8]::Assign

Source: `infra/agentinfra/governance.py:153`; AST `931fc342c8297627d5e04ec7ef9b06f7ce29e088bc5492546dc28900d8dc6571`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: body, hashlib, json. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest, json.dumps, json.dumps(body, sort_keys=True, separators=(',', ':')).encode.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[8].value::Call

Source: `infra/agentinfra/governance.py:153`; AST `952f5b23ac695055c6e17924fc29f5247f2d6ecee4620c0dc3a7ccda3ea81857`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, hashlib, json. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest, json.dumps, json.dumps(body, sort_keys=True, separators=(',', ':')).encode.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[8].value.func.value::Call

Source: `infra/agentinfra/governance.py:153`; AST `9c1d05979e6b6afa4ebe9cfb3cd2ce486dad9e4e1b50aa806eaf1b53feba8228`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, hashlib, json. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, json.dumps, json.dumps(body, sort_keys=True, separators=(',', ':')).encode.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[8].value.func.value.args[0]::Call

Source: `infra/agentinfra/governance.py:154`; AST `3fb7236273bca444222c3b50a67d9c3a37349d90007e5f6b3cf9bf4b01d21713`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.dumps(body, sort_keys=True, separators=(',', ':')).encode.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[8].value.func.value.args[0].func.value::Call

Source: `infra/agentinfra/governance.py:154`; AST `ebc0306a26909f8f3cf1ee96f5f7dbae650c0d73ee46ec5432397cb7ff7eb3b8`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value.func.value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::capture_governance::root.body[19].body[9]::Return

Source: `infra/agentinfra/governance.py:156`; AST `131700ccf0cf544a276b3c71f2d4ca639643d1f976e2a9f3ec4487d0bb231f54`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: body. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[19].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20]::FunctionDef

Source: `infra/agentinfra/governance.py:159`; AST `61a5162ed62101e6b38fdd1cbf621ebcad41d8c52be4b1572e94315fc475b361`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GovernanceViolation, Path, capture_governance, current, dict, isinstance, len, project, root, snapshot, str. Outputs/bindings: current, project.
Calls/effect boundaries: GovernanceViolation, Path, Path(root).resolve, capture_governance, current.get, isinstance, len, snapshot.get, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[0]::If

Source: `infra/agentinfra/governance.py:160`; AST `98d55a59ba80260399c06de39b4f2dc52c2e83e5c084e75227a4e6c62f7a7459`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, dict, isinstance, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, isinstance, snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[20].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(snapshot, dict) or snapshot.get('schema') != 1
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/governance.py:160`; AST `50c4e5deb1cc930128d6684d991be2b7c9b16761f77e6ebcbbb81cc2ed0e097e`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[0].test.values[1].left::Call

Source: `infra/agentinfra/governance.py:160`; AST `ee78e998b657a1454ad9a0a54e8f73730a3a891ea204a594bd3d4c8b7b51ef80`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[0].body[0]::Raise

Source: `infra/agentinfra/governance.py:161`; AST `4a212c567970295d8146b728d928fe4b686bed6103c901b3089e350db69b0bbf`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[20].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[0].body[0].exc::Call

Source: `infra/agentinfra/governance.py:161`; AST `27edadb19b854afe97fd8b53dbd6ddf8564a59884a321ec9e9ac279c9813a416`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[1]::Assign

Source: `infra/agentinfra/governance.py:162`; AST `adfb3a18626509aca1dd4631e301fa61aea2a40280f64962fd9af645b4070072`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: project.
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[1].value::Call

Source: `infra/agentinfra/governance.py:162`; AST `c730489059afc3f4aef1c52b1968dce819ad8d18695e9c28c3f4518931ce9791`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[1].value.func.value::Call

Source: `infra/agentinfra/governance.py:162`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[2]::If

Source: `infra/agentinfra/governance.py:163`; AST `01986f9bfe5bd46107d96f4718edf821c5480f43ed1736507299ab4e887d391d`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, project, snapshot, str. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, snapshot.get, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[20].body[2]; no call, error or mutation may be omitted. Condition: snapshot.get('project_root') != str(project)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[2].test.left::Call

Source: `infra/agentinfra/governance.py:163`; AST `afae8d3ba7cb3131f298a4f4b7c7e5888c9bedf8a2b6d36e0173f7b59c3fd7d1`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[2].test.comparators[0]::Call

Source: `infra/agentinfra/governance.py:163`; AST `1475de91c44ce4d417060101e8d7b6de913a11f823247a507fb52d4b35621200`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[2].body[0]::Raise

Source: `infra/agentinfra/governance.py:164`; AST `426ca96ff31670dd6eca39f17e50adf6526c7fa090ee8b4697bf5159342793a6`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[20].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[2].body[0].exc::Call

Source: `infra/agentinfra/governance.py:164`; AST `efd1006804b0ff6c3396ebb8a969b2b4b97b42025343f2e59d31dc9d534fedf2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[3]::Assign

Source: `infra/agentinfra/governance.py:165`; AST `d706b84e89675a6e2d998eb12b56766a35a2467fabecfe23b117feb878e5b027`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: capture_governance, project. Outputs/bindings: current.
Calls/effect boundaries: capture_governance.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[3].value::Call

Source: `infra/agentinfra/governance.py:165`; AST `ad9032d57a8deb72be62ab905eab66afd130f8e1af8d0eefcad26c4a38c77045`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: capture_governance, project. Outputs/bindings: (none).
Calls/effect boundaries: capture_governance.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4]::If

Source: `infra/agentinfra/governance.py:166`; AST `0e7bd8d4d07c113aea612cf29e8914ed92d8862f7acae9a08e044e766bd8cdf0`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, current, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, current.get, snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[20].body[4]; no call, error or mutation may be omitted. Condition: current.get('digest') != snapshot.get('digest') or current.get('entries') != snapshot.get('entries')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].test.values[0].left::Call

Source: `infra/agentinfra/governance.py:166`; AST `84567399685483783e37cd0f584286a589dee15dc0ed48fe24655f0f9772f9af`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].test.values[0].comparators[0]::Call

Source: `infra/agentinfra/governance.py:166`; AST `2aeef084b15eab20986908131f9cf25ced9491b21c5da2d84c8a7f328dec87dc`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].test.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].test.values[1].left::Call

Source: `infra/agentinfra/governance.py:166`; AST `bfc148105350a5c7dd0816a1bb084e67c1945d655876362dc22f04746b7eab48`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/governance.py:166`; AST `ebfb87f0e9b0b3398e0d0b009c24b26d3c021f40b3a428121257c8e2b96c0fca`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].body[0]::Raise

Source: `infra/agentinfra/governance.py:167`; AST `e929ae3a91cd3ceda2d00cbd72fd35a6e3e82bb5972458abca75a1c8c5448d57`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, current, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, current.get, snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[20].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].body[0].exc::Call

Source: `infra/agentinfra/governance.py:167`; AST `2f098c0f3666b17ada163d47850572954a6d5071ffaab0fb375e8d738e66b790`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, current, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, current.get, snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].body[0].exc.args[0].values[1].value::Call

Source: `infra/agentinfra/governance.py:168`; AST `2aeef084b15eab20986908131f9cf25ced9491b21c5da2d84c8a7f328dec87dc`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].body[0].exc.args[0].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[4].body[0].exc.args[0].values[3].value::Call

Source: `infra/agentinfra/governance.py:168`; AST `84567399685483783e37cd0f584286a589dee15dc0ed48fe24655f0f9772f9af`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].body[0].exc.args[0].values[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[5]::Return

Source: `infra/agentinfra/governance.py:170`; AST `7c3d087727453b5618c279a5825dfd15331fa218f99d540432252d54d65fa0be`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Return evaluation at root.body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::verify_governance::root.body[20].body[5].value.values[2]::Call

Source: `infra/agentinfra/governance.py:170`; AST `cf078c25256903027116a48afc43519f2c18e6e67e92596f867278a93ca953e2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21]::FunctionDef

Source: `infra/agentinfra/governance.py:173`; AST `1c8315ae39bc4b091cecf1774deca3a0f0f8e5b939a33a1e8bb994f3c50f4b80`.

Rust module: `infra::agentinfra::governance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GovernanceViolation, OSError, Path, ValueError, _GOVERNANCE_CREATION_ROOTS, _INSTRUCTION_UPDATE_TARGETS, _governing_file_identities, _identity, _path_key, _relative_casefold, candidate, current, exc, governance_creation, governing_identities, identity, instruction_update, is_path_redirect, normalized_resolved, operation, os, parent, part, project, raw, relative_parts, resolved, resolved_relative, root, str, supplied, targets, tuple. Outputs/bindings: candidate, current, governance_creation, governing_identities, identity, instruction_update, normalized_resolved, parent, part, project, raw, relative_parts, resolved, resolved_relative, supplied.
Calls/effect boundaries: GovernanceViolation, Path, Path(root).resolve, _GOVERNANCE_CREATION_ROOTS.get, _INSTRUCTION_UPDATE_TARGETS.get, _governing_file_identities, _identity, _path_key, _relative_casefold, candidate.absolute, candidate.parent.resolve, current.resolve, is_path_redirect, part.casefold, raw.is_absolute, resolved.relative_to, str, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[0]::Expr

Source: `infra/agentinfra/governance.py:174`; AST `67abfee1c3fd5e220d722cb076c8275d511e7906dc75fd05d6cc8531b80018af`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[1]::Assign

Source: `infra/agentinfra/governance.py:181`; AST `adfb3a18626509aca1dd4631e301fa61aea2a40280f64962fd9af645b4070072`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: project.
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[1].value::Call

Source: `infra/agentinfra/governance.py:181`; AST `c730489059afc3f4aef1c52b1968dce819ad8d18695e9c28c3f4518931ce9791`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[1].value.func.value::Call

Source: `infra/agentinfra/governance.py:181`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[2]::Assign

Source: `infra/agentinfra/governance.py:182`; AST `c7dde4cc595e119c6095221729bfd30b1b11ee13f1360edbb13accd3daa3454d`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _GOVERNANCE_CREATION_ROOTS, project, str. Outputs/bindings: governance_creation.
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.get, str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[2].value.left::Call

Source: `infra/agentinfra/governance.py:182`; AST `1475de91c44ce4d417060101e8d7b6de913a11f823247a507fb52d4b35621200`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[2].value.comparators[0]::Call

Source: `infra/agentinfra/governance.py:182`; AST `e9af4fa3b4058e9a0cfef4da48b6d2b6876917d8c2f4497f81c1b3059800fd8d`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _GOVERNANCE_CREATION_ROOTS. Outputs/bindings: (none).
Calls/effect boundaries: _GOVERNANCE_CREATION_ROOTS.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[3]::Assign

Source: `infra/agentinfra/governance.py:183`; AST `2f0f3eeeb7bbc52a4cee4e417c23f044064224f45c17740ca9c6a5dc79721a86`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _governing_file_identities, project. Outputs/bindings: governing_identities.
Calls/effect boundaries: _governing_file_identities.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[3].value::Call

Source: `infra/agentinfra/governance.py:183`; AST `ae5509a37618a393211bc8ede60a542d6be1f6286469724e7951cb56b82212ca`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _governing_file_identities, project. Outputs/bindings: (none).
Calls/effect boundaries: _governing_file_identities.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4]::For

Source: `infra/agentinfra/governance.py:184`; AST `8b63ddb422ec6fbfe226155b1d82dfd4d9f176a28b2aec560f94b2421302f216`.

Rust module: `infra::agentinfra::governance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: GovernanceViolation, OSError, Path, ValueError, _INSTRUCTION_UPDATE_TARGETS, _identity, _path_key, _relative_casefold, candidate, current, exc, governance_creation, governing_identities, identity, instruction_update, is_path_redirect, normalized_resolved, operation, os, parent, part, project, raw, relative_parts, resolved, resolved_relative, supplied, targets, tuple. Outputs/bindings: candidate, current, identity, instruction_update, normalized_resolved, parent, part, raw, relative_parts, resolved, resolved_relative, supplied.
Calls/effect boundaries: GovernanceViolation, Path, _INSTRUCTION_UPDATE_TARGETS.get, _identity, _path_key, _relative_casefold, candidate.absolute, candidate.parent.resolve, current.resolve, is_path_redirect, part.casefold, raw.is_absolute, resolved.relative_to, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered For evaluation at root.body[21].body[4]; no call, error or mutation may be omitted. Iteration: supplied in targets
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[0]::Assign

Source: `infra/agentinfra/governance.py:185`; AST `e0a7d962d0ad5acbcde954c8b1199971e343b42e4d18dd42b79aefcab39f51c1`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, supplied. Outputs/bindings: raw.
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[0].value::Call

Source: `infra/agentinfra/governance.py:185`; AST `c84a64ac4df534861f829c1d6ff33a700d596b8df58f150bcefa49154c8acf4b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, supplied. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[1]::If

Source: `infra/agentinfra/governance.py:186`; AST `7c558f0de106e579d8ca91b74d90c8dddbdaaab019b3b900cbe229017a1f7daa`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, operation, raw, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, raw.is_absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[1]; no call, error or mutation may be omitted. Condition: not raw.is_absolute() and '..' in raw.parts
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[1].test.values[0].operand::Call

Source: `infra/agentinfra/governance.py:186`; AST `988e0b836d3be7a8bdd28c2d328869df6f375964196e0741a1384f9a809835e5`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.is_absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[1].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[1].body[0]::Raise

Source: `infra/agentinfra/governance.py:187`; AST `4667d567435cd9097779169263154f8ceb8c8dafe2ddecce771b2100442320e7`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, operation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[1].body[0].exc::Call

Source: `infra/agentinfra/governance.py:187`; AST `fc8708f90437d65be526c72924420fa902a8f9c69926421ad8e04df5c4c6a1e6`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, operation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[2]::Assign

Source: `infra/agentinfra/governance.py:188`; AST `62798f1a5c92b4c3f853ae4a147a68cee48e2120ff6840a5552d7386241aff2a`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project, raw. Outputs/bindings: candidate.
Calls/effect boundaries: raw.is_absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[2].value.test::Call

Source: `infra/agentinfra/governance.py:188`; AST `988e0b836d3be7a8bdd28c2d328869df6f375964196e0741a1384f9a809835e5`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.is_absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[2].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[3]::Assign

Source: `infra/agentinfra/governance.py:189`; AST `161df9220fbc554c488cb361b61b44b161e168b8fce2b09d943ac91063322482`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _INSTRUCTION_UPDATE_TARGETS, _path_key, candidate. Outputs/bindings: instruction_update.
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.get, _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[3].value.left::Call

Source: `infra/agentinfra/governance.py:189`; AST `4dba725311222a0ff68b5e86faa120af3dfa834eb034d5eaf5c6ca5d51f24d74`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _path_key, candidate. Outputs/bindings: (none).
Calls/effect boundaries: _path_key.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[3].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[3].value.comparators[0]::Call

Source: `infra/agentinfra/governance.py:189`; AST `2682c1e92b30fef44b60f47633376f41aad3e3f5627b101b0608ddb6e0e6db4e`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _INSTRUCTION_UPDATE_TARGETS. Outputs/bindings: (none).
Calls/effect boundaries: _INSTRUCTION_UPDATE_TARGETS.get.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[3].value.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[4]::Assign

Source: `infra/agentinfra/governance.py:190`; AST `a019eeb79eb037080395f4d058c7cd7dafc7de332ee5fe37bd8a85ebe9d5e736`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _relative_casefold, candidate, project. Outputs/bindings: relative_parts.
Calls/effect boundaries: _relative_casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[4].value::Call

Source: `infra/agentinfra/governance.py:190`; AST `f3fa546fa1cda42775eae5167599ffec5c146858da41b583479cdca8fbbac1b1`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _relative_casefold, candidate, project. Outputs/bindings: (none).
Calls/effect boundaries: _relative_casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[5]::If

Source: `infra/agentinfra/governance.py:191`; AST `d4b22687892d9f2f26b72228fd2d5775b2c3764c6b8d7298cd92956db9cbf53f`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, operation, relative_parts, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[5]; no call, error or mutation may be omitted. Condition: relative_parts is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[5].body[0]::Raise

Source: `infra/agentinfra/governance.py:192`; AST `4e602c92a207810f2928e9f5c3bf27b0328bba0dbfd81ba73af59c51e4dbae41`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, operation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[5].body[0].exc::Call

Source: `infra/agentinfra/governance.py:192`; AST `294587d2f7398a514f49cd10a8c9fef3a6dad5ddccda3130ac926658ba7bbcd5`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, operation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[5].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[6]::If

Source: `infra/agentinfra/governance.py:193`; AST `4b72a977db8073002bd95b0246db5bcd5eee02f37254e7ec2463383bc4984679`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, governance_creation, relative_parts, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[6]; no call, error or mutation may be omitted. Condition: relative_parts and relative_parts[0] == '.agents' and (not governance_creation)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[6].body[0]::Raise

Source: `infra/agentinfra/governance.py:194`; AST `f5b1e23c5fe52cad4e1167fc75a6ec5a4743615ba771070c9bdd5e8d2e73481d`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[6].body[0].exc::Call

Source: `infra/agentinfra/governance.py:194`; AST `61ba16c7ee0ac79ad61bac06f35d61955e993908b6cc866c1594cd2aa629cae9`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[6].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[7]::If

Source: `infra/agentinfra/governance.py:195`; AST `599e66dedfab7ac7442a18c95ca686bfe13c25d64d9f60a3d889b3ae5ffa076f`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, instruction_update, os, relative_parts, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[7]; no call, error or mutation may be omitted. Condition: relative_parts and relative_parts[-1] == ('agents.md' if os.name == 'nt' else 'AGENTS.md') and (not instruction_update)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[7].body[0]::Raise

Source: `infra/agentinfra/governance.py:200`; AST `012eee81630122d33843665e72be4ffd37b45c554f53f115b0ed32b5bee2787e`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[7].body[0].exc::Call

Source: `infra/agentinfra/governance.py:200`; AST `15a755247b649a2b9fc11cb80bbeb6d66b7df673a893eb346d59cc580671ede0`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[7].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[8]::Assign

Source: `infra/agentinfra/governance.py:202`; AST `eb60ce5fe8988e63a1f13045e380004935fbb2a7a2cdb982dde8d815a94dbcea`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate. Outputs/bindings: current.
Calls/effect boundaries: candidate.absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[8].value::Call

Source: `infra/agentinfra/governance.py:202`; AST `ddceaeafa337d658529684b30e389d6d0263f5236014a8429d70d7ad46426aa2`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.absolute.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9]::While

Source: `infra/agentinfra/governance.py:203`; AST `3b49f84b5d989c972b61d55ae8abfc796087b345d3e5c954d54b74db3c7b5bc9`.

Rust module: `infra::agentinfra::governance`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: GovernanceViolation, OSError, current, exc, is_path_redirect, operation, parent, project, supplied. Outputs/bindings: current, parent.
Calls/effect boundaries: GovernanceViolation, current.resolve, is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered While evaluation at root.body[21].body[4].body[9]; no call, error or mutation may be omitted. Condition: True
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[0]::If

Source: `infra/agentinfra/governance.py:204`; AST `9513c9cbdefc376405530fbd2f1e91d5f7f38a8c77260b219f26605acde67c20`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[9].body[0]; no call, error or mutation may be omitted. Condition: is_path_redirect(current)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[0].test::Call

Source: `infra/agentinfra/governance.py:204`; AST `40016ece3accb20f8c991e15dbde33edb0976b624a9765bc08db3981c15afe10`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[9].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[0].body[0]::Raise

Source: `infra/agentinfra/governance.py:205`; AST `ea95257f5e03c72e27e8b67383319e0ba1f29e7e0e66f85b8762e6527f8e6476`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, current. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[0].body[0].exc::Call

Source: `infra/agentinfra/governance.py:205`; AST `caa8a5601a437279827c50805e126a8e77ec5b391cbddffe8bfe1c03084b0224`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, current. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[9].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1]::Try

Source: `infra/agentinfra/governance.py:206`; AST `b64716265c1d69ed5f4bff030d9c1feb29f0d3fdde545084cc1eeb81da48481b`.

Rust module: `infra::agentinfra::governance`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: GovernanceViolation, OSError, current, exc, project. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation, current.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Try evaluation at root.body[21].body[4].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1].body[0]::If

Source: `infra/agentinfra/governance.py:207`; AST `6b8cb21c79197eba5f80b14417d8679a34bc6f489731aed4bfb58c4554c72b7d`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, project. Outputs/bindings: (none).
Calls/effect boundaries: current.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[9].body[1].body[0]; no call, error or mutation may be omitted. Condition: current.resolve(strict=False) == project
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1].body[0].test.left::Call

Source: `infra/agentinfra/governance.py:207`; AST `75660c4503b14a163ef89f8fd71005ef913b8a50d4d629b6b2f7824a7d11a9de`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[9].body[1].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1].body[0].body[0]::Break

Source: `infra/agentinfra/governance.py:208`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Break evaluation at root.body[21].body[4].body[9].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/governance.py:209`; AST `090dc1a4c3e7550b3027af433c850d8056950124d0daa96adff9d45011149d74`.

Rust module: `infra::agentinfra::governance`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: GovernanceViolation, OSError, current, exc. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[21].body[4].body[9].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1].handlers[0].body[0]::Raise

Source: `infra/agentinfra/governance.py:210`; AST `826ff323341dd9bbaefdec250152230a1eb0e305f7695aae4d21e2e65e2a7ada`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, current, exc. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[9].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[1].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/governance.py:210`; AST `d74f96917361a80a891fc0df4966c4c3062e8165ffffacf8afe8b6ad962767ce`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, current. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[9].body[1].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[2]::Assign

Source: `infra/agentinfra/governance.py:213`; AST `65fc7ab6e71093d57d0573e86b4571df0db7325ff31deae8755fbb1167b56a7b`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current. Outputs/bindings: parent.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[3]::If

Source: `infra/agentinfra/governance.py:214`; AST `24ab8064643dd4954ca53fd7af5a61098df6ff0e5368e1501dbc78f5b1bc0cc1`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, current, operation, parent, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[9].body[3]; no call, error or mutation may be omitted. Condition: parent == current
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[3].body[0]::Raise

Source: `infra/agentinfra/governance.py:215`; AST `d71751bffabe2bc4d1c5659cfb9a0a9606fd2dce04ab6918e50db7ccaf16b52c`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, operation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[9].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[3].body[0].exc::Call

Source: `infra/agentinfra/governance.py:215`; AST `b3a3ec0e160683a8f3b7c17718f0fe95927d8c433c8a167dd338c05559f691ef`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, operation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[9].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[9].body[4]::Assign

Source: `infra/agentinfra/governance.py:218`; AST `da2b7dbc5b683178e62c3ce083fc2e9c83d6d308477dd4a842488b2e3e161b08`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parent. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[10]::Assign

Source: `infra/agentinfra/governance.py:220`; AST `91092e1a15efdcf52f2485c3225e2e129ffda1cb52b40c45d95f82ebfbb461d8`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate. Outputs/bindings: resolved.
Calls/effect boundaries: candidate.parent.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[10].value.left::Call

Source: `infra/agentinfra/governance.py:220`; AST `816865b7ac8fbb50b64c521dbb56b1a62b5348247859df0ba2968f97fbdcaaef`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.parent.resolve.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[10].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[11]::Try

Source: `infra/agentinfra/governance.py:221`; AST `0a357ce4c217925121682dff6a53a039fb97681f6e6f0ed73ddd843c207ec165`.

Rust module: `infra::agentinfra::governance`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: GovernanceViolation, ValueError, exc, project, resolved, supplied. Outputs/bindings: resolved_relative.
Calls/effect boundaries: GovernanceViolation, resolved.relative_to.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Try evaluation at root.body[21].body[4].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[11].body[0]::Assign

Source: `infra/agentinfra/governance.py:222`; AST `c493d353f05a90e893cfd96e393dfb8c7ee444b19f8c049b6239ce102d690e80`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project, resolved. Outputs/bindings: resolved_relative.
Calls/effect boundaries: resolved.relative_to.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[11].body[0].value::Call

Source: `infra/agentinfra/governance.py:222`; AST `2d48fa3f563e84ca03330cb71ec485c715150f6da1753bdfd488537a4302bd46`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, resolved. Outputs/bindings: (none).
Calls/effect boundaries: resolved.relative_to.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[11].handlers[0]::ExceptHandler

Source: `infra/agentinfra/governance.py:223`; AST `2972e9c52ce815ab5e955c9dbbf751cec216bdbd80b302c368f819a3fc0ff513`.

Rust module: `infra::agentinfra::governance`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: GovernanceViolation, ValueError, exc, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[21].body[4].body[11].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[11].handlers[0].body[0]::Raise

Source: `infra/agentinfra/governance.py:224`; AST `68e4a874736b76c2cdb325196ddeefc1b49451ba37d63ea0f1086ffdccb13e98`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, exc, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[11].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[11].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/governance.py:224`; AST `a04dac46ccf1d9f42a5633a6c8f35ff080306f6ab2c7884cece6ce1badc64da8`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[11].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[12]::Assign

Source: `infra/agentinfra/governance.py:225`; AST `ebce2b81856578a8ce0af6e7e72f6bb4542fe7ceeb59b4d63c33ae88763785f8`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, part, resolved_relative, tuple. Outputs/bindings: normalized_resolved, part.
Calls/effect boundaries: part.casefold, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[12].value::Call

Source: `infra/agentinfra/governance.py:225`; AST `3820dc84364be62b167c7dd2c83b6031e61b42a907606629620c2d97b31872ba`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, part, resolved_relative, tuple. Outputs/bindings: part.
Calls/effect boundaries: part.casefold, tuple.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[12].value.args[0]::GeneratorExp

Source: `infra/agentinfra/governance.py:225`; AST `41bf5fcaedb44270b62ac331c86f4ddb86f2dc170a2e838ed169210e332c6734`.

Rust module: `infra::agentinfra::governance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: os, part, resolved_relative. Outputs/bindings: part.
Calls/effect boundaries: part.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[21].body[4].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[12].value.args[0].elt.body::Call

Source: `infra/agentinfra/governance.py:226`; AST `079800cd1ad1fe20aa29eb38543d80a675f545f21b9983ce42988e6d58c588c8`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: part. Outputs/bindings: (none).
Calls/effect boundaries: part.casefold.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[12].value.args[0].elt.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[13]::If

Source: `infra/agentinfra/governance.py:228`; AST `63b9a2ec8808178f6869ea994c319e5a60727c7d79fe39257730c0177cbef416`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, governance_creation, normalized_resolved, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[13]; no call, error or mutation may be omitted. Condition: normalized_resolved and normalized_resolved[0] == '.agents' and (not governance_creation)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[13].body[0]::Raise

Source: `infra/agentinfra/governance.py:229`; AST `f2afe7491ac349bebee806922ec8e8d06a5ca7ce48c684d505e60623c02ceecc`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[13].body[0].exc::Call

Source: `infra/agentinfra/governance.py:229`; AST `ab9601b7ab74e789ecb08c1d3f3b45c231949f50e4aa707e5a0821574903e991`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[13].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[14]::Assign

Source: `infra/agentinfra/governance.py:230`; AST `030e2b7fc4f65efa3253a677da69e19cd2a24970df5f9563695ea0532ad497a0`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _identity, candidate. Outputs/bindings: identity.
Calls/effect boundaries: _identity.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[14].value::Call

Source: `infra/agentinfra/governance.py:230`; AST `fd2db82e4df7efdde55799428916a3467ebf2875d1791f122d0f78350b0e903b`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _identity, candidate. Outputs/bindings: (none).
Calls/effect boundaries: _identity.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[15]::If

Source: `infra/agentinfra/governance.py:231`; AST `2fe378eddeaeee5f109db1e4ad90158c5ff60df06268722dd4a2a7cdba59c2da`.

Rust module: `infra::agentinfra::governance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GovernanceViolation, governing_identities, identity, instruction_update, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[15]; no call, error or mutation may be omitted. Condition: identity is not None and identity in governing_identities and (not instruction_update)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[15].body[0]::Raise

Source: `infra/agentinfra/governance.py:232`; AST `2593e8b656105d91f2ac2773dc90cde459199462e3dbb84b1f527e9b0f4be970`.

Rust module: `infra::agentinfra::governance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[4].body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/governance.py::module::assert_mutation_allowed::root.body[21].body[4].body[15].body[0].exc::Call

Source: `infra/agentinfra/governance.py:232`; AST `6cdcf8645f3e0a68a7513899b3496f5ec88eb4394f61e82b8ae419856bbb44e3`.

Rust module: `infra::agentinfra::governance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GovernanceViolation, supplied. Outputs/bindings: (none).
Calls/effect boundaries: GovernanceViolation.
Dependencies: __future__, contextlib, contextvars, hashlib, json, os, pathlib, security.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[15].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
