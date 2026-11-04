# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 104. Inventory digest: `1983e24340b360b436af8cad0c38b5fcf1e06f677dc7d6368f2ab82f4ef9abd6`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_protocol.py::module::root::Module

Source: `infra/agentinfra/roadmap_protocol.py:1`; AST `9b1ea8976a683903830ffbb6ba9f16e54377f92ab0367dd5ec45280162589b00`.

Rust module: `infra::agentinfra::roadmap_protocol`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: INTERFACE_VERSION, Path, REQUIRED_SCHEMAS, b, binding, bindings_current, bool, choices, confined_path, dict, digest, directory, document, executable, file_binding, files, isinstance, k, len, manifest, matches, name, native_executable, p, path, read_json, relative, require, result, root, selected, shutil, size, sorted, source, str, total_bytes, v, v2. Outputs/bindings: INTERFACE_VERSION, REQUIRED_SCHEMAS, b, binding, choices, directory, document, executable, files, k, matches, name, p, path, result, selected, size, source, total_bytes, v, v2.
Calls/effect boundaries: Path, Path(executable).resolve, bindings_current, bool, confined_path, digest, directory.relative_to, directory.relative_to(root).as_posix, directory.rglob, document.get, file_binding, files.append, isinstance, len, manifest.get, manifest.items, name.removesuffix, native_executable, p.relative_to, p.relative_to(root).as_posix, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, path.stat, read_json, require, shutil.which, sorted, str.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:1`; AST `11905d27208ab97313f83decfd7fa153948cfb26ce360ad9bb7c7f88a0e78ad2`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_protocol.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_protocol.py:9`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_protocol.py:10`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_protocol.py:12`; AST `94f2ef7cfe57c7bfab987ff333d99818aa195b2b2e4f09c3d8608a99d87b2cad`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_protocol.py:13`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[6]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:16`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::root.body[7]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:17`; AST `99cb50c595ddfce3b42994761dbd91ff2340a96416bb08f81f95645adedd6f8f`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: REQUIRED_SCHEMAS.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8]::FunctionDef

Source: `infra/agentinfra/roadmap_protocol.py:32`; AST `72fa01151673a3e19f819d430f65b9bc55df3af146bf9aad00f615a2dff9a28d`.

Rust module: `infra::agentinfra::roadmap_protocol`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bool, dict, digest, executable, path, require, shutil, str. Outputs/bindings: executable, path.
Calls/effect boundaries: Path, Path(executable).resolve, bool, digest, path.read_bytes, require, shutil.which, str.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:33`; AST `41369df48ac8422a92c62796a520e821f604c4f732283dac8ce4be2794ddd337`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shutil. Outputs/bindings: executable.
Calls/effect boundaries: shutil.which.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:33`; AST `74e40017e0d8a1e9fff531821829ee7b9afd000ad00736ac7ac428deca217c0f`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.which.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[1]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:34`; AST `d6b65431edd198227b852fe3fbab2a3d01a9de6e72f0c6b1f53982546164ae91`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, executable, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[1].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:34`; AST `acfebd03ecdb9f0f1ac454c1873652eb0e72d79fbd3129f5daa3b705c8d2ba20`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, executable, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:34`; AST `aea1d522ef7b1cf2d77f32776bab225772ac4e21f66f84bc933301d75bf0edba`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, executable. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[2]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:35`; AST `b66884aa2a5959bb909d78ecfdc94891c04ff6200c34092db88f991e04a514e8`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, executable. Outputs/bindings: path.
Calls/effect boundaries: Path, Path(executable).resolve.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[2].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:35`; AST `997f55a5ba4607afc8857eed60536fd757ff54753828404b601480b5c396b408`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, executable. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(executable).resolve.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_protocol.py:35`; AST `145064ef9744a4eda972af4ac21c58fe4aa63f6cf41277ffa3c839cd040c8c3d`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, executable. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[3]::Return

Source: `infra/agentinfra/roadmap_protocol.py:36`; AST `a1aca61f263342126b60c4fcf85796f0678637c79ced98d54a572b428fc82a25`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, path, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, str.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Return evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[3].value.values[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:36`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[3].value.values[1]::Call

Source: `infra/agentinfra/roadmap_protocol.py:36`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::native_executable::root.body[8].body[3].value.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:36`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_protocol.py:39`; AST `1c04960871376e2871b619d111cce0218ff14e9219354a670760a1fdbe729895`.

Rust module: `infra::agentinfra::roadmap_protocol`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: INTERFACE_VERSION, Path, REQUIRED_SCHEMAS, b, binding, bool, choices, confined_path, dict, digest, directory, document, executable, file_binding, files, isinstance, len, matches, name, native_executable, path, read_json, relative, require, result, root, selected, size, sorted, source, str, total_bytes, v2. Outputs/bindings: b, binding, choices, directory, document, files, matches, name, path, result, selected, size, source, total_bytes, v2.
Calls/effect boundaries: Path, bool, confined_path, digest, directory.relative_to, directory.relative_to(root).as_posix, directory.rglob, document.get, file_binding, files.append, isinstance, len, name.removesuffix, native_executable, path.relative_to, path.relative_to(root).as_posix, path.stat, read_json, require, sorted.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:40`; AST `50f5b66cb75918cff22161ea859e7ab60652889d4ea309a53ccb3d62d036eb47`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: executable, native_executable, require. Outputs/bindings: (none).
Calls/effect boundaries: native_executable, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:40`; AST `14fee33336fc5d379af2256f1742ba313e0aa11258e9ff7af8c87d13d00c1392`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: executable, native_executable, require. Outputs/bindings: (none).
Calls/effect boundaries: native_executable, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:40`; AST `0c0169e13211f454ccdfd35a970ee34724818b99d569587ebd849bfc7e40d304`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_executable. Outputs/bindings: (none).
Calls/effect boundaries: native_executable.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[1]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:41`; AST `7eef8dbdb6b9447a6f63ca788726c6ca88596be78e9e96632092efe82f829108`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:41`; AST `63c9acf4cfde20a50eacc658154bbb4ec3954f19236b82666a93c852e8d25e5a`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:42`; AST `0c2eacfd48f178abcf50aa532a831f3b6a5a5e8a9f897cca11dcde7734ab24d2`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: files.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[3]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:43`; AST `1d6cf4d43d7ee749c50bf3f631b5a0a7c4de40e98dcd7e4cb13922ee14b96583`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: total_bytes.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4]::For

Source: `infra/agentinfra/roadmap_protocol.py:44`; AST `26e52e303a56946dc36bd64fb5378eecf84a04659c42c98551d50c3c113342f8`.

Rust module: `infra::agentinfra::roadmap_protocol`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, dict, directory, file_binding, files, isinstance, len, path, read_json, require, root, size, sorted, total_bytes. Outputs/bindings: binding, path, size, total_bytes.
Calls/effect boundaries: directory.rglob, file_binding, files.append, isinstance, len, path.relative_to, path.relative_to(root).as_posix, path.stat, read_json, require, sorted.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered For evaluation at root.body[9].body[4]; no call, error or mutation may be omitted. Iteration: path in sorted(directory.rglob('*.json'))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].iter::Call

Source: `infra/agentinfra/roadmap_protocol.py:44`; AST `471b6f5ab34311098b277cc741ba14db22ff66c980d43c76fb1c9231b0432d3f`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, sorted. Outputs/bindings: (none).
Calls/effect boundaries: directory.rglob, sorted.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].iter.args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:44`; AST `bca3675770cb44c2e84f36d65508f7d7564e1c68b073af88be953197f6169416`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rglob.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:45`; AST `b7f1dadc2f13363339751ecca92d707423981b77813c806cd947f7603cca77df`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, path, root. Outputs/bindings: binding.
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:45`; AST `2c1d399eb4c612b95d094d3989bf013bade70bc9afc145ec6ca0de71d6073a62`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_protocol.py:45`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[0].value.args[1].func.value::Call

Source: `infra/agentinfra/roadmap_protocol.py:45`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:46`; AST `715780096b7174e04275d7ef9dc4692f6199f65b978b4170e5f785e3230aa46e`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: size.
Calls/effect boundaries: path.stat.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[1].value.value::Call

Source: `infra/agentinfra/roadmap_protocol.py:46`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[2]::AugAssign

Source: `infra/agentinfra/roadmap_protocol.py:47`; AST `ee9fc279a8d0d068b1db63562f56d1eadef0e5f7be863f2ca2956c169638ee72`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: size. Outputs/bindings: total_bytes.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered AugAssign evaluation at root.body[9].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:48`; AST `0ec769e02fc7675deab641e73245395d9145c1933e16c01f220ab7dfdf38a1f5`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: files, len, require, size, total_bytes. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:48`; AST `5f95d830bee1d29f8bfb58a0c9fb1eb84317360a28c37859086a73d79f26d3b8`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, len, require, size, total_bytes. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[3].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:48`; AST `249405f5c06efa5692390e6b7257e5c24b86a142c0479c7ebc1a2478920f247e`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[4]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:50`; AST `c6c27360ee30c68add0147b622d73f47a15ee4de00a4fa83c1ec2aa547d6cbdb`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, path, read_json, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, read_json, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:50`; AST `1211234f1387bdaaffaae6ca685b468c818a4c4df93f5339604d94f479625368`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, path, read_json, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, read_json, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:50`; AST `a9371ec5c28cfaaaa8a0abbea9007a2139ee00671d6a3494a3d0311f77ea8873`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, read_json.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[4].value.args[0].args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:50`; AST `ca2a99ec0b14545aba864c1e6b22415e5a02ad33955de7320b863aa9c805bfcd`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[5]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:51`; AST `656662ae64684b48f7ef452bac78aab1135f0268452959a6c3b98a35cfce4e3a`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, files. Outputs/bindings: (none).
Calls/effect boundaries: files.append.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[4].body[5].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:51`; AST `65e41c8aa84be81526a885d89c58216d241b2c9b0e79084332ad4460261c9396`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, files. Outputs/bindings: (none).
Calls/effect boundaries: files.append.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[5]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:52`; AST `3ae8c6333b78c322583b25cb40780c53f2e2735ac6c3169acdc71ff030658bb4`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, files, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[5].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:52`; AST `f235bc6859584e605cf98f8338b0c83ff6364f8d769668bd075415494217b7ca`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, files, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:52`; AST `8e5e669d36731b0055a9febed84e1a19202921052588503d89241b9fed5a2eb0`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, files. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[6]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:53`; AST `2b3b7f1dbb20d5aa22febf81f2f2ab548822b3d4b7325267b116998d65b76b67`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: selected.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7]::For

Source: `infra/agentinfra/roadmap_protocol.py:54`; AST `4e0ff46237c82f54c088ee1f76d1002aec2dda8cb2b1ed88e24cff236858be0a`.

Rust module: `infra::agentinfra::roadmap_protocol`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, REQUIRED_SCHEMAS, b, choices, files, len, matches, name, require, selected, v2. Outputs/bindings: b, choices, matches, name, v2.
Calls/effect boundaries: Path, len, name.removesuffix, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered For evaluation at root.body[9].body[7]; no call, error or mutation may be omitted. Iteration: name in REQUIRED_SCHEMAS
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:55`; AST `de713f17cba7f0dc2fecd9d34383df639063faa0c6042f791c5a275fc667074b`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, b, files, name. Outputs/bindings: b, matches.
Calls/effect boundaries: Path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_protocol.py:55`; AST `97de5b350c2392365a0214144ecf2dda2b8d7fa72bbc998cfcaf39e75a6effe2`.

Rust module: `infra::agentinfra::roadmap_protocol`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: Path, b, files, name. Outputs/bindings: b.
Calls/effect boundaries: Path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered ListComp evaluation at root.body[9].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[0].value.generators[0].ifs[0].left.value::Call

Source: `infra/agentinfra/roadmap_protocol.py:55`; AST `ecb8687a3ecbe92262eb1b8279ca0ae3e4ac7c6a910af706ab6d6dbbc1e36fae`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, b. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[0].value.generators[0].ifs[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[1]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:56`; AST `8d87c09c92a56fc26e5772a3e1e1ed585a427461d1b55d52df87d6d54f497f82`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, matches. Outputs/bindings: b, v2.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_protocol.py:56`; AST `e956057ce7c2445899521ffa2747c3b721993008b86f1b78f3c9649b1df482ce`.

Rust module: `infra::agentinfra::roadmap_protocol`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, matches. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered ListComp evaluation at root.body[9].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[2]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:57`; AST `6def03a937ef9cd84151e1f7bdba3ce41354ba0af8d25e932685d7f09de41889`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches, v2. Outputs/bindings: choices.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[3]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:58`; AST `8ad2782693ea956064338135d3e99a694d25d67af425bd9fd0687e8007ef5aed`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: choices, len, name, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[3].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:58`; AST `9452668557aa149aaef35e8dfd5615ef59ae5d38283502f197474c2e0c011200`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: choices, len, name, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:58`; AST `408b669cc54a228b458aadd48949b75b4750553d0111703aa774d3b3f434a9d3`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: choices, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[4]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:59`; AST `c960e503f26ee8a972bd47e1b46ae9ff5342ae7e0a5222ee492fc93975c74e97`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: choices, name, selected. Outputs/bindings: (none).
Calls/effect boundaries: name.removesuffix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[7].body[4].targets[0].slice::Call

Source: `infra/agentinfra/roadmap_protocol.py:59`; AST `26d16876d0a90dbc424953d8bc053a6bec6e194d4f9a6af2b79a637efa5da1e9`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.removesuffix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[4].targets[0].slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[8]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:60`; AST `8f4577623ed99d56cecaf0296a32434adc34fc792800500b44e7c3e771577069`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: INTERFACE_VERSION, directory, executable, files, root, selected, total_bytes. Outputs/bindings: result.
Calls/effect boundaries: directory.relative_to, directory.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[8].value.values[3]::Call

Source: `infra/agentinfra/roadmap_protocol.py:61`; AST `1dfb0a0ea9a219328359251ae536e995b31633254c67f5fa76a5fa92f81ee751`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, root. Outputs/bindings: (none).
Calls/effect boundaries: directory.relative_to, directory.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[8].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[8].value.values[3].func.value::Call

Source: `infra/agentinfra/roadmap_protocol.py:61`; AST `41d4d409ea362a720c859929e8844950301050af0ee4f529bba387dc382a4346`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, root. Outputs/bindings: (none).
Calls/effect boundaries: directory.relative_to.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[8].value.values[3].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[9]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:65`; AST `986cd84aa9e2bba0446aa51664d697398b0c1ba7dccb7c0cdb7c664436a01570`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10]::For

Source: `infra/agentinfra/roadmap_protocol.py:66`; AST `7ecd5abb12a428fceb5111994b31955eccf2708cc23dfaa8f47547a96600ce55`.

Rust module: `infra::agentinfra::roadmap_protocol`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, confined_path, digest, document, name, read_json, require, result, root, selected, source. Outputs/bindings: binding, document, name, source.
Calls/effect boundaries: confined_path, digest, document.get, read_json, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered For evaluation at root.body[9].body[10]; no call, error or mutation may be omitted. Iteration: (name, source) in (('ThreadItem', 'ThreadItemsListResponse'), ('Turn', 'ThreadTurnsListResponse'))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:67`; AST `66a29cb611d0524241f4522aa27b06b23291a7962c9dfbb783ddadf7ef53a126`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: selected, source. Outputs/bindings: binding.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[1]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:68`; AST `894d58098114c171271393839bd2cfbc192a4b28d7315e757dff4740a3bcdf56`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, confined_path, read_json, root. Outputs/bindings: document.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[1].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:68`; AST `781ed7c69901254e631e8887a4f061f9d90e073a5136e5b4001231bf8ac0a69f`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:68`; AST `3cff76a4f8621efeac41053a9b6ce3e8ef8e5f85141b5ec2ef8724821ea6b41f`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[10].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[2]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:69`; AST `bc01b14ec4411bc63abb898b4e7bf23f0c9b924fdca1f04eea8cfc3c40e958a6`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: document, name, require. Outputs/bindings: (none).
Calls/effect boundaries: document.get, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[2].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:69`; AST `b74b68b86262f105a113915894a0485dbd2f2228b6171ccbd5c6dbe9d9884803`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document, name, require. Outputs/bindings: (none).
Calls/effect boundaries: document.get, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:69`; AST `dcc87607c06a1a9821a799b7692430e9637c0e89928277c0a730499112c814a1`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document. Outputs/bindings: (none).
Calls/effect boundaries: document.get.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[10].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[3]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:70`; AST `f55f56fc34752ccd7ad72e4759995199eeac8abb3242a06fcd69d80a712c14b2`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, digest, document, name, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[10].body[3].value.values[2]::Call

Source: `infra/agentinfra/roadmap_protocol.py:71`; AST `7425ae399cc7b5139467cb1354c4bf994a11684c0d365d6d0b344b0fa75178eb`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, document, name. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[10].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[11]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:72`; AST `ea550629d25e1f9e71896bf31374af5bfddb3e00134f1ff852e05146c14aecd2`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[11].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:72`; AST `9ddec37ebb871d950d3273f3c19aaf26231ea1c560172aa64604b6f8dc8f2faf`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[9].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::export_manifest::root.body[9].body[12]::Return

Source: `infra/agentinfra/roadmap_protocol.py:73`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Return evaluation at root.body[9].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_protocol.py:76`; AST `9424dde5e2905926db3ff81e5f709df5aa8cb946b60923fb5a4a9da5f33e1132`.

Rust module: `infra::agentinfra::roadmap_protocol`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: INTERFACE_VERSION, Path, b, bindings_current, confined_path, dict, digest, directory, k, manifest, native_executable, p, require, root, v. Outputs/bindings: b, directory, k, p, v.
Calls/effect boundaries: bindings_current, confined_path, digest, directory.rglob, manifest.get, manifest.items, native_executable, p.relative_to, p.relative_to(root).as_posix, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:77`; AST `2a3b623b5fd50e119fc8e5afbc6a1f2803738a1cb584b426b5142e0ba59725ef`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: INTERFACE_VERSION, digest, k, manifest, require, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, manifest.get, manifest.items, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:77`; AST `f5eba2a7ad1e5fcaf27d6c11ade837b3c9a2a5b7c55290aca24ae90e97435267`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: INTERFACE_VERSION, digest, k, manifest, require, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, manifest.get, manifest.items, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:77`; AST `9847c135795f371c1018e44dc409e24c6c57e84143bcf9745d9a51450eddc56a`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest. Outputs/bindings: (none).
Calls/effect boundaries: manifest.get.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:78`; AST `947e59235efd7aadc3b985b7bda5d84943a88ca98502029d7966519b052a82e5`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest. Outputs/bindings: (none).
Calls/effect boundaries: manifest.get.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:79`; AST `a8b44879ed7ceb82b0889f1549e31d30f4ec6cd8b9ebe65fee3f65b7db20b51d`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest. Outputs/bindings: (none).
Calls/effect boundaries: manifest.get.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap_protocol.py:79`; AST `fb8ef8d1449a0511e57b339348cbda986871a9eda8902049d8d4354fab9ad50c`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, manifest, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, manifest.items.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value.args[0].values[2].comparators[0].args[0]::DictComp

Source: `infra/agentinfra/roadmap_protocol.py:79`; AST `043f3910fb615c1d8bd3c330f659132fe1a1622c32d710f89c65adf37f8e734d`.

Rust module: `infra::agentinfra::roadmap_protocol`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, manifest, v. Outputs/bindings: k, v.
Calls/effect boundaries: manifest.items.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered DictComp evaluation at root.body[10].body[0].value.args[0].values[2].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[0].value.args[0].values[2].comparators[0].args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_protocol.py:79`; AST `49bdcd09300171360cae04b909aecbdf4244f0baaf90ad98ffcdc44b4a62d59f`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest. Outputs/bindings: (none).
Calls/effect boundaries: manifest.items.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[2].comparators[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[1]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:81`; AST `61fc484b9754651cf740d407149f04ab6a535f9a46ce0adc7573418038e96e58`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, manifest, native_executable, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, native_executable, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[1].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:81`; AST `8fa08441666bf4debed93a31dc3aee7d721e0a32cddcd41c0d91a234c29ce7f4`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, manifest, native_executable, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, native_executable, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_protocol.py:81`; AST `0c0169e13211f454ccdfd35a970ee34724818b99d569587ebd849bfc7e40d304`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_executable. Outputs/bindings: (none).
Calls/effect boundaries: native_executable.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_protocol.py:81`; AST `5ced5c112589ed7b036e6163a9dde8b0375654406f4b9da456e2b4b5396994d2`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, manifest, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[2]::Assign

Source: `infra/agentinfra/roadmap_protocol.py:83`; AST `987518d97f545eea2494d4aa281f8e33ded2887f05a526f80ca1c67acd357107`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, manifest, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[2].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:83`; AST `71009dbd52953f62b1d1e863f070da761f979d62846e4408b06a6b1373ba36e4`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, manifest, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3]::Expr

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `e9a66f739b769e0a3be9c17a16305481b5a24b4db40edb28af40ecce0dd4d05b`.

Rust module: `infra::agentinfra::roadmap_protocol`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, directory, manifest, p, require, root. Outputs/bindings: b, p.
Calls/effect boundaries: directory.rglob, p.relative_to, p.relative_to(root).as_posix, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3].value::Call

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `016af6d9ddf12364b698a3a35823512df873cb93a18198549a0bf5674dd55410`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, directory, manifest, p, require, root. Outputs/bindings: b, p.
Calls/effect boundaries: directory.rglob, p.relative_to, p.relative_to(root).as_posix, require.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `a522dcd472b1db76d28355cb475e826db2d71b25a41cfe25491bb7668fdd2811`.

Rust module: `infra::agentinfra::roadmap_protocol`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: directory, p, root. Outputs/bindings: p.
Calls/effect boundaries: directory.rglob, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered SetComp evaluation at root.body[10].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3].value.args[0].left.elt::Call

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.args[0].left.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3].value.args[0].left.elt.func.value::Call

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.args[0].left.elt.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3].value.args[0].left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `bca3675770cb44c2e84f36d65508f7d7564e1c68b073af88be953197f6169416`.

Rust module: `infra::agentinfra::roadmap_protocol`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rglob.
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.args[0].left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_protocol.py::module::assert_protocol::root.body[10].body[3].value.args[0].comparators[0]::SetComp

Source: `infra/agentinfra/roadmap_protocol.py:84`; AST `0a4bc9ad33808746bd4ad6e9a07faa084722fec6247728c5c905490bd958efb3`.

Rust module: `infra::agentinfra::roadmap_protocol`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, manifest. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security, shutil.

Invariants: Preserve ordered SetComp evaluation at root.body[10].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
