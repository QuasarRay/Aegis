# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 7. Inventory digest: `643a3011ceb8e8c7fa9a015c87f69249beb8af3b3abbb4fbcc1c3062122ba34f`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## verification/roadmap/python/policy_deal_negative.py::module::root::Module

Source: `verification/roadmap/python/policy_deal_negative.py:1`; AST `7fbd10af4e72400bc5583b217393be70ddae7e4bf8dec1d89f17d4619880c3e8`.

Rust module: `verification::roadmap::python::policy_deal_negative`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: allowed, may_reserve. Outputs/bindings: allowed.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_negative.py::module::root.body[0]::Expr

Source: `verification/roadmap/python/policy_deal_negative.py:1`; AST `6ddf68bb905d0824c3222c639ada557e9cbc8d8e4a0f04e8ca73afee175a5dd8`.

Rust module: `verification::roadmap::python::policy_deal_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_negative.py::module::root.body[1]::ImportFrom

Source: `verification/roadmap/python/policy_deal_negative.py:2`; AST `46b4a2cc221e6da19ffc05ec2a7f910dae3a68ac2bfe92af1845519bce0dc856`.

Rust module: `verification::roadmap::python::policy_deal_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_negative.py::module::deliberately_wrong_budget_assertion::root.body[2]::FunctionDef

Source: `verification/roadmap/python/policy_deal_negative.py:5`; AST `2bf571403ea1343743c8ead7557600c8b689b71184926a35b4c587ee642a3d51`.

Rust module: `verification::roadmap::python::policy_deal_negative`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: allowed, may_reserve. Outputs/bindings: allowed.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered FunctionDef evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_negative.py::module::deliberately_wrong_budget_assertion::root.body[2].body[0]::Assign

Source: `verification/roadmap/python/policy_deal_negative.py:6`; AST `94a425e89d69487c9fd21fe0c40dee84970ee9d60ca17f1e609417962c3bde41`.

Rust module: `verification::roadmap::python::policy_deal_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: may_reserve. Outputs/bindings: allowed.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_negative.py::module::deliberately_wrong_budget_assertion::root.body[2].body[0].value::Call

Source: `verification/roadmap/python/policy_deal_negative.py:6`; AST `bfd6e9bf4377452f55367e6d880c237b71ac73d9fde8cb3fa933493a09e537b8`.

Rust module: `verification::roadmap::python::policy_deal_negative`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: may_reserve. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_negative.py::module::deliberately_wrong_budget_assertion::root.body[2].body[1]::Assert

Source: `verification/roadmap/python/policy_deal_negative.py:7`; AST `a0f42728b67eeb550cae2287b94c95524ea5c1da2d5ce5e97d5f87b503c7eb46`.

Rust module: `verification::roadmap::python::policy_deal_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allowed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assert evaluation at root.body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
