# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 9. Inventory digest: `356a32368a76d43e76130dd5ffff7070362be5326ecfd1cb29e90e4a9498e201`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## verification/roadmap/python/policy_negative.py::module::root::Module

Source: `verification/roadmap/python/policy_negative.py:1`; AST `0ab76165f97c2d6d5f9b801d9c475ff43d1b767a37ff06677b0d9a48d722550b`.

Rust module: `verification::roadmap::python::policy_negative`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Assert, allowed, may_reserve. Outputs/bindings: allowed.
Calls/effect boundaries: Assert, may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_negative.py::module::root.body[0]::Expr

Source: `verification/roadmap/python/policy_negative.py:1`; AST `74c8a360261e3e0c0af66178d516c74573feea379190b70b430f3da9c5fb4d29`.

Rust module: `verification::roadmap::python::policy_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_negative.py::module::root.body[1]::ImportFrom

Source: `verification/roadmap/python/policy_negative.py:6`; AST `7ab73ac3efcc2cd4b6897bfe1b4c6f9b2f718b4bd534767b42a35a63d7b5762b`.

Rust module: `verification::roadmap::python::policy_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_negative.py::module::root.body[2]::ImportFrom

Source: `verification/roadmap/python/policy_negative.py:7`; AST `46b4a2cc221e6da19ffc05ec2a7f910dae3a68ac2bfe92af1845519bce0dc856`.

Rust module: `verification::roadmap::python::policy_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_negative.py::module::deliberately_wrong_budget_assertion::root.body[3]::FunctionDef

Source: `verification/roadmap/python/policy_negative.py:10`; AST `d75072cd3a058c8336d86062df74c474af5391a49ade61fbdd88f1355e79f5cf`.

Rust module: `verification::roadmap::python::policy_negative`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Assert, allowed, may_reserve. Outputs/bindings: allowed.
Calls/effect boundaries: Assert, may_reserve.
Dependencies: agentinfra.roadmap_policy, nagini_contracts.contracts.

Invariants: Preserve ordered FunctionDef evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/python/policy_negative.py::module::deliberately_wrong_budget_assertion::root.body[3].body[0]::Assign

Source: `verification/roadmap/python/policy_negative.py:11`; AST `94a425e89d69487c9fd21fe0c40dee84970ee9d60ca17f1e609417962c3bde41`.

Rust module: `verification::roadmap::python::policy_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_negative.py::module::deliberately_wrong_budget_assertion::root.body[3].body[0].value::Call

Source: `verification/roadmap/python/policy_negative.py:11`; AST `bfd6e9bf4377452f55367e6d880c237b71ac73d9fde8cb3fa933493a09e537b8`.

Rust module: `verification::roadmap::python::policy_negative`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

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

## verification/roadmap/python/policy_negative.py::module::deliberately_wrong_budget_assertion::root.body[3].body[1]::Expr

Source: `verification/roadmap/python/policy_negative.py:12`; AST `bf7e3909b90e9371b949d91b6ba3944aa42fd0749398678ef63231fc8f96609f`.

Rust module: `verification::roadmap::python::policy_negative`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

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

## verification/roadmap/python/policy_negative.py::module::deliberately_wrong_budget_assertion::root.body[3].body[1].value::Call

Source: `verification/roadmap/python/policy_negative.py:12`; AST `d522608ebd2a0c182f88b82667f702f23be39de199c4ee03921fd7406af23de2`.

Rust module: `verification::roadmap::python::policy_negative`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

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
