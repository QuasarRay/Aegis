# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 75. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_knowledge.py::module::root::Module

Source: `infra/agentinfra/roadmap_knowledge.py:1`; AST `a173f1fab533531574e33592cf5fc569393d8087d5187dfe53ffe639bfd28899`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, bindings_current, confined_path, content, dict, digest, end, ids, int, item, len, lines, manifest, matches, max_bytes, path, read_json, require, root, s, set, skill, source_id, start, str, text, type. Outputs/bindings: content, ids, item, lines, manifest, matches, path, s, skill, text.
Calls/effect boundaries: '\n'.join, bindings_current, confined_path, confined_path(root, item['binding']['path'], must_exist=True).read_text, confined_path(root, item['binding']['path'], must_exist=True).read_text().splitlines, content.encode, digest, len, manifest.get, path.read_text, read_json, require, set, skill.get, text.count, text.encode, text.startswith, type.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:1`; AST `847db5b9dfcbec08ef7c97105d3a079a2020745688d438f330aae22f04fe9f61`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_knowledge.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_knowledge.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_knowledge.py:6`; AST `bc40cff7f4721d6e94a9b7a934f453365503e4faa00b75989946ce9e1e0bd8d4`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_knowledge.py:7`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_knowledge.py:10`; AST `737fda93d92c7865d1c99e1bd7b3b4c62dfc62ee44dffa7de0f7a90ab40acd8f`.

Rust module: `infra::agentinfra::roadmap_knowledge`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bindings_current, confined_path, content, dict, digest, end, int, item, len, lines, manifest, matches, max_bytes, read_json, require, root, s, source_id, start, str, type. Outputs/bindings: content, item, lines, manifest, matches, s.
Calls/effect boundaries: '\n'.join, bindings_current, confined_path, confined_path(root, item['binding']['path'], must_exist=True).read_text, confined_path(root, item['binding']['path'], must_exist=True).read_text().splitlines, content.encode, digest, len, read_json, require, type.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:11`; AST `e8f9dfe526bf15df5385ad8fb868b742dc65f26b4db8a9a4d9d203e2c9fe3acc`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: manifest.
Calls/effect boundaries: read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:11`; AST `3f9e47b7e604104ba976819f8e585ffc77e99447c8338baa2b0f3c2f0825a12e`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[1]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:12`; AST `f0de202d076bf2d3bf9362b4a85dabc08f2e7ea647c21908e56fa1111d0a5f3e`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: manifest, s, source_id. Outputs/bindings: matches, s.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_knowledge.py:12`; AST `78e4190687237a1d258a2d7d49f11f36f91b1984c56e54a7c924470709e76d41`.

Rust module: `infra::agentinfra::roadmap_knowledge`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: manifest, s, source_id. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ListComp evaluation at root.body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[2]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:13`; AST `cb736a36f83b8a7368d2f170102626f5cded78eedb60b198dae64b88478a359d`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:13`; AST `0835275c3861001c16d19c0fb0455a4040c1b46e90da300620722c85d323efbd`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:13`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[3]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:14`; AST `3d8c7238bbbed82e3c442528e740b179015c9b53358c005ace58e1d8dd8ec361`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches. Outputs/bindings: item.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[4]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:15`; AST `f16f33800a0eb3c53bf642bb70050f4b7336282f22432a2839ff290b79d47891`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:15`; AST `a1fd08867c140630d48afd7c942ac5c75d449205b198081953b01be894e73f16`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[5]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:16`; AST `a66945e072844e66d65c475fbc4aa99b0f8ac8c9767b586526319f6f66ac9998`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, item, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[5].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:16`; AST `f39959d965956596bbed8c64d0b2dfa8d75cdf830e5dcdd183d8d441dc58cee0`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, item, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:16`; AST `99dd672390d447db630981e4f5fe460ca6f3cda2e7936e96717018740678e4ef`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, item, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[6]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:17`; AST `6b737dff0dc419a9238db6a8d8adeb517b9cfb7dae8a7e8a4b05fd1cd82c184c`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: end, int, require, start, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[6].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:17`; AST `31791b284538eb10bda859d6d57cdfa37ee47cfc638e4b0ee8695a1cb0d649aa`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, int, require, start, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:17`; AST `54f13f957d758be41c49f1e01a0455451f268fa4e5bfb32280bd7d97028edf09`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: start, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[6].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:17`; AST `d4c5e4852327d2032fddd88fe18d0ab350cd188f39426a8c6e82a1ed171c66a3`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[7]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:18`; AST `b1ee84e1a5e986fcfa7af7df6191c5c467ec6c948ab68ccad22bd5feb2f31253`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, item, root. Outputs/bindings: lines.
Calls/effect boundaries: confined_path, confined_path(root, item['binding']['path'], must_exist=True).read_text, confined_path(root, item['binding']['path'], must_exist=True).read_text().splitlines.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[7].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:18`; AST `29b684ba26008344540341bf02f3c1324d1bae871caf9e9bc8c31e56b8ad559c`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, item, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, item['binding']['path'], must_exist=True).read_text, confined_path(root, item['binding']['path'], must_exist=True).read_text().splitlines.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[7].value.func.value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:18`; AST `a92f55e94020dc52be4a680047e6beb5086391515810b15892485e7f55f5b34c`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, item, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, item['binding']['path'], must_exist=True).read_text.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[7].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[7].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:18`; AST `be4a42d73472a579380e5129541c0b080ccfa7f80dbdfb619d0bf9c21cbf192b`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, item, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[7].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[8]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:19`; AST `6f80b4e89f494f5916449388705478673db4c817ee70d9e0a3b21a3461e7e33d`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: end, len, lines, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[8].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:19`; AST `4e18731f5a98ac0fd3145c4f6f880dec4fc6bb8248a455e5415ad871ec327a01`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, len, lines, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[8].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:19`; AST `07afbb7a385f382c1b40fcda6b6f7e9c91706969b1e8ab06f90f28b01f56b98a`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, lines. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[8].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[9]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:20`; AST `223034be312d40fb660af2d1922680cc45b7c62dd0666de545bf8a6780ebc00f`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: end, lines, start. Outputs/bindings: content.
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[9].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:20`; AST `a1344c3e0f3cf07acf05b1e051427850cd3087c56458c518e7bd469e42dac7fd`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, lines, start. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[10]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:21`; AST `dce96e60d318dd4e50c397d71a2877d6580ef96477787ef697c3622ea3077bef`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: content, len, max_bytes, require. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[10].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:21`; AST `4b34b0e5d75c650dc6f1208cd4a6e4a8720cd6cc888f9472df2f5379f0f6c411`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, len, max_bytes, require. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[10].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:21`; AST `87009a06c42c936e419415306577bd7ff5f5cce2278545822fac3817e5ddaf30`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, len. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[10].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[10].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:21`; AST `afb1628361c96c3ef5d11385774759e83fdc9a907c70bbd3cbb4a6a834ad4563`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content. Outputs/bindings: (none).
Calls/effect boundaries: content.encode.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[10].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[11]::Return

Source: `infra/agentinfra/roadmap_knowledge.py:22`; AST `ca1b8abe1a5cbb0a681c34fb137f77b357fe3be9ef0b8e4f3369cb0eaffe224f`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: content, digest, end, item, source_id, start. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, digest.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[5].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[11].value.values[5]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:23`; AST `a99a981fa0d440ed94a13f0d98bb84600a5809f81ff1617e03c57333c5ac6cde`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, digest. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, digest.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[11].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::retrieve::root.body[5].body[11].value.values[5].args[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:23`; AST `afb1628361c96c3ef5d11385774759e83fdc9a907c70bbd3cbb4a6a834ad4563`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content. Outputs/bindings: (none).
Calls/effect boundaries: content.encode.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[11].value.values[5].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_knowledge.py:27`; AST `c62791249a547466bf573a0b09fdf20ff56583b2026b532792d355d8b839dcf8`.

Rust module: `infra::agentinfra::roadmap_knowledge`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bindings_current, confined_path, dict, ids, len, manifest, path, read_json, require, root, s, set, skill, text. Outputs/bindings: ids, manifest, path, s, skill, text.
Calls/effect boundaries: bindings_current, confined_path, len, manifest.get, path.read_text, read_json, require, set, skill.get, text.count, text.encode, text.startswith.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:28`; AST `9233fbb67db7263300367580492020ae80dd3ebe5c9603c0ff1439c3f7e5c9a5`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: manifest.
Calls/effect boundaries: read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:28`; AST `a6ee9507e187dfde727ff14beb13224f94b3acc513298d67603408c2869fc805`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[1]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:29`; AST `ca257927fa7c04ca104ae310ed29178d7c9af7a64cc2404ed5e7a7076a453801`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: manifest, require. Outputs/bindings: (none).
Calls/effect boundaries: manifest.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:29`; AST `fe69d848db07dea389f8aab857b272b790a70b98dbbaf6455dff9a64d5ae018c`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest, require. Outputs/bindings: (none).
Calls/effect boundaries: manifest.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:29`; AST `9847c135795f371c1018e44dc409e24c6c57e84143bcf9745d9a51450eddc56a`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: manifest. Outputs/bindings: (none).
Calls/effect boundaries: manifest.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[2]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:30`; AST `999d474a1c59486f408cadbea6bb0354eafe9bbda3c09bbe03c727bdc451132d`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: manifest, s. Outputs/bindings: ids, s.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_knowledge.py:30`; AST `cdc3bf7f65da7d501dbff5d94d6eeb1900934ffb8bfa5fac7ef2d60864ce3705`.

Rust module: `infra::agentinfra::roadmap_knowledge`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: manifest, s. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ListComp evaluation at root.body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[3]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:31`; AST `1162daeb47bffe96dfea7473e650ce9b73d03932e56d9bcb627e4692215543c5`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[3].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:31`; AST `ca23023485592c74a03680425cc2c0e40437db1d0d089b6a73c0a19561f1649b`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:31`; AST `e9ff8c6d4cd447580e3ae476d39cdd538e64139104de929c715ef5318d853424`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[3].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:31`; AST `392a9c6c899c1b887c4cb41a948a33de0352ff7c7be2a32c7a4d965ee6b3a8a2`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[3].value.args[0].values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:31`; AST `b5d0e953c49c3b05c4f5acc7b5c0af435cfb16d965600b49af73f1b9fe8b980e`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4]::For

Source: `infra/agentinfra/roadmap_knowledge.py:32`; AST `e95b401d091d7c58d235710ee2c4b5c32baa2478b091191768748142c887a105`.

Rust module: `infra::agentinfra::roadmap_knowledge`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: bindings_current, confined_path, len, manifest, path, require, root, skill, text. Outputs/bindings: path, skill, text.
Calls/effect boundaries: bindings_current, confined_path, len, path.read_text, require, skill.get, text.count, text.encode, text.startswith.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered For evaluation at root.body[6].body[4]; no call, error or mutation may be omitted. Iteration: skill in manifest['skills']
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:33`; AST `c55da4343c0cede75c3c2f3a972c146124d8e998b4bbf1419879fcdebd1422b9`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, require, root, skill. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:33`; AST `db592be78ea7d63a91d121287933910be3a324bdbd1120d8ed80484b42be395c`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, require, root, skill. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:33`; AST `c072c781310582872eeab427c215af7d4a03c3754e4fd6cc6c86042c0df3b97a`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, skill. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:34`; AST `42d283699a1099b58167f29fec03f714f21bae3f766e94ea67ddc6edc6b1c6c6`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root, skill. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:34`; AST `8ed79c15dd5d68f404dfacebf5b806ec9622056e8fba62306c0b52caf614bb1a`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, skill. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[2]::Assign

Source: `infra/agentinfra/roadmap_knowledge.py:35`; AST `741e0feb8dbbf948203e8ea783ab0e1a9b765cc1e13415b9fb6f19f22f8afc78`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: text.
Calls/effect boundaries: path.read_text.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:35`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:36`; AST `1b39ec2f37c65c7ddd4de28bc93b9ce887878b4e749c8876ab14241aa903e195`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, skill, text. Outputs/bindings: (none).
Calls/effect boundaries: require, text.count, text.startswith.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:36`; AST `3797050ea087402b41f56a180b2d451e7fe996c6715d778d9c24905463065b94`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, skill, text. Outputs/bindings: (none).
Calls/effect boundaries: require, text.count, text.startswith.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[3].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:36`; AST `350e4a9768d0745e0a78ddf417108c2a9a655035224f14a91f078e3a7f131d03`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.startswith.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[3].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[3].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:36`; AST `acfb9c3f30737abd267ad83328da7d617a0df2b41efae33a84c517102e9509e1`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.count.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[3].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[4]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:38`; AST `2dbbacbcdb89bd37a6d4d0de045f12dc3f91c7d1ddf07bd0757e875f94f68341`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, skill. Outputs/bindings: (none).
Calls/effect boundaries: require, skill.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:38`; AST `231f74f45428263db35d2d655968cbcf4d829b8b2880ec51847d1f0c3558ecec`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, skill. Outputs/bindings: (none).
Calls/effect boundaries: require, skill.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[4].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:38`; AST `620fbff37041789236f35b2687701c5592e0c77788dd42fe71b57aa78fecd849`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: skill. Outputs/bindings: (none).
Calls/effect boundaries: skill.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[4].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[4].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:38`; AST `7862c36a5d503d5f368609aa86f6d3c15031796fe6cdbbb2cdffa98ac2c26836`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: skill. Outputs/bindings: (none).
Calls/effect boundaries: skill.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[5]::Expr

Source: `infra/agentinfra/roadmap_knowledge.py:39`; AST `1c09bc04f9498feb02dccaea555ade6580cd19df7ef89e8322ef8af055f8ce96`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, text. Outputs/bindings: (none).
Calls/effect boundaries: len, require, text.encode.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[5].value::Call

Source: `infra/agentinfra/roadmap_knowledge.py:39`; AST `97e32563e75275bda290d34321031133c3cafa7caf213617adcb2a37af3d1cf5`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, text. Outputs/bindings: (none).
Calls/effect boundaries: len, require, text.encode.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_knowledge.py:39`; AST `80addfdec0c38cd7341886bb1209ec18f446f05b1002e3bd0df467b6fcd56902`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, text. Outputs/bindings: (none).
Calls/effect boundaries: len, text.encode.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[4].body[5].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:39`; AST `7b01d8402eaa68fa08a88ea0fe995d452426cfe6dabb2459ddbcf08758697095`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.encode.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[5].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[5]::Return

Source: `infra/agentinfra/roadmap_knowledge.py:40`; AST `fb3d45c2a46656ed70e2b4c4dc87c52209f5eaf1a293ae863bd65c65f02ff5dd`.

Rust module: `infra::agentinfra::roadmap_knowledge`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_knowledge.py::module::validate_skills::root.body[6].body[5].value.values[1]::Call

Source: `infra/agentinfra/roadmap_knowledge.py:40`; AST `e9ff8c6d4cd447580e3ae476d39cdd538e64139104de929c715ef5318d853424`.

Rust module: `infra::agentinfra::roadmap_knowledge`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
