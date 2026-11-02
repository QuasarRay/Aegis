# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 28. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_scope.py::module::root::Module

Source: `infra/agentinfra/roadmap_scope.py:1`; AST `c570221569b675eaa4a5ac37b1a0d5f4f07481fecdffa3eb6851b1bdc282c8c9`.

Rust module: `infra::agentinfra::roadmap_scope`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, PurePosixPath, any, bool, confined_path, contract, dict, fnmatchcase, list, name, p, path, paths, require, root, str. Outputs/bindings: name, p, path.
Calls/effect boundaries: PurePosixPath, any, bool, confined_path, fnmatchcase, path.is_absolute, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_scope.py:1`; AST `1736a16da3e5da614b36920ee71106b95071617f2ff8505f6ab5be99521bce98`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_scope.py:2`; AST `5a4d5aee3e8b8e43e04439231735e712438acb7be12f9452a6a6a3ad1da90da8`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_scope.py:3`; AST `40c6b803ee13cbcec633052def0cd7814baf9bfd67818b3dd46dd82625d3e333`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_scope.py:5`; AST `e95249989368c7d7ae0f1aa5a170930b03e95124541e59b22a0e6a58198a3be2`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_scope.py:6`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_scope.py:9`; AST `d60a6d5bdaaa88f7d1294fb205425d2cf77d172a43856127a7b53723363f1e4b`.

Rust module: `infra::agentinfra::roadmap_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, PurePosixPath, any, bool, confined_path, contract, dict, fnmatchcase, list, name, p, path, paths, require, root, str. Outputs/bindings: name, p, path.
Calls/effect boundaries: PurePosixPath, any, bool, confined_path, fnmatchcase, path.is_absolute, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_scope.py:10`; AST `db6c46c4ad5aef0817055711842b27260a87b73b464fbaa48d0007df73d2ea62`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, paths, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_scope.py:10`; AST `eef4764bcae37c244db1072d77015e5375edc2bcda2f06adcd8f5f45c6c20d8b`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, paths, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_scope.py:10`; AST `28c20a38faccf6f5e045e227bb6b6ca5fa9a19b283260ef7f5fb45752b7cabc5`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, paths. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1]::For

Source: `infra/agentinfra/roadmap_scope.py:11`; AST `6ca20613ecbda2613cf4add24adf5d29417c7a22ce7ef9a9db72d9ef58ad6b57`.

Rust module: `infra::agentinfra::roadmap_scope`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: PurePosixPath, any, confined_path, contract, fnmatchcase, name, p, path, paths, require, root. Outputs/bindings: name, p, path.
Calls/effect boundaries: PurePosixPath, any, confined_path, fnmatchcase, path.is_absolute, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered For evaluation at root.body[5].body[1]; no call, error or mutation may be omitted. Iteration: name in paths
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_scope.py:12`; AST `83077c68c8b276e1d8a694f60d13d940e0bdeb91b3d4b875b75ff9f5015c902c`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PurePosixPath, name. Outputs/bindings: path.
Calls/effect boundaries: PurePosixPath.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_scope.py:12`; AST `cc48c4c9f96747100b7a924d79efd2ae9d5fdec8080b87f89008f71c72cf773e`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PurePosixPath, name. Outputs/bindings: (none).
Calls/effect boundaries: PurePosixPath.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_scope.py:13`; AST `3850688d5b45f08f3c1cf711f4a8c0da026c6e3d7bafdfaa2474e02e67476a55`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.is_absolute, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_scope.py:13`; AST `5c0fab3e8ff63fe0974fe55b6ab1c3aaf5b24463bfb74d50ec5a596ff93e70ce`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.is_absolute, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[1].value.args[0].values[0].operand::Call

Source: `infra/agentinfra/roadmap_scope.py:13`; AST `b6c359348f99100e1e49132bf117e1cf4485da0246e8b496522239d8400f0c44`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_absolute.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[1].value.args[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_scope.py:14`; AST `354a3880726cd5c698cfeabf9a57095c24d956fc85b0b0970b994a07787624c1`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_scope.py:14`; AST `b47a8a3b6f15106807bf162be4b1ff7629277aaa3b76c7468e899a83ccabbf03`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_scope.py:15`; AST `249d16834c252cd97e093acd04459f8d15ef2c08a2aece4fde0eccb9b2ea94db`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, contract, fnmatchcase, name, p, require. Outputs/bindings: p.
Calls/effect boundaries: any, fnmatchcase, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_scope.py:15`; AST `919b2e9eb6ed464447040fc0e4d9ef9ab82f7b5584332b489d11ec54851aee13`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, contract, fnmatchcase, name, p, require. Outputs/bindings: p.
Calls/effect boundaries: any, fnmatchcase, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[3].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_scope.py:15`; AST `6045c12f3888b5827af488b04b21f93dc5710821daf890391509a9ad8d3046bd`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, contract, fnmatchcase, name, p. Outputs/bindings: p.
Calls/effect boundaries: any, fnmatchcase.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[3].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[3].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_scope.py:15`; AST `e91bb8e06f723d8b2f3a530f5a4fd8f8f1c6b135fded46d3c5a93b281a931f1b`.

Rust module: `infra::agentinfra::roadmap_scope`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: contract, fnmatchcase, name, p. Outputs/bindings: p.
Calls/effect boundaries: fnmatchcase.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[5].body[1].body[3].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[3].value.args[0].operand.args[0].elt::Call

Source: `infra/agentinfra/roadmap_scope.py:15`; AST `40b7e1559ff357dbd0050b8d616968e1fb0e97db08255d23531addf7b3d56418`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fnmatchcase, name, p. Outputs/bindings: (none).
Calls/effect boundaries: fnmatchcase.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[3].value.args[0].operand.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[4]::Expr

Source: `infra/agentinfra/roadmap_scope.py:16`; AST `fe18d7070fdba0e62f9982bf9e9f80731bf2fa8399f478284e52f7ebdf30ec3d`.

Rust module: `infra::agentinfra::roadmap_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, contract, fnmatchcase, name, p, require. Outputs/bindings: p.
Calls/effect boundaries: any, fnmatchcase, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[4].value::Call

Source: `infra/agentinfra/roadmap_scope.py:16`; AST `e5cb73c59f926bb2fbdd8e6cd3d5c63b1cab9019359de91505ff333c911553b5`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, contract, fnmatchcase, name, p, require. Outputs/bindings: p.
Calls/effect boundaries: any, fnmatchcase, require.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_scope.py:16`; AST `79d038c9699ea1baff66da4d00ae6e7eba4528d976377e6dc664aadb73a7a857`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, contract, fnmatchcase, name, p. Outputs/bindings: p.
Calls/effect boundaries: any, fnmatchcase.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[4].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_scope.py:16`; AST `4c4ae22c8ebf7670bae8c3b6c37ec73ad4de931fbb20eda316d1848d21288b05`.

Rust module: `infra::agentinfra::roadmap_scope`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: contract, fnmatchcase, name, p. Outputs/bindings: p.
Calls/effect boundaries: fnmatchcase.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[5].body[1].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_scope.py::module::validate_write_scope::root.body[5].body[1].body[4].value.args[0].args[0].elt::Call

Source: `infra/agentinfra/roadmap_scope.py:16`; AST `40b7e1559ff357dbd0050b8d616968e1fb0e97db08255d23531addf7b3d56418`.

Rust module: `infra::agentinfra::roadmap_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fnmatchcase, name, p. Outputs/bindings: (none).
Calls/effect boundaries: fnmatchcase.
Dependencies: fnmatch, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[4].value.args[0].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
