# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 98. Inventory digest: `b94d97a70a28e2ead889acc39a1ff42c0c77efefe95211d4f5f3bb9db249b056`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_verification.py::module::root::Module

Source: `infra/agentinfra/roadmap_verification.py:1`; AST `61f5340dc08f1573aa133916cd83f9bd5fb33a70d636e03935c791e7158e8552`.

Rust module: `infra::agentinfra::roadmap_verification`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: actual, after, all, any, before, bool, candidate, confirmed, desired, dict, digest, executed, expected, field, fields, int, k, len, list, missing, new, old, passing, r, reasons, require, required, response, set, sorted, str, t, test, test_occurrence_identity, type. Outputs/bindings: actual, confirmed, expected, field, fields, k, missing, new, old, passing, r, reasons, t.
Calls/effect boundaries: after.get, all, any, before.get, bool, digest, len, reasons.append, require, response.get, set, sorted, t.get, test_occurrence_identity, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:1`; AST `dc959e59da1d047bf26e5bf7253835b4360bb5d78f457e3854f3f8c6ca265f12`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_verification.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_verification.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_verification.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_verification.py:4`; AST `dcc141a1e9bd471992df89dfef26417080014b0f5967e497f55034dd43ec3a33`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_verification.py:7`; AST `e96251891dbfece0a10e78987315a0a52738a9dff1f096201fc6ad6eac425a8b`.

Rust module: `infra::agentinfra::roadmap_verification`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, dict, digest, fields, k, require, str, test. Outputs/bindings: fields, k.
Calls/effect boundaries: all, digest, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_verification.py:8`; AST `38e5d69a6f6f3cbe6a752c77f6ff385cf6f2e58e8c0d982052f10527f557d864`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: fields.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_verification.py:9`; AST `c5692b1cd910d9d3e6abbf357f06e42c490ebbfeff3da2a839d288c3dbd61b58`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, fields, k, require, test. Outputs/bindings: k.
Calls/effect boundaries: all, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_verification.py:9`; AST `fbf8137f1b8fdf21356fb28768e5b4958674310db2a93ad23e9afcb3cc67146f`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, fields, k, require, test. Outputs/bindings: k.
Calls/effect boundaries: all, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:9`; AST `267a76b3e196337c8eeba3f609fdd8beb56a3fc5029bccc2bfabf4bda87e0a36`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, fields, k, test. Outputs/bindings: k.
Calls/effect boundaries: all.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[1].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_verification.py:9`; AST `e4fa208e37ad98cd3cdaf9c20e309eeb54b4dda15bf05b43d2344140df2ad58e`.

Rust module: `infra::agentinfra::roadmap_verification`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: fields, k, test. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[3].body[1].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_verification.py:10`; AST `68e8cf8866b98dd75c165d432126c098d8f8af0514eab3aecd01351d4f3d9ee9`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, k, require, test. Outputs/bindings: k.
Calls/effect boundaries: all, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_verification.py:10`; AST `2d2e97cbe931ced6942989f65b9edf2e558b954e11b022c7ce10b4ed72aa58bc`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, k, require, test. Outputs/bindings: k.
Calls/effect boundaries: all, require.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:10`; AST `1f8d1fed2bdc13e0d47a5e0a2253000699c2febc846baeda085e6db189ddf6c5`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, k, test. Outputs/bindings: k.
Calls/effect boundaries: all.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[3].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[2].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_verification.py:10`; AST `648d08468ae1ac629019d1849be814cedeaf4df90b072bde315a97b0cf46c461`.

Rust module: `infra::agentinfra::roadmap_verification`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: k, test. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[3].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[3]::Return

Source: `infra/agentinfra/roadmap_verification.py:11`; AST `a71c80297e1dbc8c946998836060ac250c755551e1739aa5341632e7f02e0850`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, fields, k, test. Outputs/bindings: k.
Calls/effect boundaries: digest.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_verification.py:11`; AST `690c80a724780b372929267a694bba5d76ad67f52903c083372a4af7a87b5e7a`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, fields, k, test. Outputs/bindings: k.
Calls/effect boundaries: digest.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::test_occurrence_identity::root.body[3].body[3].value.args[0]::DictComp

Source: `infra/agentinfra/roadmap_verification.py:11`; AST `4601c8a09e2e014509c9c1a05f4a2d4988ccbda91c6f72e2dcf412bc88c33d92`.

Rust module: `infra::agentinfra::roadmap_verification`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: fields, k, test. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered DictComp evaluation at root.body[3].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_verification.py:14`; AST `2febe96c397c9a9928fc00fc49719907b7def27161953137e7c4defd8bd90d24`.

Rust module: `infra::agentinfra::roadmap_verification`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: actual, bool, candidate, dict, executed, expected, len, list, missing, passing, require, required, set, sorted, str, t, test_occurrence_identity. Outputs/bindings: actual, expected, missing, passing, t.
Calls/effect boundaries: bool, len, require, set, sorted, t.get, test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_verification.py:15`; AST `7ef6cbb5324893e353dc1bde55f75812dd1a20304c1df5e546192530b786382a`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: required, t, test_occurrence_identity. Outputs/bindings: expected, t.
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_verification.py:15`; AST `19f987c2036694c12c756ccd1cd9fb339d003918776b3496942cde3036b910c3`.

Rust module: `infra::agentinfra::roadmap_verification`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: required, t, test_occurrence_identity. Outputs/bindings: t.
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered ListComp evaluation at root.body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[0].value.elt::Call

Source: `infra/agentinfra/roadmap_verification.py:15`; AST `6a5cce7c9cb0c84fe998e377bbc308e2baedfa36a88e317bb2f8571f4095e1e8`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t, test_occurrence_identity. Outputs/bindings: (none).
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[0].value.elt; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[1]::Expr

Source: `infra/agentinfra/roadmap_verification.py:16`; AST `f9522ba91b6d7694fef6273273ba2afec61c620df947fa621fa606a4e1a3493b`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_verification.py:16`; AST `313cd2d6b3514d5c75c4606b335f41fe2e7c7d44e22694253798af6c2a20f211`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_verification.py:16`; AST `c2d06b163e3f45e9d7be910cb5ac5a89b21e57724763b4159be61fb15e2f5005`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[1].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:16`; AST `92c7b105ab8208e6c0d99003aa501423395c1925384705c62d883a1c21cf675e`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[1].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[1].value.args[0].values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:16`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[1].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[2]::Assign

Source: `infra/agentinfra/roadmap_verification.py:17`; AST `42cbe573114177b1ab3b3b1e2fd075725565553842fadc8ef456faf9a04f5576`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: executed, t, test_occurrence_identity. Outputs/bindings: actual, t.
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_verification.py:17`; AST `2e7b651b60dbe423cdc990cc6e82b34f8b42ffc9d0501820425e398274b77bc0`.

Rust module: `infra::agentinfra::roadmap_verification`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: executed, t, test_occurrence_identity. Outputs/bindings: t.
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered ListComp evaluation at root.body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[2].value.elt::Call

Source: `infra/agentinfra/roadmap_verification.py:17`; AST `6a5cce7c9cb0c84fe998e377bbc308e2baedfa36a88e317bb2f8571f4095e1e8`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t, test_occurrence_identity. Outputs/bindings: (none).
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[2].value.elt; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_verification.py:18`; AST `253b5e890144a8d248e321464f4cbc22953e8e66ea2f4ab1ac0d9f3bfc3ac3a7`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_verification.py:18`; AST `74816a51c24f1bbca4c05dd26d404838b31b0a84309a121079bbcb3a0a8d9109`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:18`; AST `adb3cd8db9be869bc971de58124aa0c6c4176af8faf71dc5f35778aa7a24d429`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[3].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:18`; AST `9975a2dfd52200ad978c02c2e490080b1f4e7f98869d6bcb91183ad9d6c81863`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[3].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:18`; AST `f3b94940b2cabe37e2711e0ac31aa2ac688a4d9ad8dba19b27a18c4c0fee98ba`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[3].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[4]::Expr

Source: `infra/agentinfra/roadmap_verification.py:19`; AST `11fc90932e0ff701f1010f6b61ca84cfef2542e83198900850029e12d42356ab`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, expected, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_verification.py:19`; AST `e56f14e4b76f382c415ff699c2b2de0ba8e9d83d3f22fcd1e528022a480ea1e7`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, expected, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:19`; AST `f3b94940b2cabe37e2711e0ac31aa2ac688a4d9ad8dba19b27a18c4c0fee98ba`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[4].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:19`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[4].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5]::Assign

Source: `infra/agentinfra/roadmap_verification.py:20`; AST `5b0f78a3a76c350acbb6a2a4594b6ea3104db029695b480b582cbefd74b27fa1`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, candidate, executed, t, test_occurrence_identity. Outputs/bindings: passing, t.
Calls/effect boundaries: bool, t.get, test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value::SetComp

Source: `infra/agentinfra/roadmap_verification.py:20`; AST `be632d51cb5ee4864bdbe76fab97e8581a7248fdf6eb09dcd447e56847e1b47d`.

Rust module: `infra::agentinfra::roadmap_verification`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: bool, candidate, executed, t, test_occurrence_identity. Outputs/bindings: t.
Calls/effect boundaries: bool, t.get, test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.elt::Call

Source: `infra/agentinfra/roadmap_verification.py:20`; AST `6a5cce7c9cb0c84fe998e377bbc308e2baedfa36a88e317bb2f8571f4095e1e8`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t, test_occurrence_identity. Outputs/bindings: (none).
Calls/effect boundaries: test_occurrence_identity.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.elt; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.generators[0].ifs[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:21`; AST `39d084f39ee706aa52acc3bfbee67fa7dbf88a51c4864d40867b060e5a930c0f`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t. Outputs/bindings: (none).
Calls/effect boundaries: t.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.generators[0].ifs[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.generators[0].ifs[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_verification.py:21`; AST `bd4a5fef3472edc89cf6c95d2d3cc0461ad711d43233bca2cc53580dac69ecdc`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t. Outputs/bindings: (none).
Calls/effect boundaries: t.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.generators[0].ifs[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.generators[0].ifs[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_verification.py:22`; AST `9ce8435d0958af5344687a70d477cf933e5196f7dcae5b306f48fb274174a7f0`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t. Outputs/bindings: (none).
Calls/effect boundaries: t.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.generators[0].ifs[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.generators[0].ifs[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:22`; AST `ff7dec3a1f87af46cf8b0d32fba8e236aba94e280fdf0ad537f1bf6bf8d2ccd5`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t. Outputs/bindings: (none).
Calls/effect boundaries: t.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.generators[0].ifs[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.generators[0].ifs[0].values[3]::Call

Source: `infra/agentinfra/roadmap_verification.py:22`; AST `fd057a90791e894f635eeac1f465708c75536386a102e90f95bd3897e79085d4`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, t. Outputs/bindings: (none).
Calls/effect boundaries: bool, t.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.generators[0].ifs[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[5].value.generators[0].ifs[0].values[3].args[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:22`; AST `9ce8435d0958af5344687a70d477cf933e5196f7dcae5b306f48fb274174a7f0`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: t. Outputs/bindings: (none).
Calls/effect boundaries: t.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[5].value.generators[0].ifs[0].values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[6]::Assign

Source: `infra/agentinfra/roadmap_verification.py:23`; AST `0a37d8cf12f3a7d36a6058313763228ee9330822dfc51be867a31e4a00242bb5`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, passing, set, sorted. Outputs/bindings: missing.
Calls/effect boundaries: set, sorted.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_verification.py:23`; AST `d9144cbfc4c8e18b3376beef29f8b9ca73f16297b0ec8ace121756c9ac0ec2df`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, passing, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[6].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:23`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[7]::Return

Source: `infra/agentinfra/roadmap_verification.py:24`; AST `22d62f0104943ea2701b5ff617b0be445aa2bc8c541f34828b6869b1ecddd0c2`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, len, missing, passing. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[7].value.values[1]::Call

Source: `infra/agentinfra/roadmap_verification.py:24`; AST `c2d06b163e3f45e9d7be910cb5ac5a89b21e57724763b4159be61fb15e2f5005`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[7].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_original_tests::root.body[4].body[7].value.values[2]::Call

Source: `infra/agentinfra/roadmap_verification.py:24`; AST `f5d9bfa2ef6c736085b2249b4f0da78f74b90f0bd6e76b4f548f926bec507eb1`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, passing. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[4].body[7].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_verification.py:27`; AST `4e2cdc85daca7facbbdd27874e48c32c082a9c7de33304182dc35f24359f0379`.

Rust module: `infra::agentinfra::roadmap_verification`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: after, any, before, bool, confirmed, desired, dict, digest, field, int, new, old, r, reasons, response, str, type. Outputs/bindings: confirmed, field, new, old, r, reasons.
Calls/effect boundaries: after.get, any, before.get, bool, digest, reasons.append, response.get, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:28`; AST `c6cb351a4114660dfa1515e0ec8dd6c077aa7866d8619d6ec69bf8f5c75b6698`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[1]::Assign

Source: `infra/agentinfra/roadmap_verification.py:29`; AST `faf14f7c71c5d60e7d6c6ee9138825667c49802e0d07381a92e1f4e8076b2c65`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: reasons.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[2]::If

Source: `infra/agentinfra/roadmap_verification.py:30`; AST `636a20d07169dca0a21b5797d0d3c12dce97b291cd5787df7a2319fb64bc8dfa`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: reasons, response. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append, response.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[2]; no call, error or mutation may be omitted. Condition: response is None or response.get('error')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[2].test.values[1]::Call

Source: `infra/agentinfra/roadmap_verification.py:30`; AST `6d6a4d724bc2157548fba0988fa380e1c5875d31393eb9eb94e10826f774d2f0`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response. Outputs/bindings: (none).
Calls/effect boundaries: response.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:31`; AST `d9891dd9f47db1cd2492d72e8d191126e9da61023228e47b0bec8387dcc79a25`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_verification.py:31`; AST `d2e7376155bcfef35429cca1c528019b0c4fecd510d480616fd159e8fc0069fa`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3]::If

Source: `infra/agentinfra/roadmap_verification.py:32`; AST `f266fbb25be4fc690815fe8b5bd84b80aef10d1fbc993c3dfab10d2c17a57c2e`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, before, desired, field, int, new, old, reasons, type. Outputs/bindings: field, new, old.
Calls/effect boundaries: after.get, before.get, reasons.append, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[3]; no call, error or mutation may be omitted. Condition: not after
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:33`; AST `c8c1705d51609c483b0f1fedd16ea945417d158b82858c7488d1f3fe5bb367b3`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_verification.py:33`; AST `fc7cfa08ecd400ceb9d1fa49a538e94ad520b7cc4acfd7595fb3796e494da94e`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0]::For

Source: `infra/agentinfra/roadmap_verification.py:35`; AST `35d4d1cea525637a51725823bbc2c0acda31523381d2bc0486d473c4b4600e5c`.

Rust module: `infra::agentinfra::roadmap_verification`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: after, before, field, reasons. Outputs/bindings: field.
Calls/effect boundaries: after.get, before.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[5].body[3].orelse[0]; no call, error or mutation may be omitted. Iteration: field in ('threadId', 'objective')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0].body[0]::If

Source: `infra/agentinfra/roadmap_verification.py:36`; AST `91e3db5343419828550ac379e0c7a0ed217a02183a9b28bd4720c251dd512b23`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, before, field, reasons. Outputs/bindings: (none).
Calls/effect boundaries: after.get, before.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[3].orelse[0].body[0]; no call, error or mutation may be omitted. Condition: after.get(field) != before.get(field) or not before.get(field)
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0].body[0].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:36`; AST `8006c7adf12ec09fd38010a58030b96c2625d28b2090d2b42ca2ddd1ee774672`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, field. Outputs/bindings: (none).
Calls/effect boundaries: after.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[0].body[0].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0].body[0].test.values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:36`; AST `8bedaf6d0c2cf005ef5f1e89a38a20c35b8c47137f2cf7d08036ef149fc3d617`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, field. Outputs/bindings: (none).
Calls/effect boundaries: before.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[0].body[0].test.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_verification.py:36`; AST `8bedaf6d0c2cf005ef5f1e89a38a20c35b8c47137f2cf7d08036ef149fc3d617`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, field. Outputs/bindings: (none).
Calls/effect boundaries: before.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[0].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:37`; AST `40b13d75ab8483c228b2cdefc20a499a176f29a1288cbaebb3710ecb7233cfc3`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[3].orelse[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_verification.py:37`; AST `53b411e9a4bdf4be8ac303be52fe44da6dc42d80e21023f8ccd897f8492d05a4`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[1]::If

Source: `infra/agentinfra/roadmap_verification.py:38`; AST `a94a5222686f2ca28ed7cad53dca81e6d32b7f0255463b16b248082a1b81728f`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, desired, reasons. Outputs/bindings: (none).
Calls/effect boundaries: after.get, reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[3].orelse[1]; no call, error or mutation may be omitted. Condition: after.get('status') != desired
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[1].test.left::Call

Source: `infra/agentinfra/roadmap_verification.py:38`; AST `633937bee7db1dd8e38adfe54744228779f88f4f28b69b9d13ed2d5ce959cc19`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after. Outputs/bindings: (none).
Calls/effect boundaries: after.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:39`; AST `54dcd24ceb7eed1b1a65b87c4fb29984598c804c407adba8f59eb1d69ed5f5ee`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[3].orelse[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_verification.py:39`; AST `0993537ec5646a28c702230f038e38fe042230d5e28a6717782bfbb9c1338370`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2]::For

Source: `infra/agentinfra/roadmap_verification.py:40`; AST `6efe0557230be842fdd9c0f28f9191140c645575e2aedd9f62972711cc1b53f7`.

Rust module: `infra::agentinfra::roadmap_verification`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: after, before, field, int, new, old, reasons, type. Outputs/bindings: field, new, old.
Calls/effect boundaries: after.get, before.get, reasons.append, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[5].body[3].orelse[2]; no call, error or mutation may be omitted. Iteration: field in ('tokensUsed', 'timeUsedSeconds')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_verification.py:41`; AST `d48a8192a51ff5f1cf39f4586d32b8c7a6cc416c7c1de6bd375d3de1d907fc29`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, field. Outputs/bindings: new, old.
Calls/effect boundaries: after.get, before.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[3].orelse[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[0].value.elts[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:41`; AST `8bedaf6d0c2cf005ef5f1e89a38a20c35b8c47137f2cf7d08036ef149fc3d617`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, field. Outputs/bindings: (none).
Calls/effect boundaries: before.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[2].body[0].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[0].value.elts[1]::Call

Source: `infra/agentinfra/roadmap_verification.py:41`; AST `8006c7adf12ec09fd38010a58030b96c2625d28b2090d2b42ca2ddd1ee774672`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, field. Outputs/bindings: (none).
Calls/effect boundaries: after.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[2].body[0].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[1]::If

Source: `infra/agentinfra/roadmap_verification.py:42`; AST `af2f3a6302fe9227bb250701bac9d394e78d67ea2c17531e21730789e7db758a`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: int, new, old, reasons, type. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[3].orelse[2].body[1]; no call, error or mutation may be omitted. Condition: type(old) is not int or type(new) is not int or new < old
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[1].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:42`; AST `bd1431d2ce73ce7f73a650eeaa62a0721228e7e7aad46fd218928155798ec9eb`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[2].body[1].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[1].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_verification.py:42`; AST `469f77bb2e8660981a88b7d15101231c31f4fd37fdec04b7d3572166502ca32e`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: new, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[2].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:43`; AST `7efa5c946a14e8b5e953209aa5d0c459ebb986d36623ad0ab14127c2cb16e11c`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[3].orelse[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[2].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_verification.py:43`; AST `fa60dce5c0dcc1510216bcdcc9525b7f965b2747739d8d9b9920ce828f6747cc`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[3]::If

Source: `infra/agentinfra/roadmap_verification.py:44`; AST `4f7b0042dbdb5e6945b40a1039cfc1824bf7e188a06a99049bbc35cb55e251e0`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, before, int, reasons, type. Outputs/bindings: (none).
Calls/effect boundaries: after.get, before.get, reasons.append, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[3].orelse[3]; no call, error or mutation may be omitted. Condition: before.get('createdAt') is not None and (type(after.get('createdAt')) is not int or after['createdAt'] != before['createdAt'])
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[3].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:44`; AST `77cb9428053a12f4b71b5909b3ecd3905ba4e0b02bb62bd65ab00e869b293be6`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[3].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[3].test.values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_verification.py:44`; AST `c3467e69633ae948a46862da2fabb701ae5d7507debfb9580d25e4a249faf415`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, type. Outputs/bindings: (none).
Calls/effect boundaries: after.get, type.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[3].test.values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[3].test.values[1].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:44`; AST `1f1b8371a8a316f04aff5c4082c3777b05611337ca42a033c4f7ab449486c699`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after. Outputs/bindings: (none).
Calls/effect boundaries: after.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[3].test.values[1].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_verification.py:46`; AST `fa4218d92910970b5d77b66eb4eb702b704bdace09fbc46886ac6c5611530250`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[3].orelse[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[3].orelse[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_verification.py:46`; AST `0622a59cd8e6b4345c4c54982f7e893da7238fc4f03269fd44c0283754114b39`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reasons. Outputs/bindings: (none).
Calls/effect boundaries: reasons.append.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[3].orelse[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[4]::Assign

Source: `infra/agentinfra/roadmap_verification.py:48`; AST `1f1d5738f5a7a364163843c9c472e9e55a1bd4be4c543ecea488d9f45578b870`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, any, bool, r, reasons. Outputs/bindings: confirmed, r.
Calls/effect boundaries: any, bool.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[4].value.values[0]::Call

Source: `infra/agentinfra/roadmap_verification.py:48`; AST `9595c2e99ac4bfa8bac2f3b8cb0e81df5d7a3f665c6fd91d4cfa2aa025572c88`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, bool. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[4].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[4].value.values[1].operand::Call

Source: `infra/agentinfra/roadmap_verification.py:48`; AST `62b1763421c6fabec79f5c324800748e18da068b87edafcc5db0ccdc61458845`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, r, reasons. Outputs/bindings: r.
Calls/effect boundaries: any.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[4].value.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[4].value.values[1].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_verification.py:48`; AST `998752cf80fb0ebcbe82534ae4ba54561548e6c9056bf573472f8953c3fd0c3a`.

Rust module: `infra::agentinfra::roadmap_verification`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, reasons. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[5].body[4].value.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[5]::If

Source: `infra/agentinfra/roadmap_verification.py:49`; AST `224a0ffe1885e4b522e2da4ef34662df3c10e54d9e975ae8e2971031b334fc85`.

Rust module: `infra::agentinfra::roadmap_verification`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: response. Outputs/bindings: confirmed.
Calls/effect boundaries: response.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[5].body[5]; no call, error or mutation may be omitted. Condition: response and response.get('error')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[5].test.values[1]::Call

Source: `infra/agentinfra/roadmap_verification.py:49`; AST `6d6a4d724bc2157548fba0988fa380e1c5875d31393eb9eb94e10826f774d2f0`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response. Outputs/bindings: (none).
Calls/effect boundaries: response.get.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[5].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_verification.py:50`; AST `f82726c152e00d9eb9ebe3bd1f96ba663e6066073259f8710646216c3cac2cf6`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: confirmed.
Calls/effect boundaries: (none).
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[6]::Return

Source: `infra/agentinfra/roadmap_verification.py:51`; AST `f833872ca873c54e5cc8cf8ea8bbe31fabc2c16771a001dc27d36c1ce7deac92`.

Rust module: `infra::agentinfra::roadmap_verification`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, confirmed, digest, reasons. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_verification.py::module::reconcile_native_transition::root.body[5].body[6].value.values[2].body::Call

Source: `infra/agentinfra/roadmap_verification.py:52`; AST `064cb3f084a888036f0d3d248443b4d6766fc289df8318e68a3ca4b89419389f`.

Rust module: `infra::agentinfra::roadmap_verification`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[5].body[6].value.values[2].body; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
