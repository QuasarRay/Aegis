# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 14. Inventory digest: `670d8ecda5a5ee551f24d0a3a47024d67c91015eab0d9361a9e421a47970169b`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## bin/destinyctl.py::module::root::Module

Source: `bin/destinyctl.py:1`; AST `ae32f9467a51bdc2703a9299b9e6284021ee8e4acfa696d1ee86a909cf371ccb`.

Rust module: `bin::destinyctl`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, SystemExit, __file__, __name__, main, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, SystemExit, main, str, sys.path.insert.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[0]::Expr

Source: `bin/destinyctl.py:2`; AST `99a4ec969f8f74f330bc2301b27faf1ba45ffdaef332db2429b228355291b79c`.

Rust module: `bin::destinyctl`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[1]::ImportFrom

Source: `bin/destinyctl.py:3`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `bin::destinyctl`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[2]::Import

Source: `bin/destinyctl.py:4`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `bin::destinyctl`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[3]::Expr

Source: `bin/destinyctl.py:6`; AST `4f45a6a49a7cac9626e80d858bfdfefac28f90ef55850b5338c8d6da56e7f5e4`.

Rust module: `bin::destinyctl`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Expr evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[3].value::Call

Source: `bin/destinyctl.py:6`; AST `8c2f813b3125891555f706a374432a157b212461e618d617e41266a51a8fe2a7`.

Rust module: `bin::destinyctl`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[3].value.args[1]::Call

Source: `bin/destinyctl.py:6`; AST `277d0ebebd12c50938f1ac4d6ad77deb778f9dcc4eec3c8114e239572a6f79b0`.

Rust module: `bin::destinyctl`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[3].value.args[1].args[0].left.value.value::Call

Source: `bin/destinyctl.py:6`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `bin::destinyctl`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[3].value.args[1].args[0].left.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[3].value.args[1].args[0].left.value.value.func.value::Call

Source: `bin/destinyctl.py:6`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `bin::destinyctl`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[3].value.args[1].args[0].left.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[4]::ImportFrom

Source: `bin/destinyctl.py:7`; AST `e2bcb5f7c1261405be883520a22d9b9d60038d04f073b92306823268f8810dd1`.

Rust module: `bin::destinyctl`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[5]::If

Source: `bin/destinyctl.py:9`; AST `f0ea0be627ebd2887d7f161de9c610e749cbd38d176e8efffefbc0424d175c46`.

Rust module: `bin::destinyctl`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SystemExit, __name__, main. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit, main.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered If evaluation at root.body[5]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[5].body[0]::Raise

Source: `bin/destinyctl.py:10`; AST `0634336e225749743986a4f7a082980f4f2712d05fe8333bc0c5cc9f00697679`.

Rust module: `bin::destinyctl`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SystemExit, main. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit, main.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Raise evaluation at root.body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[5].body[0].exc::Call

Source: `bin/destinyctl.py:10`; AST `ff6163839ec73a868582955a0c13ef79bd60ed979b4984a53f1d521fdca2e714`.

Rust module: `bin::destinyctl`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SystemExit, main. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit, main.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## bin/destinyctl.py::module::root.body[5].body[0].exc.args[0]::Call

Source: `bin/destinyctl.py:10`; AST `612de6187c097f49a7c6002bfa6b205845dac081e9c3dc6b160fd9a6f584c826`.

Rust module: `bin::destinyctl`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: agentinfra.destiny, pathlib, sys.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].exc.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
