# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 5. Inventory digest: `41bbcaca0805d12a8b3afba25e0a8ba9c9cc32ddd2adf8085184122d1968ac88`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/__init__.py::module::root::Module

Source: `infra/agentinfra/__init__.py:1`; AST `806f1488c94cb39127f27a9b28c267f869319737851458bf8d6bc6236830130e`.

Rust module: `infra::agentinfra::__init__`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: (none). Outputs/bindings: INTERFACE_VERSION, LEGACY_DESTINY_VERSION, __version__.
Calls/effect boundaries: (none).
Dependencies: (none).

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/__init__.py::module::root.body[0]::Expr

Source: `infra/agentinfra/__init__.py:1`; AST `915af1ddf4b972423a0c0e79c4cbc5cfc0e7688e056af31ec65c38babf4b348d`.

Rust module: `infra::agentinfra::__init__`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: (none).

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/__init__.py::module::root.body[1]::Assign

Source: `infra/agentinfra/__init__.py:2`; AST `8acc898b6c451fb84e1b6102cb6e5d70a9554ac3cad2561b367362ac43438383`.

Rust module: `infra::agentinfra::__init__`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: __version__.
Calls/effect boundaries: (none).
Dependencies: (none).

Invariants: Preserve ordered Assign evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/__init__.py::module::root.body[2]::Assign

Source: `infra/agentinfra/__init__.py:3`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::__init__`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: (none).

Invariants: Preserve ordered Assign evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/__init__.py::module::root.body[3]::Assign

Source: `infra/agentinfra/__init__.py:4`; AST `5b96fff6759d5d1dd1b0f040bd2b555743e57b1c886ce0d161b516f9d501dc97`.

Rust module: `infra::agentinfra::__init__`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: LEGACY_DESTINY_VERSION.
Calls/effect boundaries: (none).
Dependencies: (none).

Invariants: Preserve ordered Assign evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
