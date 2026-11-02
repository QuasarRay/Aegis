# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 38. Inventory digest: `bfb29e794f42d4201d202e67c15259aad737e4e250edd86066ce390dc23bd505`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/validate_roadmaps.py::module::root::Module

Source: `scripts/validate_roadmaps.py:1`; AST `363e82d7e6d5bda82f9786f4d31a7bc5d7983fb9c83b293864f5ec94d4ae7603`.

Rust module: `scripts::validate_roadmaps`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, ROOT, __file__, __name__, audit, audit_evidence, compile_roadmaps, dict, first, ident, json, len, packet, print, require, root, second, skills, str, sys, validate_package, validate_skills. Outputs/bindings: ROOT, audit, first, ident, second, skills.
Calls/effect boundaries: Path, Path(__file__).resolve, audit_evidence, compile_roadmaps, json.dumps, len, packet, print, require, str, sys.path.insert, validate_package, validate_skills.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[0]::Expr

Source: `scripts/validate_roadmaps.py:1`; AST `87938080bd27cdb4bf6a1d4e254cc651bd1ec5a3769c3d25e255eb19657f2cda`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[1]::ImportFrom

Source: `scripts/validate_roadmaps.py:2`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[2]::Import

Source: `scripts/validate_roadmaps.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[3]::Import

Source: `scripts/validate_roadmaps.py:4`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[4]::Assign

Source: `scripts/validate_roadmaps.py:6`; AST `7efba0850e8eeaef93e5c3de6b7d47927a3e4bde0e8161dfb3d03fc10717d3c2`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[4].value.value.value::Call

Source: `scripts/validate_roadmaps.py:6`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[4].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[4].value.value.value.func.value::Call

Source: `scripts/validate_roadmaps.py:6`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[4].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[5]::Expr

Source: `scripts/validate_roadmaps.py:7`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[5].value::Call

Source: `scripts/validate_roadmaps.py:7`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[5].value.args[1]::Call

Source: `scripts/validate_roadmaps.py:7`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[6]::ImportFrom

Source: `scripts/validate_roadmaps.py:8`; AST `df62ea87f9b1249feb13e71ded10d4084349dcaf9904ef6bb7b23da85d8ed1d5`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[7]::ImportFrom

Source: `scripts/validate_roadmaps.py:9`; AST `1d05a1783aa666f1d852e3d5496957b79c9ff52ee6f44e7965b3028fe9a7ec43`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[8]::ImportFrom

Source: `scripts/validate_roadmaps.py:10`; AST `74f4cf9cbead1dea5943fc42f9e208b2d9d76b1734bfbdc2430dd1c1436421d9`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9]::FunctionDef

Source: `scripts/validate_roadmaps.py:13`; AST `805652a1982db6bce192d6f447b275ec21be0e104b41cd1b56283bb1e408921e`.

Rust module: `scripts::validate_roadmaps`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, audit, audit_evidence, compile_roadmaps, dict, first, ident, len, packet, require, root, second, skills, validate_skills. Outputs/bindings: audit, first, ident, second, skills.
Calls/effect boundaries: audit_evidence, compile_roadmaps, len, packet, require, validate_skills.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[0]::Assign

Source: `scripts/validate_roadmaps.py:14`; AST `592e457d3eea6d161881b9d8001e86acd2e3bd325f502016913012b8aa6e6889`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: first.
Calls/effect boundaries: compile_roadmaps.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[0].value::Call

Source: `scripts/validate_roadmaps.py:14`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[1]::Assign

Source: `scripts/validate_roadmaps.py:15`; AST `c2fd3b0b6a34365836cc98c99fd106575ea99a1c2bf7dd4d40d0c23aef2fd69e`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: second.
Calls/effect boundaries: compile_roadmaps.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[1].value::Call

Source: `scripts/validate_roadmaps.py:15`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[2]::Expr

Source: `scripts/validate_roadmaps.py:16`; AST `457021597a4886e2ffeefed21d8fabbf5f361efb172995388e8d7d2b644a824a`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, require, second. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[2].value::Call

Source: `scripts/validate_roadmaps.py:16`; AST `0e18912ab12ada5dc326e3fd718c39d345f12062e02b6923227b86084cb787c3`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, require, second. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[3]::Assign

Source: `scripts/validate_roadmaps.py:17`; AST `1563a0cf81a23bc50f9a0711bd91e8cb184e7fbcdb2f43081f274c217b5199aa`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit_evidence, first, root. Outputs/bindings: audit.
Calls/effect boundaries: audit_evidence.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[3].value::Call

Source: `scripts/validate_roadmaps.py:17`; AST `916e7da0dce766c3bc42ac709ccf463884d3e91423e1cc164fdd4bb9664d9a79`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit_evidence, first, root. Outputs/bindings: (none).
Calls/effect boundaries: audit_evidence.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[4]::For

Source: `scripts/validate_roadmaps.py:18`; AST `88acff91c4587a8d19149d91b3eaeaa7b118ef53964911a0dba3ee100bf44961`.

Rust module: `scripts::validate_roadmaps`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: audit, first, ident, packet, require. Outputs/bindings: ident.
Calls/effect boundaries: packet, require.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered For evaluation at root.body[9].body[4]; no call, error or mutation may be omitted. Iteration: ident in first['order']
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[4].body[0]::Expr

Source: `scripts/validate_roadmaps.py:19`; AST `ee351abff2ff3b2e8cc59de87a3b8ae7816cbfc0ba59e65e8d1da694f2902181`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[4].body[0].value::Call

Source: `scripts/validate_roadmaps.py:19`; AST `eb9d041016b9066f4c2725ad6de97b5047f4396e88454043b112458aa7aecd18`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[4].body[1]::Expr

Source: `scripts/validate_roadmaps.py:20`; AST `5b311a49beeef8b911e73ab2fa2df015b7555e374f8dc781a09f0269c5c1d0e4`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit, first, ident, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[4].body[1].value::Call

Source: `scripts/validate_roadmaps.py:20`; AST `dec570813257b9f742525877f95f7ac65862402087abc818eac77608c6ed2e02`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit, first, ident, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[5]::Assign

Source: `scripts/validate_roadmaps.py:21`; AST `46d0d45ed2e79e2ab095864e23de90773e0f8547027365d7a6d707885122aca0`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, validate_skills. Outputs/bindings: skills.
Calls/effect boundaries: validate_skills.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[5].value::Call

Source: `scripts/validate_roadmaps.py:21`; AST `058a684a59952bf7321b2dca779c67fea9fccce702659f76c7c2ae7f32107527`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[6]::Return

Source: `scripts/validate_roadmaps.py:22`; AST `3689e637f8a2690f1c3614de42f27e411f1fbde2b842d774736f6d4a11b5208a`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, len, skills. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Return evaluation at root.body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[6].value.values[3]::Call

Source: `scripts/validate_roadmaps.py:23`; AST `b25ba9efcb69dd5c49c8aad19b2c181448ad2025c5d33a3713bdd9493f1f4590`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::validate_package::root.body[9].body[6].value.values[4]::Call

Source: `scripts/validate_roadmaps.py:23`; AST `3416d7616e0f58f407fb1f6850415753200ac52ae0280972dd01de13e6003b6f`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[10]::If

Source: `scripts/validate_roadmaps.py:27`; AST `44d87f821a9d8f66231240246f4d07228cafc86fc90577253f02a80e99ff007d`.

Rust module: `scripts::validate_roadmaps`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, __name__, json, print, validate_package. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print, validate_package.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered If evaluation at root.body[10]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[10].body[0]::Expr

Source: `scripts/validate_roadmaps.py:28`; AST `259a52ab489a00db8575f43967098907ab1450f19c7442f685a2abd781b8239c`.

Rust module: `scripts::validate_roadmaps`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, json, print, validate_package. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print, validate_package.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[10].body[0].value::Call

Source: `scripts/validate_roadmaps.py:28`; AST `5c82e322de6a34cf96f2740f32b82949f61f852e0ff8d50864f18bcebb95a969`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, json, print, validate_package. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print, validate_package.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[10].body[0].value.args[0]::Call

Source: `scripts/validate_roadmaps.py:28`; AST `14a1125d1e66f83a1184990f7a53bab78b76e6c2d643aaa386032c3a7535d94b`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, json, validate_package. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, validate_package.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/validate_roadmaps.py::module::root.body[10].body[0].value.args[0].args[0]::Call

Source: `scripts/validate_roadmaps.py:28`; AST `517b726739ca845e0ee1d31a87d4e9ea1791e1e0a1a8aa71f7b2ac3378ed17f7`.

Rust module: `scripts::validate_roadmaps`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, validate_package. Outputs/bindings: (none).
Calls/effect boundaries: validate_package.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_knowledge, agentinfra.roadmap_records, json, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
