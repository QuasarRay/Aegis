# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 259. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_policy.py::module::root::Module

Source: `infra/agentinfra/roadmap_policy.py:1`; AST `0789dcc266b524923862200398fb314f09dcc446b733f47be86d02bf77f30af4`.

Rust module: `infra::agentinfra::roadmap_policy`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: DOMAIN_BACKENDS, SEMANTIC_FIELDS, acceptance, action, actual, all, all_satisfied, any, bool, budget, cgp_eligible, context, current, dict, digest, errors, expected, field, g, group, groups, int, k, len, limit, list, n, obligation, original, owners, p, params, project_states, reasons, requested, require, required, reserved, result, review, satisfied, semantic_digest, semantic_identity, set, source_ids, str, t, targets, translated, type, used, user_authorized, v. Outputs/bindings: COMPLETION, DOMAIN_BACKENDS, SEMANTIC_FIELDS, action, actual, budget, errors, expected, field, g, group, k, n, owners, p, params, reasons, review, semantic_digest, t, targets, v.
Calls/effect boundaries: actual.values, all, all_satisfied, any, bool, cgp_eligible, context.get, current.get, digest, errors.append, g.get, group.get, len, obligation.get, project_states.get, reasons.append, requested.get, require, result.get, review.get, semantic_identity, set, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:1`; AST `de35b90ed4186e2659059cec50a04ba649d58b7ddc210e6699dedbdd859f2b21`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_policy.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_policy.py:4`; AST `ba6b1d77193cb16eea6b719c54828bababa3d2f1452a499322e41a0f3da40238`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::root.body[3]::Assign

Source: `infra/agentinfra/roadmap_policy.py:7`; AST `17d6ea1b543177590debd6177b3951b1f61529f5b1531dccf7abe20c5385a9f1`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: COMPLETION.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::root.body[4]::Assign

Source: `infra/agentinfra/roadmap_policy.py:9`; AST `38e46e964d6fd1c46ec8850b7e70c956f664b64978886dc0b148e066ccb0e81b`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: DOMAIN_BACKENDS.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::root.body[5]::Assign

Source: `infra/agentinfra/roadmap_policy.py:10`; AST `b0f2426ec3a6f26f9043118acd5457884eac63bcd8a0b794253abcd738531457`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: SEMANTIC_FIELDS.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::may_reserve::root.body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:15`; AST `45f0b94f4f133fad88d68dd023efbfcab3211801b33133eadf8ae2f7eee7a2a7`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, bool, int, limit, n, requested, reserved, type, used. Outputs/bindings: n.
Calls/effect boundaries: all, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::may_reserve::root.body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:16`; AST `53af02df3ebc375cf827534d9fee40101c1841ab8ac780b461204bc759160f7e`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::may_reserve::root.body[6].body[1]::Return

Source: `infra/agentinfra/roadmap_policy.py:21`; AST `01385715fcba805c43c640dd510acafdd8bb670639e398974f5998697a986ba6`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, int, limit, n, requested, reserved, type, used. Outputs/bindings: n.
Calls/effect boundaries: all, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::may_reserve::root.body[6].body[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:21`; AST `e85192ab5028b0f53add5deb9e23024e7a5adc2ea10ea34863b166b0a136181a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, int, limit, n, requested, reserved, type, used. Outputs/bindings: n.
Calls/effect boundaries: all, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::may_reserve::root.body[6].body[1].value.values[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_policy.py:21`; AST `904fee2752c4830793e085f2dc8f40a5d39fdf9de08ec08627e24036483549e1`.

Rust module: `infra::agentinfra::roadmap_policy`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: int, limit, n, requested, reserved, type, used. Outputs/bindings: n.
Calls/effect boundaries: type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[6].body[1].value.values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::may_reserve::root.body[6].body[1].value.values[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_policy.py:21`; AST `85e7a2e312e7e7418036f9ca6445071411c4cd46d71ed50840cc84a83522834b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: n, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].value.values[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:26`; AST `2988843bed500fa1ff199642784d50d77720f1dac1090157500547853d775bd2`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, len, list, required, satisfied, set, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:27`; AST `5e77bde0bac611c477a42c8b30edad577148eb963ec7b92fec7824cf406153dc`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1]::Return

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `3986076e7fe1a82cc41f84eeea8d7d470d0504e80b25f550c446d550c9eadfde`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, len, required, satisfied, set. Outputs/bindings: (none).
Calls/effect boundaries: bool, len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `36a656515d1fed103d071b8a04f760b19474e347e094327b17a942de466ef0f5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, required. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1].value.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `90a1982def62dfa1037d7200016e32235f53757032252f8eebfed9b1603095e7`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, required. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1].value.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `907a664a05565bd0a99bb3c8260dfe4a3f766a27f3b867850f0b0f9b62d38f45`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, required, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1].value.values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `80501c0ec40fe29b73f36c3dfa25a3f820126585e1d283c476b217a199ece8cd`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: required, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1].value.values[2].left::Call

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `80501c0ec40fe29b73f36c3dfa25a3f820126585e1d283c476b217a199ece8cd`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: required, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::all_satisfied::root.body[7].body[1].value.values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:31`; AST `0e00b1920f5c89729bec3f6ff418954367a936e47ff7c01bc2b8f65058ffa458`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: satisfied, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::cgp_eligible::root.body[8]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:34`; AST `7fa651db1b6f49c1717f0e55a7a6f9a7fa56a1968c4144ad3f2da348919f3fa0`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, bool, dict, p, project_states, str. Outputs/bindings: p.
Calls/effect boundaries: all, project_states.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::cgp_eligible::root.body[8].body[0]::Return

Source: `infra/agentinfra/roadmap_policy.py:35`; AST `a1a193fd33429f292cdf8c30889c9e37b308b39ce84988ed6bbbc51172013cea`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, p, project_states. Outputs/bindings: p.
Calls/effect boundaries: all, project_states.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::cgp_eligible::root.body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:35`; AST `befa02e270f48831e448262cb8dc984c122f2975a89fb724f77459f2d107e288`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, p, project_states. Outputs/bindings: p.
Calls/effect boundaries: all, project_states.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::cgp_eligible::root.body[8].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_policy.py:35`; AST `de88a1e804db1d9502b94808c04024b97e4f9bd4e3d004e67f62194e19673677`.

Rust module: `infra::agentinfra::roadmap_policy`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: p, project_states. Outputs/bindings: p.
Calls/effect boundaries: project_states.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::cgp_eligible::root.body[8].body[0].value.args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_policy.py:35`; AST `bd451cdf673f5aea808e836a77304570dafcd0c2d04112d0cbfdc0d3e22f52be`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, project_states. Outputs/bindings: (none).
Calls/effect boundaries: project_states.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::semantic_identity::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:39`; AST `851cddf49d2069d5476b7b0111fd4cc584b3a3cf5ac8551d70cd8ca3655cbe77`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: SEMANTIC_FIELDS, bool, dict, original, set, translated. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::semantic_identity::root.body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:40`; AST `a5b926276832ab2987bf11d93f465e9d687cd6df11aba9c7cf048d27fc3310ef`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::semantic_identity::root.body[9].body[1]::Return

Source: `infra/agentinfra/roadmap_policy.py:44`; AST `43a6957baca68b589f39eed4cfcd65f37afa9818e070d69c6e3ee38debce3d82`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SEMANTIC_FIELDS, original, set, translated. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::semantic_identity::root.body[9].body[1].value.values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:44`; AST `d6bb022cabf342f9aa396882f8b632040cf0f6bfb92f4db3616b4319d0d4b986`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::semantic_identity::root.body[9].body[1].value.values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:44`; AST `1729d921535b7fb4611231f395fce93285c0616466985d69d2ab56290b1be64e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SEMANTIC_FIELDS, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::semantic_identity::root.body[9].body[1].value.values[0].comparators[1]::Call

Source: `infra/agentinfra/roadmap_policy.py:44`; AST `ec3ba9585e23477d9b231a3bb4d8484d1230811ce61bc1995e22fa820f170a1f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, translated. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[0].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:47`; AST `32e8827acd90b68b91e41fa128c4bf95ce907d6713a46456892322470596a775`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, dict, errors, g, group, groups, len, list, owners, set, source_ids, str, t, targets. Outputs/bindings: errors, g, group, owners, t, targets.
Calls/effect boundaries: any, errors.append, g.get, group.get, len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_policy.py:48`; AST `77905525b1838757d9a36638b843bc37695d709437ca6ae4dd4e7b7ff74949e3`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: errors.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[1]::If

Source: `infra/agentinfra/roadmap_policy.py:49`; AST `2fc3647297564ac6db8ae6c76c2d0a4a9b4c277f71ba3b5acacf507698604368`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, len, set, source_ids. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[10].body[1]; no call, error or mutation may be omitted. Condition: not source_ids or len(set(source_ids)) != len(source_ids)
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[1].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:49`; AST `11b569fd60398f3b44d0d750e27d222df922a30df9f5769845b6c77eeb80e86f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, set, source_ids. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[1].test.values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:49`; AST `50ab27901259ce959c93bdee1d36bd14006581ca3ccc3539d8e2fbba4fc38fb2`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, source_ids. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].test.values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[1].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:49`; AST `771a131f411b9c63527e0e62f3e12a550fcac700a97943d41b4ba1f34b97b392`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, source_ids. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:50`; AST `a709ff44344d4955494514166d2f8edb1609f1ef0447c0c5bdc3ceb2120cba45`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:50`; AST `af97a50c04b7c66cac12b237b87ee014f032fb64ae36a144daaecd3cbbf54d32`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[2]::Assign

Source: `infra/agentinfra/roadmap_policy.py:51`; AST `8b4af9e119a96445890586b754558610448ef1b46d4a7a56aa8fa95d21e08937`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: g, groups. Outputs/bindings: g, owners.
Calls/effect boundaries: g.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_policy.py:51`; AST `7fde58a0105be601f47653295f980da8c8759a2826e65a3032b11981b27d1076`.

Rust module: `infra::agentinfra::roadmap_policy`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: g, groups. Outputs/bindings: g.
Calls/effect boundaries: g.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered ListComp evaluation at root.body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[2].value.elt::Call

Source: `infra/agentinfra/roadmap_policy.py:51`; AST `4737dbc7c294acf5db10047463f35138b7a6a5b4e14cda55c658437d3ea4a59d`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: g. Outputs/bindings: (none).
Calls/effect boundaries: g.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].value.elt; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[3]::Assign

Source: `infra/agentinfra/roadmap_policy.py:52`; AST `d85c98174c314819166207631df8e80b0a7f8a121c2d342563888909449c28b0`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: g, groups. Outputs/bindings: g, targets.
Calls/effect boundaries: g.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[3].value::ListComp

Source: `infra/agentinfra/roadmap_policy.py:52`; AST `0d392ff39a9b96b3d5cd6d19f800cbff9fd77900d7509b6e8780193514af4edc`.

Rust module: `infra::agentinfra::roadmap_policy`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: g, groups. Outputs/bindings: g.
Calls/effect boundaries: g.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered ListComp evaluation at root.body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[3].value.elt::Call

Source: `infra/agentinfra/roadmap_policy.py:52`; AST `8314d07856dcb641b5a5c433c22a81a2175a0603489502f3a6d6213f0f20d60a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: g. Outputs/bindings: (none).
Calls/effect boundaries: g.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.elt; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4]::If

Source: `infra/agentinfra/roadmap_policy.py:53`; AST `30335b469df0910b0802da2df5c80a816aabba36b13ffa446aa869f5dbec50c4`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, len, owners, set, source_ids. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[10].body[4]; no call, error or mutation may be omitted. Condition: set(owners) != set(source_ids) or len(owners) != len(set(owners))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:53`; AST `11520a34d05a3292801addcf55f6c71da46ff4187d0caaee707acc1accee722c`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owners, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].test.values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:53`; AST `50ab27901259ce959c93bdee1d36bd14006581ca3ccc3539d8e2fbba4fc38fb2`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, source_ids. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].test.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:53`; AST `facc6ff0abf5cb9b406ba28eb527853a6394dc62a5c79f04f348fc9e4ea80dce`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, owners. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:53`; AST `125e88894c5a2236c1562555f482b53ec4dff831c61aa7c3d207d8be26fd3afa`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, owners, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].test.values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:53`; AST `11520a34d05a3292801addcf55f6c71da46ff4187d0caaee707acc1accee722c`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owners, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].test.values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:54`; AST `fb72a1e3ee1e54ad21db12fdd0489fc3939db60c73eb333e0c13ca8ba352f966`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:54`; AST `ead7b43e08edb3c5c1b80bc41b5547aac180aabcc507d6457f0c7894d182f71f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5]::If

Source: `infra/agentinfra/roadmap_policy.py:55`; AST `142c3f33bdeb7f3ad7f9bff357c8996ffa9153f21a599d7cac29f6cb69b65c87`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, errors, len, set, t, targets. Outputs/bindings: t.
Calls/effect boundaries: any, errors.append, len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[10].body[5]; no call, error or mutation may be omitted. Condition: any((not t for t in targets)) or len(targets) != len(set(targets))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].test.values[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:55`; AST `316ecf874f291cc220eccdb059174ce2e559e4427ece883059047f14e506baaa`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, t, targets. Outputs/bindings: t.
Calls/effect boundaries: any.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].test.values[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_policy.py:55`; AST `e49e526cf715061ee54f536e13c6062923f89f432c784677afd2e395ff434306`.

Rust module: `infra::agentinfra::roadmap_policy`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: t, targets. Outputs/bindings: t.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[5].test.values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:55`; AST `0436b6d3f80d06ba7aedbb02b88c30c920436e9e6357878875b8941620b03391`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, targets. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:55`; AST `5d5896b9df6b49761ecd63deaf26f91a6d998a4912eeead1a8e68202f0d2ea9b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, set, targets. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].test.values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:55`; AST `8942adca9fcadeb50e227a08d09d2198deda26d90437dff8bd0bda057c14c7d2`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, targets. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].test.values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:56`; AST `627ed5eec2b14a00d3a64a5c35193779871c5edcb529c1c8ac3ae77df0219dae`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:56`; AST `b3912d23f963e08f1da64f0258399da515d80959b1f0deb97ae53fc874039062`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6]::For

Source: `infra/agentinfra/roadmap_policy.py:57`; AST `4d6a45b8315bebc108a0a481f8fed05c28c7172ae041d48de26de1395cb17526`.

Rust module: `infra::agentinfra::roadmap_policy`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: errors, group, groups, set. Outputs/bindings: group.
Calls/effect boundaries: errors.append, group.get, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[10].body[6]; no call, error or mutation may be omitted. Iteration: group in groups
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[0]::If

Source: `infra/agentinfra/roadmap_policy.py:58`; AST `b0a3b329e7de65ccede2c5bae833a2ad829b71f6d8adbf8a8df7207419f50387`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, group. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[10].body[6].body[0]; no call, error or mutation may be omitted. Condition: not group.get('production_bindings') or not group.get('members')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:58`; AST `a82da6127e01c0addfdd7b7d9f092de2ff0035e418b24ad3752ef74bab31c939`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:58`; AST `24368a0c94c421a2d97630c7e2b735280075074c95a0f475dff6f003323d0790`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:59`; AST `7bca7b77c359760b71b031c51b82a2bd59054e0fdbe267c0df403c7c3af22e90`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, group. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:59`; AST `af26f072a0dd0b772ab03debf0ee0625a8d22d254748f1e02e79f64198391501`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, group. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[0].body[0].value.args[0].values[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:59`; AST `7b1ce8d3525b3878dd2ea15d76dd922e2a5dcf5f01f09a06a10adc3b57c87156`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[0].value.args[0].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1]::If

Source: `infra/agentinfra/roadmap_policy.py:60`; AST `f13b12b5cce3a59d02770c6a617e45c6ae0d1a3ffd9053b3f968be80aba85686`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, group, set. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, group.get, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[10].body[6].body[1]; no call, error or mutation may be omitted. Condition: set(group.get('required_relationships', [])) != set(group.get('implemented_relationships', []))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:60`; AST `4ed78db8df6ba4a5c060960508d58aabd1bdc9fd72fd0b575d975d2a7ea3eaad`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group, set. Outputs/bindings: (none).
Calls/effect boundaries: group.get, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].test.left.args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:60`; AST `aa9d7da004b6fc21a17415ef2bc81a54451d7f2169a20a4fdc7ff1dcd35fe994`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].test.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].test.comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:60`; AST `6506827c5e4b967054cb3248b31f1554866ced2a6f047bb1c148279cc066daeb`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group, set. Outputs/bindings: (none).
Calls/effect boundaries: group.get, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].test.comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:60`; AST `c7c9ea628889abd0dcd807660cce1b2146343fab0b1e114be606593d7e19b17c`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].test.comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:61`; AST `ed556f05e8c20cff1943dd402d2ab5f1f0beafd69921e8ac428e41ff81118afd`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, group. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:61`; AST `635ccaba0ff03dd610a6b573e8fdec2fa2c818224d4e52fff4bd570b381a235b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, group. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[6].body[1].body[0].value.args[0].values[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:61`; AST `7b1ce8d3525b3878dd2ea15d76dd922e2a5dcf5f01f09a06a10adc3b57c87156`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].body[0].value.args[0].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::correspondence_errors::root.body[10].body[7]::Return

Source: `infra/agentinfra/roadmap_policy.py:62`; AST `95659ec2764e1068e57db3e38e5a541ca59148b7402bfb0198a0ccf386555978`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:65`; AST `40b3561458c883fcc9e6563d4f5e02e57f5be389d91c66b2e2fe706f481526d5`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: DOMAIN_BACKENDS, actual, any, dict, digest, errors, expected, field, list, obligation, result, review, semantic_digest, semantic_identity, set, str, v. Outputs/bindings: actual, errors, expected, field, review, semantic_digest, v.
Calls/effect boundaries: actual.values, any, digest, errors.append, obligation.get, result.get, review.get, semantic_identity, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[0]::Assign

Source: `infra/agentinfra/roadmap_policy.py:66`; AST `77905525b1838757d9a36638b843bc37695d709437ca6ae4dd4e7b7ff74949e3`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: errors.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[1]::If

Source: `infra/agentinfra/roadmap_policy.py:67`; AST `558e3383d69fc8fc826f16083f449d8ac5fc4cc940ac507a003044f23f68d334`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: DOMAIN_BACKENDS, errors, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[1]; no call, error or mutation may be omitted. Condition: result.get('backend') not in DOMAIN_BACKENDS
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:67`; AST `8e87fa24dc187e5c5671cf90f3c2f02f132ff68e204dec3459bf108a96605a5d`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:68`; AST `8b0f72588fe178ae4c75ad700bf4bc89b711a33459e4140e865e978f86ad65ec`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:68`; AST `b2d0054bc6bea47adab54bf36c55e55fa18f7572c621aeee9b1a3f9c6c32e30b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[2]::If

Source: `infra/agentinfra/roadmap_policy.py:69`; AST `62e346862938b9c3458289bca1e891a560dd7a129fc2a4ebdb956e38862e7de1`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, obligation, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, obligation.get, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[2]; no call, error or mutation may be omitted. Condition: result.get('backend') != obligation.get('backend')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[2].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:69`; AST `8e87fa24dc187e5c5671cf90f3c2f02f132ff68e204dec3459bf108a96605a5d`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[2].test.comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:69`; AST `7614d3295bf703996d9ce200241d4c3f05990802a7977e7ad36d430a69c69148`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:70`; AST `ea0be98b805249f0aa936f7c5ec7051f1602880cb89d9f3173a99fee9b1d736b`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:70`; AST `e070b72d16911a332c922aaced844a637d42a4be68e01e09ec0b1247c498581e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[3]::If

Source: `infra/agentinfra/roadmap_policy.py:71`; AST `b2c606fad07857debdfd864c3f1b0eb2b7679b870b6182d8661c9753aafd895f`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[3]; no call, error or mutation may be omitted. Condition: result.get('status') != 'PROVED' or result.get('executed') is not True
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[3].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:71`; AST `27c18dc9e36361ad373e3a25c80feb42fab1b867ec7169a27d35468d95c69b08`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[3].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:71`; AST `8abf622c79396d7fc6c5ebfb8c543fcf17fc9225dbeed2ed55a57027d5d991e8`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:72`; AST `14128aed67e610258af3853c335ee17c1c3e1c7d6709e38920c66309f63b6a89`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:72`; AST `82366c8959f19e5a228196782f9c8403ed38f73d6127871864712f6191995503`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[4]::For

Source: `infra/agentinfra/roadmap_policy.py:73`; AST `5e52512481eb67c7dabec1b2f0f64ffe1ce7fadf1f8ee3fa704c430ee0b26955`.

Rust module: `infra::agentinfra::roadmap_policy`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: errors, field, result. Outputs/bindings: field.
Calls/effect boundaries: errors.append, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[11].body[4]; no call, error or mutation may be omitted. Iteration: field in ('timed_out', 'truncated', 'unsupported', 'unwind_incomplete', 'model_only')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[4].body[0]::If

Source: `infra/agentinfra/roadmap_policy.py:74`; AST `38184879c629ec15aba107d36744f0c404264ff1596aca40821d2db725341fd3`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, field, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted. Condition: result.get(field) is not False
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[4].body[0].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:74`; AST `9d473b3f36dfac6c9aaf2b6fabe3b438dcd768708fb7d8484e19c3445f685829`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[4].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:75`; AST `6755ced04f0c67952903a4c4e0c9c0fb7737601f5261175b1901fc81ee31c233`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:75`; AST `247492c283c5b0dacac18c9151de9cb907191a15ab3412d1eae4d71b1d043fb5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5]::For

Source: `infra/agentinfra/roadmap_policy.py:76`; AST `be54d5bc697813acd79cf6a35e108b3b82b2180002c02c1819bf37c4da1ff7a5`.

Rust module: `infra::agentinfra::roadmap_policy`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: errors, field, obligation, result. Outputs/bindings: field.
Calls/effect boundaries: errors.append, obligation.get, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[11].body[5]; no call, error or mutation may be omitted. Iteration: field in ('obligation_id', 'candidate', 'production_digest', 'contract_digest')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5].body[0]::If

Source: `infra/agentinfra/roadmap_policy.py:77`; AST `301aba8fc38780479115efc0df34919aaea508d356294fdac64a110fed8ddd02`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, field, obligation, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, obligation.get, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[0]; no call, error or mutation may be omitted. Condition: not obligation.get(field) or result.get(field) != obligation.get(field)
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:77`; AST `f50bf6d6d992cc68274a66423cb50c34c478f8fcd3322f61a2eb10072077f1bf`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5].body[0].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:77`; AST `9d473b3f36dfac6c9aaf2b6fabe3b438dcd768708fb7d8484e19c3445f685829`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5].body[0].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:77`; AST `f50bf6d6d992cc68274a66423cb50c34c478f8fcd3322f61a2eb10072077f1bf`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:78`; AST `15dd03d9782fc1dc488a79b455a1a7a17bac00d378477fccbb7bbf0d8171514e`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[5].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:78`; AST `412fa0b4debdc1bacad7ac6bfad2929c5ece8d3870edb1262e61218e493ae8ba`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6]::For

Source: `infra/agentinfra/roadmap_policy.py:79`; AST `76c1cadeb2ff0da3b72c0c64d8d6fb927d426b2081751a31be5a60fee900b103`.

Rust module: `infra::agentinfra::roadmap_policy`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: actual, any, errors, expected, field, obligation, result, set, v. Outputs/bindings: actual, expected, field, v.
Calls/effect boundaries: actual.values, any, errors.append, obligation.get, result.get, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[11].body[6]; no call, error or mutation may be omitted. Iteration: field in ('assertions', 'covers')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_policy.py:80`; AST `b3688f6f7eae4372c36bbc50cec87d346720eb1ab1c2bd2f7abd18ff16216b7e`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, obligation. Outputs/bindings: expected.
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:80`; AST `0b2e3ef695109064ecd2ca838434bd3da705612d2f2e595c8fa40de6ae753c1e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_policy.py:81`; AST `31d2781d4594eb83849d71cf719275890929a3edfbf3c6af98dd3dd29d2bb39b`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, result. Outputs/bindings: actual.
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_policy.py:81`; AST `7d6be7eb467a7857968bb9b67001cd0600492d9d3a3abcbe36d3a99d10098d95`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2]::If

Source: `infra/agentinfra/roadmap_policy.py:82`; AST `7c5f0f35f6bfc535f6415732ade21a508e2f42c075cbd30c6a5e43467def20a6`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: actual, any, errors, expected, field, set, v. Outputs/bindings: v.
Calls/effect boundaries: actual.values, any, errors.append, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[6].body[2]; no call, error or mutation may be omitted. Condition: not expected or set(expected) != set(actual) or any((v != 'SUCCESS' for v in actual.values()))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:82`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[2].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:82`; AST `f3b94940b2cabe37e2711e0ac31aa2ac688a4d9ad8dba19b27a18c4c0fee98ba`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[2].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].test.values[2]::Call

Source: `infra/agentinfra/roadmap_policy.py:82`; AST `dffc6870ac74973e138e5c4d03c117a7103202ec2e4a11629d8bd5390f7211ef`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, any, v. Outputs/bindings: v.
Calls/effect boundaries: actual.values, any.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[2].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].test.values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_policy.py:82`; AST `d250ef2ff57b8944c0b0a0a23d90edc04dc9061d936b72c7049c3040c38371a1`.

Rust module: `infra::agentinfra::roadmap_policy`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: actual, v. Outputs/bindings: v.
Calls/effect boundaries: actual.values.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[6].body[2].test.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].test.values[2].args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_policy.py:82`; AST `f476cc16845688a1ea8d32254a6c9ffce0cb76ce20e67198ccaef8ede2b01494`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual. Outputs/bindings: (none).
Calls/effect boundaries: actual.values.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[2].test.values[2].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:83`; AST `9327e08a67d17c7af258e7d70888478fc86bc175924843e09f3233be46064b1e`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[6].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:83`; AST `5c59feb195f7c32f0271e662c5bb8ad249753dc7dccf9f51b0cb76e8ac97e0b8`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[7]::For

Source: `infra/agentinfra/roadmap_policy.py:84`; AST `ee0f928226c4b32551f960371e7de164e5c1d5ba03c5f26b66e0d45f7be26497`.

Rust module: `infra::agentinfra::roadmap_policy`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: errors, field, obligation, result. Outputs/bindings: field.
Calls/effect boundaries: errors.append, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[11].body[7]; no call, error or mutation may be omitted. Iteration: field in ('assumptions', 'bounds', 'toolchain')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[7].body[0]::If

Source: `infra/agentinfra/roadmap_policy.py:85`; AST `3116f86bd873e90e7dd5a4b927fe8952309bf3c89da31fdcaa4f9980eb90a60c`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, field, obligation, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[7].body[0]; no call, error or mutation may be omitted. Condition: field not in obligation or result.get(field) != obligation[field]
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[7].body[0].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:85`; AST `9d473b3f36dfac6c9aaf2b6fabe3b438dcd768708fb7d8484e19c3445f685829`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[7].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:86`; AST `f32767dc3a0aa62678c965925cc25888cdf05695decfea374e3b8a533a1ec942`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[7].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:86`; AST `9baddceb34db60975501380c2772d19db201da771b3a23c96edb4136b882d99b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, field. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8]::If

Source: `infra/agentinfra/roadmap_policy.py:87`; AST `625346bc506eb1d58610da8431977c5ffeedbaf8faaa870a2b76d26fd6cea250`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: digest, errors, obligation, review, semantic_digest, semantic_identity. Outputs/bindings: review, semantic_digest.
Calls/effect boundaries: digest, errors.append, obligation.get, review.get, semantic_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[8]; no call, error or mutation may be omitted. Condition: obligation.get('origin') == 'original_test'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:87`; AST `389f03451aa54ff630419392009d91c79763937f8c4762d9374cf591e063173f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[0]::If

Source: `infra/agentinfra/roadmap_policy.py:88`; AST `b0c29c5a8c87605acc8cd26edf8ec1f0d344960750d10000fd5fb1be234e1a0d`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, obligation, semantic_identity. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, obligation.get, semantic_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[8].body[0]; no call, error or mutation may be omitted. Condition: not semantic_identity(obligation.get('original_semantics', {}), obligation.get('harness_semantics', {}))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[0].test.operand::Call

Source: `infra/agentinfra/roadmap_policy.py:88`; AST `cda3455a7ea3828f62b3c2253b898a08fd68322ba6ae879e698ad28d1d8add58`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, semantic_identity. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get, semantic_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[0].test.operand.args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:88`; AST `5dcc8eeaba910b5ce34279eb515b09acf7b44e636c843e7f345d713a63936ff1`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[0].test.operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[0].test.operand.args[1]::Call

Source: `infra/agentinfra/roadmap_policy.py:88`; AST `7806f9e310cf69421cfba1f8defd46973b63cf1e6c7fafb3669bcbcf78d3d0a7`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[0].test.operand.args[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:89`; AST `1171ee6ec709a3c9972ef7411170bbb437106005a11164f2f3cde49fefa5ee28`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:89`; AST `392f64eabcb60982f8149a507e850bb4babf1cad1474162d72e5fbd426470442`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[1]::Assign

Source: `infra/agentinfra/roadmap_policy.py:90`; AST `63992346f4d4bceca01af3ec60380a577ff34a2f45fdf91ad2f6293780d554fb`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation. Outputs/bindings: review.
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[1].value::Call

Source: `infra/agentinfra/roadmap_policy.py:90`; AST `0fd32e69414c733f304521e123529cfd86b55894ab1699d8b9c81a7edff18d9a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[2]::Assign

Source: `infra/agentinfra/roadmap_policy.py:91`; AST `4643ad087eb6be56e84011438fbec4959c3e258ce2f6a7d630d2aa88133be4cb`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, obligation. Outputs/bindings: semantic_digest.
Calls/effect boundaries: digest, obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[2].value::Call

Source: `infra/agentinfra/roadmap_policy.py:91`; AST `ebd7a148a4c9c9f8e6e5d54d40be3ee35a396488c916c5a352eb3de28d8cef8e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, obligation. Outputs/bindings: (none).
Calls/effect boundaries: digest, obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[2].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:91`; AST `aba9d50c2775791ad57da1b3066c389cffe77eff80033a4b9d6e2dcd189f2c82`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_policy.py:92`; AST `53a74e33ba9e0a936890baa7033142154296e65bb548f972d3b19be7e01087b5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[2].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_policy.py:93`; AST `464f729760442ef5efdd4610ddb94b0f5416c456ba18d63804f8c9727974a264`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3]::If

Source: `infra/agentinfra/roadmap_policy.py:94`; AST `95bc9a9a1dd09a9a8c29faba48d9dcd309a4ea167e0938916422e0bc67ab6877`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: errors, review, semantic_digest. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, review.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[8].body[3]; no call, error or mutation may be omitted. Condition: review.get('decision') != 'approve_translation' or not review.get('human') or (not review.get('provenance')) or (review.get('semantic_digest') != semantic_digest) or ('original_to_harness' not in review.get('scope', []))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:94`; AST `708d628bda40ad8854ca4f2417cd210a8846033fb36d473496fb9ee953426acc`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:94`; AST `643cde3ac90c7be87ffe8d3f54bcfa80cdfb33e28f6e2f43c7ebab7b443194b2`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].test.values[2].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:95`; AST `0623150d38d7f503e22d9091368d77c8b0872a46be13257c0f812506e6765b96`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].test.values[3].left::Call

Source: `infra/agentinfra/roadmap_policy.py:95`; AST `eb5eeba06ebde458efd7021267688c61676db3d6cce613687ef319a5fd7e4017`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].test.values[3].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].test.values[4].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:96`; AST `6b7c6e720ced04e0f8860a6efb904f0a128a273116343311ab61613661bafb61`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].test.values[4].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:97`; AST `65d52bcd5db344aa61289a83512799bb64d236d3fcb069c72177fe9a615509f1`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[8].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[8].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:97`; AST `40ff7f51b9904d453424c9d8e705528135f37730dcde1a17b6e3532372e8eefa`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::proof_errors::root.body[11].body[9]::Return

Source: `infra/agentinfra/roadmap_policy.py:98`; AST `95659ec2764e1068e57db3e38e5a541ca59148b7402bfb0198a0ccf386555978`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[11].body[9]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:101`; AST `bb4d11f3a142f8da39d4fd834010e12acce3b500f77ddbf7962048a5acb821de`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: action, all_satisfied, any, cgp_eligible, context, dict, digest, k, reasons, str. Outputs/bindings: k, reasons.
Calls/effect boundaries: all_satisfied, any, cgp_eligible, context.get, digest, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_policy.py:102`; AST `faf14f7c71c5d60e7d6c6ee9138825667c49802e0d07381a92e1f4e8076b2c65`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: reasons.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[1]::If

Source: `infra/agentinfra/roadmap_policy.py:103`; AST `ee51d8bd4d47a82867da7a66fd85acdd860d5b8acb28ff8d7a81c82f5fbc897d`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[1]; no call, error or mutation may be omitted. Condition: context.get('provider') != 'codex'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:103`; AST `77ac056041f86d12f4b5ec36098a511aaca50b220f004b3284407361ef800c72`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:104`; AST `373ecb1b9ec7572d74f11f179615ca8b4954d650c497dd82063fe7fe97148ae3`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:104`; AST `af4515be72bbb71d623164df601939a3cbdd6d695cc40059552809b0727d94c5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[2]::If

Source: `infra/agentinfra/roadmap_policy.py:105`; AST `bfcbdb59ef30835d4f02c4ef619e72bc9c9d596ec438b2636f39598d8feed569`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[2]; no call, error or mutation may be omitted. Condition: action not in {'read', 'plan', 'implement', 'verify', 'publish', 'complete', 'review_campaign', 'cgp'}
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:106`; AST `6209617043e54aa80f20d85b215031746c1ab6538fd02518d9d52db1a17737ff`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:106`; AST `3b46fcffacc685456153e6b81635dc043de546099bb1fc64e8c9de9ccf0e45ab`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3]::If

Source: `infra/agentinfra/roadmap_policy.py:107`; AST `3bdf722bb6caaed096a62150c7ca37af000d9218a1c4c408a18c82bddce93f45`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, any, context, k, reasons. Outputs/bindings: k.
Calls/effect boundaries: any, context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3]; no call, error or mutation may be omitted. Condition: action not in {'read', 'plan'}
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_policy.py:108`; AST `44f0d5630e5bf9773954658618dd5e7f6c7f73e2a44ba384d8956102c59f39bb`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted. Condition: context.get('mode') != 'execute'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[0].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:108`; AST `a23620c010a0886ebd629bd758913725ef0f0e9c6198e732156ed109c098fe6e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:109`; AST `dc34d13896c4efc961be76976b57a25dfef5df5da9d74f516b250fb7d30941e4`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:109`; AST `66834abf69c2ca6555f05036b4ef72ce357964eee70d45b5555cd53e0861742d`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[1]::If

Source: `infra/agentinfra/roadmap_policy.py:110`; AST `8a4ef9702dcacb91a21ecfd898eaef63dcbc80de52cff6544f1689fe39bc744b`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[1]; no call, error or mutation may be omitted. Condition: context.get('authorized') is not True
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:110`; AST `a495580ed1eb8d5b267e6dd20c0372395fd3960c4346cb759554b3d4e67e3e24`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:111`; AST `9ed3660c286485ab0d69db4e908f28fea6aaa0eaacc2e12f521897d51b54c986`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:111`; AST `1cab1d680ef9dd81f9746c1d1d7e002f5966fac2176262b1e6395d8d323e0f23`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[2]::If

Source: `infra/agentinfra/roadmap_policy.py:112`; AST `58160aafef29f01af0b78f6f6000bf9976b24a2aa4f62c1ffc96184ed311651b`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[2]; no call, error or mutation may be omitted. Condition: context.get('goal_status') != 'active'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[2].test.left::Call

Source: `infra/agentinfra/roadmap_policy.py:112`; AST `6a30137b3f61f5e40841d58d4c6fd1a8e8edad8ea1915455a244171bb1fa581a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:113`; AST `893aac4c6c929f8aff4504c9a8054eb1f21c8e9bc585b7d187c17d95948d9849`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:113`; AST `6638d62671388ac5217367de167fd4e367e61f69d1b55a487ff07798cac68059`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[3]::If

Source: `infra/agentinfra/roadmap_policy.py:114`; AST `21c2d0a9e6208d97c8cb96d95773a2085ab12507e9632baaeecbe5744f153bec`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, context, k, reasons. Outputs/bindings: k.
Calls/effect boundaries: any, context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[3]; no call, error or mutation may be omitted. Condition: any((context.get(k) != 'max' for k in ('requested_effort', 'accepted_effort', 'effective_effort')))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[3].test::Call

Source: `infra/agentinfra/roadmap_policy.py:114`; AST `c5678d7e4cb5ebf27ed25803e1a17a13f61ad01905d294dee2fd6ba5dd9cc3be`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, context, k. Outputs/bindings: k.
Calls/effect boundaries: any, context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].test; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[3].test.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_policy.py:114`; AST `c8a37fb04f17974c43756ae493a5d391fdd372e3f86097dc6bf0b303b02f359f`.

Rust module: `infra::agentinfra::roadmap_policy`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: context, k. Outputs/bindings: k.
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[3].body[3].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[3].test.args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_policy.py:114`; AST `ec3b2d851cd7f265ed9e06dc96cfcf35f8742f93186e0c40bf1292d567067c18`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, k. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].test.args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:115`; AST `e7d425c8a2f453643ce01faaa3dfe5df41c6737ec644eca551638bda251584e1`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:115`; AST `ddd8faa4fac96088e4de513bb476c7c82b4b4556404da9b63ef6d1d32211e8c5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[4]::If

Source: `infra/agentinfra/roadmap_policy.py:116`; AST `1657068aa016b92ccab0bf747087d0bfb981af294e1e3f718a5667e928d6b3ed`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[4]; no call, error or mutation may be omitted. Condition: not context.get('selected_model') or context.get('observed_model') != context.get('selected_model')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[4].test.values[0].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:116`; AST `c68cfba29e2d4b7ee72eabe9c72ab075a0f44ea6376343c8a0a054ade79db04d`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[4].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[4].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:116`; AST `ed5f35df1aef93a6ca907e38b6a5e3a8d20be42ea7f1af9e09690ebdd7c1e370`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[4].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:116`; AST `c68cfba29e2d4b7ee72eabe9c72ab075a0f44ea6376343c8a0a054ade79db04d`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[4].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:117`; AST `e7c725526bb150846153ed7601367645dc823cd360674afeecb67ee46d09f002`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:117`; AST `79e900d50ccc764a87fd373140ea1d3984aba7e776742c7018d071698839c949`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[5]::If

Source: `infra/agentinfra/roadmap_policy.py:118`; AST `3d81c8dc820f4decc8b88701360e544e5563ee34e8918d23a86c899b9fad57b3`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[5]; no call, error or mutation may be omitted. Condition: context.get('monetary_cap') is not None and context.get('cap_enforceable') is not True
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[5].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:118`; AST `7f9c7217c0fc621cc538019c04c39cb6ce7015f6dcc083b3756a9159e0f4ec8f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[5].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[5].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:118`; AST `7c97086997eedbbde9fb349f52a19f138ed15ad53974222791b39cc3e25c08f5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[5].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:119`; AST `72a057332d02c6b19e089ed9927303a7f3ba1780c049f45aa7409c1a1362d582`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:119`; AST `82137ee003d98abae3c0104ce6209468b7aa60ceeb8dfc1d3261a1467d817684`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[6]::If

Source: `infra/agentinfra/roadmap_policy.py:120`; AST `7814471598453694c7ce54186e43b4652f244dc345ccdbdf2bedda1130f128b3`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[6]; no call, error or mutation may be omitted. Condition: context.get('active_agents') != 1 or context.get('lease_valid') is not True
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[6].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:120`; AST `24d9c677ea763e477c2d512e1d68b028315c0bc726c9f9e1cf7122ee3f7c556a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[6].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[6].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:120`; AST `744b2b080ca734bbef797f713f202f36e77c3712197cf59fd436c131d40be1b4`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[6].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:121`; AST `4e120e7140dec2acc0c45cd80997dafeb0586411e865db0c7ed4caf95c53fc49`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:121`; AST `ea03801864db21df7e6e1f313f6d3d61b80dbccae609cbf9a9fc88b1e8d0d66e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[7]::If

Source: `infra/agentinfra/roadmap_policy.py:122`; AST `682f16dcf47953ddeac034d3136f2d47b4d63bb4a0ae36208d75400cb2f51d8c`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[7]; no call, error or mutation may be omitted. Condition: not context.get('expected_inputs') or context.get('expected_inputs') != context.get('current_inputs')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[7].test.values[0].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:122`; AST `067f842de3916f26f131a34dcee0b28a818e15e40259abe38fa9d5e4428ffe53`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[7].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[7].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:122`; AST `067f842de3916f26f131a34dcee0b28a818e15e40259abe38fa9d5e4428ffe53`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[7].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[7].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:122`; AST `83e7ff9534454d47d39a0a1c2aeebaa90e3cd344bddbb3262fe021b688658f5f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[7].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:123`; AST `d20021191c76c2358b1a3a50fb981ebd0b2c8c377ca193b42e9e18679eb7668b`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[3].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:123`; AST `ca334f9e175884aa568bb345eb1d134ac827dae85e8dae2ebc3e9cf7233971e8`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[4]::If

Source: `infra/agentinfra/roadmap_policy.py:124`; AST `36fa033e9c969bd9ebf983daf66902e16f9de6e9a5657b9189fa8e653df538ca`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[4]; no call, error or mutation may be omitted. Condition: action == 'verify' and context.get('phase') == 'implementation' and (not context.get('early_proof_justification'))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[4].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:124`; AST `c539a8927cd486bf83063e1bd65347897c6b7a8be09f00abef209b9571e58f0f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[4].test.values[2].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:124`; AST `777ff8e7ac7fa42ada0fbb0dc322e4e62e6e91c724b95be8dbd76afe3e4212a5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:125`; AST `2b43cd4f1ab5404583d92f0a30057cff7b12a311b06576a2c739807688c284d3`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:125`; AST `c21b8e5a9c29f11fa12a16faefe801285d8143eb1f5b785a3c448391759a67d4`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[5]::If

Source: `infra/agentinfra/roadmap_policy.py:126`; AST `f52176942e7506308fdfcde1583bab47f076a758947722224f2a437c77ed3b14`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[5]; no call, error or mutation may be omitted. Condition: action == 'review_campaign' and context.get('campaign_authorized') is not True
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[5].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_policy.py:126`; AST `6a183bb52f8b9637ee800a33ea847f32d4765e14fe0298542237a4ad477a394b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:127`; AST `7a9fd427ba7efdcc5fc4380f7ff96671d8571e562e012f13ef39d849db9191c5`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:127`; AST `190bb3aa97f4093ea545c2fd1a38e997ffc316d77362adee1be1672cb29fb33f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[6]::If

Source: `infra/agentinfra/roadmap_policy.py:128`; AST `9514ff229e88fba3c43b7e7002dbe1d18f1dcd7c4e6f6e5ab1514b71a8329a50`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, cgp_eligible, context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: cgp_eligible, context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[6]; no call, error or mutation may be omitted. Condition: action == 'cgp' and (not cgp_eligible(context.get('project_states', {})))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[6].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:128`; AST `f729bb7d5fc642dc2b00f8b0d65ed8a4598a239fad8e8241bfe022dfd69ada05`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cgp_eligible, context. Outputs/bindings: (none).
Calls/effect boundaries: cgp_eligible, context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[6].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:128`; AST `767dfcca764cee10d73bb76f2d1deebe9bb104462fa7c9a9061720e2cc6cc026`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:129`; AST `0bbcb068726c9f25cb6387a82d626fbc513165bea990e027f193ef2d86af3ac3`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:129`; AST `0fbb79a1caec8611f9733a6633a53ad3a9dcf29f3881345b53cd9d2c27abb8e1`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[7]::If

Source: `infra/agentinfra/roadmap_policy.py:130`; AST `78166878592ecbf8a3d91a5bf3f084682a6eb8ab217a6b2f3958001db1a622d3`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, all_satisfied, context, reasons. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied, context.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[12].body[7]; no call, error or mutation may be omitted. Condition: action == 'complete' and (not all_satisfied(context.get('required_gates', []), context.get('satisfied_gates', [])))
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[7].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_policy.py:130`; AST `484126305faf255535a1427c8a411e98083891450e096c94345d642b1907f630`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied, context. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied, context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[7].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:130`; AST `6bfe7c48809ae977dee8acc314c8bf8610c2cb74bbf065bbcbd52a7c3833ae40`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[7].test.values[1].operand.args[1]::Call

Source: `infra/agentinfra/roadmap_policy.py:130`; AST `2a004335f58f2fb428bcd07babbd22575a60c1c8dcf543be3dd08991e2bed4ce`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].test.values[1].operand.args[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:131`; AST `554407ace795cfc184f3be4abf7f4283a0ac0cf45482628b7339b3c09f1803a5`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:131`; AST `a033044166f728af6a8b10f006773f39b8208176f10b8226017d84c25e08c8c6`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[8]::Return

Source: `infra/agentinfra/roadmap_policy.py:132`; AST `df373b379cba2a6c14a6432906c85fc86b30e5982d2106ffbb7e049b79cc5d07`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, digest, reasons. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::authorize::root.body[12].body[8].value.values[2]::Call

Source: `infra/agentinfra/roadmap_policy.py:132`; AST `3a476c946fc733ae107f93816b44dae3f1516dec40574253df866fb8b6295087`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_policy.py:135`; AST `ad88b9d6a6d37882cafa34d801e38ffcfe3779d01627cdcc41a37878948f4de0`.

Rust module: `infra::agentinfra::roadmap_policy`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: acceptance, action, bool, budget, current, dict, int, params, requested, require, type, user_authorized. Outputs/bindings: action, budget, params.
Calls/effect boundaries: bool, current.get, requested.get, require, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:136`; AST `834a90043c06b0c4a00fb7f598328b3a30d7c249957781406dfc454592013630`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[1]::Expr

Source: `infra/agentinfra/roadmap_policy.py:137`; AST `cb7575b7f4546c5e1b9597a6a291676c97712f178873e113fbdee8519b627113`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap_policy.py:137`; AST `30ce7a83768e2c7f1d258f096694657bcda9000a392edcd4000bb17059859721`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_policy.py:138`; AST `5daab065152cf1009567ba4a293294bd2797a2250bc365e4a1f89daaa62bdd7f`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, current, requested, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, current.get, requested.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_policy.py:138`; AST `96bb2b47c8c3499aa6717f27b60944954adc71ed1339f10d66d2ca39168fcf69`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, current, requested, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, current.get, requested.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:138`; AST `4ccb105654fe5597a1697c4bc7ed1fa4156596a3cdcaf5c2d74171123b78250e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[2].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:138`; AST `8c791e933690da5ab2f1be99f3b4ace10f5ade345c96fe9103e5850f8cf5408f`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requested. Outputs/bindings: (none).
Calls/effect boundaries: requested.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_policy.py:138`; AST `adb25434387b71430b6690d815983821e2125ecf03f5d7114908d27a04df7782`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, current. Outputs/bindings: (none).
Calls/effect boundaries: bool, current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[2].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:138`; AST `4ccb105654fe5597a1697c4bc7ed1fa4156596a3cdcaf5c2d74171123b78250e`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[3]::Assign

Source: `infra/agentinfra/roadmap_policy.py:139`; AST `83e5840cefe5fcf1d9b892f8d0ee98b7e854e554adc933665d57330c33683d32`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: requested. Outputs/bindings: action.
Calls/effect boundaries: requested.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_policy.py:139`; AST `5fb24c2fe2be527205014b511d32bb295a67081febe10b26cad80dfb28707c40`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requested. Outputs/bindings: (none).
Calls/effect boundaries: requested.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[4]::Expr

Source: `infra/agentinfra/roadmap_policy.py:140`; AST `39f77a1140da8bb9f962a541df16d794142ed7f84d54e685645e74b5928be54b`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: action, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_policy.py:140`; AST `c28aca50adc5f6ad34a1f650f48a71cd5ff1847f9d661ff941a8055bf081c38b`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: action, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[5]::Expr

Source: `infra/agentinfra/roadmap_policy.py:141`; AST `132bea5b6977f3cd8973d4256d167cbd3f545770ad9f68f2678003330b260852`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, requested, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, requested.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap_policy.py:141`; AST `cc3efcb238ecdf870132c260760dfcf0ad5bc6d77c9dee4fd09d096e2f416ba6`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, requested, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, requested.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:141`; AST `be160ff24b4fc7e3ef4fee6360904b91168019dac9220dad42bfbfb05fd3adf9`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, requested. Outputs/bindings: (none).
Calls/effect boundaries: current.get, requested.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[5].value.args[0].left.args[1]::Call

Source: `infra/agentinfra/roadmap_policy.py:141`; AST `3beffb005f8194405958ef8600c2659db46ff8b6c64576b316f9ee5f3d94c2f5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.args[0].left.args[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[5].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_policy.py:141`; AST `3beffb005f8194405958ef8600c2659db46ff8b6c64576b316f9ee5f3d94c2f5`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[6]::If

Source: `infra/agentinfra/roadmap_policy.py:142`; AST `23f127442b179a2fb76289f2c8a13b5780fb4382ad65e34f24be44347581d726`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: acceptance, action, current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[13].body[6]; no call, error or mutation may be omitted. Condition: action == 'complete'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:143`; AST `4a0acdc38a5b8fc709c60ab096dcfe81c6ed3f752cb38fe733730dff55990b2c`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: acceptance, current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:143`; AST `af3f0681a53f7e1f4c2c724281f499caf38a6f2c30c01e12766df220097cedfe`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: acceptance, current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[6].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:143`; AST `4564f2316102ae2d9684337f0c37be3269780dcb9098d035a36273ecd2599a82`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[7]::If

Source: `infra/agentinfra/roadmap_policy.py:144`; AST `fb1405486f9c7dd9bddd937a7a51616ed64b420d04b5d2b44a67cced9622fa71`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[13].body[7]; no call, error or mutation may be omitted. Condition: action == 'resume'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_policy.py:145`; AST `5fdafb27c5cb013eadab8d0bee375a7242f24063f4b09ff313476390513b32ff`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:145`; AST `0919a107706872adf14118c5c7b9509fa92566241b412c1526c6bdf3bb86251a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[7].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:145`; AST `4564f2316102ae2d9684337f0c37be3269780dcb9098d035a36273ecd2599a82`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[8]::Assign

Source: `infra/agentinfra/roadmap_policy.py:146`; AST `4ab44879311882542ce23ae23d761d316157a58689817b3d43cce447da75c26e`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: action, current. Outputs/bindings: params.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9]::If

Source: `infra/agentinfra/roadmap_policy.py:147`; AST `ed6f9c7114e7fe8d436a0ee3bbb238bc8832c02a52561a3ec3852c597d52033e`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, budget, int, params, requested, require, type. Outputs/bindings: budget.
Calls/effect boundaries: requested.get, require, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[13].body[9]; no call, error or mutation may be omitted. Condition: action == 'budget'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_policy.py:148`; AST `2d0cc9d3cce53aab63340324cb7a0d7e94d4ab0d36449c47621ddf0bc7eb0561`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: requested. Outputs/bindings: budget.
Calls/effect boundaries: requested.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_policy.py:148`; AST `afa3b4614dc00f6a86483702ef8b5b2dd929076d9d6004cac1d451e7c8e25982`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requested. Outputs/bindings: (none).
Calls/effect boundaries: requested.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].body[1]::Expr

Source: `infra/agentinfra/roadmap_policy.py:149`; AST `2287e9ae0c342d26dc254122a5e2816a6da7af9911d1c07830d39d1531ef98a7`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: budget, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_policy.py:149`; AST `ff151975a1916407561b7c5a9c3c4ef415c79346cedc2247a8e7163718286373`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: budget, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_policy.py:149`; AST `b11f3040269a44354c4dcae41c84262b0a7a9d7248b086d9bb05d6716c4e669a`.

Rust module: `infra::agentinfra::roadmap_policy`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: budget, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_policy.py:150`; AST `83de434b4dbd2a9aa9868e4ce5a6ba61ff756225c9b0ff49d70887dfd7d9f0a9`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: budget, params. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].orelse[0]::If

Source: `infra/agentinfra/roadmap_policy.py:151`; AST `e682071af1ca83d4e68e6e9957a2df799e1dfe4e0fd48ddd91c6d5227eac5285`.

Rust module: `infra::agentinfra::roadmap_policy`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: action, params. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[13].body[9].orelse[0]; no call, error or mutation may be omitted. Condition: action != 'clear'
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[9].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_policy.py:152`; AST `74b0087b706c91b66c9176a741309254eb2f97ed354221f7685d05aabf0e47b8`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: action, params. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[9].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_policy.py::module::goal_transition::root.body[13].body[10]::Return

Source: `infra/agentinfra/roadmap_policy.py:153`; AST `82914b652547a9465f9c2d0f1f07ce3b05ba074dbb26af1151b50e00797b4b48`.

Rust module: `infra::agentinfra::roadmap_policy`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: action, params. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
