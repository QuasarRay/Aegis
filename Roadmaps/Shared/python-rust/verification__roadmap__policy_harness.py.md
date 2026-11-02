# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 42. Inventory digest: `9e5c819456569b8b11d5cd02b655491bc75554eec5bdc096aa8cc378a0025a54`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## verification/roadmap/policy_harness.py::module::root::Module

Source: `verification/roadmap/policy_harness.py:1`; AST `2f26a238626ca2218d8a1b041515e40460b3a9d72fcf8a5ada738133316f309e`.

Rust module: `verification::roadmap::policy_harness`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, ROOT, __file__, __name__, all, all_satisfied, allowed, cgp_eligible, checked, dict, finite_policy_checks, int, limit, mapping, may_reserve, min, print, product, range, requested, reserved, states, str, sys, used, x, zip. Outputs/bindings: ROOT, allowed, checked, limit, mapping, requested, reserved, states, used, x.
Calls/effect boundaries: Path, Path(__file__).resolve, all, all_satisfied, cgp_eligible, dict, finite_policy_checks, may_reserve, min, print, product, range, str, sys.path.insert, zip.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[0]::Expr

Source: `verification/roadmap/policy_harness.py:1`; AST `f2c2072077b7a93ba788802110fcec36f58ead8c03e59b3742e295fd34e5d2fe`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[1]::ImportFrom

Source: `verification/roadmap/policy_harness.py:6`; AST `1e3ac448cf1ae2b666f4fb69984807dd0fde9d2059571a6e9f3499fc2b8c7ee5`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[2]::ImportFrom

Source: `verification/roadmap/policy_harness.py:7`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[3]::Import

Source: `verification/roadmap/policy_harness.py:8`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[4]::Assign

Source: `verification/roadmap/policy_harness.py:10`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[4].value.value.value::Call

Source: `verification/roadmap/policy_harness.py:10`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[4].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[4].value.value.value.func.value::Call

Source: `verification/roadmap/policy_harness.py:10`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[4].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[5]::Expr

Source: `verification/roadmap/policy_harness.py:11`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[5].value::Call

Source: `verification/roadmap/policy_harness.py:11`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[5].value.args[1]::Call

Source: `verification/roadmap/policy_harness.py:11`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[6]::ImportFrom

Source: `verification/roadmap/policy_harness.py:12`; AST `d254018eac85f387b15c4db7656717b5791ae6e77ada84a791080a8690bd94d8`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7]::FunctionDef

Source: `verification/roadmap/policy_harness.py:15`; AST `93b1e8b749fec176d67e5537d02ec03b21aca0556b7df31288fe17f7ebb33243`.

Rust module: `verification::roadmap::policy_harness`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, all_satisfied, allowed, cgp_eligible, checked, dict, int, limit, mapping, may_reserve, min, product, range, requested, reserved, states, used, x, zip. Outputs/bindings: allowed, checked, limit, mapping, requested, reserved, states, used, x.
Calls/effect boundaries: all, all_satisfied, cgp_eligible, dict, may_reserve, min, product, range, zip.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[0]::Assign

Source: `verification/roadmap/policy_harness.py:16`; AST `e3ebabfb7daa41cb8fb2d409112906f0ff125e4864acfb82f09dd71b95b5390c`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: checked.
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1]::For

Source: `verification/roadmap/policy_harness.py:17`; AST `3d9caab4dc8a4f93c2115f7c76459b5a71060f01f6b88b1e9091899cdd1f11ea`.

Rust module: `verification::roadmap::policy_harness`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: allowed, limit, may_reserve, min, product, range, requested, reserved, used. Outputs/bindings: allowed, checked, limit, requested, reserved, used.
Calls/effect boundaries: may_reserve, min, product, range.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered For evaluation at root.body[7].body[1]; no call, error or mutation may be omitted. Iteration: (used, reserved, requested, limit) in product(range(-1, 6), repeat=4)
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].iter::Call

Source: `verification/roadmap/policy_harness.py:17`; AST `ca8168b7112d795b4504f6a6f89b181cd6b3cc094455d0755434fa229129997d`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: product, range. Outputs/bindings: (none).
Calls/effect boundaries: product, range.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].iter.args[0]::Call

Source: `verification/roadmap/policy_harness.py:17`; AST `0f7d878e695e75960f882fa94387ddfb28b360f27d84fa2d8fccc790a14665b1`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].body[0]::Assign

Source: `verification/roadmap/policy_harness.py:18`; AST `29d72ed819c169533e9fe8a22c40e81aac54031c87fab48cb393f8656d050fe6`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: limit, may_reserve, requested, reserved, used. Outputs/bindings: allowed.
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].body[0].value::Call

Source: `verification/roadmap/policy_harness.py:18`; AST `0ddd3192576f45eb3303f3e6bc303f8d52f72a1553bf81910dd7b64533d49cdd`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: limit, may_reserve, requested, reserved, used. Outputs/bindings: (none).
Calls/effect boundaries: may_reserve.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].body[1]::Assert

Source: `verification/roadmap/policy_harness.py:19`; AST `e5f5825fddd5305be067b81858b31660597c21d6029c17eabeaebd022cc9110d`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allowed, limit, min, reserved, used. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assert evaluation at root.body[7].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].body[1].test.values[1].left::Call

Source: `verification/roadmap/policy_harness.py:19`; AST `212f4c3d058756fff806504666c10fb964ca8e1b05062868e24cdf942f196958`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: limit, min, reserved, used. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].body[2]::Assert

Source: `verification/roadmap/policy_harness.py:20`; AST `188e61716ce067b9610783f73fe2c57c78ec9565c07a8878ca73d0903f7d37b9`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allowed, limit, requested, reserved, used. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assert evaluation at root.body[7].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[1].body[3]::AugAssign

Source: `verification/roadmap/policy_harness.py:21`; AST `41b2efce71140ea410d7dd85f0008dd5290e85961061ddabf3de98a46f9c57c5`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: checked.
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered AugAssign evaluation at root.body[7].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2]::For

Source: `verification/roadmap/policy_harness.py:22`; AST `c3b81aa3843413a43fe72616db768c12b0100b453cbf1db0bec18b6de7c36db9`.

Rust module: `verification::roadmap::policy_harness`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: all, cgp_eligible, dict, mapping, product, states, x, zip. Outputs/bindings: checked, mapping, states, x.
Calls/effect boundaries: all, cgp_eligible, dict, product, zip.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered For evaluation at root.body[7].body[2]; no call, error or mutation may be omitted. Iteration: states in product(('PROJECT_COMPLETE', 'IMPLEMENTATION_READY', 'DOMAIN_VERIFIED', 'UNKNOWN'), repeat=3)
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].iter::Call

Source: `verification/roadmap/policy_harness.py:22`; AST `bd006df48da4f28a8027e7cb5086fd83d60e16d2b81bd3f961d34574823301eb`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: product. Outputs/bindings: (none).
Calls/effect boundaries: product.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[0]::Assign

Source: `verification/roadmap/policy_harness.py:23`; AST `a8b87ab421b0c7bf6a5120355fbf8aef462f4eae2d225d93c5779ddd9eecad7b`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, states, zip. Outputs/bindings: mapping.
Calls/effect boundaries: dict, zip.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[0].value::Call

Source: `verification/roadmap/policy_harness.py:23`; AST `6eb6b570752805b1989fcdb2233efa4613c63da315b31095848c6e4402eaccde`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, states, zip. Outputs/bindings: (none).
Calls/effect boundaries: dict, zip.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[0].value.args[0]::Call

Source: `verification/roadmap/policy_harness.py:23`; AST `88cac87a6c27cc20e82938c9d3dc162c9e30aeb61c255b70d7a5c10826259828`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: states, zip. Outputs/bindings: (none).
Calls/effect boundaries: zip.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[1]::Assert

Source: `verification/roadmap/policy_harness.py:24`; AST `418de31e82fbf9014b0b5037e8e868e2bd24cd94f040ddc70e070a62bd9b79ba`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, cgp_eligible, mapping, states, x. Outputs/bindings: x.
Calls/effect boundaries: all, cgp_eligible.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assert evaluation at root.body[7].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[1].test.left::Call

Source: `verification/roadmap/policy_harness.py:24`; AST `3b60870acf700be9ec5f57d2ecfab94ece4685abcc459d58daa74d539abacb4d`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cgp_eligible, mapping. Outputs/bindings: (none).
Calls/effect boundaries: cgp_eligible.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[1].test.comparators[0]::Call

Source: `verification/roadmap/policy_harness.py:24`; AST `c41163a6715f30838ad6eecb638140c40d96f4034b034b81e8b7f7621cf3ffb8`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, states, x. Outputs/bindings: x.
Calls/effect boundaries: all.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[1].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[1].test.comparators[0].args[0]::GeneratorExp

Source: `verification/roadmap/policy_harness.py:24`; AST `d2c7e77f482e2e840f0e63c6688a7c2fcf1c5932f5116eb68ebb51be4933d172`.

Rust module: `verification::roadmap::policy_harness`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: states, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[7].body[2].body[1].test.comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[2].body[2]::AugAssign

Source: `verification/roadmap/policy_harness.py:25`; AST `41b2efce71140ea410d7dd85f0008dd5290e85961061ddabf3de98a46f9c57c5`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: checked.
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered AugAssign evaluation at root.body[7].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[3]::Assert

Source: `verification/roadmap/policy_harness.py:26`; AST `a20f6def35b599e0880b517c0b2848ca027b0098e0f2a38fa768f5e5f711d0a1`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assert evaluation at root.body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[3].test.operand::Call

Source: `verification/roadmap/policy_harness.py:26`; AST `082b9aa29713d8991733e3230cbd3e7fba8d6b0cb0864f276d260846edcaefed`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[4]::Assert

Source: `verification/roadmap/policy_harness.py:27`; AST `4d080e12f52ecfac7e00cb04ccb20f13f51b706120e6cca9f9c5774bfb39f01c`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Assert evaluation at root.body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[4].test.operand::Call

Source: `verification/roadmap/policy_harness.py:27`; AST `6b9d221f500f5278067bcce421a80bed61418077bbb8424abdae2d3fc683e6ab`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all_satisfied. Outputs/bindings: (none).
Calls/effect boundaries: all_satisfied.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::finite_policy_checks::root.body[7].body[5]::Return

Source: `verification/roadmap/policy_harness.py:28`; AST `20596f43d89c346716f53c0dab8a4f35a110ea9de038aa73f84f72674edfb4cf`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Return evaluation at root.body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[8]::If

Source: `verification/roadmap/policy_harness.py:31`; AST `1fbcedff94f87a4b18cd7352c9ad334394982b3a6320c2eda488c91a23e2596f`.

Rust module: `verification::roadmap::policy_harness`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, finite_policy_checks, print. Outputs/bindings: (none).
Calls/effect boundaries: finite_policy_checks, print.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered If evaluation at root.body[8]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[8].body[0]::Expr

Source: `verification/roadmap/policy_harness.py:32`; AST `f9445d17c6f1522aaf222799bab7e0202d5510144727f66bd3c9edc6bf464264`.

Rust module: `verification::roadmap::policy_harness`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: finite_policy_checks, print. Outputs/bindings: (none).
Calls/effect boundaries: finite_policy_checks, print.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[8].body[0].value::Call

Source: `verification/roadmap/policy_harness.py:32`; AST `0b496c7080952b95e22d23359b0f5baa778aa5918599fff00bad2ca0c693634a`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finite_policy_checks, print. Outputs/bindings: (none).
Calls/effect boundaries: finite_policy_checks, print.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## verification/roadmap/policy_harness.py::module::root.body[8].body[0].value.args[0].values[0].value::Call

Source: `verification/roadmap/policy_harness.py:32`; AST `73e572635d308adeb5692ac8b1f9588c866f631c882558443a56468e3f76989e`.

Rust module: `verification::roadmap::policy_harness`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finite_policy_checks. Outputs/bindings: (none).
Calls/effect boundaries: finite_policy_checks.
Dependencies: agentinfra.roadmap_policy, itertools, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
