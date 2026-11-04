# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 161. Inventory digest: `4d28a7be47ae9372c320f62512c508e2a9781a5f85c785c8b9b5b79d1483c4f4`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/roadmap_deal.py::module::root::Module

Source: `scripts/roadmap_deal.py:1`; AST `8ef93e14a016d64624b9f0c3c6aeba2081797bff544535f5e4f89f8fc0982476`.

Rust module: `scripts::roadmap_deal`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Exception, ObservedTheorem, Path, ROOT, Theorem, UnsupportedError, __doc__, __file__, __name__, alias, allowed, argparse, args, assertions, ast, astroid, atomic_write_json, confined_path, constraint, declarations, descr, dict, digest, exc, file_binding, formula, func, importlib, imports, inferred, inferred_imports, isinstance, iter, len, list, main, module, n, name, node, observe, parser, path, policy, print, proof, property, record, relative, require, result, root, solver, source, source_closure, staticmethod, str, super, sys, t, theorem, theorems, type, use, uses, x, z3. Outputs/bindings: ROOT, alias, allowed, args, assertions, constraint, declarations, formula, imports, inferred, inferred_imports, module, n, name, node, parser, path, policy, proof, record, result, source, t, theorem, theorems, use, uses, x.
Calls/effect boundaries: ObservedTheorem.from_astroid, Path, Path(__file__).resolve, Path(inferred[0].root().file).resolve, Path(module.file).resolve, Path(module.file).resolve().relative_to, Path(module.file).resolve().relative_to(root).as_posix, Theorem._prove, UnsupportedError, argparse.ArgumentParser, ast.dump, ast.dump(n, include_attributes=False).encode, ast.parse, ast.walk, astroid.MANAGER.ast_from_file, atomic_write_json, confined_path, constraint.condition.expr.sexpr, digest, file_binding, formula.encode, importlib.metadata.version, inferred[0].root, inferred_imports.append, isinstance, iter, len, list, main, module.nodes_of_class, observe, parser.add_argument, parser.parse_args, path.read_bytes, policy.read_bytes, policy.relative_to, policy.relative_to(root).as_posix, print, record.get, record.update, record['constraints'].append, record['solver_results'].append, require, source_closure, str, super, sys.path.insert, theorem.prove, type, use.infer, z3.get_version_string.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[0]::Expr

Source: `scripts/roadmap_deal.py:1`; AST `b5eb6d61d327227544021b4a607c11408ab922519621e367c4641869bfc9b071`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[1]::ImportFrom

Source: `scripts/roadmap_deal.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[2]::Import

Source: `scripts/roadmap_deal.py:8`; AST `356e6775028bc09e699d8b986887aaebc5e3e8e414a507fe911e3ba7da1264d9`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[3]::Import

Source: `scripts/roadmap_deal.py:9`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[4]::Import

Source: `scripts/roadmap_deal.py:10`; AST `19cad813dd36e7d2d28e34158c09f15d31fc9763ab13c9e42e639b952e3b32f6`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[5]::ImportFrom

Source: `scripts/roadmap_deal.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[6]::Import

Source: `scripts/roadmap_deal.py:12`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[7]::Assign

Source: `scripts/roadmap_deal.py:14`; AST `7efba0850e8eeaef93e5c3de6b7d47927a3e4bde0e8161dfb3d03fc10717d3c2`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[7].value.value.value::Call

Source: `scripts/roadmap_deal.py:14`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[7].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[7].value.value.value.func.value::Call

Source: `scripts/roadmap_deal.py:14`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[7].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[8]::Expr

Source: `scripts/roadmap_deal.py:15`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[8].value::Call

Source: `scripts/roadmap_deal.py:15`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[8].value.args[1]::Call

Source: `scripts/roadmap_deal.py:15`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[9]::ImportFrom

Source: `scripts/roadmap_deal.py:17`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[10]::ImportFrom

Source: `scripts/roadmap_deal.py:18`; AST `6ec1f57b05a0868100633c99a7da2f6640381f55496fafdd70cc006ccbd23c65`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[11]::ImportFrom

Source: `scripts/roadmap_deal.py:19`; AST `712baf434efc2709034e1a9b717a3a3d90def95e7cdfb1fb542a1add8bf519f2`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[12]::ImportFrom

Source: `scripts/roadmap_deal.py:20`; AST `860451982277a7f5c435b7fc36a0eb328ab43d13fe8858ce9091906ca6dcc079`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13]::FunctionDef

Source: `scripts/roadmap_deal.py:23`; AST `cc54c79f268b0080b7424a5cc23486fb00d7da78fabdc44b0b5c82d877a5125b`.

Rust module: `scripts::roadmap_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, ObservedTheorem, Path, Theorem, UnsupportedError, alias, allowed, assertions, ast, astroid, confined_path, constraint, declarations, descr, dict, digest, exc, file_binding, formula, func, importlib, imports, inferred, inferred_imports, isinstance, iter, len, list, module, n, name, node, path, policy, proof, property, record, relative, require, result, root, solver, source, source_closure, staticmethod, str, super, t, theorem, theorems, type, use, uses, x, z3. Outputs/bindings: alias, allowed, assertions, constraint, declarations, formula, imports, inferred, inferred_imports, module, n, name, node, path, policy, proof, record, result, source, t, theorem, theorems, use, uses, x.
Calls/effect boundaries: ObservedTheorem.from_astroid, Path, Path(inferred[0].root().file).resolve, Path(module.file).resolve, Path(module.file).resolve().relative_to, Path(module.file).resolve().relative_to(root).as_posix, Theorem._prove, UnsupportedError, ast.dump, ast.dump(n, include_attributes=False).encode, ast.parse, ast.walk, astroid.MANAGER.ast_from_file, confined_path, constraint.condition.expr.sexpr, digest, file_binding, formula.encode, importlib.metadata.version, inferred[0].root, inferred_imports.append, isinstance, iter, len, list, module.nodes_of_class, path.read_bytes, policy.read_bytes, policy.relative_to, policy.relative_to(root).as_posix, record.update, record['constraints'].append, record['solver_results'].append, require, source_closure, str, super, theorem.prove, type, use.infer, z3.get_version_string.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[0]::Assign

Source: `scripts/roadmap_deal.py:24`; AST `4df800311e7bfc389938443d14b349a8c557e1627a4f3dbea5f45a06365b1e75`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: allowed.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[1]::Expr

Source: `scripts/roadmap_deal.py:26`; AST `5e97197f921d3bf036d3b00dd6367bd2a9ce0fec84c101e677798ec9093ded3a`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allowed, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[1].value::Call

Source: `scripts/roadmap_deal.py:26`; AST `eb4560d204bfd523572b80779d40034744ef0058ccf29d11a84cf72b6c61db32`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: allowed, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[2]::Assign

Source: `scripts/roadmap_deal.py:27`; AST `e46824fd830d49aa0997b5da19da993dd7e9cb85a0ba53ccab360b6a9a0037b9`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[2].value::Call

Source: `scripts/roadmap_deal.py:27`; AST `63c9acf4cfde20a50eacc658154bbb4ec3954f19236b82666a93c852e8d25e5a`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[3]::Assign

Source: `scripts/roadmap_deal.py:28`; AST `a50c7909edab130434b65b3ce999f2cb3c5ae8db1a12999d79df85e34c157706`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, path, relative. Outputs/bindings: source.
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[3].value::Call

Source: `scripts/roadmap_deal.py:28`; AST `67537485f475d118833b444d0c543289a0b717cd6e77cfec6a7f66c408daf6ad`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, path, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[3].value.args[0]::Call

Source: `scripts/roadmap_deal.py:28`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4]::Assign

Source: `scripts/roadmap_deal.py:29`; AST `4719a22886305f80928f66fe0f8a86db0e651124fa0f63763d4835cdba114e12`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, digest, isinstance, n, source. Outputs/bindings: assertions, n.
Calls/effect boundaries: ast.dump, ast.dump(n, include_attributes=False).encode, ast.walk, digest, isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4].value::ListComp

Source: `scripts/roadmap_deal.py:29`; AST `7b0e51d12f32dac2bfa8f8c4d4006009511801fa1e15b40c398c8733c0e2a6b6`.

Rust module: `scripts::roadmap_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, digest, isinstance, n, source. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.dump(n, include_attributes=False).encode, ast.walk, digest, isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4].value.elt.values[1]::Call

Source: `scripts/roadmap_deal.py:29`; AST `b9fecb10fec2d2fb91f2fac02fce60e11c9be54d478d34b3585f48ed4d5c56d6`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(n, include_attributes=False).encode, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4].value.elt.values[1].args[0]::Call

Source: `scripts/roadmap_deal.py:29`; AST `9cb290152edcd3383e39d9a85798c8b75bc1b40c1229e05b2b7ddb32e43c942f`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(n, include_attributes=False).encode.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.elt.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4].value.elt.values[1].args[0].func.value::Call

Source: `scripts/roadmap_deal.py:29`; AST `a8894dcbc048f57508ef0b204d52c09827f7d3518c19439cca92c87fcdaa7146`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.elt.values[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4].value.generators[0].iter::Call

Source: `scripts/roadmap_deal.py:30`; AST `346b55b40177f4e8607bbae929596b640c5f55232d6b62be80a906dedeb30447`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, source. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[4].value.generators[0].ifs[0]::Call

Source: `scripts/roadmap_deal.py:30`; AST `ec459fe7660e2311b9d6374445e99c314277891140df6f9795bcc3affd02ce37`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[5]::Assign

Source: `scripts/roadmap_deal.py:31`; AST `fe65fcdafdecbb2b5f11d8fc92fc3f47c397047e79e3a6caea50629bda62c0a2`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertions, file_binding, relative, root, source_closure. Outputs/bindings: record.
Calls/effect boundaries: file_binding, source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[5].value.values[4]::Call

Source: `scripts/roadmap_deal.py:32`; AST `e8457929e4b469f5fb6798717852b1b34d5ad1a0970999a9e33bb237cecc4b61`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[5].value.values[10]::Call

Source: `scripts/roadmap_deal.py:34`; AST `9541f4c9d8dff7d7ff3112bf1ab4deb4b2305a0241438b75b655ce54f3816385`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.values[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6]::Try

Source: `scripts/roadmap_deal.py:36`; AST `acaca214cfb496e6747d81030af2e85f4f8323303aa901cc30f0ccf5c69191ab`.

Rust module: `scripts::roadmap_deal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, ObservedTheorem, Path, Theorem, UnsupportedError, alias, allowed, ast, astroid, constraint, declarations, descr, digest, exc, file_binding, formula, func, importlib, imports, inferred, inferred_imports, isinstance, iter, len, list, module, n, name, node, path, policy, proof, property, record, relative, require, result, root, solver, source, staticmethod, str, super, t, theorem, theorems, type, use, uses, x, z3. Outputs/bindings: alias, constraint, declarations, formula, imports, inferred, inferred_imports, module, n, name, node, policy, proof, result, t, theorem, theorems, use, uses, x.
Calls/effect boundaries: ObservedTheorem.from_astroid, Path, Path(inferred[0].root().file).resolve, Path(module.file).resolve, Path(module.file).resolve().relative_to, Path(module.file).resolve().relative_to(root).as_posix, Theorem._prove, UnsupportedError, ast.parse, astroid.MANAGER.ast_from_file, constraint.condition.expr.sexpr, digest, file_binding, formula.encode, importlib.metadata.version, inferred[0].root, inferred_imports.append, isinstance, iter, len, list, module.nodes_of_class, policy.read_bytes, policy.relative_to, policy.relative_to(root).as_posix, record.update, record['constraints'].append, record['solver_results'].append, require, str, super, theorem.prove, type, use.infer, z3.get_version_string.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Try evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[0]::Import

Source: `scripts/roadmap_deal.py:37`; AST `a64e9c7d59b5a230cb263e08a84f600bb1cfcf7928f31b392291ae92be47c90d`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Import evaluation at root.body[13].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[1]::Import

Source: `scripts/roadmap_deal.py:38`; AST `9161e8188a946ab701e183641f8a41580dbd502ae4a4664351e4def9491a2059`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Import evaluation at root.body[13].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[2]::ImportFrom

Source: `scripts/roadmap_deal.py:39`; AST `67fc71410cf61a0965753965265533cc5d747ea5dd54013b5c640f523fd44195`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[3]::ImportFrom

Source: `scripts/roadmap_deal.py:40`; AST `2951f0826e7233dd1a0cf6597ae2f97cbe08d6108624da71b48027af27eafae3`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[4]::Assign

Source: `scripts/roadmap_deal.py:42`; AST `ada60aa06aa67f9514d09c01f5ba4d1992eb0073522a91e20036621fef6e0f1f`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: importlib, name, record. Outputs/bindings: name.
Calls/effect boundaries: importlib.metadata.version.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[4].value::DictComp

Source: `scripts/roadmap_deal.py:42`; AST `7a58a6895bbbcbbb821f90c21654fd76cd4f9c284355c3b0c1baadce010e007f`.

Rust module: `scripts::roadmap_deal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: importlib, name. Outputs/bindings: name.
Calls/effect boundaries: importlib.metadata.version.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[4].value.value::Call

Source: `scripts/roadmap_deal.py:42`; AST `b364a6e93cb303f43825134df9582a69ef85e03c654cf9d949710336659b9e85`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: importlib, name. Outputs/bindings: (none).
Calls/effect boundaries: importlib.metadata.version.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[4].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[5]::Assign

Source: `scripts/roadmap_deal.py:43`; AST `541897700616f46db84a16e092e5e53ae2d74f98e99a55e450c5a6512715aa43`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, z3. Outputs/bindings: (none).
Calls/effect boundaries: z3.get_version_string.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[5].value::Call

Source: `scripts/roadmap_deal.py:43`; AST `119f0fe4ee2999fac836bf2b32cf8674d15b0e464cf0d6a8387dfee3e2e36841`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: z3. Outputs/bindings: (none).
Calls/effect boundaries: z3.get_version_string.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[6]::Assign

Source: `scripts/roadmap_deal.py:44`; AST `041a05da80dbef71ae4e78d5d5ce075b9d514f43b1346b69acc1d5150b53de77`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: astroid, path, str. Outputs/bindings: module.
Calls/effect boundaries: astroid.MANAGER.ast_from_file, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[6].value::Call

Source: `scripts/roadmap_deal.py:44`; AST `f2e8e7bbb064eef9945017d669a9396fe07b8c4a3c7be9265411e88897025911`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: astroid, path, str. Outputs/bindings: (none).
Calls/effect boundaries: astroid.MANAGER.ast_from_file, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[6].value.args[0]::Call

Source: `scripts/roadmap_deal.py:44`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[7]::Assign

Source: `scripts/roadmap_deal.py:45`; AST `3f31c6d7e41f7b7093acfeaf12847aec3a51e894dcfa41152c9bb08199723dc9`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, file_binding, module, record, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.file).resolve, Path(module.file).resolve().relative_to, Path(module.file).resolve().relative_to(root).as_posix, file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[7].value::Call

Source: `scripts/roadmap_deal.py:45`; AST `a54961ef9cb8492ffa6e811c2c012a77d4adc72c14a7862e9e1ce78b29546649`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, file_binding, module, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.file).resolve, Path(module.file).resolve().relative_to, Path(module.file).resolve().relative_to(root).as_posix, file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[7].value.args[1]::Call

Source: `scripts/roadmap_deal.py:45`; AST `a91c7bf07688df79fca59ec2a637eaadbf374ae22f6ed7116b2725eec53d2807`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, module, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.file).resolve, Path(module.file).resolve().relative_to, Path(module.file).resolve().relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[7].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[7].value.args[1].func.value::Call

Source: `scripts/roadmap_deal.py:45`; AST `4891d71178954112d2f8869ac2a7059a2ccf64bcb16b50daf1c0743f7fd4206e`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, module, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.file).resolve, Path(module.file).resolve().relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[7].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[7].value.args[1].func.value.func.value::Call

Source: `scripts/roadmap_deal.py:45`; AST `43dd2e21a434448e494803ff9df3e32eb85e12b81f009b58741b898ad38f4065`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, module. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.file).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[7].value.args[1].func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[7].value.args[1].func.value.func.value.func.value::Call

Source: `scripts/roadmap_deal.py:45`; AST `8532bb0c6d8a8173d78f018d4898257fe4d0b1d36ed4400067f2d706e2df5825`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, module. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[7].value.args[1].func.value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[8]::Assign

Source: `scripts/roadmap_deal.py:46`; AST `9cae5011e5bf4ff3c796311daab58c6e292e78ad5a8a595abe353d9d65ce5401`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: policy.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[9]::Assign

Source: `scripts/roadmap_deal.py:47`; AST `61d9be77256d5eda962b811074df65b302d5953ff50af1ab4cd5ec11950a6fe1`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, policy. Outputs/bindings: declarations, n.
Calls/effect boundaries: ast.parse, isinstance, policy.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[9].value::DictComp

Source: `scripts/roadmap_deal.py:47`; AST `77a54caebc9946c47ffa9433ecc0b95eab2649b4942b0eb2ff42bf01360045eb`.

Rust module: `scripts::roadmap_deal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: ast, isinstance, n, policy. Outputs/bindings: n.
Calls/effect boundaries: ast.parse, isinstance, policy.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[6].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[9].value.generators[0].iter.value::Call

Source: `scripts/roadmap_deal.py:47`; AST `ab67010fec2d3fb43e3e0ea50b41d08baaa9c7a0a05d66ae461c52444b6e122b`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, policy. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, policy.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[9].value.generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[9].value.generators[0].iter.value.args[0]::Call

Source: `scripts/roadmap_deal.py:47`; AST `ce808b10802e7a9d96009c51aae233886c7209a171790fdfffff5e3b0984b03a`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[9].value.generators[0].iter.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[9].value.generators[0].ifs[0]::Call

Source: `scripts/roadmap_deal.py:47`; AST `6be47f9e1551f535bf2aed1cf83932df0390bf06e04c27a299cb9ed3d358cabb`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[9].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[10]::Assign

Source: `scripts/roadmap_deal.py:48`; AST `61835fc0f6abc07d4800ee4b19dfe2374080940cf96dd4468515703a99c759a4`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: alias, ast, isinstance, node, source. Outputs/bindings: alias, imports, node.
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[10].value::ListComp

Source: `scripts/roadmap_deal.py:48`; AST `d37482d36d10555cef97273bee629984eae071bd0f3a106881a29c11af6908ac`.

Rust module: `scripts::roadmap_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: alias, ast, isinstance, node, source. Outputs/bindings: alias, node.
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[6].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[10].value.generators[0].ifs[0].values[0]::Call

Source: `scripts/roadmap_deal.py:48`; AST `590fb849ed19f160c1e37ff1ac642a8b6c15e24fbebaf71c0325db10ff5a8938`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[10].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[11]::Assign

Source: `scripts/roadmap_deal.py:50`; AST `813b3028cfc8dd0248abba0fb0ce38305ec4a4f9e7cfeb98e5bba4e50430d1ff`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: inferred_imports.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12]::For

Source: `scripts/roadmap_deal.py:51`; AST `1494336d3e23a0e46bb7aaebc0fcec349c222271159e2678f984432ead17c98e`.

Rust module: `scripts::roadmap_deal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, astroid, declarations, file_binding, imports, inferred, inferred_imports, isinstance, len, module, n, name, policy, require, root, use, uses. Outputs/bindings: inferred, n, name, use, uses.
Calls/effect boundaries: Path, Path(inferred[0].root().file).resolve, file_binding, inferred[0].root, inferred_imports.append, isinstance, len, module.nodes_of_class, policy.relative_to, policy.relative_to(root).as_posix, require, use.infer.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered For evaluation at root.body[13].body[6].body[12]; no call, error or mutation may be omitted. Iteration: name in imports
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[0]::Assign

Source: `scripts/roadmap_deal.py:52`; AST `4573be67da0643f6313f093443ae068b65dd90ac1fd1c2f750385ab34ecdd5e8`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: astroid, isinstance, module, n, name. Outputs/bindings: n, uses.
Calls/effect boundaries: isinstance, module.nodes_of_class.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[0].value::ListComp

Source: `scripts/roadmap_deal.py:52`; AST `b586440bd282eab80a8fd9d5a7c3e8d9cbad405a8f28daac5d16b337a2c3e478`.

Rust module: `scripts::roadmap_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: astroid, isinstance, module, n, name. Outputs/bindings: n.
Calls/effect boundaries: isinstance, module.nodes_of_class.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[6].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[0].value.generators[0].iter::Call

Source: `scripts/roadmap_deal.py:52`; AST `560750d4a47d425950349f73b67e7ff8adc4aa41b2df865f91eb2f2d25332356`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: astroid, module. Outputs/bindings: (none).
Calls/effect boundaries: module.nodes_of_class.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[0].value.generators[0].ifs[0].values[1]::Call

Source: `scripts/roadmap_deal.py:53`; AST `fc3f22f92acb5a9f79e69d8d24d868057eee2f0f5fb6da1779bb8e7acf547841`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: astroid, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[0].value.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[1]::Expr

Source: `scripts/roadmap_deal.py:54`; AST `2c7134a7dae946758464502704172877397bf4487d34996f0307456a0c07ccc7`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, uses. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[1].value::Call

Source: `scripts/roadmap_deal.py:54`; AST `65a6c209413469864d4747a0c85f41df865cb7c226729d8d194b3bbace4b4c19`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, uses. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2]::For

Source: `scripts/roadmap_deal.py:55`; AST `5d9b876bc37789feb0f32095fdb79edc2640ea6b3d48ea5aada3fd934ab0e69b`.

Rust module: `scripts::roadmap_deal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, astroid, declarations, file_binding, inferred, inferred_imports, isinstance, len, n, name, policy, require, root, use, uses. Outputs/bindings: inferred, n, use.
Calls/effect boundaries: Path, Path(inferred[0].root().file).resolve, file_binding, inferred[0].root, inferred_imports.append, isinstance, len, policy.relative_to, policy.relative_to(root).as_posix, require, use.infer.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered For evaluation at root.body[13].body[6].body[12].body[2]; no call, error or mutation may be omitted. Iteration: use in uses
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[0]::Assign

Source: `scripts/roadmap_deal.py:56`; AST `dfb6f437bf52dbeffdd6eb1e6168385053bfce5d0a366daf16571a4d3fd6621f`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: astroid, isinstance, n, use. Outputs/bindings: inferred, n.
Calls/effect boundaries: isinstance, use.infer.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[0].value::ListComp

Source: `scripts/roadmap_deal.py:56`; AST `6e1a11f9f2ee29fe40ef19f873a21dddb9244d75cd350afc8012b0483bb3455d`.

Rust module: `scripts::roadmap_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: astroid, isinstance, n, use. Outputs/bindings: n.
Calls/effect boundaries: isinstance, use.infer.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[6].body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[0].value.generators[0].iter::Call

Source: `scripts/roadmap_deal.py:56`; AST `d217b1289527e27246a6567cbf6caa611a3012be1171aaa335ea8b412681df1d`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: use. Outputs/bindings: (none).
Calls/effect boundaries: use.infer.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[0].value.generators[0].ifs[0]::Call

Source: `scripts/roadmap_deal.py:56`; AST `5feb836ccde06ac29d0497176f0bcd1beeba82c4db3e7bd9d32fac5199ea92f6`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: astroid, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[0].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[1]::Expr

Source: `scripts/roadmap_deal.py:57`; AST `5b49780bb0f15fa842d969f8d357c03afece6c82a0fbde682506ce2edee7947f`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, declarations, inferred, len, name, policy, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(inferred[0].root().file).resolve, inferred[0].root, len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[12].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[1].value::Call

Source: `scripts/roadmap_deal.py:57`; AST `f9613f57389edd3144b4b38aa94a01d154338d1bfed9928ddfac3411e1e3a86d`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, declarations, inferred, len, name, policy, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(inferred[0].root().file).resolve, inferred[0].root, len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[0].left::Call

Source: `scripts/roadmap_deal.py:57`; AST `1074797eaba25689755e85c6e1e39d1709a1e8c96cc27c53b4f095017457f37a`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inferred, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[2].left::Call

Source: `scripts/roadmap_deal.py:57`; AST `95deb9fad58676567ac38a267a7bf397de058ef361b4ff3ea73cb0b685bb5f66`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, inferred. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(inferred[0].root().file).resolve, inferred[0].root.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[2].left.func.value::Call

Source: `scripts/roadmap_deal.py:57`; AST `3d7c4f0193e06c3184bbe05c61f3621ea4423662c7227bcc18dfd63d46fee2c8`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, inferred. Outputs/bindings: (none).
Calls/effect boundaries: Path, inferred[0].root.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[2].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[2].left.func.value.args[0].value::Call

Source: `scripts/roadmap_deal.py:57`; AST `1916bf358a55a8456b6ea64f05de032b22d234676369decbddb7bb75b86eebcf`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inferred. Outputs/bindings: (none).
Calls/effect boundaries: inferred[0].root.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[1].value.args[0].values[2].left.func.value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[2]::Expr

Source: `scripts/roadmap_deal.py:60`; AST `73f22553a5a220ce725ceb9a2dba8801da45e3f43b80cf74c3576e8c69f660a6`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, inferred, inferred_imports, name, policy, root, use. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, inferred_imports.append, policy.relative_to, policy.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[12].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[2].value::Call

Source: `scripts/roadmap_deal.py:60`; AST `703a56a9769793e7ba208a9ab78007645318b4df3baa47cecba687547005ad71`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, inferred, inferred_imports, name, policy, root, use. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, inferred_imports.append, policy.relative_to, policy.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[2].value.args[0].values[2]::Call

Source: `scripts/roadmap_deal.py:61`; AST `c88167da3ec1f92b2f9283c7f1927094e5346a5d318da6caf13abb3d39e3fcec`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, policy, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, policy.relative_to, policy.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[2].value.args[0].values[2].args[1]::Call

Source: `scripts/roadmap_deal.py:61`; AST `c08c54f6796f32d36583e3756b5b4c22c31361504d709ea0225ebc50d103e36a`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, root. Outputs/bindings: (none).
Calls/effect boundaries: policy.relative_to, policy.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[2].value.args[0].values[2].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[12].body[2].body[2].value.args[0].values[2].args[1].func.value::Call

Source: `scripts/roadmap_deal.py:61`; AST `f9af1cb4d6bbf3b99f135da1ab928ead5c72949f4f9c45898ef0b2bc85afccc7`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, root. Outputs/bindings: (none).
Calls/effect boundaries: policy.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[12].body[2].body[2].value.args[0].values[2].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[13]::Assign

Source: `scripts/roadmap_deal.py:63`; AST `fa7aa3cb60daedbae4e8aa09dd8749a711dd7e1c8717204a96a2704eac466f10`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inferred_imports, record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::root.body[13].body[6].body[14]::ClassDef

Source: `scripts/roadmap_deal.py:65`; AST `1dc0282fbb33a625f01592fa76b9e786b26ef75cea17fdf632fe6b821be1a858`.

Rust module: `scripts::roadmap_deal`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Theorem, UnsupportedError, constraint, descr, digest, formula, func, iter, len, property, record, require, result, solver, staticmethod, str, super. Outputs/bindings: constraint, formula, result.
Calls/effect boundaries: Theorem._prove, UnsupportedError, constraint.condition.expr.sexpr, digest, formula.encode, iter, len, record['constraints'].append, record['solver_results'].append, require, str, super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ClassDef evaluation at root.body[13].body[6].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::get_contracts::root.body[13].body[6].body[14].body[0]::FunctionDef

Source: `scripts/roadmap_deal.py:67`; AST `9c44fdeda9452621d8a7110623e500480b6f53e61be458a5154eb1c1f567e371`.

Rust module: `scripts::roadmap_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: UnsupportedError, func, iter, staticmethod. Outputs/bindings: (none).
Calls/effect boundaries: UnsupportedError, iter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[6].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::get_contracts::root.body[13].body[6].body[14].body[0].body[0]::If

Source: `scripts/roadmap_deal.py:68`; AST `6bb16a1f61b5fbe7a6f8d9bed22546c7d4dac33f5caa8976dd8ee6cb168ea7bf`.

Rust module: `scripts::roadmap_deal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: UnsupportedError, func. Outputs/bindings: (none).
Calls/effect boundaries: UnsupportedError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered If evaluation at root.body[13].body[6].body[14].body[0].body[0]; no call, error or mutation may be omitted. Condition: func.decorators and func.decorators.nodes
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::get_contracts::root.body[13].body[6].body[14].body[0].body[0].body[0]::Raise

Source: `scripts/roadmap_deal.py:69`; AST `23834ab39ef5573b65157cae8a52dc5479e2c0b5eb2e38d7136a56c82ef60154`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: UnsupportedError, func. Outputs/bindings: (none).
Calls/effect boundaries: UnsupportedError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[6].body[14].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::get_contracts::root.body[13].body[6].body[14].body[0].body[0].body[0].exc::Call

Source: `scripts/roadmap_deal.py:69`; AST `82f2731a1ef14913ba956fa4254a2a13910b8f6fc1dd6e0cffab4c5455a81e9b`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: UnsupportedError, func. Outputs/bindings: (none).
Calls/effect boundaries: UnsupportedError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[0].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::get_contracts::root.body[13].body[6].body[14].body[0].body[1]::Return

Source: `scripts/roadmap_deal.py:70`; AST `8b0b875790c623f03661e3558de7d2fc43d880c8af1a3057120d6d74b8de9473`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: iter. Outputs/bindings: (none).
Calls/effect boundaries: iter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Return evaluation at root.body[13].body[6].body[14].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::get_contracts::root.body[13].body[6].body[14].body[0].body[1].value::Call

Source: `scripts/roadmap_deal.py:70`; AST `859c17a84488295ad8d5a2f3037109fccb2f0b017018c5a73991cadc10bbef77`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: iter. Outputs/bindings: (none).
Calls/effect boundaries: iter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1]::FunctionDef

Source: `scripts/roadmap_deal.py:73`; AST `ac8b4c0e0394433c03a980c2a0fe1e658417657460d7d163023d0e19d7456892`.

Rust module: `scripts::roadmap_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: constraint, digest, formula, len, property, record, require, super. Outputs/bindings: constraint, formula.
Calls/effect boundaries: constraint.condition.expr.sexpr, digest, formula.encode, len, record['constraints'].append, require, super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[6].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0]::For

Source: `scripts/roadmap_deal.py:74`; AST `0f5b084e9f6678088df11ae0b0d957208d652a7fdf35dd668b5501cf68caf84d`.

Rust module: `scripts::roadmap_deal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: constraint, digest, formula, len, record, require, super. Outputs/bindings: constraint, formula.
Calls/effect boundaries: constraint.condition.expr.sexpr, digest, formula.encode, len, record['constraints'].append, require, super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered For evaluation at root.body[13].body[6].body[14].body[1].body[0]; no call, error or mutation may be omitted. Iteration: constraint in super().constraints
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].iter.value::Call

Source: `scripts/roadmap_deal.py:74`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[0]::Assign

Source: `scripts/roadmap_deal.py:75`; AST `f4566a3e8c76a2f9a3ab7f3ffc0cabc4e226ebf3d666c71311e54521f157b2b6`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: constraint. Outputs/bindings: formula.
Calls/effect boundaries: constraint.condition.expr.sexpr.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[14].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[0].value::Call

Source: `scripts/roadmap_deal.py:75`; AST `aa369f749153e0b49dae6c93ed15c207808aeb62bc98526910694c4ff2a82eed`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: constraint. Outputs/bindings: (none).
Calls/effect boundaries: constraint.condition.expr.sexpr.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[1]::Expr

Source: `scripts/roadmap_deal.py:76`; AST `e0b0891852beff9c6eb4cfb5061d43675257a8adb14b1a8a64721ec2f372b1b6`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: formula, len, record, require. Outputs/bindings: (none).
Calls/effect boundaries: formula.encode, len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[14].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[1].value::Call

Source: `scripts/roadmap_deal.py:76`; AST `3b692089dc12d4cb1060fa70d2563a6851ac88cede1930ca3a0e4b2c7661e194`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: formula, len, record, require. Outputs/bindings: (none).
Calls/effect boundaries: formula.encode, len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[1].value.args[0].values[0].left::Call

Source: `scripts/roadmap_deal.py:76`; AST `a6396511d09beff6d6f63e49924b166aee8f6c4b883465aa76efb283ef27bfa8`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[1].value.args[0].values[1].left::Call

Source: `scripts/roadmap_deal.py:76`; AST `e3ea3b75a9f74816f5d31ff47b85b25e5ad26ffb25c6f1d5a645c98517648d36`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: formula, len. Outputs/bindings: (none).
Calls/effect boundaries: formula.encode, len.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[1].value.args[0].values[1].left.args[0]::Call

Source: `scripts/roadmap_deal.py:76`; AST `c173b1b441f5e533fffd2ad33c85ba33493b06ea1b43efe41fef1677c1dfb92a`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: formula. Outputs/bindings: (none).
Calls/effect boundaries: formula.encode.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[1].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[2]::Expr

Source: `scripts/roadmap_deal.py:78`; AST `fa8af824f33347c9e1e4f3fa76197cf413246f41d898ad70b0e9aa072556f7c6`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: constraint, digest, formula, record. Outputs/bindings: (none).
Calls/effect boundaries: digest, formula.encode, record['constraints'].append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[14].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[2].value::Call

Source: `scripts/roadmap_deal.py:78`; AST `98b629fc53c1fe52122d5c62bdd8c420ea1ecda8a260d786451189314aecb6dd`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: constraint, digest, formula, record. Outputs/bindings: (none).
Calls/effect boundaries: digest, formula.encode, record['constraints'].append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[2].value.args[0].values[2]::Call

Source: `scripts/roadmap_deal.py:79`; AST `702a19c22b61fe2c146367a8c0058639b5bd6fa435d45e028b742277459a3134`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, formula. Outputs/bindings: (none).
Calls/effect boundaries: digest, formula.encode.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[2].value.args[0].values[2].args[0]::Call

Source: `scripts/roadmap_deal.py:79`; AST `c173b1b441f5e533fffd2ad33c85ba33493b06ea1b43efe41fef1677c1dfb92a`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: formula. Outputs/bindings: (none).
Calls/effect boundaries: formula.encode.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[1].body[0].body[2].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::constraints::root.body[13].body[6].body[14].body[1].body[0].body[3]::Expr

Source: `scripts/roadmap_deal.py:80`; AST `333929a4cd57810718079aff98c36f51a8ea327838d00dbff29028cd519d1be4`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: constraint. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[14].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2]::FunctionDef

Source: `scripts/roadmap_deal.py:82`; AST `926273a8065a6c2f833d7ff0c209c915d90e43a8fa2d792100c794f4da69f244`.

Rust module: `scripts::roadmap_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Theorem, descr, record, result, solver, str. Outputs/bindings: result.
Calls/effect boundaries: Theorem._prove, record['solver_results'].append, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[6].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[0]::Assign

Source: `scripts/roadmap_deal.py:83`; AST `a66021e7a01be362e8535c99afe0413df6a30e1faf0d669408be83fcdfcbaa59`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Theorem, descr, solver. Outputs/bindings: result.
Calls/effect boundaries: Theorem._prove.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[14].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[0].value::Call

Source: `scripts/roadmap_deal.py:83`; AST `2553a053ded2ee9a6650c8225509d8f6337ee8c331d4b2ed325b92225f24ba27`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Theorem, descr, solver. Outputs/bindings: (none).
Calls/effect boundaries: Theorem._prove.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[1]::Expr

Source: `scripts/roadmap_deal.py:84`; AST `6cac7ec0430b69bfe583491514c66bfc5d9dca1c460b787f4d76b6e91d07c324`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: descr, record, result, str. Outputs/bindings: (none).
Calls/effect boundaries: record['solver_results'].append, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[14].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[1].value::Call

Source: `scripts/roadmap_deal.py:84`; AST `9b7338119ec0c27bf07e62fe9b37c3d8e13696768d0c1370763b435446a82921`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: descr, record, result, str. Outputs/bindings: (none).
Calls/effect boundaries: record['solver_results'].append, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[1].value.args[0].values[2].body::Call

Source: `scripts/roadmap_deal.py:85`; AST `89699f1b1cce76c1c8c90802be1c60633a323827775940dd21c09501b0f90321`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[2].body[1].value.args[0].values[2].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[1].value.args[0].values[3].body::Call

Source: `scripts/roadmap_deal.py:86`; AST `97cd0989a16248ae144dfc3d408c3d7d89a794e16d9f44f0fab8bbe82515c307`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[14].body[2].body[1].value.args[0].values[3].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::ObservedTheorem::_prove::root.body[13].body[6].body[14].body[2].body[2]::Return

Source: `scripts/roadmap_deal.py:87`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Return evaluation at root.body[13].body[6].body[14].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[15]::Assign

Source: `scripts/roadmap_deal.py:89`; AST `f8224fd62d78e2486f4402692f3ce57d84b6503b1cf2995796d632f055297410`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ObservedTheorem, list, module. Outputs/bindings: theorems.
Calls/effect boundaries: ObservedTheorem.from_astroid, list.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[15].value::Call

Source: `scripts/roadmap_deal.py:89`; AST `fcbf8652393f21164c66c25c397823f84dfba883d5850f7535154d9c190d9426`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ObservedTheorem, list, module. Outputs/bindings: (none).
Calls/effect boundaries: ObservedTheorem.from_astroid, list.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[15].value.args[0]::Call

Source: `scripts/roadmap_deal.py:89`; AST `7ffe28927d1c91c90fe95d18d86f70427c897583c86ac408c4bba3be4a052300`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ObservedTheorem, module. Outputs/bindings: (none).
Calls/effect boundaries: ObservedTheorem.from_astroid.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[15].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[16]::Expr

Source: `scripts/roadmap_deal.py:90`; AST `551134552400246a8a1e083425402655d53394c08df5afac5c016d2a0ff97674`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allowed, relative, require, t, theorems. Outputs/bindings: t.
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[16].value::Call

Source: `scripts/roadmap_deal.py:90`; AST `39266d39ab902fb7a2b0b377807090d454c9cd42c761527bd1294d1d864f33d4`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: allowed, relative, require, t, theorems. Outputs/bindings: t.
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[16].value.args[0].left::ListComp

Source: `scripts/roadmap_deal.py:90`; AST `882d1f87a7ca52c325b3a54a8955972bb700163ecd741892cd9b63f1be2e59b6`.

Rust module: `scripts::roadmap_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: t, theorems. Outputs/bindings: t.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[6].body[16].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[17]::Assign

Source: `scripts/roadmap_deal.py:91`; AST `65fa8881c0787bd7c391742f13cedf370e649e63b81b3040c197e77f29cde8ed`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: theorems. Outputs/bindings: theorem.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[18]::Assign

Source: `scripts/roadmap_deal.py:92`; AST `8b1f51f4150d37087855544067e0d99c9d2f7dc1bf587bf7987cad857add2084`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: theorem. Outputs/bindings: proof.
Calls/effect boundaries: theorem.prove.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[18].value::Call

Source: `scripts/roadmap_deal.py:92`; AST `1f849e5678542b98ef76fb225dcc444109e39244bc225ede6de7db6faa6f6da1`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: theorem. Outputs/bindings: (none).
Calls/effect boundaries: theorem.prove.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[19]::Expr

Source: `scripts/roadmap_deal.py:93`; AST `ec422e55e10e3ca9f636a97f041ebc9237fef58a1932b96d1485faaf89bb7f7a`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proof, record, str, theorem, x. Outputs/bindings: x.
Calls/effect boundaries: record.update, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[19].value::Call

Source: `scripts/roadmap_deal.py:93`; AST `ad90d6fb848cabe89857a843216ab25151aca95332948b8674c0656f08a75fa3`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof, record, str, theorem, x. Outputs/bindings: x.
Calls/effect boundaries: record.update, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[19].value.keywords[2].value.values[2].body::Call

Source: `scripts/roadmap_deal.py:95`; AST `95378671fa283f189b9d25742e03582d472ece9b92f010ed4233aefe69dd51f2`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[19].value.keywords[2].value.values[2].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[19].value.keywords[2].value.values[3].body::Call

Source: `scripts/roadmap_deal.py:96`; AST `c82963b63a01589e25cdccc18ce78e1bd1877cdab000b4a8ea72cb3528f09e15`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[19].value.keywords[2].value.values[3].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[19].value.keywords[3].value::ListComp

Source: `scripts/roadmap_deal.py:97`; AST `8b247184f4ad2ad71d8b74d221cbe6ec571497bc084b76b96bf160f447aa3d81`.

Rust module: `scripts::roadmap_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: str, theorem, x. Outputs/bindings: x.
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[6].body[19].value.keywords[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].body[19].value.keywords[3].value.elt::Call

Source: `scripts/roadmap_deal.py:97`; AST `c20c125f7500c98b1e9110b282f7886b46f1300c9be9803a8cde67b106477606`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, x. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[19].value.keywords[3].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].handlers[0]::ExceptHandler

Source: `scripts/roadmap_deal.py:98`; AST `99d8b0caeae30848b9c8b22ac5b524b144645a59345cce3cf880a04d7ea18a06`.

Rust module: `scripts::roadmap_deal`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, exc, record, str, type. Outputs/bindings: (none).
Calls/effect boundaries: str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[13].body[6].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].handlers[0].body[0]::Assign

Source: `scripts/roadmap_deal.py:99`; AST `ab79d832db92fe9b2958c28df8cb2022c44eed8b1027f76bdc695227362b8f83`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, record, str, type. Outputs/bindings: (none).
Calls/effect boundaries: str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].handlers[0].body[0].value.values[0].value::Call

Source: `scripts/roadmap_deal.py:99`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].handlers[0].body[0].value.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[6].handlers[0].body[0].value.values[1]::Call

Source: `scripts/roadmap_deal.py:99`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].handlers[0].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::observe::root.body[13].body[7]::Return

Source: `scripts/roadmap_deal.py:100`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Return evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14]::FunctionDef

Source: `scripts/roadmap_deal.py:103`; AST `5bad9f62ef5a7f46ba97cb1e325328c2e79b5c8ff4277a69d122c8f3302502d1`.

Rust module: `scripts::roadmap_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, __doc__, argparse, args, atomic_write_json, confined_path, observe, parser, print, record. Outputs/bindings: args, parser, record.
Calls/effect boundaries: argparse.ArgumentParser, atomic_write_json, confined_path, observe, parser.add_argument, parser.parse_args, print, record.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[0]::Assign

Source: `scripts/roadmap_deal.py:104`; AST `c4ad6d457d8034b25dcc473a40ed9c6629dab3a54fd3b776e18da1d1367bd02c`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: parser.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[0].value::Call

Source: `scripts/roadmap_deal.py:104`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[1]::Expr

Source: `scripts/roadmap_deal.py:105`; AST `8ed0f27de801f9dec3e0fad110e7d2e80a02910fe7188382daa14e5e02f3778f`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[1].value::Call

Source: `scripts/roadmap_deal.py:105`; AST `dabb15dffe9d399f067e249c5934ba7a3b8ead227150029cb610dd99a27ad883`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[2]::Expr

Source: `scripts/roadmap_deal.py:106`; AST `9da33d77a9d730d1b0a37192c8581046a68572dcd897195379ae8e318be418ad`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[2].value::Call

Source: `scripts/roadmap_deal.py:106`; AST `fec4fbf48af0ce6f50e4b9bb90b76836907b3da18e1361a79d252cbbf372ac6f`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[3]::Assign

Source: `scripts/roadmap_deal.py:107`; AST `6275c8d1600da776fb862cf3f5fef974e2559c70800565172097404dcea6fef6`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: args.
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[3].value::Call

Source: `scripts/roadmap_deal.py:107`; AST `c865e8043798bf46a3b13d6774886772cbfabc2836b109a02aef4d3c2ad2a7ef`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[4]::Assign

Source: `scripts/roadmap_deal.py:108`; AST `e002250987f81ebe280f91c325c98221a12dd1008e366d0a3237217612b1c9a2`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, observe. Outputs/bindings: record.
Calls/effect boundaries: observe.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[4].value::Call

Source: `scripts/roadmap_deal.py:108`; AST `011507cb33bdbd72147f6829e5df5f0de0bdc59a40b607f4a66bd62f5de39ab8`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, observe. Outputs/bindings: (none).
Calls/effect boundaries: observe.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[5]::Expr

Source: `scripts/roadmap_deal.py:109`; AST `2788f7d1a826115b2255675302e6c2cd93f4df2a5223f3eaecb94d4c11b4b788`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, atomic_write_json, confined_path, record. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[5].value::Call

Source: `scripts/roadmap_deal.py:109`; AST `1209d46f3f10722f678ef162b5edbdfa00556b405784c29b195e774046189b74`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, atomic_write_json, confined_path, record. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[5].value.args[0]::Call

Source: `scripts/roadmap_deal.py:109`; AST `bd2c4103df935f33b6c3362a61ace084743aa0c8c3bc6058f572e1ed907f0aa0`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[6]::Expr

Source: `scripts/roadmap_deal.py:110`; AST `b5dd8c3bdad3b482d3700b634d17115f9f311add244f7cac83eeeab98e30a249`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: print, record. Outputs/bindings: (none).
Calls/effect boundaries: print, record.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[6].value::Call

Source: `scripts/roadmap_deal.py:110`; AST `ccd1fdce14b47bbdc67f4f4c46e14317185692f7f2d16978198ad19e9459f094`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: print, record. Outputs/bindings: (none).
Calls/effect boundaries: print, record.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[6].value.args[0].values[3]::Call

Source: `scripts/roadmap_deal.py:111`; AST `293d9f793b5b16a7581beb55da06cd1f9b787c4e150c06e06f01cd5ab726864d`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::main::root.body[14].body[6].value.args[0].values[4]::Call

Source: `scripts/roadmap_deal.py:111`; AST `adbe94c313cfea696b9d4815e69cda9e73f594f8fa9bb0a2ab61bd5a0e6a19b2`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[15]::If

Source: `scripts/roadmap_deal.py:114`; AST `3340fd16ba41ba1ddf3989cd136a498b72a97f7796e0f7fad6e815585dbc1c52`.

Rust module: `scripts::roadmap_deal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered If evaluation at root.body[15]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[15].body[0]::Expr

Source: `scripts/roadmap_deal.py:115`; AST `26412f54b9dfeb741e0d31e60ab8bd5c087bc77b2e3192f46a2fa84cd9152b86`.

Rust module: `scripts::roadmap_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_deal.py::module::root.body[15].body[0].value::Call

Source: `scripts/roadmap_deal.py:115`; AST `612de6187c097f49a7c6002bfa6b205845dac081e9c3dc6b160fd9a6f584c826`.

Rust module: `scripts::roadmap_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, ast, astroid, deal_solver, deal_solver._exceptions, importlib.metadata, pathlib, sys, z3.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
