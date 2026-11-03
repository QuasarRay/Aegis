# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 23. Inventory digest: `f17ce03723fdd72db6b8171d8e7d038c76be3a68118ab126792da3b333692fa8`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## verification/roadmap/python/policy_deal_positive.py::module::root::Module

Source: `verification/roadmap/python/policy_deal_positive.py:1`; AST `59ba59ad2db24a99818453f80c02b4a8ac8433f800edcbefa0cebdb75a580857`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: all_satisfied, allowed, boolean, cgp_eligible, dict, empty, incomplete, may_reserve, modernize, over. Outputs/bindings: allowed, boolean, empty, incomplete, modernize, over.
Calls/effect boundaries: all_satisfied, cgp_eligible, dict, may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::root.body[0]::Expr

Source: `verification/roadmap/python/policy_deal_positive.py:1`; AST `71599cd5df73ce66ba641484b5a79059c07c362168708b5e211f030e378d3584`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_deal_positive.py::module::root.body[1]::ImportFrom

Source: `verification/roadmap/python/policy_deal_positive.py:6`; AST `7b70d2104182992758f38c4c6f3036e1e68dd46f22137951a6ae157257cc2aaf`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2]::FunctionDef

Source: `verification/roadmap/python/policy_deal_positive.py:9`; AST `8e1acb964308f71d0b790493914acb917a42934e8b3775dc13d66edcc15ea11e`.

Rust module: `verification::roadmap::python::policy_deal_positive`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all_satisfied, allowed, boolean, cgp_eligible, dict, empty, incomplete, may_reserve, modernize, over. Outputs/bindings: allowed, boolean, empty, incomplete, modernize, over.
Calls/effect boundaries: all_satisfied, cgp_eligible, dict, may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered FunctionDef evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[0]::Assign

Source: `verification/roadmap/python/policy_deal_positive.py:10`; AST `94a425e89d69487c9fd21fe0c40dee84970ee9d60ca17f1e609417962c3bde41`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[0].value::Call

Source: `verification/roadmap/python/policy_deal_positive.py:10`; AST `bfd6e9bf4377452f55367e6d880c237b71ac73d9fde8cb3fa933493a09e537b8`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

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

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[1]::Assert

Source: `verification/roadmap/python/policy_deal_positive.py:11`; AST `969a417cb2fd3358fe162fc8b34520fc3c5476c9eb032e67a827d7dfb8b35488`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[2]::Assign

Source: `verification/roadmap/python/policy_deal_positive.py:12`; AST `9d237b089d7dcccdfb91acbaa356976324151b51139c92ec0601b52c74614809`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: may_reserve. Outputs/bindings: over.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[2].value::Call

Source: `verification/roadmap/python/policy_deal_positive.py:12`; AST `5a33ca4865985e47b3dcdd441e07ab0bd2db45c0544c01ed062a8a9b2a21ae46`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: may_reserve. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[3]::Assert

Source: `verification/roadmap/python/policy_deal_positive.py:13`; AST `ee72c68a4fd53e5174deaab2c0a7929d2963b5a73c1aae58d79f5e0b3f95678f`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: over. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assert evaluation at root.body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[4]::Assign

Source: `verification/roadmap/python/policy_deal_positive.py:14`; AST `e59a80ba5a2fce1efe2cba19f3adfb0ac3d7d476fcefad3f1a8083311436c9b6`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: may_reserve. Outputs/bindings: boolean.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[4].value::Call

Source: `verification/roadmap/python/policy_deal_positive.py:14`; AST `248fc8934134e0bf5b4a36372256f0a76a9bd2d0f17fd0a886a5827493194c66`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: may_reserve. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[5]::Assert

Source: `verification/roadmap/python/policy_deal_positive.py:15`; AST `f603cfe7378da2f77230fc512bdecd164bce6618407c26182255367b80955c8b`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: boolean. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assert evaluation at root.body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[6]::Assign

Source: `verification/roadmap/python/policy_deal_positive.py:16`; AST `514d1e563504b1151a64b4027e2d8947822cecdf38c237d9da910a18cd7c5c54`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all_satisfied. Outputs/bindings: empty.
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[6].value::Call

Source: `verification/roadmap/python/policy_deal_positive.py:16`; AST `082b9aa29713d8991733e3230cbd3e7fba8d6b0cb0864f276d260846edcaefed`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[7]::Assert

Source: `verification/roadmap/python/policy_deal_positive.py:17`; AST `a0b86a490d08af9837d3408245ba1449862b2057cb2cb851bab42dd3b0d98420`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: empty. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assert evaluation at root.body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[8]::Assign

Source: `verification/roadmap/python/policy_deal_positive.py:18`; AST `079f299363826fe5a964c6cb9c8b260d333dcc44ebf741d02111622e7a250533`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all_satisfied. Outputs/bindings: incomplete.
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[8].value::Call

Source: `verification/roadmap/python/policy_deal_positive.py:18`; AST `0cc7257bec9f2715cf6fa6b218825836ab225317e7be33188ae1c8917b4b8087`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[9]::Assert

Source: `verification/roadmap/python/policy_deal_positive.py:19`; AST `61678d339890115111a9df44a936ea2803530569c02832bbc06b9a0103a66a27`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: incomplete. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assert evaluation at root.body[2].body[9]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[10]::Assign

Source: `verification/roadmap/python/policy_deal_positive.py:20`; AST `0ab96f1c579ce8dba31c8685218ce5715e8280611a0f7880836f45dd416b837c`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cgp_eligible, dict. Outputs/bindings: modernize.
Calls/effect boundaries: cgp_eligible, dict.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[10].value::Call

Source: `verification/roadmap/python/policy_deal_positive.py:20`; AST `a4ec6d66d9a19b87df15994454e2583e968f0d3df3b20bd5ce732745e661ec92`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cgp_eligible, dict. Outputs/bindings: (none).
Calls/effect boundaries: cgp_eligible, dict.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[10].value.args[0]::Call

Source: `verification/roadmap/python/policy_deal_positive.py:20`; AST `61a77424fd19dbd690f0c66643bcc2c29d65c3ee4ebbf06709992ef46bc257a8`.

Rust module: `verification::roadmap::python::policy_deal_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Call evaluation at root.body[2].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_deal_positive.py::module::original_budget_and_completion::root.body[2].body[11]::Assert

Source: `verification/roadmap/python/policy_deal_positive.py:21`; AST `1eaabed005a8e55f8404717406797f5e4e563fdbfcd2eae0dd601cad1c009754`.

Rust module: `verification::roadmap::python::policy_deal_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: modernize. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy.

Invariants: Preserve ordered Assert evaluation at root.body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
