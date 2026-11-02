# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 14. Inventory digest: `98c53be4b2d3aeb43bcc01ef3d9cfa9f726f7165d631e91bf82628e55cda62cd`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/cli.py::module::root::Module

Source: `infra/agentinfra/cli.py:1`; AST `4ab3df945609c3356a74b8a7784a99eb4a7a76bc4cd1534cc83e5165cdd88e8a`.

Rust module: `infra::agentinfra::cli`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: argv, families, legacy_main, list, roadmap_main, sys. Outputs/bindings: argv, families.
Calls/effect boundaries: legacy_main, list, roadmap_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::root.body[0]::Expr

Source: `infra/agentinfra/cli.py:1`; AST `265a13662fc1593f1294aa6482477c53f2ad5a1d79890bfbc28bff45fe7d2dc8`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::root.body[1]::Import

Source: `infra/agentinfra/cli.py:2`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2]::FunctionDef

Source: `infra/agentinfra/cli.py:5`; AST `67aea91731d1607359569a63de05a370920560d3f2591c912b4626ce85d2af1e`.

Rust module: `infra::agentinfra::cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: argv, families, legacy_main, list, roadmap_main, sys. Outputs/bindings: argv, families.
Calls/effect boundaries: legacy_main, list, roadmap_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[0]::Assign

Source: `infra/agentinfra/cli.py:6`; AST `65f331559ab94a4c351b5ea5468c3da1d8953d20dce96c79d278eb4423f68507`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, list, sys. Outputs/bindings: argv.
Calls/effect boundaries: list.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[0].value::Call

Source: `infra/agentinfra/cli.py:6`; AST `2d95692f63033bad593f14c136ab335d2bcf2c12755b4f5d0ba4880d1b26ec90`.

Rust module: `infra::agentinfra::cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, list, sys. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Call evaluation at root.body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[1]::Assign

Source: `infra/agentinfra/cli.py:7`; AST `d7656c484f07cb9c85581b4e0365d5712e548c2f7e000675815fb34198381a3a`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: families.
Calls/effect boundaries: (none).
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Assign evaluation at root.body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[2]::If

Source: `infra/agentinfra/cli.py:8`; AST `f63256db33d34f361c3762dd0b64e118d9587e58fce5c507ebb3b8e03e302773`.

Rust module: `infra::agentinfra::cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: argv, families, roadmap_main. Outputs/bindings: (none).
Calls/effect boundaries: roadmap_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered If evaluation at root.body[2].body[2]; no call, error or mutation may be omitted. Condition: argv and (argv[0] in families or argv[0] == '--root')
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[2].body[0]::ImportFrom

Source: `infra/agentinfra/cli.py:9`; AST `6b979d7198244e63128e1d9113cfb2efc2926ed7e9467496f3837c01687b70d9`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[2].body[1]::Return

Source: `infra/agentinfra/cli.py:10`; AST `e27140d689cf28c7627497b0cb0323530d6d43fd109a0fb47bcd08a0ca33f76a`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, roadmap_main. Outputs/bindings: (none).
Calls/effect boundaries: roadmap_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Return evaluation at root.body[2].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[2].body[1].value::Call

Source: `infra/agentinfra/cli.py:10`; AST `46f034fa39f11b472048bf2f9a05c3b25626fb309fe2c473c8140cc6854ea376`.

Rust module: `infra::agentinfra::cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, roadmap_main. Outputs/bindings: (none).
Calls/effect boundaries: roadmap_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Call evaluation at root.body[2].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[3]::ImportFrom

Source: `infra/agentinfra/cli.py:11`; AST `1608060c2dc9977afa2c6f6835d99cc108442dc95be9bb36c8197bb2ec44971e`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[4]::Return

Source: `infra/agentinfra/cli.py:12`; AST `6e85688329c505820841d84c7efe4ce5e6fe77c4822b4ded755e707dd30098f9`.

Rust module: `infra::agentinfra::cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, legacy_main. Outputs/bindings: (none).
Calls/effect boundaries: legacy_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Return evaluation at root.body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/cli.py::module::main::root.body[2].body[4].value::Call

Source: `infra/agentinfra/cli.py:12`; AST `99d4424ce5d8be7a79d73ee8565729ea768e1e5ffe53eae776102ce92c127853`.

Rust module: `infra::agentinfra::cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, legacy_main. Outputs/bindings: (none).
Calls/effect boundaries: legacy_main.
Dependencies: destiny, roadmap_cli, sys.

Invariants: Preserve ordered Call evaluation at root.body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
