# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 30. Inventory digest: `7b0cd4871e196dae899f13ac975532f9281e678e2bc6cf15939969b7031f7c7a`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## verification/roadmap/python/policy_positive.py::module::root::Module

Source: `verification/roadmap/python/policy_positive.py:1`; AST `686f5b23cd01166ac11c5c61f30123daccfd768258f4fe674db000fcfa872fde`.

Rust module: `verification::roadmap::python::policy_positive`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Assert, all_satisfied, allowed, boolean, cgp_eligible, dict, empty, incomplete, may_reserve, modernize, over. Outputs/bindings: allowed, boolean, empty, incomplete, modernize, over.
Calls/effect boundaries: Assert, all_satisfied, cgp_eligible, dict, may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::root.body[0]::Expr

Source: `verification/roadmap/python/policy_positive.py:1`; AST `eaeba615df3b58adb49c804453aecda7a5dad307f60169b63153b7522cab0a34`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::root.body[1]::ImportFrom

Source: `verification/roadmap/python/policy_positive.py:7`; AST `7ab73ac3efcc2cd4b6897bfe1b4c6f9b2f718b4bd534767b42a35a63d7b5762b`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::root.body[2]::ImportFrom

Source: `verification/roadmap/python/policy_positive.py:8`; AST `7b70d2104182992758f38c4c6f3036e1e68dd46f22137951a6ae157257cc2aaf`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3]::FunctionDef

Source: `verification/roadmap/python/policy_positive.py:11`; AST `29d7ff923184059d3f4dc570f90142dab9baf4e54f6245cfee280dc8b1e33007`.

Rust module: `verification::roadmap::python::policy_positive`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Assert, all_satisfied, allowed, boolean, cgp_eligible, dict, empty, incomplete, may_reserve, modernize, over. Outputs/bindings: allowed, boolean, empty, incomplete, modernize, over.
Calls/effect boundaries: Assert, all_satisfied, cgp_eligible, dict, may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered FunctionDef evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[0]::Assign

Source: `verification/roadmap/python/policy_positive.py:12`; AST `94a425e89d69487c9fd21fe0c40dee84970ee9d60ca17f1e609417962c3bde41`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: may_reserve. Outputs/bindings: allowed.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[0].value::Call

Source: `verification/roadmap/python/policy_positive.py:12`; AST `bfd6e9bf4377452f55367e6d880c237b71ac73d9fde8cb3fa933493a09e537b8`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: may_reserve. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[1]::Expr

Source: `verification/roadmap/python/policy_positive.py:13`; AST `6db4b125589d2780c365becfac3aa72d43286748192aead40fb62e76a3bc9bf3`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Assert, allowed. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[1].value::Call

Source: `verification/roadmap/python/policy_positive.py:13`; AST `7f226342b84c6b7cf28cdf58ef5e708754c288d3316e98716491f599f6b444be`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Assert, allowed. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[2]::Assign

Source: `verification/roadmap/python/policy_positive.py:14`; AST `9d237b089d7dcccdfb91acbaa356976324151b51139c92ec0601b52c74614809`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: may_reserve. Outputs/bindings: over.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[2].value::Call

Source: `verification/roadmap/python/policy_positive.py:14`; AST `5a33ca4865985e47b3dcdd441e07ab0bd2db45c0544c01ed062a8a9b2a21ae46`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: may_reserve. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[3]::Expr

Source: `verification/roadmap/python/policy_positive.py:15`; AST `e31055fb054733b5790a136e3e8c67ea9017edb6ce69f908ed01756e93f59530`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Assert, over. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[3].value::Call

Source: `verification/roadmap/python/policy_positive.py:15`; AST `0699f207d1793faffb9317350101b661d96d926b029b55c395481df25aa6b01d`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Assert, over. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[4]::Assign

Source: `verification/roadmap/python/policy_positive.py:16`; AST `e59a80ba5a2fce1efe2cba19f3adfb0ac3d7d476fcefad3f1a8083311436c9b6`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: may_reserve. Outputs/bindings: boolean.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[4].value::Call

Source: `verification/roadmap/python/policy_positive.py:16`; AST `248fc8934134e0bf5b4a36372256f0a76a9bd2d0f17fd0a886a5827493194c66`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: may_reserve. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[5]::Expr

Source: `verification/roadmap/python/policy_positive.py:17`; AST `8f691c3953c7ca9ade9dbe6605a8b8addbc7bef7de5236191681b37124f55f44`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Assert, boolean. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[5].value::Call

Source: `verification/roadmap/python/policy_positive.py:17`; AST `d1ad7e5ea1560949f2e840bad029b6b48dcf2974f8c4354121d7353840e37a02`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Assert, boolean. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[6]::Assign

Source: `verification/roadmap/python/policy_positive.py:18`; AST `514d1e563504b1151a64b4027e2d8947822cecdf38c237d9da910a18cd7c5c54`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all_satisfied. Outputs/bindings: empty.
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[6].value::Call

Source: `verification/roadmap/python/policy_positive.py:18`; AST `082b9aa29713d8991733e3230cbd3e7fba8d6b0cb0864f276d260846edcaefed`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[7]::Expr

Source: `verification/roadmap/python/policy_positive.py:19`; AST `30d26ad620368637c79010ad928382d1d3062173b88ff020c9e6793cfcc47356`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Assert, empty. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[7].value::Call

Source: `verification/roadmap/python/policy_positive.py:19`; AST `26d4418d41394b15893da5e07840f387a7819f65ad01ccac2d0f5915c9d7d3e1`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Assert, empty. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[8]::Assign

Source: `verification/roadmap/python/policy_positive.py:20`; AST `079f299363826fe5a964c6cb9c8b260d333dcc44ebf741d02111622e7a250533`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all_satisfied. Outputs/bindings: incomplete.
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[8].value::Call

Source: `verification/roadmap/python/policy_positive.py:20`; AST `0cc7257bec9f2715cf6fa6b218825836ab225317e7be33188ae1c8917b4b8087`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[9]::Expr

Source: `verification/roadmap/python/policy_positive.py:21`; AST `c7e90ddae705b90d0e345587465fbfb66bb6cc3d3f5734ca91be4315f2f893de`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Assert, incomplete. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[9].value::Call

Source: `verification/roadmap/python/policy_positive.py:21`; AST `fcb4fffc479e583b39835ea3f5ac60a7b7a08fee555d6eac1e156e18e5ca36aa`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Assert, incomplete. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[10]::Assign

Source: `verification/roadmap/python/policy_positive.py:22`; AST `0ab96f1c579ce8dba31c8685218ce5715e8280611a0f7880836f45dd416b837c`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cgp_eligible, dict. Outputs/bindings: modernize.
Calls/effect boundaries: cgp_eligible, dict.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Assign evaluation at root.body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[10].value::Call

Source: `verification/roadmap/python/policy_positive.py:22`; AST `a4ec6d66d9a19b87df15994454e2583e968f0d3df3b20bd5ce732745e661ec92`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cgp_eligible, dict. Outputs/bindings: (none).
Calls/effect boundaries: cgp_eligible, dict.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[10].value.args[0]::Call

Source: `verification/roadmap/python/policy_positive.py:22`; AST `61a77424fd19dbd690f0c66643bcc2c29d65c3ee4ebbf06709992ef46bc257a8`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[11]::Expr

Source: `verification/roadmap/python/policy_positive.py:23`; AST `0b7f5aaa93a7d9c7c4fdd72c7549db0d2005bc65e30f49dc0658033201a1aa5f`.

Rust module: `verification::roadmap::python::policy_positive`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Assert, modernize. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Expr evaluation at root.body[3].body[11]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_positive.py::module::original_budget_and_completion::root.body[3].body[11].value::Call

Source: `verification/roadmap/python/policy_positive.py:23`; AST `61b806ca043fa54a5cb4189c84ff3082bc720a2a569d221f1dbbbec1c3970272`.

Rust module: `verification::roadmap::python::policy_positive`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Assert, modernize. Outputs/bindings: (none).
Calls/effect boundaries: Assert.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Call evaluation at root.body[3].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
