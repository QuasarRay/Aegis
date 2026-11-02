# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 100. Inventory digest: `7be18a013278a637c2095f5eaf5120b643996cef3b321324774938b38c4ded23`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/roadmap_native.py::module::root::Module

Source: `scripts/roadmap_native.py:1`; AST `16746ce7fbc1eb15a5a5551e6ca7a00e765dde26b643fe3ec4145639970cdaf0`.

Rust module: `scripts::roadmap_native`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, NativeGoalAdapter, NativeRpc, Path, ProjectAdapter, ROOT, WorkspaceLease, __doc__, __file__, __name__, argparse, args, artifacts, atomic_write_json, calls, candidate, capability_snapshot, collect, compile_roadmaps, compiled, completion_guard, confined_path, dict, digest, directory, execution, file_binding, goal, list, main, name, native, observe_goal, observe_plan, output, parser, path, plan, print, protocol, read_json, record, refusal, require, result, root, root_turns, rpc, snapshot, str, sys, target, value. Outputs/bindings: ROOT, args, artifacts, calls, compiled, completion_guard, directory, execution, goal, name, native, parser, path, plan, record, result, root_turns, rpc, snapshot, target, value.
Calls/effect boundaries: ContractError, NativeGoalAdapter, NativeGoalAdapter(root, protocol).prepare, NativeRpc, Path, Path(__file__).resolve, ProjectAdapter, ProjectAdapter(root).read, WorkspaceLease, WorkspaceLease(root).qualify, argparse.ArgumentParser, artifacts.values, atomic_write_json, capability_snapshot, collect, compile_roadmaps, confined_path, digest, file_binding, list, main, observe_goal, observe_plan, parser.add_argument, parser.parse_args, path.as_posix, print, read_json, require, rpc.turns, rpc.watch, str, sys.path.insert, target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[0]::Expr

Source: `scripts/roadmap_native.py:1`; AST `a7ca54c73878d5c4b496ab07f81a741bfe31fa03d1c322641bae0ea57214a3f2`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[1]::ImportFrom

Source: `scripts/roadmap_native.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[2]::Import

Source: `scripts/roadmap_native.py:4`; AST `356e6775028bc09e699d8b986887aaebc5e3e8e414a507fe911e3ba7da1264d9`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[3]::ImportFrom

Source: `scripts/roadmap_native.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[4]::Import

Source: `scripts/roadmap_native.py:6`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[5]::Assign

Source: `scripts/roadmap_native.py:8`; AST `7efba0850e8eeaef93e5c3de6b7d47927a3e4bde0e8161dfb3d03fc10717d3c2`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[5].value.value.value::Call

Source: `scripts/roadmap_native.py:8`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[5].value.value.value.func.value::Call

Source: `scripts/roadmap_native.py:8`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[6]::Expr

Source: `scripts/roadmap_native.py:9`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[6].value::Call

Source: `scripts/roadmap_native.py:9`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[6].value.args[1]::Call

Source: `scripts/roadmap_native.py:9`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[6].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[7]::ImportFrom

Source: `scripts/roadmap_native.py:10`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[8]::ImportFrom

Source: `scripts/roadmap_native.py:11`; AST `3b1f096af51b088fc8db1bcf6f2df1bf3d578425197b6db1f15386d0b11cf950`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[9]::ImportFrom

Source: `scripts/roadmap_native.py:12`; AST `7e9c3f5290a99e55259b83ed615988e11578a991178ada162c503777b0b68347`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[10]::ImportFrom

Source: `scripts/roadmap_native.py:13`; AST `615d06ea4a69d66e3d8c64e850f39f7c3518794a7ffd01cdc39971345d086076`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[11]::ImportFrom

Source: `scripts/roadmap_native.py:14`; AST `126a181471f1f7f5135676c50f2d495e40a0d7783e6cb63eeb6bed1d8f8d15e3`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[12]::ImportFrom

Source: `scripts/roadmap_native.py:15`; AST `b6c26cc525d5df9f1ece9ea002acbd092066251227fdcd430287e38c6b1098bd`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[13]::ImportFrom

Source: `scripts/roadmap_native.py:16`; AST `860451982277a7f5c435b7fc36a0eb328ab43d13fe8858ce9091906ca6dcc079`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14]::FunctionDef

Source: `scripts/roadmap_native.py:19`; AST `acd70e0fe90640ba00ffe037b64042c5fbbe683d77f851c4616d1c2b606be33a`.

Rust module: `scripts::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, NativeGoalAdapter, NativeRpc, Path, ProjectAdapter, WorkspaceLease, artifacts, atomic_write_json, calls, candidate, capability_snapshot, compile_roadmaps, compiled, completion_guard, confined_path, dict, digest, directory, execution, file_binding, goal, list, name, native, observe_goal, observe_plan, output, path, plan, protocol, read_json, record, refusal, require, root, root_turns, rpc, snapshot, str, target, value. Outputs/bindings: artifacts, calls, compiled, completion_guard, directory, execution, goal, name, native, path, plan, record, root_turns, rpc, snapshot, target, value.
Calls/effect boundaries: ContractError, NativeGoalAdapter, NativeGoalAdapter(root, protocol).prepare, NativeRpc, Path, ProjectAdapter, ProjectAdapter(root).read, WorkspaceLease, WorkspaceLease(root).qualify, artifacts.values, atomic_write_json, capability_snapshot, compile_roadmaps, confined_path, digest, file_binding, list, observe_goal, observe_plan, path.as_posix, read_json, require, rpc.turns, rpc.watch, str, target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[0]::Assign

Source: `scripts/roadmap_native.py:20`; AST `afbfde35d4c7d3cc97dc305cc1f264cb71c1c2255447e09f03f654a738892641`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, root. Outputs/bindings: record.
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[0].value::Call

Source: `scripts/roadmap_native.py:20`; AST `aebfe9f0e99b7598f3da209b858f5afb31082b520cf878a8582e3946d9cfd8f6`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[0].value.func.value::Call

Source: `scripts/roadmap_native.py:20`; AST `a885979b048414ab9ab482a4aaa51e20efe2db175d6aaf5096c07c6e15434558`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[1]::Assign

Source: `scripts/roadmap_native.py:21`; AST `e0e9d6aaa5cae6167af8fa88e07a13a439f9b554d86164a022da676b042fdb2e`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: execution.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[2]::Assign

Source: `scripts/roadmap_native.py:22`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[2].value::Call

Source: `scripts/roadmap_native.py:22`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[3]::Assign

Source: `scripts/roadmap_native.py:23`; AST `dd73c7a810014f44f1c07e2377447ab88afa8489fa308129b41b983aaddbeb53`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, execution, root. Outputs/bindings: native.
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).qualify.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[3].value::Call

Source: `scripts/roadmap_native.py:23`; AST `50f3341f9674ca21002aa0bf5835affe5fc259fb47b984ed16d4b153234da8aa`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, execution, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).qualify.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[3].value.func.value::Call

Source: `scripts/roadmap_native.py:23`; AST `9af565e67ae5d334b545886bccb7b0f27fb8d8189b6644c9267610cbdb6cc4e6`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[4]::Expr

Source: `scripts/roadmap_native.py:24`; AST `6f6f39a67dbff186653b8a327072616f4315b5814d7ec5358802efa38507d308`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, native, protocol, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[4].value::Call

Source: `scripts/roadmap_native.py:24`; AST `eff5959b80484926580fc92af745ba820589057a20607789a589c3dcbb87c773`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, native, protocol, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5]::With

Source: `scripts/roadmap_native.py:27`; AST `8946159b28c0f163c9a670813dae86f857ca2e7e0ae5dc023f1a5d821f688492`.

Rust module: `scripts::roadmap_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: NativeRpc, capability_snapshot, compiled, execution, goal, list, native, observe_goal, observe_plan, protocol, root, rpc. Outputs/bindings: calls, goal, plan, root_turns, rpc, snapshot.
Calls/effect boundaries: NativeRpc, capability_snapshot, list, observe_goal, observe_plan, rpc.turns, rpc.watch.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered With evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].items[0].context_expr::Call

Source: `scripts/roadmap_native.py:27`; AST `fa7e59cfe755aa9510090de85e9186019526ab9716fbf7155617ede338244b46`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: NativeRpc, protocol, root. Outputs/bindings: (none).
Calls/effect boundaries: NativeRpc.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[0]::Expr

Source: `scripts/roadmap_native.py:28`; AST `42b2fbbb89c2e848419078126209bc01a11a98415c23ba68ab0566d1de7f51a0`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native, rpc. Outputs/bindings: (none).
Calls/effect boundaries: rpc.watch.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[0].value::Call

Source: `scripts/roadmap_native.py:28`; AST `c56aa1b2c67dc62500e4eec2e83ed917e2fabbd3b6987204ab24427654de96f2`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native, rpc. Outputs/bindings: (none).
Calls/effect boundaries: rpc.watch.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[1]::Assign

Source: `scripts/roadmap_native.py:29`; AST `beea506551a28d42267621c4c40bf2c5ec13066239ded492a317ea46c06d051b`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, execution, observe_goal, root, rpc. Outputs/bindings: goal.
Calls/effect boundaries: observe_goal.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[1].value::Call

Source: `scripts/roadmap_native.py:29`; AST `2f5c9bfe8b999d69e55826f36a19152f06f5b6d300f9b960a2e4e78a4ff1e24d`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, execution, observe_goal, root, rpc. Outputs/bindings: (none).
Calls/effect boundaries: observe_goal.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[2]::Assign

Source: `scripts/roadmap_native.py:30`; AST `dee3339254ed1db9ef8299bda471085358f201b377448bd9584411e087925f1b`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, execution, observe_plan, root, rpc. Outputs/bindings: plan.
Calls/effect boundaries: observe_plan.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[2].value::Call

Source: `scripts/roadmap_native.py:30`; AST `577c4ee85516a1956d4d38e521e61045ecf0687ed19b8366f161209bdcc7db4e`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, execution, observe_plan, root, rpc. Outputs/bindings: (none).
Calls/effect boundaries: observe_plan.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[3]::Assign

Source: `scripts/roadmap_native.py:31`; AST `458054f0abe771c72986d55bd940951078b571c3ec2b30c306ca847552f9c7cf`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: goal, rpc. Outputs/bindings: root_turns.
Calls/effect boundaries: rpc.turns.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[3].value::Call

Source: `scripts/roadmap_native.py:31`; AST `8b20a9c5992dea49985cb1f2039e613298d6f7ba33b221b981cab3d7904596f7`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal, rpc. Outputs/bindings: (none).
Calls/effect boundaries: rpc.turns.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[4]::Assign

Source: `scripts/roadmap_native.py:32`; AST `2be51e2095c7d4e5e647768d14270611fa3ef8606c194f235e3fc18f26a7666f`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: capability_snapshot, native, root, rpc. Outputs/bindings: snapshot.
Calls/effect boundaries: capability_snapshot.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[4].value::Call

Source: `scripts/roadmap_native.py:32`; AST `46959238aad2b86f64000a3f9f9938fd1b4356018c9494ffb2a8249919901496`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: capability_snapshot, native, root, rpc. Outputs/bindings: (none).
Calls/effect boundaries: capability_snapshot.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[5]::Assign

Source: `scripts/roadmap_native.py:33`; AST `fb3066d09fc2913413b9b1d9dc9f08ec38d56d07692c81d265456866a8340d2e`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, rpc. Outputs/bindings: calls.
Calls/effect boundaries: list.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[5].body[5].value::Call

Source: `scripts/roadmap_native.py:33`; AST `95fa7e5901191a9224a3cee420161f0a04190f087324a111bf483746c33946a1`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, rpc. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6]::Try

Source: `scripts/roadmap_native.py:34`; AST `d762db9f86fc177fc76551da0e05a614d90dbde777f89eaf568cd4723c904e0b`.

Rust module: `scripts::roadmap_native`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ContractError, NativeGoalAdapter, protocol, refusal, root, str. Outputs/bindings: completion_guard.
Calls/effect boundaries: ContractError, NativeGoalAdapter, NativeGoalAdapter(root, protocol).prepare, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Try evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].body[0]::Expr

Source: `scripts/roadmap_native.py:35`; AST `03d31c829a5d48e792790080e62d95506d6ceebf729492fa2340c2ab1db0f11c`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: NativeGoalAdapter, protocol, root. Outputs/bindings: (none).
Calls/effect boundaries: NativeGoalAdapter, NativeGoalAdapter(root, protocol).prepare.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].body[0].value::Call

Source: `scripts/roadmap_native.py:35`; AST `50ecad8def0107a08b21186ec84d1bd92f9399b322912c68605b0579a1fe2305`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: NativeGoalAdapter, protocol, root. Outputs/bindings: (none).
Calls/effect boundaries: NativeGoalAdapter, NativeGoalAdapter(root, protocol).prepare.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].body[0].value.func.value::Call

Source: `scripts/roadmap_native.py:35`; AST `c19f32afa54408790259049da47e4d0202cc671aff637e1b1791115551229f41`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: NativeGoalAdapter, protocol, root. Outputs/bindings: (none).
Calls/effect boundaries: NativeGoalAdapter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].handlers[0]::ExceptHandler

Source: `scripts/roadmap_native.py:36`; AST `292df57f298a878f8c314e86bc355976eba45385827bd961b9b6200feeeb12e6`.

Rust module: `scripts::roadmap_native`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ContractError, refusal, str. Outputs/bindings: completion_guard.
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[6].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].handlers[0].body[0]::Assign

Source: `scripts/roadmap_native.py:37`; AST `7ca64472c7a9f82afc1a412dd00dc3b62b327b0a33751d2118cca73b8be3b006`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: refusal, str. Outputs/bindings: completion_guard.
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].handlers[0].body[0].value.values[1]::Call

Source: `scripts/roadmap_native.py:37`; AST `f96319207a092836c898d994ad5b662104e78e8c5b90d88193b481e84a9f3b93`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: refusal, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].handlers[0].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].orelse[0]::Raise

Source: `scripts/roadmap_native.py:39`; AST `b82725250dd9249374b7cb221ba4575ac7d08236ca335885efbb41ee04e54582`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[6].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[6].orelse[0].exc::Call

Source: `scripts/roadmap_native.py:39`; AST `32775d9511031d890ae7052649a9bfc10900e8f501ee28010fb3a40804031a4a`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].orelse[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[7]::Assign

Source: `scripts/roadmap_native.py:40`; AST `cf011820d3a49f553a0288352b19ca44e83c6411ec31e677247b58390d2adb16`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, output. Outputs/bindings: directory.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[7].value.value::Call

Source: `scripts/roadmap_native.py:40`; AST `d17869c6f354df543cf78a1fc81a8b860bf9ce6a9291e5761f26df3ba400ea7e`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, output. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[8]::Assign

Source: `scripts/roadmap_native.py:41`; AST `1fe413f8bcc4ccd57c20277d66b7386de02d9cfbd422a1a841ce0acfaa68d956`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: artifacts.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9]::For

Source: `scripts/roadmap_native.py:42`; AST `d00cb2816096c8988f37ef7dbfb47fea1c236fc63f3d148092983854ec589244`.

Rust module: `scripts::roadmap_native`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: artifacts, atomic_write_json, calls, completion_guard, confined_path, digest, directory, file_binding, goal, name, native, path, plan, read_json, require, root, root_turns, snapshot, target, value. Outputs/bindings: name, path, target, value.
Calls/effect boundaries: atomic_write_json, confined_path, digest, file_binding, path.as_posix, read_json, require, target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered For evaluation at root.body[14].body[9]; no call, error or mutation may be omitted. Iteration: (name, value) in (('goal-binding', goal), ('plan-observation', plan), ('capability-snapshot', snapshot), ('rpc-observations', {'schema': 1, 'calls': calls, 'root_turns': root_turns, 'completion_guard': completion_guard}), ('active-host', native))
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[0]::Assign

Source: `scripts/roadmap_native.py:45`; AST `642b5b07e5ad654962ad8e84655cd8ab8270a1e85a22ddcba763a6f92a43aaff`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, directory, name, value. Outputs/bindings: path.
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[0].value.right.left.right::Call

Source: `scripts/roadmap_native.py:45`; AST `f5478a66fd3247b8968c1306f6cc686ba6a06ab0db4348065f96da8baff25481`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, value. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[0].value.right.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[1]::Assign

Source: `scripts/roadmap_native.py:46`; AST `119f43902858e92131526cd5ce22a2fd1548cfe1f94372cdc89258fc7c25bc0c`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, path, root. Outputs/bindings: target.
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[1].value::Call

Source: `scripts/roadmap_native.py:46`; AST `b98e71315974837f2feb88621658a1aeab5d2a65661950f37123496ad43be4dc`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2]::If

Source: `scripts/roadmap_native.py:47`; AST `b6ade5df590cc5888b43528c6039065d3ae4aa21ce5315a1935f0af610b1f53a`.

Rust module: `scripts::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: atomic_write_json, read_json, require, root, target, value. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, read_json, require, target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered If evaluation at root.body[14].body[9].body[2]; no call, error or mutation may be omitted. Condition: target.exists()
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2].test::Call

Source: `scripts/roadmap_native.py:47`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2].body[0]::Expr

Source: `scripts/roadmap_native.py:48`; AST `7670b870acc5dc4240e58b42d9f908bae144c7f1470adcb0a2ad6ecc60f9d62e`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, require, target, value. Outputs/bindings: (none).
Calls/effect boundaries: read_json, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2].body[0].value::Call

Source: `scripts/roadmap_native.py:48`; AST `6ff0e061704ef2daafee585d01ae95ca6947b616ec8184c30f3ef05d24468147`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, require, target, value. Outputs/bindings: (none).
Calls/effect boundaries: read_json, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2].body[0].value.args[0].left::Call

Source: `scripts/roadmap_native.py:48`; AST `e295b18879a1dcd4575e64d13dfdae82fdf58c8267dc659e2fbe19c2f441c322`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, target. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[2].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2].orelse[0]::Expr

Source: `scripts/roadmap_native.py:50`; AST `c45db436b5b93b5c9b95354adab681099664c5e8ce8c6df7d736ddd85768a5c1`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, root, target, value. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9].body[2].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[2].orelse[0].value::Call

Source: `scripts/roadmap_native.py:50`; AST `170efcb4dc3831d0ed051bf63199b7d2edef2168eec9220592d94ee3b7291f8e`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, root, target, value. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[2].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[3]::Assign

Source: `scripts/roadmap_native.py:51`; AST `ec09f6633dc7081e27d0d0fdc68fa467c07558637d88174e367b2898aab2480f`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, file_binding, name, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[3].value::Call

Source: `scripts/roadmap_native.py:51`; AST `72bd3a939cadd524151c0a6ddc0f86b0c48e80d76e42aaccfea40211cda28285`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[9].body[3].value.args[1]::Call

Source: `scripts/roadmap_native.py:51`; AST `316aa3c00160481aca41ecff6f0f8ffe1060e3ee9b716034cc4fb2dc976bc855`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[10]::Return

Source: `scripts/roadmap_native.py:52`; AST `0774983f7a161609ee311b04b538fd2edb6904079e9b871a5ad74568f669b3b7`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, candidate, list, plan, protocol. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.values, list.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Return evaluation at root.body[14].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[10].value.values[8]::Call

Source: `scripts/roadmap_native.py:55`; AST `33b8a716c36751cd9cfb60ff5bd974e9ccd056ef2ee5c5c40d12a176dd664716`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, list. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.values, list.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::collect::root.body[14].body[10].value.values[8].args[0]::Call

Source: `scripts/roadmap_native.py:55`; AST `3cce69a4cd65239ca884574ba7e2d1a13da64071183f4489bc2490e746074292`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.values.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].value.values[8].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15]::FunctionDef

Source: `scripts/roadmap_native.py:61`; AST `56a9d59f1b660b434d6e0765469cdd099348fe42f42d5b3fa538bd7b2ea5432c`.

Rust module: `scripts::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, __doc__, argparse, args, atomic_write_json, collect, confined_path, parser, print, read_json, result. Outputs/bindings: args, parser, result.
Calls/effect boundaries: argparse.ArgumentParser, atomic_write_json, collect, confined_path, parser.add_argument, parser.parse_args, print, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[0]::Assign

Source: `scripts/roadmap_native.py:62`; AST `c4ad6d457d8034b25dcc473a40ed9c6629dab3a54fd3b776e18da1d1367bd02c`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: parser.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[0].value::Call

Source: `scripts/roadmap_native.py:62`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[1]::Expr

Source: `scripts/roadmap_native.py:63`; AST `f917f39e368c280ee869698ebdf3f536cf106a173263850b570d1acf7109233d`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[1].value::Call

Source: `scripts/roadmap_native.py:63`; AST `fc47aab0c293c16d7920946b8962d0daa215fd88d9b60910da7a7ac5f32efd23`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[2]::Expr

Source: `scripts/roadmap_native.py:64`; AST `a51cc65b34e6ae27ea4236c917ae93ad9d7a9f7e62b108258b8ba4b1db9b65f4`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[2].value::Call

Source: `scripts/roadmap_native.py:64`; AST `377c28d69737677c26c948f8d399b37d833c1d2d3130759c9dd617f5ecb6faa6`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[3]::Expr

Source: `scripts/roadmap_native.py:65`; AST `9da33d77a9d730d1b0a37192c8581046a68572dcd897195379ae8e318be418ad`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[3].value::Call

Source: `scripts/roadmap_native.py:65`; AST `fec4fbf48af0ce6f50e4b9bb90b76836907b3da18e1361a79d252cbbf372ac6f`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[4]::Expr

Source: `scripts/roadmap_native.py:66`; AST `4dc5801b9512d0ab4f7d67781330b07dcfe712734bf0b719389f03a9217552b6`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[4].value::Call

Source: `scripts/roadmap_native.py:66`; AST `1ec65a7b2bb9c75b74e5e087b7144be3df10847cfcd4b35415c851ac404d3884`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[5]::Assign

Source: `scripts/roadmap_native.py:67`; AST `6275c8d1600da776fb862cf3f5fef974e2559c70800565172097404dcea6fef6`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: args.
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[5].value::Call

Source: `scripts/roadmap_native.py:67`; AST `c865e8043798bf46a3b13d6774886772cbfabc2836b109a02aef4d3c2ad2a7ef`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[6]::Assign

Source: `scripts/roadmap_native.py:68`; AST `18ffe7bae1468b11c4d5553b49508292cbe264b366ba731c576ef4cbde66a421`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, collect, confined_path, read_json. Outputs/bindings: result.
Calls/effect boundaries: collect, confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[6].value::Call

Source: `scripts/roadmap_native.py:68`; AST `52b3a83182860ad4bed485ccd5826dd550d63ef7a72d40194644ef4aa3e21d7e`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, collect, confined_path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: collect, confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[6].value.args[1]::Call

Source: `scripts/roadmap_native.py:68`; AST `48f220fc5c2273d349ebfb1fb3af0a251867fa979fde120931d8abbe3dd8d381`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[6].value.args[1].args[0]::Call

Source: `scripts/roadmap_native.py:68`; AST `212c86d7103c06bf6e809ad93f976e30ed55c9df86b5ec12e1faf1aec33c0391`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[7]::Expr

Source: `scripts/roadmap_native.py:69`; AST `e686a0a49602a1b9c763a3bbbd8c483105d743d89b35b8c4d3209e9b94667631`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, atomic_write_json, confined_path, result. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[7].value::Call

Source: `scripts/roadmap_native.py:69`; AST `0045fe8f13bf74cb8f238c99d8a21c7b9bf259b3373427e2799bde7dae8589a4`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, atomic_write_json, confined_path, result. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[7].value.args[0]::Call

Source: `scripts/roadmap_native.py:69`; AST `bd2c4103df935f33b6c3362a61ace084743aa0c8c3bc6058f572e1ed907f0aa0`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[8]::Expr

Source: `scripts/roadmap_native.py:70`; AST `bde7bac086e1c56a912ab78734372e282b03630d3da298b7aafb4004842fc6f7`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: print, result. Outputs/bindings: (none).
Calls/effect boundaries: print.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::main::root.body[15].body[8].value::Call

Source: `scripts/roadmap_native.py:70`; AST `1eea6a428422b0a50c70d8c70a33f02184c490dc445305dbb0ff09a5a29a6580`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: print, result. Outputs/bindings: (none).
Calls/effect boundaries: print.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[16]::If

Source: `scripts/roadmap_native.py:74`; AST `3340fd16ba41ba1ddf3989cd136a498b72a97f7796e0f7fad6e815585dbc1c52`.

Rust module: `scripts::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered If evaluation at root.body[16]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[16].body[0]::Expr

Source: `scripts/roadmap_native.py:75`; AST `26412f54b9dfeb741e0d31e60ab8bd5c087bc77b2e3192f46a2fa84cd9152b86`.

Rust module: `scripts::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_native.py::module::root.body[16].body[0].value::Call

Source: `scripts/roadmap_native.py:75`; AST `612de6187c097f49a7c6002bfa6b205845dac081e9c3dc6b160fd9a6f584c826`.

Rust module: `scripts::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_native_adapter, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
