# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 3. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/__init__.py::module::root::Module

Source: `infra/agentinfra/__init__.py:1`; AST `c642028ed687cadc086f3ad77e019eb25f119ae38ce4c7b1cf3fa7f84c06afee`.

Rust module: `infra::agentinfra::__init__`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: (none). Outputs/bindings: __version__.
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

Source: `infra/agentinfra/__init__.py:1`; AST `4798376a1a11938f834f17d22f560cac4348def94c4ea9a77f373097a9f3f4f4`.

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

Source: `infra/agentinfra/__init__.py:2`; AST `4cac6062f64f7ce9912cda034c1a509b94bcf8c8684cf72ef4147af257f5a6e0`.

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
