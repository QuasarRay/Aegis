# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 200. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_portability.py::module::root::Module

Source: `infra/agentinfra/roadmap_portability.py:1`; AST `6b45789e8eddf39e6687123bc52cf3ba5150538ea92138f67e472c5fc2588060`.

Rust module: `infra::agentinfra::roadmap_portability`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BLOCKS, PATTERNS, Path, ROOTS, a, ast, calls, canonical, child, dict, digest, effects, enumerate, field, fields, files, getattr, hasattr, i, imports, index, int, invariant, isinstance, k, kind, len, length, lib, libraries, lines, list, maintained_python, max_bytes, n, name, names_in, names_out, next_owner, node, override, overrides, overrides_path, owner, p, parts, path, pending, proposal, raw, read_json, record, relative, require, root, route, set, size, sorted, source, str, tree, tuple, type, u, unit, units, v, value, visit. Outputs/bindings: BLOCKS, PATTERNS, ROOTS, a, calls, child, effects, field, fields, files, i, imports, index, invariant, k, kind, length, lib, libraries, lines, n, name, names_in, names_out, next_owner, override, overrides, overrides_path, p, parts, path, pending, proposal, raw, relative, size, source, tree, u, unit, units, v, value.
Calls/effect boundaries: ', '.join, '; '.join, '\n'.join, (root / name).rglob, PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.parse, ast.unparse, ast.walk, canonical, digest, enumerate, files.append, getattr, hasattr, isinstance, len, libraries.items, lines.extend, maintained_python, override.get, override.items, overrides.get, overrides['units'].get, overrides_path.exists, p.is_symlink, parts.items, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, pending.append, raw.splitlines, read_json, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, tuple, type, unit.update, units.append, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:1`; AST `9edc05090754d2b0044035557d793dba4fe9999077dced372e68b38fbfd4b63e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_portability.py:4`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:7`; AST `6c0b999a4dc63c099720f0d89b9447455ab13475e75a0d921f92f7d6b89b6a7a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:10`; AST `4d7236569a281e304dec328f8020429a47e2dd70146fb72c4ad3facb6e230a0c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: ROOTS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:11`; AST `23111c155d9d1305f2045b6e286e884f6759717cbd323f586004e57e2b894d81`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: PATTERNS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[7]::Assign

Source: `infra/agentinfra/roadmap_portability.py:34`; AST `7edb7b39a0f380b1ebba400f88dd4f30f01142c5c202774f61d8d19a380e720a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PATTERNS, ast, getattr, hasattr, n, tuple. Outputs/bindings: BLOCKS, n.
Calls/effect boundaries: getattr, hasattr, tuple.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[7].value::Call

Source: `infra/agentinfra/roadmap_portability.py:34`; AST `c9cd933bdd1e1eae78c66d697d152174f139bbf99d5ad79ab40e26490a06ce29`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PATTERNS, ast, getattr, hasattr, n, tuple. Outputs/bindings: n.
Calls/effect boundaries: getattr, hasattr, tuple.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[7].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_portability.py:34`; AST `66ec03446351f0d3a78b6136c2f4ef6642de1d30cbe59ee160cca285b743a5c3`.

Rust module: `infra::agentinfra::roadmap_portability`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: PATTERNS, ast, getattr, hasattr, n. Outputs/bindings: n.
Calls/effect boundaries: getattr, hasattr.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[7].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_portability.py:34`; AST `34a9448fc48e1cf1860d7b6c56869755da96bc301950bdb415b6b9a8b6412a15`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, getattr, n. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[7].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:34`; AST `a9ca879dfffe8d226240b522c3d9889b9682db05f63f7ed735a3f30d997e5741`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, hasattr, n. Outputs/bindings: (none).
Calls/effect boundaries: hasattr.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[7].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[8]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:37`; AST `c10621859d62eb628b6d33b883eb399440d00c4cf47bfbf85a6dcee361755715`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOTS, list, name, p, root, sorted. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[8].body[0]::Return

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `7227d774754b00bad91fada8e1079b8f2d5df206d485ff44d5b4703b6964cb23`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOTS, name, p, root, sorted. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `bcd3d953fb0e3fd40239738aa521938e48193485881e8728ebdaf35ad8d96b0c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOTS, name, p, root, sorted. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[8].body[0].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `ff9ac1f941864e10f8eca0d8998d32fd39e1e1310b127e510d70da7ce77f5952`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ROOTS, name, p, root. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[8].body[0].value.args[0].generators[1].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `bdd13823e887a09994643e0b04325038502dc5e335f380e5c0c5a7d93853375c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, root. Outputs/bindings: (none).
Calls/effect boundaries: (root / name).rglob.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].generators[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[8].body[0].value.args[0].generators[1].ifs[0].values[1].operand::Call

Source: `infra/agentinfra/roadmap_portability.py:39`; AST `e9cab480c97fe5effaf0b2cd191d671f332cea8d0957cd0f4ecd6d4870d0f0db`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_symlink.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].generators[1].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:42`; AST `30e9dcd1c6c4b8ae58e8450544f3180c333b1d5de9e86e6af25f36154a212d95`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BLOCKS, PATTERNS, Path, a, ast, calls, child, dict, digest, effects, enumerate, field, fields, files, getattr, i, imports, invariant, isinstance, k, kind, len, lib, libraries, list, maintained_python, n, names_in, names_out, next_owner, node, override, overrides, overrides_path, owner, path, proposal, raw, read_json, relative, require, root, route, set, sorted, source, str, tree, type, u, unit, units, v, value, visit. Outputs/bindings: a, calls, child, effects, field, fields, files, i, imports, invariant, k, kind, lib, libraries, n, names_in, names_out, next_owner, override, overrides, overrides_path, path, proposal, raw, relative, source, tree, u, unit, units, v, value.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.parse, ast.unparse, ast.walk, digest, enumerate, files.append, getattr, isinstance, len, libraries.items, maintained_python, override.get, override.items, overrides.get, overrides['units'].get, overrides_path.exists, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, raw.splitlines, read_json, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:43`; AST `90a6c094b354d27312545b39da72412f10c8285131322d35965aa0ba3a6b09c9`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: files, units.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:44`; AST `eef9b44734747afa7024306e763477fd62c460ae7851a92e1b3132edc8f110f9`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: overrides_path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:45`; AST `72312fdc3ffff844f0688512ae36e5a719b7f56c72dfff75ef5de4a9a89f4fab`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides_path, read_json. Outputs/bindings: overrides.
Calls/effect boundaries: overrides_path.exists, read_json.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[2].value.test::Call

Source: `infra/agentinfra/roadmap_portability.py:45`; AST `9cca35c10f2d4f6cd17f52e0aa77e76e747480b3f24f4f0ce30c9e1758c20236`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides_path. Outputs/bindings: (none).
Calls/effect boundaries: overrides_path.exists.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[2].value.body::Call

Source: `infra/agentinfra/roadmap_portability.py:45`; AST `acdae178c25d831c8260a315e6cb6ae9b0bcdb404812a3b0659dcef69a6ce7b8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides_path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:46`; AST `671e21879a9b6e8d5297566746e261ecc696e7d01c9f2df44657e89322875d41`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides, require. Outputs/bindings: (none).
Calls/effect boundaries: overrides.get, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:46`; AST `057e2ae28778da13e699e8aaf1b7232ebf098d980ffd1530ca293125035de920`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, require. Outputs/bindings: (none).
Calls/effect boundaries: overrides.get, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:46`; AST `0c1eb0551fb6a7d3ce50e6c94bfa4ee7a8492ae038ffe79042116f71cb2c07dd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides. Outputs/bindings: (none).
Calls/effect boundaries: overrides.get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4]::For

Source: `infra/agentinfra/roadmap_portability.py:47`; AST `90fb70e682c5a7e4266930f94a64b05e14b9a0ae888122c5c87049070e48b481`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: BLOCKS, PATTERNS, a, ast, calls, child, digest, effects, enumerate, field, fields, files, getattr, i, imports, invariant, isinstance, k, kind, len, lib, libraries, list, maintained_python, n, names_in, names_out, next_owner, node, override, overrides, owner, path, proposal, raw, relative, require, root, route, set, sorted, source, str, tree, type, unit, units, v, value, visit. Outputs/bindings: a, calls, child, effects, field, fields, i, imports, invariant, k, kind, lib, libraries, n, names_in, names_out, next_owner, override, path, proposal, raw, relative, source, tree, unit, v, value.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.parse, ast.unparse, ast.walk, digest, enumerate, files.append, getattr, isinstance, len, libraries.items, maintained_python, override.get, override.items, overrides['units'].get, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[9].body[4]; no call, error or mutation may be omitted. Iteration: path in maintained_python(root)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:47`; AST `ebe3343fcce41557451c3ee0c98810e3fb3b8c363ee8f3dc1f06b697298b0596`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: maintained_python, root. Outputs/bindings: (none).
Calls/effect boundaries: maintained_python.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:48`; AST `c9a5d02444369221b50b662c72fded4efbbded9a1bf01f8bacecd9d7badf680c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, root. Outputs/bindings: relative.
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:48`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:48`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:49`; AST `cb5aaaf42a08c91666ce0e4859112cf066cdeebf56910b462a58b24332914278`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: raw.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:49`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:50`; AST `14d1cbc39c65636461267a28fac89eae79afd1a9c3719f12ca278873c196fdb6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, raw, relative. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:50`; AST `1c71510402688fc66f9f18274201ccd890bc521b89fde860e421ef3d24826eab`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:51`; AST `a0409c055ff3c2a219199795d4be0eefb79f7d601517390cea92afd386e07a27`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, files, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: digest, files.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:51`; AST `7f92c1717b0088be29e549a5d013cc155b2cd545479363038b647d2821ae2646`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, files, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: digest, files.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:51`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `15c6440df8c5f19bea783323cf490d8707b0489ed136d30c695dc1ff39c1c9c0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ast, isinstance, n, sorted, tree. Outputs/bindings: a, imports, n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `519e357672fce79a71c99b7276463d101c90fd063e69cb8d9b649abf83d0af38`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, ast, isinstance, n, sorted, tree. Outputs/bindings: a, n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `4f768a0365389e1c92649eb94488efc3d781fc38fafda131ccc6c1c7e3b25514`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, tree. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[4].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value.args[0].left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value.args[0].left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value.args[0].left.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `52edc674ca61c4e36a3426e46d14df197a6820006835ec8e49b980d7d0c36bea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value.args[0].left.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value.args[0].right::SetComp

Source: `infra/agentinfra/roadmap_portability.py:53`; AST `22e12de18f55e3fd31d22c54a9483b6e1804179ee083152d6f65c44cb572f45e`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, ast, isinstance, n, tree. Outputs/bindings: a, n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[4].body[4].value.args[0].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value.args[0].right.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:53`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value.args[0].right.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[4].value.args[0].right.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:53`; AST `496d46f79aca0b6694f6f8aa40d9d5327eabf2d2b3881871ee0407f17c12d937`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value.args[0].right.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:55`; AST `5bdbc50af7807096b773b2137c8d37c0599416faa270dd359a6e766f4d8b8f86`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BLOCKS, PATTERNS, ast, calls, child, digest, effects, enumerate, field, fields, getattr, i, imports, invariant, isinstance, k, kind, len, lib, libraries, list, n, names_in, names_out, next_owner, node, override, overrides, owner, proposal, raw, relative, require, route, set, sorted, source, str, type, unit, units, v, value, visit. Outputs/bindings: calls, child, effects, field, fields, i, invariant, k, kind, lib, libraries, n, names_in, names_out, next_owner, override, proposal, source, unit, v, value.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.unparse, ast.walk, digest, enumerate, getattr, isinstance, len, libraries.items, override.get, override.items, overrides['units'].get, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:56`; AST `aeb8c7294e40fa6069655169831da75e125397d372c5e046c7324cb842ac5a13`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner. Outputs/bindings: next_owner.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[1]::If

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `aeddaae2bf74b82a248ae1303ce72674dec481d2cac31ba4b4723badd34df959`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node, owner. Outputs/bindings: next_owner.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[1]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[1].test::Call

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `03f4d863af03611234c7247b6ee125dada11915164b7ebf16339435bb5a26fde`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:58`; AST `47f667885c9b8cab2f2391ed7cb48151287e7738be5e34e3b73b26b9ec505c0d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, owner. Outputs/bindings: next_owner.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2]::If

Source: `infra/agentinfra/roadmap_portability.py:59`; AST `0cf709aa21ba3bd36a3730c761dc27a39dbca723aac4f6e43dbb4ec0fac16ca6`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: BLOCKS, PATTERNS, ast, calls, digest, effects, fields, getattr, imports, invariant, isinstance, k, kind, len, lib, libraries, n, names_in, names_out, next_owner, node, override, overrides, proposal, raw, relative, require, route, set, sorted, source, type, unit, units, v. Outputs/bindings: calls, effects, fields, invariant, k, kind, lib, libraries, n, names_in, names_out, override, proposal, source, unit, v.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.unparse, ast.walk, digest, getattr, isinstance, len, libraries.items, override.get, override.items, overrides['units'].get, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[2]; no call, error or mutation may be omitted. Condition: isinstance(node, BLOCKS) or isinstance(node, ast.stmt)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].test.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:59`; AST `b995adca511acc0fdc2469d2378b0b07f22a9c53713efead10f373bb5c55c933`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BLOCKS, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].test.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:59`; AST `e2bf93f2a9fbb0ec1d60a97184ee8f38d6b9356ea52441475e25c1a753382661`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:60`; AST `376758b2e642b07775831af0b29699bdf85bf7ec83a7ecaee8437b472c5f273b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, type. Outputs/bindings: kind.
Calls/effect boundaries: type.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[0].value.value::Call

Source: `infra/agentinfra/roadmap_portability.py:60`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `5c2cbb8ee8b3b622c144e77188a1bda0da2fd2052f990d96d8ac50e9944a58da`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n, names_in.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `c9d09a0d3e566624b56c69ad100118af486759121aa0554e69f87ddfe2c5269c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[1].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `17afd473726c5a678c32adc3cc8a96a8b31e262e8021ccf924ac11383cf08c54`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[4].body[5].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[1].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[1].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `4ce1a533696addd77247fef745b07cd543b5c26836077f5c88931ecde16ee2a4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `59f0d4aa6f7a1a18af1d35baf29ff5cdef611b8ce7b9b2f0126a9598271fc62c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `335acc0c40ceeed7848058ff4fe25b684b6700f5ee6f9f55c11d3f303569faa8`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n, names_out.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `940a93eabfa057790c473f67a142ecd50591b3beb1a71497a0ae634a7c9834db`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[2].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `eb7831f9922987a45b31c04d6ce7c3a0aade097c89a7241da28ca7f191ef6167`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[4].body[5].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[2].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[2].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `4ce1a533696addd77247fef745b07cd543b5c26836077f5c88931ecde16ee2a4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `5f001159691f54aea19f198a393bbdbfe698328fc76a38534361c7af35bc3ddd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `a86e3420d469e4dbffb250abce2c9c563f5c76b337a3936ef5153abfa2437aa3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: calls, n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `8a7f514d6474230e891f4a4e86910c94e4a90221ef1c161990fd26e064ceb86d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[3].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `b28d31c16e535d7d6d83960a7a0b58226ee0b45fee19949fa9e731670bd978c1`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[4].body[5].body[2].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[3].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `d37398c81d3e6778e173e0fabe4b6a4f1ccdff3685fe8d32f06e0aa03e719370`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[3].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[3].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[3].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[3].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[3].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:64`; AST `ed72708867a1c6fc476ac17795e1df2c658dad0fd9deccc4e2bc887bbaf9331c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PATTERNS, kind. Outputs/bindings: proposal.
Calls/effect boundaries: PATTERNS.get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:64`; AST `0695e0c1cb211fa7dcd91ccaac0c33145e2ce78a6b9f209014cb4e5d13688599`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PATTERNS, kind. Outputs/bindings: (none).
Calls/effect boundaries: PATTERNS.get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `8048819bb13fa216be8b931209ed2587518272999ac993b40cd72c086662d426`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: effects, n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `52cdb3991ddaba7230122c8d524fa2e151aa72d4ea5917fce43e64ad5ae8140d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[5].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `45b74ddd3e455cbac6a5745e2e8f189d72cd3a13c79cfda24eac6542cfab12d6`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[4].body[5].body[2].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[5].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `2b61e5decfd609e82d91ed65f92b014a281c19986d2bb625356b5e6a69a6ec6e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[5].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[5].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[5].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[5].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `5b78f524d545185ae95c46ca9ec96e6c4f9394bfd7137b82122cd2a7a21e87ea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[5].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `3074d8635e8eebd9f572d8c5f1bc5a152ce7f0a767e75b1e9c350340d88a8a9a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: libraries.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[7]::Assign

Source: `infra/agentinfra/roadmap_portability.py:73`; AST `2b5f347c335fcaeea42147b66ba5b6acb2edd07340d8677eab01fe65bdb9b7d6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kind, route. Outputs/bindings: invariant.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[8]::If

Source: `infra/agentinfra/roadmap_portability.py:74`; AST `f3289b71d97c382fcb95e6df2a3525aa35a7a044be36cfdfaed4e8b26aceead8`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[2].body[8]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.If, ast.While))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[8].test::Call

Source: `infra/agentinfra/roadmap_portability.py:74`; AST `1927d8456fe888e91df9776a3bb4b2f16582ee1dd48e9f3d60d7af2d33a0dc90`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[8].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[8].body[0]::AugAssign

Source: `infra/agentinfra/roadmap_portability.py:75`; AST `41e9159d21fe1dfde7d298dde26d49c9a4f72d60c89d6719be1bc88397bad19c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered AugAssign evaluation at root.body[9].body[4].body[5].body[2].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[8].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_portability.py:75`; AST `c18b20fc6a931aa1203440f1f8b4c0265224667054888e8fa512b84ef0e52745`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[8].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[9]::If

Source: `infra/agentinfra/roadmap_portability.py:76`; AST `4590a674f66719cf34b95a9e7d3a90901c62b0906802df03f5f5fa761737d372`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[2].body[9]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.For, ast.AsyncFor))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[9].test::Call

Source: `infra/agentinfra/roadmap_portability.py:76`; AST `34e9b2cb8ebf80d43c80578f8e9262e62ecd98636232d0a1169061045b0d5d6c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[9].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[9].body[0]::AugAssign

Source: `infra/agentinfra/roadmap_portability.py:77`; AST `58deffa8bc2b492ad3162467fc60784ac3665ee24f7c210a17afa2f9bb60da25`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered AugAssign evaluation at root.body[9].body[4].body[5].body[2].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[9].body[0].value.left.left.right::Call

Source: `infra/agentinfra/roadmap_portability.py:77`; AST `bc6add1b97d423a6645739f36aa98f7316ecc56a99043994541a5d45ce7cff7e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[9].body[0].value.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[9].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_portability.py:77`; AST `f9be1754c1227970de354dc4b31bbcdfcca3518fc52e79c548a9fc12de9f1dc8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[9].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10]::Assign

Source: `infra/agentinfra/roadmap_portability.py:78`; AST `8011d4582cca4f8781b7ea78d194a87e163d0f068c80808dc19dc50dcccb1add`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, calls, digest, effects, getattr, imports, invariant, kind, len, lib, libraries, names_in, names_out, next_owner, node, proposal, raw, relative, route, source. Outputs/bindings: lib, source, unit.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest, getattr, len, libraries.items, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:79`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[3]::Call

Source: `infra/agentinfra/roadmap_portability.py:79`; AST `7e015840e16c88c823dd5259f4b55423b299ef9fa3c5de015b0073b6888bb2fb`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[3].args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:79`; AST `62642a7f86696182149656fb0833b390cc3f67cf8dd17c2b5151717295dc243e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[3].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:79`; AST `3fb94b2b8e1dc6a1bc206dc19bca3c2e71190137190d141090f14ace7aaa9d73`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[3].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:80`; AST `ccefd2bb5e25c3c40bb9fccc5f34ff179c59a0845b3ae29f825ddcd9f81afbcd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, node. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:80`; AST `c331789f037f08c0f906694e60140e82b9e02ec9a8e33a91a8f245bc525c4185`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, len, node, raw. Outputs/bindings: (none).
Calls/effect boundaries: getattr, len, raw.splitlines.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[1].args[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:80`; AST `47e2ce18890fe3dce0f518f5b24f3b83f3042f750aaef69e50f25bc7af5d7d1d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len, raw.splitlines.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[1].args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[1].args[2].args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:80`; AST `cdbc843ce77bcc95a6c9708e311d0f275743d081107aed5c5b33b34b08a7178b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.splitlines.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[4].elts[1].args[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[11]::ListComp

Source: `infra/agentinfra/roadmap_portability.py:83`; AST `329ba7608484fee5442d961d9e9c030c589b18743b987c35c182a2b444f4841f`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: imports, lib, libraries, source. Outputs/bindings: lib, source.
Calls/effect boundaries: libraries.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered ListComp evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[11].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:83`; AST `bbcad9c952da994d6bdad031f0425fac2a2a6a39ad6b745bfee5abf0abecda66`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: libraries. Outputs/bindings: (none).
Calls/effect boundaries: libraries.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[11].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[13]::Call

Source: `infra/agentinfra/roadmap_portability.py:84`; AST `35b73a3b161a22835375d116155b2c1ebea7855ee7ef79683dd86213e4cbb9ea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removesuffix, relative.removesuffix('.py').replace.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[10].value.values[13].func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:84`; AST `04012b32da117e0853b4f15077bb8158d9a58d0112f7993f469f181bfc80f38b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removesuffix.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[10].value.values[13].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[11]::Assign

Source: `infra/agentinfra/roadmap_portability.py:92`; AST `372e235dbe87bf361126a98c6dd517fc3b0c7b11308b5ba159fcf143a11d430e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides, unit. Outputs/bindings: override.
Calls/effect boundaries: overrides['units'].get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[11].value::Call

Source: `infra/agentinfra/roadmap_portability.py:92`; AST `66592063ae5d2b8e35a9b57f5d5f1912e54eb7f9e07468ad08202b66a601cb3f`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, unit. Outputs/bindings: (none).
Calls/effect boundaries: overrides['units'].get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12]::If

Source: `infra/agentinfra/roadmap_portability.py:93`; AST `0dbca37045cf548377b32929db10ac0df28c2c4cd589ef7376428dc922a8fa1a`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: fields, k, override, require, set, unit, v. Outputs/bindings: fields, k, v.
Calls/effect boundaries: override.get, override.items, require, set, unit.update.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[2].body[12]; no call, error or mutation may be omitted. Condition: override
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:94`; AST `d1119a31140eba9d5f90037cd177bd9485ef4da3cb94dcc61e04f0d4ada85b25`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: override, require, unit. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5].body[2].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:94`; AST `11cac8b4e0f7bf1f4525cb834fbb5b55462c8e33f1312043a42e5d173aa3f873`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override, require, unit. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:94`; AST `f944e5d0736f3756a4689fd2de598221b7aceb5821d5498f0cb75f540ca44157`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:94`; AST `d5123be86d221ada39cdd42a4e89583104d8d5c1f53af3bb4dd2e52de598b461`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:95`; AST `b3d816531a439e0353293a5dd7533e714b7a2365b388ac4fa7e99417e152ca5d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: fields.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[2]::Expr

Source: `infra/agentinfra/roadmap_portability.py:96`; AST `ab6693562eec34bf31d5633ff276726e7efcf7274704240b6e4cb8e863b03a40`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, override, require, set. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require, set.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5].body[2].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:96`; AST `ae661d434af5b75015a26f2a850c3d0008dfddbe780971bb1516395b413a4c25`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, override, require, set. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require, set.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:96`; AST `cb1a7e686a5034da28ca1791a7d883bd58eba59e2368304b7b986f955c512b94`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:96`; AST `f9370e5d53318114203af0a6b83ef10439f7a552fd4b1ad214a6e62fba6b4804`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.get.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:97`; AST `8f8b24dc9167079078b4b8e0b2e7d3997f952e4c04c7d90e1e344d17495e6d6a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, k, override, unit, v. Outputs/bindings: k, v.
Calls/effect boundaries: override.items, unit.update.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5].body[2].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:97`; AST `0abe98663ebcbf7174dbbcc69f0e4090df79230c199eaffe33c653d93e259b28`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, k, override, unit, v. Outputs/bindings: k, v.
Calls/effect boundaries: override.items, unit.update.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[3].value.args[0]::DictComp

Source: `infra/agentinfra/roadmap_portability.py:97`; AST `91313c7928045c15f4b3b9fb77ff7b21754df8640767eaf17b15e047aea008f6`.

Rust module: `infra::agentinfra::roadmap_portability`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: fields, k, override, v. Outputs/bindings: k, v.
Calls/effect boundaries: override.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered DictComp evaluation at root.body[9].body[4].body[5].body[2].body[12].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[3].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:97`; AST `3eede006f5d161df1d034bc8de3cff772ef59c52037817866699b65850d00108`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[12].body[3].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:98`; AST `b75049395c98da5c450286ef8f50b9890bf87ff14db0f7bd47a2b85999424e2e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: override, unit. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[5].body[2].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[13]::Expr

Source: `infra/agentinfra/roadmap_portability.py:99`; AST `80a859dc4d7d22fe0d0ffdc8cf8e95938089d12d68e0a29d4c42dcf2be53a383`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unit, units. Outputs/bindings: (none).
Calls/effect boundaries: units.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5].body[2].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[2].body[13].value::Call

Source: `infra/agentinfra/roadmap_portability.py:99`; AST `1d22c0d6d427ef708f23cb2bc1822fd2339d707f6b48e16181a065d37d130474`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit, units. Outputs/bindings: (none).
Calls/effect boundaries: units.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[2].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3]::For

Source: `infra/agentinfra/roadmap_portability.py:100`; AST `7dbbdf94540821b6ca8608d25ebb9ee63fa2ec8585d502683d385d3400b7ce8d`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, child, enumerate, field, i, isinstance, list, next_owner, node, route, value, visit. Outputs/bindings: child, field, i, value.
Calls/effect boundaries: ast.iter_fields, enumerate, isinstance, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[9].body[4].body[5].body[3]; no call, error or mutation may be omitted. Iteration: (field, value) in ast.iter_fields(node)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:100`; AST `09b6e3b003896a4fa601486a87b76cab47e19e25562c99483afd9a0fa4af0043`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.iter_fields.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_portability.py:101`; AST `237cb01ad52ff4d173955e4350bc5131265c652f9b80dcdbcffc70cf01b21a5a`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, enumerate, field, i, isinstance, list, next_owner, route, value, visit. Outputs/bindings: child, i.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[3].body[0]; no call, error or mutation may be omitted. Condition: isinstance(value, ast.AST)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].test::Call

Source: `infra/agentinfra/roadmap_portability.py:101`; AST `518ae0204e0bc2a7a9a0fdeab27cd350bacc9a97c1a593b3402c0f44457a4dd2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:102`; AST `26cdc8a92d058e8db75544ff1f8d156f045e07b344bb1caa53aa52ae1ea3d2c4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, next_owner, route, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:102`; AST `41b2481bb0f92b2d99e7d1b14c9c88acca2bed6718d95909d8e278967e2bf55d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, next_owner, route, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_portability.py:103`; AST `ca27472712279a088ffe26f4a3855408006880c6ae8ffee9146fa76a54a98b9f`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, enumerate, field, i, isinstance, list, next_owner, route, value, visit. Outputs/bindings: child, i.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(value, list)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_portability.py:103`; AST `f5635b2e334fb6e97f358f32dbb2b0086496303066699278ebd49fcf85562492`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0]::For

Source: `infra/agentinfra/roadmap_portability.py:104`; AST `9f101e75a9617e84d44a85e08e487a7770d138f83b4b500bfc48db3f63c6322c`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, child, enumerate, field, i, isinstance, next_owner, route, value, visit. Outputs/bindings: child, i.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0]; no call, error or mutation may be omitted. Iteration: (i, child) in enumerate(value)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:104`; AST `7319a75af29aa16ce29cee5b47f4824c2eea50c99daf127db96a63b65622d4e7`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, value. Outputs/bindings: (none).
Calls/effect boundaries: enumerate.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_portability.py:105`; AST `2de338419d1104614497ad306df94ac11e0435abf2cdedffa607a1f316a059b1`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, field, i, isinstance, next_owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(child, ast.AST)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0].test::Call

Source: `infra/agentinfra/roadmap_portability.py:105`; AST `bfd7a1d88fedbb3dac987f7a025d0b34fc3cab5882e0033352cecaa2e8492640`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, child, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:106`; AST `6d0d2b285266d5532492c616356135e1a2f3830e05f4733a6169c5a6437ed8ab`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child, field, i, next_owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:106`; AST `2fddc1348ad25f6f859d43c16388ee1946a9f5d9c4cd4f42090e8e1d7a94452e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child, field, i, next_owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[6]::Expr

Source: `infra/agentinfra/roadmap_portability.py:107`; AST `cf5b7f268e71083a292c249902b2e7f6ba9bde87d724e00a88b2abc89ec1e85d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:107`; AST `54d9837e7b8ee2da2a44fcc7b0d9ac2e34afef27ad26515c17ea2951989f198a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[5]::Expr

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `2aeed883cea2019bd96dbc9ad811c0c7dc1e44ebe026b9619d4304bed075431f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, u, units. Outputs/bindings: u.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `99f74107437faaa8878cbb7591c5a2dadb7d600d4353900327c8f56aaee8a54b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, u, units. Outputs/bindings: u.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `8fab30b6203427492d68560cbbe1bcc928799e0969ddeafe764ac4c92e3adca2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, u, units. Outputs/bindings: u.
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[5].value.args[0].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `9d44ba12a05af66e1da558a6a35bb4bf799ffc3eb26e7af15f3ccaf003bdccf4`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[5].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[5].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `d334ac4951312a2e5ce0e7d19e1cf4c4a0351088858089c704b81b4d02ed725c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, units. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[6]::Expr

Source: `infra/agentinfra/roadmap_portability.py:109`; AST `e257ce6d86c5c86320a2b6c7ddc69a9352ea46589a2abe56a75fb3aee4bc955d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides, require, set, u, units. Outputs/bindings: u.
Calls/effect boundaries: require, set.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:109`; AST `0a3e0a8674a80468c5ab08237b635c595a65a5473df3d813bd51033fa14ba814`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, require, set, u, units. Outputs/bindings: u.
Calls/effect boundaries: require, set.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[6].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:109`; AST `65a14c580ddf50b1dd6ee2b51204520784cb5edb1d49bc8e77ee97982b56bbde`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[6].value.args[0].comparators[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:109`; AST `9d44ba12a05af66e1da558a6a35bb4bf799ffc3eb26e7af15f3ccaf003bdccf4`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered SetComp evaluation at root.body[9].body[6].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[7]::Return

Source: `infra/agentinfra/roadmap_portability.py:110`; AST `100b57566810c0c964664dfbf7df779b9c33aa2c7f2eec069be54f046f958d9d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, files, units. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[9].body[7].value.values[4]::Call

Source: `infra/agentinfra/roadmap_portability.py:111`; AST `f446143c5c08ab2b81ba051b93df3be743c4b494c9196d900dbfa98768d1b6aa`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, files, units. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:114`; AST `94bce2652d975ddfeb01cfbfa802512dd038725dbbaec8468898b41105dc852c`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, len, lines, record, str, unit. Outputs/bindings: lines, unit.
Calls/effect boundaries: ', '.join, '; '.join, '\n'.join, len, lines.extend.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:115`; AST `d0eb5455745bbf4c80aa843a7f618906fabc298a7642c0f1c477d3c60af530ed`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record. Outputs/bindings: lines.
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[0].value.elts[4].values[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:117`; AST `df46df88acf5e6ef901488c4610d14a5b71f816377a047e8ea3cd040d31bfe4e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.elts[4].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[0].value.elts[4].values[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:117`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.elts[4].values[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1]::For

Source: `infra/agentinfra/roadmap_portability.py:119`; AST `77a62c393e6c915f44bcb6c30dc0f1015e65da910cc2acc3af49ef923439ec33`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: lines, record, unit. Outputs/bindings: unit.
Calls/effect boundaries: ', '.join, '; '.join, lines.extend.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[10].body[1]; no call, error or mutation may be omitted. Iteration: unit in record['units']
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:120`; AST `7214c7ce317834d6cbe4b960b79b5d796e3392d39ca0fa87d4d80375949cac1e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lines, unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join, '; '.join, lines.extend.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:120`; AST `2f1e236c8398f68b266600a683dce712520e40f7173635fe4f096f0abb91dae5`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lines, unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join, '; '.join, lines.extend.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[6].values[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:122`; AST `3aa75dfcd6cf2d291b6ec84458f21047b34b2f04bf0804e36248fda78c60ba78`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[6].values[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[6].values[3].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:122`; AST `7c3780615bb5771e4ca9f5d087ce504e83d0dd79897dffbb1140aaf0a363213c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[6].values[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[7].values[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:123`; AST `726fa29e3f627d9e668c1ad09509678d21692d5ba1e15adc192cffd096842a03`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[7].values[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[8].values[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:124`; AST `d79bc397e6a9ef3e4311a110e7c7ff8ee0a8612018f2bb343e54ea0fb5727365`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[8].values[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[10].right::Call

Source: `infra/agentinfra/roadmap_portability.py:125`; AST `a30df28dce224c0c9b901371b5549363fbffb5cb321af3076afc461dcf537390`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[10].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[11].right::Call

Source: `infra/agentinfra/roadmap_portability.py:126`; AST `f2928483541b170613d9c1ea7ce91addc0f1d24fe94957326a7bf64fa21dee39`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[11].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[12].right::Call

Source: `infra/agentinfra/roadmap_portability.py:127`; AST `d47f35417844d1e678c0f992bb2cf326884e436dfd849df789635a9cd2b36bcb`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[12].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[1].body[0].value.args[0].elts[18].left.right::Call

Source: `infra/agentinfra/roadmap_portability.py:129`; AST `957fbb11409ac5db1d3c88efc016095c3d41048da646a57d9d02824ccd9338ce`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].elts[18].left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[2]::Return

Source: `infra/agentinfra/roadmap_portability.py:130`; AST `183ef5d77c056458d553680b183e97de67803fa0aafc226ee5a655c9c44c4c28`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lines. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[10].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:130`; AST `4fffb99bc7d4169bb6278b954681e4ff82ab160a1898ea7351b0ad0db5c4cbd1`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lines. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:133`; AST `88fd58db2dce99b653c6874bcf4428179f2c8c5379b1ba8cfe9ab8c0986d3b04`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: canonical, dict, digest, index, int, len, length, max_bytes, name, parts, pending, record, require, size, str, tuple, type, unit, value. Outputs/bindings: index, length, name, parts, pending, size, unit, value.
Calls/effect boundaries: canonical, digest, len, parts.items, pending.append, require, type.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:134`; AST `1b9cb15e98ee7800b8724a15eb7a15bb56e3a29bdeb9e109487c36e890e0832d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:135`; AST `98975d602361a0e91087677e9f46b6c32db77945afb23b5426b1b55d52ba5e94`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, max_bytes, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:135`; AST `a1140d0ecd373cf63e3e5d2014e09948f45a9048d35b9dbd4ed939f3c47a383e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, max_bytes, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:135`; AST `c99ed4947b38c030b13015cab080bcc1db01a4478b079df565678d930d284956`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max_bytes, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:136`; AST `60bb05a5335c369bbcfa4bb83080a0c7ff71b283b64e910b7a83df6d495c5547`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: parts, pending, size.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3]::For

Source: `infra/agentinfra/roadmap_portability.py:137`; AST `451e71c8f6f9d2f58014f6b550d8944be9ab98e06ebd427842a5db2791a93ada`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: canonical, len, length, max_bytes, parts, pending, record, require, size, unit. Outputs/bindings: length, pending, size, unit.
Calls/effect boundaries: canonical, len, pending.append, require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered For evaluation at root.body[11].body[3]; no call, error or mutation may be omitted. Iteration: unit in record['units']
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:138`; AST `d64b2c09565ec621cfa1cdcd97cd4eb43027a8b91dbc8cf125e1a61b5e5b9b7e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, len, unit. Outputs/bindings: length.
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[0].value.left::Call

Source: `infra/agentinfra/roadmap_portability.py:138`; AST `190357797879b5c3468a911a0e4690cbb83ffe2fc7ee146cb112e2fa6c408172`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, unit. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[0].value.left.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:138`; AST `df4d83f2dfe250fd034b95293eb762500b931b51e045651dfd07ee8dd195d2c6`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, unit. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:139`; AST `7c8ea856d648f6738579642233fe0a2da47e19371edee864228d77226480b64c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: length, max_bytes, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:139`; AST `70f69a5133597dcfafb0b66d7841363d125024931ab233ad912be065b373cd39`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: length, max_bytes, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[2]::If

Source: `infra/agentinfra/roadmap_portability.py:140`; AST `ea4ffd0c13cdbf824330e4d89c09a2c285af91867583228f2fc49789a8f15231`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: len, length, max_bytes, parts, pending, size. Outputs/bindings: pending, size.
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[2]; no call, error or mutation may be omitted. Condition: pending and size + length >= max_bytes
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:141`; AST `8977d12a9a8ecaf1befcb8225840b9a111d12ce592abb77cd397f1cb7618762f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, parts, pending. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[2].body[0].targets[0].slice.values[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:141`; AST `059b0e4f7177f35990c6a2d1d8eee991b362a7579d462eedd70a67c44c33444a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, parts. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].body[0].targets[0].slice.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:142`; AST `0e6653873e82ee91e1af3c57b42dc4227a8fb4a7edaa332609a70d1878cdbd51`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: pending, size.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:143`; AST `3032c119739567217ee6562abdd56c2a33c22c2571176b0a2b13ce9792d92037`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending, unit. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:143`; AST `e7b38fe3839fdca844a1a3b32b8cebcfff2db2040db1703639efa945c0567860`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending, unit. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[3].body[4]::AugAssign

Source: `infra/agentinfra/roadmap_portability.py:143`; AST `94ddd76ec1170e4ab07f01f8866e2fd045c2c8caf691a1d620eea3eabbefa000`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: length. Outputs/bindings: size.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered AugAssign evaluation at root.body[11].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[4]::If

Source: `infra/agentinfra/roadmap_portability.py:144`; AST `818310a9578369e87e4736f2573f631356fedaf0e824ab5a762cb6b5a96afd56`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: len, parts, pending. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered If evaluation at root.body[11].body[4]; no call, error or mutation may be omitted. Condition: pending
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:144`; AST `8977d12a9a8ecaf1befcb8225840b9a111d12ce592abb77cd397f1cb7618762f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, parts, pending. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[4].body[0].targets[0].slice.values[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:144`; AST `059b0e4f7177f35990c6a2d1d8eee991b362a7579d462eedd70a67c44c33444a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, parts. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].targets[0].slice.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:145`; AST `8bb4fdf22c800953938ac0b6e0f260fe58095e9880d40ab3803e29951178b955`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, len, name, parts, record, value. Outputs/bindings: index, name, value.
Calls/effect boundaries: digest, len, parts.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[5].value.values[4]::Call

Source: `infra/agentinfra/roadmap_portability.py:146`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[5].value.values[6]::ListComp

Source: `infra/agentinfra/roadmap_portability.py:147`; AST `39dda19efba106eb481a9efcc2261096c57de6da03d60f274b6c13ecc5a46b3e`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: digest, len, name, parts, value. Outputs/bindings: name, value.
Calls/effect boundaries: digest, len, parts.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[5].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[5].value.values[6].elt.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:147`; AST `f5478a66fd3247b8968c1306f6cc686ba6a06ab0db4348065f96da8baff25481`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, value. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].value.values[6].elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[5].value.values[6].elt.values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:147`; AST `713329791aec59f53add5caf311c586cba099b711d44eb59dd19773ebb41188f`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].value.values[6].elt.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[5].value.values[6].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:148`; AST `2141119718c6153bf438d761a03d90f528922a00b6347b49ce2232dc5bc7f360`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.items.
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].value.values[6].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[11].body[6]::Return

Source: `infra/agentinfra/roadmap_portability.py:149`; AST `621d0d10fd5acd4378f7bca76335de4bbc01b31f0b1dbcdab94b30cbb24f08e4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, parts. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_records.

Invariants: Preserve ordered Return evaluation at root.body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
