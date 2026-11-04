# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 144. Inventory digest: `f9dff9527f32a70023d9369b3709d006620a30ada801509867a5289b46e6259d`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_persistence.py::module::root::Module

Source: `infra/agentinfra/roadmap_persistence.py:1`; AST `3d0ac54417f914811e8e2d088c672ae75e317c3ab786931436af144326eeed95`.

Rust module: `infra::agentinfra::roadmap_persistence`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: POLICY_PATH, PRESERVES, Path, STRATEGIES, a, all, alternatives, ancestor, attempts, binding, bindings_current, by_id, confined_path, dict, digest, evidence, failed, field, file_binding, fingerprint, frozenset, ident, inherited, inputs, isinstance, k, len, list, old, packet, pending, plan, policy, policy_binding, prior, read_execution_policy, read_json, recovery_packet, require, root, selected, set, sorted, str, tuple, work_id. Outputs/bindings: POLICY_PATH, PRESERVES, STRATEGIES, a, alternatives, ancestor, by_id, evidence, failed, field, fingerprint, ident, k, old, packet, pending, plan, policy, selected.
Calls/effect boundaries: a.get, a['reason'].strip, all, bindings_current, by_id[ident].get, confined_path, digest, file_binding, frozenset, isinstance, len, list, pending.append, pending.pop, plan.get, plan[k].strip, policy.get, policy_binding, read_execution_policy, read_json, recovery_packet, require, selected.add, set, sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:1`; AST `2c636b22af175254232302c7d8bd8a62fefaf11616362008d37ddcdc4eb86e08`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_persistence.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_persistence.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_persistence.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_persistence.py:8`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_persistence.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_persistence.py:10`; AST `94f2ef7cfe57c7bfab987ff333d99818aa195b2b2e4f09c3d8608a99d87b2cad`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_persistence.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_persistence.py:11`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_persistence.py::module::root.body[5]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:14`; AST `42aad19bac45f5f5fade9dd23674ff7dc41df268c83e33749554b07a5851ba5e`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: POLICY_PATH.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::root.body[6]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:15`; AST `946c69991a0b64667f0e46a139317e3977b01738e11d4c829f56f0741fdc94ea`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: frozenset. Outputs/bindings: STRATEGIES.
Calls/effect boundaries: frozenset.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::root.body[6].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:15`; AST `a054e6d429b82c37213c63f3feded51ed51a1651fdf9ebf95aa6034f1cd154b7`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: frozenset. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::root.body[7]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:18`; AST `071d402a4f496c62e230b5431a237007de859feb83ba3fc52a22f17867d0f8f8`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: PRESERVES.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8]::FunctionDef

Source: `infra/agentinfra/roadmap_persistence.py:22`; AST `fae76b7465454a787baa861d571df4cd9346880922d397dfd2c6dc708f006d6e`.

Rust module: `infra::agentinfra::roadmap_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: POLICY_PATH, PRESERVES, Path, STRATEGIES, all, confined_path, dict, field, policy, read_json, require, root, sorted. Outputs/bindings: field, policy.
Calls/effect boundaries: all, confined_path, policy.get, read_json, require, sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:23`; AST `8b9ca89c1deb4e89c1679c54b926784c69baf9e5ad496adac358050094599296`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, confined_path, read_json, root. Outputs/bindings: policy.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:23`; AST `d081ebf732a5076ea80080077ee05eed0cc3e1dbe0afdab57a3ff72456cae974`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, confined_path, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:23`; AST `5bdd9b5c01bd125a424c1f9d0d39aae66e9ab63f6ce4889586c0ed8d993ed01e`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[1]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:24`; AST `abf540e35377e4b31588fe1264adc7e2823b6fb76aedcfbae127928951b40590`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[1].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:24`; AST `8ab36fd43318f2c10d338ef4b00a813b47bb24b2ab7f2809ca46224cf8a5bbb7`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:24`; AST `4f4917a694d078dcde9a0b2b3f36334ce31176634b9e12cecc4a86db64cf7e07`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:24`; AST `40ccaf1a59fed3f3c1117c7ee94437543b2908330e6f3847e2ca88fd7c19552d`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[1].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:25`; AST `a9236f7f42560d9e1f1c8ae665147d7e19772990293841680b10df29203aedf6`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[2]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:26`; AST `dacace49e55282debc85dc3a2971ccd6bb93edd7b713fe5395bccd1bb024ab62`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, field, policy, require. Outputs/bindings: field.
Calls/effect boundaries: all, policy.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[2].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:26`; AST `56dec430cbac3529cc061acecba4460ff2d9e4730ff319813e7ce91339167ca1`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, field, policy, require. Outputs/bindings: field.
Calls/effect boundaries: all, policy.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:26`; AST `ca54981b5a6cfe88f8bf43f393a3a717a254c6b6f75060e730815734fed411e6`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, field, policy. Outputs/bindings: field.
Calls/effect boundaries: all, policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[2].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_persistence.py:26`; AST `c7e79bf8ab35d3faef6f9f1a94334cc41285ea2951cedc1a90af172931e002c3`.

Rust module: `infra::agentinfra::roadmap_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: field, policy. Outputs/bindings: field.
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[2].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_persistence.py:26`; AST `aeb046fb2e74730daa88b3c212a15f8aec160ac826320a75345a8803abdb89a4`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:28`; AST `7bbf0d088318fd8f6b3dc306096d299f3e43eb1e5b6c285bbb33140014507af1`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PRESERVES, STRATEGIES, policy, require, sorted. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require, sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:28`; AST `e43c24e8e5bb8ecda0ee93b43e46955457876cbb0db2063c6b4a96e7766068ea`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PRESERVES, STRATEGIES, policy, require, sorted. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require, sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:28`; AST `9583b52bd6391907f66eae4ad26d0417f41ebb7826bb39ce62297946ea38076b`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:28`; AST `0a0daef762043e391ee66dcec29158d38e1766437eff5754901598990009f285`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STRATEGIES, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:29`; AST `87429c9f1b5b2c51a6956c5cc565672973f7349cfa90e1266e97044107edcdd7`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:29`; AST `4d64c4d5233028882d76c14862b0329b08b7d3065eea889f40ece35af53ca36f`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:30`; AST `81dedd4207fed56039ee1d03ec4ad77cbdfa2846192b89dc2c97fe42d88298d3`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[3].value.args[0].values[4].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:31`; AST `ae1ef5d881eaafa1e047b30f4e23ebec26edf4974d6e339a2c2f57f0f00f2ab0`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[4].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[4]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:33`; AST `d87453f12de3c4920ee0029eec2d474aaa06f33dd4e1a32cfc64a1078206a328`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[4].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:33`; AST `82f09fce7ee22e9dd7f75fd8fb77445ab522f012216b910c2eb447e79e35c08c`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[4].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:33`; AST `cf65f6ef51cc227bd3a33fc277cd23fc3bf4e4d687b28631f4b97088e1c554ce`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[4].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:34`; AST `070cf11dda8d337f8a7097f4c8f7808e3f1e12bffa2c104aa18762b60f80a093`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[4].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:35`; AST `54e576648361baf39270d843e93c99569b1b21553dbc34755ab79e870641f556`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[4].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:36`; AST `cccb9090c79f4f679892c20382f39dec59362727dc94ad2ca910d286e4edfacc`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::read_execution_policy::root.body[8].body[5]::Return

Source: `infra/agentinfra/roadmap_persistence.py:38`; AST `f38e8c7b49f49258700f63ece88446824ff7772f42414fe8c7662760c8476f35`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::policy_binding::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_persistence.py:41`; AST `e1afe8d662331984c3006ed053d54536201cbd683ff012337270b4bda54f5d6a`.

Rust module: `infra::agentinfra::roadmap_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: POLICY_PATH, Path, dict, file_binding, read_execution_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, read_execution_policy.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::policy_binding::root.body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:42`; AST `8fde9caeeab2c3d95f7b97b4971c20c06b88e43b14194d23a51ada165d498355`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_execution_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: read_execution_policy.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::policy_binding::root.body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:42`; AST `16f23314ea1291719c49ed66fa2e8838454531d4300ece2f608ebff5a5cab8aa`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_execution_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: read_execution_policy.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::policy_binding::root.body[9].body[1]::Return

Source: `infra/agentinfra/roadmap_persistence.py:43`; AST `5ca0b56f7e2e235e73f89fa879ba91d91acb1fad1649016c99f2dbc40b6ce7bb`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::policy_binding::root.body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:43`; AST `1a9ca2b5eb30c0a2bc5aa9be66def389cd27a25af016bbdf2c99077c8dd32a7f`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_policy_binding::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_persistence.py:46`; AST `c3bd83c37e4780be72ba7eaa29c0a6ea07a044502093e50f27231ddfb9838dcf`.

Rust module: `infra::agentinfra::roadmap_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, binding, bindings_current, dict, policy_binding, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, policy_binding, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_policy_binding::root.body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:47`; AST `06de6240e895c39d184dba87a592ec3e33345c6e2e14d0c4c7996a02846574b9`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, bindings_current, policy_binding, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, policy_binding, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_policy_binding::root.body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:47`; AST `f41cf441cb37342817dbe00252365e28e89b23e63f7a2cdf725c373bdc3789c0`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, policy_binding, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, policy_binding, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_policy_binding::root.body[10].body[0].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:47`; AST `0f6fb9081af5dda829cc40a8483970d2a917c4f597b6c56df382be7780e184c2`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: policy_binding.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_policy_binding::root.body[10].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_persistence.py:47`; AST `c257a7f2655cc69270fda2c99acf98c4ac7884fc49d5a5eefb6440b2a4ebcecb`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_persistence.py:51`; AST `e469c0c7a7334eb4fd77f1c169f779b0bba4377725bcd0db748327376953f00e`.

Rust module: `infra::agentinfra::roadmap_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: a, ancestor, attempts, by_id, dict, ident, inherited, len, list, pending, require, selected, set, str, tuple, work_id. Outputs/bindings: a, ancestor, by_id, ident, pending, selected.
Calls/effect boundaries: by_id[ident].get, len, list, pending.append, pending.pop, require, selected.add, set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[0]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:52`; AST `0e1789f689cbe3f11616f4d92d0dbd0f0d9b06f487085e78d10d058358c17353`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, attempts. Outputs/bindings: a, by_id.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[0].value::DictComp

Source: `infra/agentinfra/roadmap_persistence.py:52`; AST `61807b34bd0bb8a478c3acd5ac5e03504e3941f25e73e397bb2d316526dd59ac`.

Rust module: `infra::agentinfra::roadmap_persistence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: a, attempts. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[1]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:53`; AST `98d972591a9e86e697339bca0f6615843eb39518309a975651ef070f8c3732f5`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempts, by_id, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:53`; AST `5e3af312e5c10877ec1c2170e77407eb4c8c03c9d2de1d2c904cbe764855a0f4`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, by_id, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:53`; AST `fca7519555a1766ecc40eb735a14669b85381de9aec70a807c39a18392a1e9e2`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[1].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:53`; AST `d96ff57c85b1de5e02701b259745dec95870fd23f436944c4ef0110a889a4cad`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[2]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:54`; AST `20275c4b2c4c1f45e2ae4b06dca7abdf5da9524d355ea4b89f69e522f61e2577`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, attempts, inherited, set, work_id. Outputs/bindings: a, selected.
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[2].value.left::SetComp

Source: `infra/agentinfra/roadmap_persistence.py:54`; AST `69a3376b9db8c0c4d1cea06440985203e042337cf962cd7150f87396174db2c7`.

Rust module: `infra::agentinfra::roadmap_persistence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, attempts, work_id. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered SetComp evaluation at root.body[11].body[2].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[2].value.right::Call

Source: `infra/agentinfra/roadmap_persistence.py:54`; AST `15306928578a62f7e67a209e3b76d9e461f2586934556ba8cddcdedd2b63fdb1`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inherited, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[3]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:55`; AST `7990f26d0c3ac3e5ff243f6f29817986c68c08db2968416c4969e47aa3ddc83c`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, selected. Outputs/bindings: pending.
Calls/effect boundaries: list.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[3].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:55`; AST `0ce818bc2d969dfc1e42388bad21082a934be1abae8978b431f8a4bd8411fda8`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, selected. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4]::While

Source: `infra/agentinfra/roadmap_persistence.py:56`; AST `159d3d5e8b1a66f7d9ac2e0f0455c89a1bad0398edf4bb6e679a48a05307e9f7`.

Rust module: `infra::agentinfra::roadmap_persistence`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: ancestor, by_id, ident, pending, require, selected. Outputs/bindings: ancestor, ident.
Calls/effect boundaries: by_id[ident].get, pending.append, pending.pop, require, selected.add.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered While evaluation at root.body[11].body[4]; no call, error or mutation may be omitted. Condition: pending
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:57`; AST `cd29c37b04bb134dfe779600c3ed77c11c577cd4af8f6422efc7626707e31451`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending. Outputs/bindings: ident.
Calls/effect boundaries: pending.pop.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:57`; AST `b59b504ea575e0473ea0b5cc17902585c9dde56c94712f38bdafbec0ce738e98`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.pop.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[1]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:58`; AST `8c49cf7e12d3b1f052ec70307c3fa3f0a77cd03656fadab2ad5ba960b355c5c1`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:58`; AST `ffef15aeb3dbd554acfbf6659b08e67bd440bb74cd33b244d648fbd4fad6958d`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2]::For

Source: `infra/agentinfra/roadmap_persistence.py:59`; AST `0129a9053ae619ce45e0460dc9c89ddb08d9d941afd50cbddae1bb6fddaab00b`.

Rust module: `infra::agentinfra::roadmap_persistence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ancestor, by_id, ident, pending, selected. Outputs/bindings: ancestor.
Calls/effect boundaries: by_id[ident].get, pending.append, selected.add.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered For evaluation at root.body[11].body[4].body[2]; no call, error or mutation may be omitted. Iteration: ancestor in by_id[ident].get('inherited_attempt_ids', [])
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2].iter::Call

Source: `infra/agentinfra/roadmap_persistence.py:59`; AST `b2c30f811df6ec5631268ba55a53c847a07689d33e3a9a0764f8630811872cdc`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, ident. Outputs/bindings: (none).
Calls/effect boundaries: by_id[ident].get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_persistence.py:60`; AST `fc09a4bed97dc46c99ed744c30f971daaad81bf27be8a733459934d763e1f625`.

Rust module: `infra::agentinfra::roadmap_persistence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ancestor, pending, selected. Outputs/bindings: (none).
Calls/effect boundaries: pending.append, selected.add.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered If evaluation at root.body[11].body[4].body[2].body[0]; no call, error or mutation may be omitted. Condition: ancestor not in selected
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:61`; AST `2c682e2f8524ca6b5ce4f91409613a6255b5817ad8a7474ec2481c80e468d2e5`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestor, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:61`; AST `ec99ea1b1aaab3ab414875620660191a2bb130b1499c49b30a4d2fccca28a70c`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestor, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:62`; AST `c03f05ed75d424f2b2ec867fb7af802a7515d870db2922b6ace3c08ae2a42b3b`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestor, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[4].body[2].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:62`; AST `1f4ccbf08b1678df0c7c38f3a544222b1727ed365102028e05856bbca8efb3d9`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestor, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[2].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[5]::Return

Source: `infra/agentinfra/roadmap_persistence.py:63`; AST `35b1728dca98bbb26358ad795669e114e40f6b95db6dc424abe74fead3bec888`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, attempts, selected. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::retained_history::root.body[11].body[5].value::ListComp

Source: `infra/agentinfra/roadmap_persistence.py:63`; AST `939e9cf05c555f75c6cf48d4e74dcb563eeb6152adc9912918d54a322ef5794a`.

Rust module: `infra::agentinfra::roadmap_persistence`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, attempts, selected. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::recovery_packet::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_persistence.py:66`; AST `3118a35159fc8e14b8a364fd7dc81e9e77ba0017363c69721a6099b327effdcc`.

Rust module: `infra::agentinfra::roadmap_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: PRESERVES, STRATEGIES, dict, digest, failed, inputs, list, prior, sorted, str, work_id. Outputs/bindings: failed.
Calls/effect boundaries: digest, sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::recovery_packet::root.body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:67`; AST `9a3be7c58ff9affbc1b91dec21d5087e459facabd325fa060a86bebfa6928835`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior. Outputs/bindings: failed.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::recovery_packet::root.body[12].body[1]::Return

Source: `infra/agentinfra/roadmap_persistence.py:68`; AST `60eb8f007fce2dc27896ae4402dbac2de6290cc1da9fe7ec33148c87876c9893`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PRESERVES, STRATEGIES, digest, failed, inputs, prior, sorted, work_id. Outputs/bindings: (none).
Calls/effect boundaries: digest, sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::recovery_packet::root.body[12].body[1].value.values[6]::Call

Source: `infra/agentinfra/roadmap_persistence.py:71`; AST `d32e486e0f2dbc9dba46867d5a5bf8b4fac71765cb260ce2a84a7314bfab20ea`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, prior. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::recovery_packet::root.body[12].body[1].value.values[7]::Call

Source: `infra/agentinfra/roadmap_persistence.py:71`; AST `0a0daef762043e391ee66dcec29158d38e1766437eff5754901598990009f285`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STRATEGIES, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_persistence.py:76`; AST `893e0c1b09eef38076e66b96e1527b5f37be82323e8637792c8a8af9e2bffa47`.

Rust module: `infra::agentinfra::roadmap_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, STRATEGIES, a, all, alternatives, binding, bindings_current, confined_path, dict, digest, evidence, fingerprint, inputs, isinstance, k, len, list, old, packet, plan, prior, read_json, recovery_packet, require, root, str, work_id. Outputs/bindings: a, alternatives, evidence, fingerprint, k, old, packet, plan.
Calls/effect boundaries: a.get, a['reason'].strip, all, bindings_current, confined_path, digest, isinstance, len, plan.get, plan[k].strip, read_json, recovery_packet, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[0]::If

Source: `infra/agentinfra/roadmap_persistence.py:78`; AST `bc232ff1b9b2d4ab407609cb15dea06570e431ebe152f8d70663e5d6fded5ccf`.

Rust module: `infra::agentinfra::roadmap_persistence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered If evaluation at root.body[13].body[0]; no call, error or mutation may be omitted. Condition: not prior or prior[-1]['status'] == 'SUCCESS'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:79`; AST `50dffa408afce1dfd01be2354feb6339a27e170c53aca3455a4f86634bb2290d`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:79`; AST `c98c4a8541e53fa5f32a5af03fca4e69389c3d4e74817eff68e692165de52afa`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[0].body[1]::Return

Source: `infra/agentinfra/roadmap_persistence.py:80`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[13].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[1]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:81`; AST `7abe9209b2420316270babb41158ebe4d4d0e370e5b70446ddf344a825999666`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:81`; AST `7c33eb06aef26d061ddcc2e643a2c88149b0d2726c66ef6d68f89f3b42097f6a`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:82`; AST `f2ba981db1949d0317ddcb7cec13439f2533f9db2a19090fc33fc0a444f8d982`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, bindings_current, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:82`; AST `5ca9403dbb39a4869a1f7c05cec1b96901cdf5ea12e87aee0e9282fb0bb8d221`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_persistence.py:82`; AST `c257a7f2655cc69270fda2c99acf98c4ac7884fc49d5a5eefb6440b2a4ebcecb`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[3]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:83`; AST `f7b26644635e67c5af1056512de52d0890a904176e18c431269b52bc2d7c145c`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, confined_path, read_json, root. Outputs/bindings: plan.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:83`; AST `8620e8a50e28581dd0b93fa649bafb377c4e6af4ae92751fb8cb898df0a71ab9`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:83`; AST `e93e7f2e055f15c3c8a83d6679f6cba3cc79f2c763673a69522794ba24c465f4`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:84`; AST `5bd8023c8ee6dac461ad50e7be824ce39961763e16e4f39cad8c7f6848354820`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inputs, prior, recovery_packet, work_id. Outputs/bindings: packet.
Calls/effect boundaries: recovery_packet.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:84`; AST `1ce1b450447e60c485b6a1f61139052972530d019f449b5e3e7d283fd94c53d8`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inputs, prior, recovery_packet, work_id. Outputs/bindings: (none).
Calls/effect boundaries: recovery_packet.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[5]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:85`; AST `0fe133f462def001b271a4188628533b7f884a3617dd4a610259fc2ec73719dc`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, k, packet, plan, require. Outputs/bindings: k.
Calls/effect boundaries: all, plan.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:85`; AST `239c1684ed37b6cf3cd6975b553e0752709b4abc23eb1df1d446f5337f1c061f`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, k, packet, plan, require. Outputs/bindings: k.
Calls/effect boundaries: all, plan.get, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:85`; AST `68c9b507d76fb6abcc69cdc72151a85da41b013fdf6b3ec37ea872974fba0878`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, k, packet, plan. Outputs/bindings: k.
Calls/effect boundaries: all, plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[5].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_persistence.py:85`; AST `ce7be5c16fe8d9ff61af19083aec1deb4cd43036f17a15adf1dd962781c41a01`.

Rust module: `infra::agentinfra::roadmap_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: k, packet, plan. Outputs/bindings: k.
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[5].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[5].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_persistence.py:85`; AST `984dcb6f73b829e8423c038368828b7998dffe6d1c31252d217e485c68b02e30`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:88`; AST `4f3dccea23819db1e66e7db52acffd66a6827af89cefc6adaccc00cdf8def0d8`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: STRATEGIES, all, isinstance, k, plan, require, str. Outputs/bindings: k.
Calls/effect boundaries: all, isinstance, plan.get, plan[k].strip, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:88`; AST `4c11643968c815198cb7815765d51b94263376d4cb754ac780b9cb36f5959b78`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STRATEGIES, all, isinstance, k, plan, require, str. Outputs/bindings: k.
Calls/effect boundaries: all, isinstance, plan.get, plan[k].strip, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:88`; AST `49f3437d228b4c85fadbb9d2c4f5c04feb199fc363ae0fd459958ccbd5cda458`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_persistence.py:89`; AST `47d83ccd5cbd153d763db4a44d7e70ae8564c85742f492b0e51084f98fabb00b`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, isinstance, k, plan, str. Outputs/bindings: k.
Calls/effect boundaries: all, isinstance, plan.get, plan[k].strip.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_persistence.py:89`; AST `905b53abf7420db7ed7e1dbff9fc0eecc70fd80a42f24005ee2b12ad3bc153e2`.

Rust module: `infra::agentinfra::roadmap_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: isinstance, k, plan, str. Outputs/bindings: k.
Calls/effect boundaries: isinstance, plan.get, plan[k].strip.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[6].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value.args[0].values[1].args[0].elt.values[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:89`; AST `504ecbe9222fe03e7affc91f7769c5bbb9501eb38724f5d6716a58a16f64610e`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, k, plan, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].values[1].args[0].elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value.args[0].values[1].args[0].elt.values[0].args[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:89`; AST `984dcb6f73b829e8423c038368828b7998dffe6d1c31252d217e485c68b02e30`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].values[1].args[0].elt.values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[6].value.args[0].values[1].args[0].elt.values[1]::Call

Source: `infra/agentinfra/roadmap_persistence.py:89`; AST `883c17da3cafd092da9ab400b10cda8781436399e372c367cf6e34a967b2c55c`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, plan. Outputs/bindings: (none).
Calls/effect boundaries: plan[k].strip.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].values[1].args[0].elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[7]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:91`; AST `96a16bd3c07838fc9fd292814a4b2d1b5768ef421e4df528eb71a67420703c3f`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan. Outputs/bindings: alternatives.
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:91`; AST `9e847fb5045e580a8398d7c0ba10275e807e227953638401394518624d685c69`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:92`; AST `4fc89c5aeee70115cd08b4b8d3b87b69071a0046e0e2ae459f9eee6236988b55`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: STRATEGIES, a, all, alternatives, dict, isinstance, len, list, plan, require, str. Outputs/bindings: a.
Calls/effect boundaries: a.get, a['reason'].strip, all, isinstance, len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:92`; AST `425df0a2c98744e654765725d4298ee8c7ffec841e1792e5409342de8d1411b3`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STRATEGIES, a, all, alternatives, dict, isinstance, len, list, plan, require, str. Outputs/bindings: a.
Calls/effect boundaries: a.get, a['reason'].strip, all, isinstance, len, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:92`; AST `d8e3406e1eab6af0823df5f48eb45ca534ebbf38f1f29787761354559d126360`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: alternatives, isinstance, list. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:92`; AST `832188a8105afbf7bc53983e76fb5bc7470bfbe6e2f26ba43cc04f266611c501`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: alternatives, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_persistence.py:93`; AST `d699bbf6bd134a4a7ad26b5722a7b37a33127d05f2fe538249ed5e0c14b53783`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, alternatives, dict, isinstance. Outputs/bindings: a.
Calls/effect boundaries: all, isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_persistence.py:93`; AST `e850c66f2bd7e30c2a90d68d0410fb8fabe4385dfb87368074c8932b3ee04069`.

Rust module: `infra::agentinfra::roadmap_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, alternatives, dict, isinstance. Outputs/bindings: a.
Calls/effect boundaries: isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[8].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[2].args[0].elt::Call

Source: `infra/agentinfra/roadmap_persistence.py:93`; AST `1a406026d0e34dd4f0f37abc0af7babac88d8450a5c921429b49812e6cb0ac27`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[2].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:94`; AST `ffbd2c059ba96617ffde688b0820a588b73d2dd207a448f10cd0f7ef128ca72c`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, alternatives, len. Outputs/bindings: a.
Calls/effect boundaries: a.get, len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[3].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_persistence.py:94`; AST `f9c9f5c1d8cfa329f73102f5bc165ec5ef2d39aa78bab0f4a73b6f07eef88bec`.

Rust module: `infra::agentinfra::roadmap_persistence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, alternatives. Outputs/bindings: a.
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[8].value.args[0].values[3].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[3].left.args[0].elt::Call

Source: `infra/agentinfra/roadmap_persistence.py:94`; AST `1acc99d10d1e55bfd22d5699979d2c54aba9075913039a94e9fcb59d8bab596a`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[3].left.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[3].comparators[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:94`; AST `832188a8105afbf7bc53983e76fb5bc7470bfbe6e2f26ba43cc04f266611c501`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: alternatives, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[3].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[4]::Call

Source: `infra/agentinfra/roadmap_persistence.py:95`; AST `48dfb39eb579bf9c95e1ccdb7dd5facb743e6da67d934068f467e06d2b9de2cc`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STRATEGIES, a, all, alternatives, isinstance, str. Outputs/bindings: a.
Calls/effect boundaries: a.get, a['reason'].strip, all, isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[4].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_persistence.py:95`; AST `345f001220194075fee0322d4db8f2e643ac02a5982b24a7d04761aaf9f0da50`.

Rust module: `infra::agentinfra::roadmap_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: STRATEGIES, a, alternatives, isinstance, str. Outputs/bindings: a.
Calls/effect boundaries: a.get, a['reason'].strip, isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[8].value.args[0].values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[4].args[0].elt.values[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:95`; AST `1acc99d10d1e55bfd22d5699979d2c54aba9075913039a94e9fcb59d8bab596a`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[4].args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[4].args[0].elt.values[1]::Call

Source: `infra/agentinfra/roadmap_persistence.py:95`; AST `d7122726147cc1001bd8a4cb2b37b16615af69dd6be98f68ada9bbf0350f9c61`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: a.get, isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[4].args[0].elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[4].args[0].elt.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:95`; AST `922eb15b9f8e6b5cb67f02167c47d72cc5179413e9c5f89312234570591157f9`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[4].args[0].elt.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[4].args[0].elt.values[2]::Call

Source: `infra/agentinfra/roadmap_persistence.py:95`; AST `c6a680b788f94a844546167b3aa539b74c0c3d6ab00bb4db197b0ac3366f94f7`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a['reason'].strip.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[4].args[0].elt.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[8].value.args[0].values[5].comparators[0]::SetComp

Source: `infra/agentinfra/roadmap_persistence.py:96`; AST `6d12ae3f1e8f1eee42c5c1706f8516956dfdca90b80650dc62535d3e67f56030`.

Rust module: `infra::agentinfra::roadmap_persistence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, alternatives. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[8].value.args[0].values[5].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[9]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:98`; AST `63052a025468b811f9f2c80c44770bb69b58bf5433307c081749216ec09911c3`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan. Outputs/bindings: evidence.
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[9].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:98`; AST `3558cc5e677834fdf9eebac2202b2824b0c107eeec63e19417eafab4c7bac532`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[10]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:99`; AST `ad7b28a890f34b0a444494431503b4ee1587fdf3929ff975ad92d17553c69abb`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, evidence, isinstance, list, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, isinstance, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[10].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:99`; AST `9ce22f1c5cd02f149a46167bcbd105e7685c886e0795302c7bd0b838671a57b3`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, evidence, isinstance, list, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, isinstance, require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[10].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_persistence.py:99`; AST `aade29289304ac8b943de627d41e37448be316ddd61be44394c9d22223b2a42c`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: evidence, isinstance, list. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[10].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_persistence.py:99`; AST `9815c7fd11407069c27f9af43cd94083a778f1165afb0af145460a6ea8c91ddf`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, evidence, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[11]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:101`; AST `3a3d3b2a1fc7d29ae48dedb9422682f5cfdca3df5be7794e1804e3ecc05c9a91`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, k, plan. Outputs/bindings: fingerprint, k.
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[11].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:101`; AST `d4b3404bde79c76a8921502e4444596b1c65e0c24a83292504b419055c61e766`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, plan. Outputs/bindings: k.
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[11].value.args[0]::DictComp

Source: `infra/agentinfra/roadmap_persistence.py:101`; AST `1629cdf16f1fca2f4a85dbe644b7c0cddc48bfd3546ef210dbee1a2fbd01c4f6`.

Rust module: `infra::agentinfra::roadmap_persistence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, plan. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[12]::Assign

Source: `infra/agentinfra/roadmap_persistence.py:102`; AST `332f9a9ba6acbca9244f255dc2adf44c31abc7aa103562d6506ca3009cad0e0a`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, inputs, prior. Outputs/bindings: a, old.
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[12].value::ListComp

Source: `infra/agentinfra/roadmap_persistence.py:102`; AST `9e9ee88467f21f59f7f0d6bf1cbce909f6758c3031ba101afe9b9f4a804ca9e3`.

Rust module: `infra::agentinfra::roadmap_persistence`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[12].value.elt::Call

Source: `infra/agentinfra/roadmap_persistence.py:102`; AST `fa98c468e2810cdf0f29936880db98059b925e69c0f2b350a0366897db0c0c96`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[12].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[12].value.generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_persistence.py:102`; AST `78fcb06a1c27b47376a4e92470643363519f1c2d7e547fbf3a5d216c2d7c67dd`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[12].value.generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[13]::Expr

Source: `infra/agentinfra/roadmap_persistence.py:103`; AST `4eb6b96ccfa402ef2a756487ea5c90e9a3b44c7d46deaeb74e3d2692406e979b`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fingerprint, old, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[13].value::Call

Source: `infra/agentinfra/roadmap_persistence.py:103`; AST `32011c44d688393a8b3d5f223428538f0cc6b98bafd286c6d62ca57e63d5ba39`.

Rust module: `infra::agentinfra::roadmap_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fingerprint, old, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[13].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_persistence.py::module::validate_recovery::root.body[13].body[14]::Return

Source: `infra/agentinfra/roadmap_persistence.py:104`; AST `f5d73ec6b3fda27a658743558b10ee9c04de0434eddbe5b6bc3d40c310c8afd2`.

Rust module: `infra::agentinfra::roadmap_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, fingerprint, plan. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[13].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
