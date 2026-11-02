# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 466. Inventory digest: `cf08f3caf7713cec3bb1c997c8f119d88af9d8e78d796f6f6563bccda264c96b`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_portability.py::module::root::Module

Source: `infra/agentinfra/roadmap_portability.py:1`; AST `18f31c93b486f0016d2989a60008d10312723961cd3c32da30591df1261c123d`.

Rust module: `infra::agentinfra::roadmap_portability`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BLOCKS, ContractError, FileLock, FileTransaction, Mutation, PATTERNS, Path, ROOTS, TransactionError, _document_path, _previous_artifacts, a, after, artifacts, assert_sources, ast, base, before, bindings_current, bytes, calls, canonical, child, confined_path, dict, digest, documents, effects, enumerate, exc, expected, f, field, fields, file_record, files, flush, getattr, group, hasattr, i, imports, index, int, invariant, isinstance, json, k, kind, layout, len, length, lib, libraries, lines, list, loads, local, lock, maintained_python, markdown, max_bytes, mutations, n, name, names_in, names_out, next_owner, node, old_index, ordinal, ordinals, output, overhead, override, overrides, overrides_path, owned, owner, p, parts, path, pending, previous, proposal, raw, raw_index, raw_overrides, record, recover_named_transactions, relative, require, root, route, set, shard, shards, size, sorted, source, state, str, tree, tuple, type, u, unit, units, v, value, visit. Outputs/bindings: BLOCKS, PATTERNS, ROOTS, _, a, after, base, before, calls, child, documents, effects, expected, f, field, fields, files, group, i, imports, index, invariant, k, kind, layout, length, lib, libraries, lines, local, lock, mutations, n, name, names_in, names_out, next_owner, old_index, ordinal, ordinals, output, overhead, override, overrides, overrides_path, owned, owner, p, parts, path, pending, previous, proposal, raw, raw_index, raw_overrides, record, relative, root, shard, size, source, state, tree, u, unit, units, v, value.
Calls/effect boundaries: ', '.join, '; '.join, '\n'.join, (json.dumps(value, indent=2, sort_keys=True) + '\n').encode, (root / name).rglob, ContractError, FileLock, FileTransaction, FileTransaction(root, mutations, state_dir=state, name='aegis-portability').commit, Mutation, PATTERNS.get, _document_path, _previous_artifacts, artifacts, assert_sources, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.parse, ast.unparse, ast.walk, bindings_current, canonical, confined_path, confined_path(base, relative, must_exist=True).read_bytes, confined_path(root, base / relative, must_exist=True).read_bytes, dict, digest, documents.append, enumerate, expected.items, file_record, files.append, flush, getattr, group.encode, hasattr, index.get, isinstance, json.dumps, len, libraries.items, lines.extend, loads, lock.acquire, lock.release, maintained_python, markdown, markdown(file_record(record, source)).encode, markdown(local).encode, mutations.append, ordinals.get, output.get, override.get, override.items, overrides.get, overrides['units'].get, overrides_path.exists, overrides_path.read_bytes, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, parts.items, path.exists, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, pending.append, previous.get, raw.decode, raw.splitlines, raw_index.decode, raw_overrides.decode, record.get, record.get('configuration', {}).get, recover_named_transactions, relative.endswith, relative.removesuffix, relative.removesuffix('.py').replace, relative.startswith, require, root.resolve, set, shards, sorted, source.replace, tuple, type, unit.get, unit.update, units.append, units.extend, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
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
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
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
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
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
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_portability.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:8`; AST `f49eec2be7586a81b0fa34570d7cbaa58bc5eeaa5e471a05fac611f36b0ee7bd`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:9`; AST `e1940aa38db3623064556ff370b5181c22a0b9a032832b95ab173dfd8b7830f0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:10`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_portability.py:11`; AST `d7f1f4e5e4d1a9aabce3064aa7598cd67b1f166a30588cf7dc39ebd4e73f8227`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[9]::Assign

Source: `infra/agentinfra/roadmap_portability.py:14`; AST `4d7236569a281e304dec328f8020429a47e2dd70146fb72c4ad3facb6e230a0c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: ROOTS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[10]::Assign

Source: `infra/agentinfra/roadmap_portability.py:15`; AST `23111c155d9d1305f2045b6e286e884f6759717cbd323f586004e57e2b894d81`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: PATTERNS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[11]::Assign

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `7edb7b39a0f380b1ebba400f88dd4f30f01142c5c202774f61d8d19a380e720a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PATTERNS, ast, getattr, hasattr, n, tuple. Outputs/bindings: BLOCKS, n.
Calls/effect boundaries: getattr, hasattr, tuple.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[11].value::Call

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `c9cd933bdd1e1eae78c66d697d152174f139bbf99d5ad79ab40e26490a06ce29`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PATTERNS, ast, getattr, hasattr, n, tuple. Outputs/bindings: n.
Calls/effect boundaries: getattr, hasattr, tuple.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[11].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `66ec03446351f0d3a78b6136c2f4ef6642de1d30cbe59ee160cca285b743a5c3`.

Rust module: `infra::agentinfra::roadmap_portability`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: PATTERNS, ast, getattr, hasattr, n. Outputs/bindings: n.
Calls/effect boundaries: getattr, hasattr.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[11].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `34a9448fc48e1cf1860d7b6c56869755da96bc301950bdb415b6b9a8b6412a15`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, getattr, n. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::root.body[11].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:38`; AST `a9ca879dfffe8d226240b522c3d9889b9682db05f63f7ed735a3f30d997e5741`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, hasattr, n. Outputs/bindings: (none).
Calls/effect boundaries: hasattr.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:41`; AST `c10621859d62eb628b6d33b883eb399440d00c4cf47bfbf85a6dcee361755715`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOTS, list, name, p, root, sorted. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[12].body[0]::Return

Source: `infra/agentinfra/roadmap_portability.py:42`; AST `7227d774754b00bad91fada8e1079b8f2d5df206d485ff44d5b4703b6964cb23`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOTS, name, p, root, sorted. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:42`; AST `bcd3d953fb0e3fd40239738aa521938e48193485881e8728ebdaf35ad8d96b0c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOTS, name, p, root, sorted. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[12].body[0].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:42`; AST `ff9ac1f941864e10f8eca0d8998d32fd39e1e1310b127e510d70da7ce77f5952`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ROOTS, name, p, root. Outputs/bindings: name, p.
Calls/effect boundaries: (root / name).rglob, p.is_symlink.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[12].body[0].value.args[0].generators[1].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:42`; AST `bdd13823e887a09994643e0b04325038502dc5e335f380e5c0c5a7d93853375c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, root. Outputs/bindings: (none).
Calls/effect boundaries: (root / name).rglob.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value.args[0].generators[1].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::maintained_python::root.body[12].body[0].value.args[0].generators[1].ifs[0].values[1].operand::Call

Source: `infra/agentinfra/roadmap_portability.py:43`; AST `e9cab480c97fe5effaf0b2cd191d671f332cea8d0957cd0f4ecd6d4870d0f0db`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_symlink.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value.args[0].generators[1].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:46`; AST `7dfe9d3fd75d7079257e9373abd50644d1de0b57db6726d137717573905c5f1f`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BLOCKS, PATTERNS, Path, a, assert_sources, ast, calls, child, dict, digest, effects, enumerate, field, fields, files, getattr, i, imports, invariant, isinstance, k, kind, len, lib, libraries, list, loads, maintained_python, n, names_in, names_out, next_owner, node, override, overrides, overrides_path, owner, path, proposal, raw, raw_overrides, record, relative, require, root, route, set, sorted, source, str, tree, type, u, unit, units, v, value, visit. Outputs/bindings: a, calls, child, effects, field, fields, files, i, imports, invariant, k, kind, lib, libraries, n, names_in, names_out, next_owner, override, overrides, overrides_path, path, proposal, raw, raw_overrides, record, relative, source, tree, u, unit, units, v, value.
Calls/effect boundaries: PATTERNS.get, assert_sources, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.parse, ast.unparse, ast.walk, digest, enumerate, files.append, getattr, isinstance, len, libraries.items, loads, maintained_python, override.get, override.items, overrides.get, overrides['units'].get, overrides_path.exists, overrides_path.read_bytes, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, raw.splitlines, raw_overrides.decode, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:47`; AST `90a6c094b354d27312545b39da72412f10c8285131322d35965aa0ba3a6b09c9`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: files, units.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:48`; AST `eef9b44734747afa7024306e763477fd62c460ae7851a92e1b3132edc8f110f9`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: overrides_path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:49`; AST `b5b7d071050f64e7a0d73ccde33d92d05f229ecfc0771d668cfc5b0047778126`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides_path. Outputs/bindings: raw_overrides.
Calls/effect boundaries: overrides_path.exists, overrides_path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[2].value.test::Call

Source: `infra/agentinfra/roadmap_portability.py:49`; AST `9cca35c10f2d4f6cd17f52e0aa77e76e747480b3f24f4f0ce30c9e1758c20236`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides_path. Outputs/bindings: (none).
Calls/effect boundaries: overrides_path.exists.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[2].value.body::Call

Source: `infra/agentinfra/roadmap_portability.py:49`; AST `3bfee3961e2521587b7fbd1821054f5e38cacf63f9d0fb828df19c201d78be90`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides_path. Outputs/bindings: (none).
Calls/effect boundaries: overrides_path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:50`; AST `df529ff0b24a80ef657b1cb1c64f0873fe78805f94f1985876d7ff2eacea10d6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, raw_overrides. Outputs/bindings: overrides.
Calls/effect boundaries: loads, raw_overrides.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[3].value.body::Call

Source: `infra/agentinfra/roadmap_portability.py:50`; AST `2c34eac2f5eaa00970d1315b2cb52cbcf5b4a7e378a97a0a9407435886c98f25`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, raw_overrides. Outputs/bindings: (none).
Calls/effect boundaries: loads, raw_overrides.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[3].value.body.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:50`; AST `f904ea227ab94ae1295507cc081bda5f6b052abec3c88577fcc5912a85ca6095`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw_overrides. Outputs/bindings: (none).
Calls/effect boundaries: raw_overrides.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[4]::Expr

Source: `infra/agentinfra/roadmap_portability.py:51`; AST `671e21879a9b6e8d5297566746e261ecc696e7d01c9f2df44657e89322875d41`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides, require. Outputs/bindings: (none).
Calls/effect boundaries: overrides.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:51`; AST `057e2ae28778da13e699e8aaf1b7232ebf098d980ffd1530ca293125035de920`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, require. Outputs/bindings: (none).
Calls/effect boundaries: overrides.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:51`; AST `0c1eb0551fb6a7d3ce50e6c94bfa4ee7a8492ae038ffe79042116f71cb2c07dd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides. Outputs/bindings: (none).
Calls/effect boundaries: overrides.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5]::For

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `90fb70e682c5a7e4266930f94a64b05e14b9a0ae888122c5c87049070e48b481`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: BLOCKS, PATTERNS, a, ast, calls, child, digest, effects, enumerate, field, fields, files, getattr, i, imports, invariant, isinstance, k, kind, len, lib, libraries, list, maintained_python, n, names_in, names_out, next_owner, node, override, overrides, owner, path, proposal, raw, relative, require, root, route, set, sorted, source, str, tree, type, unit, units, v, value, visit. Outputs/bindings: a, calls, child, effects, field, fields, i, imports, invariant, k, kind, lib, libraries, n, names_in, names_out, next_owner, override, path, proposal, raw, relative, source, tree, unit, v, value.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.parse, ast.unparse, ast.walk, digest, enumerate, files.append, getattr, isinstance, len, libraries.items, maintained_python, override.get, override.items, overrides['units'].get, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[5]; no call, error or mutation may be omitted. Iteration: path in maintained_python(root)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:52`; AST `ebe3343fcce41557451c3ee0c98810e3fb3b8c363ee8f3dc1f06b697298b0596`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: maintained_python, root. Outputs/bindings: (none).
Calls/effect boundaries: maintained_python.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:53`; AST `c9a5d02444369221b50b662c72fded4efbbded9a1bf01f8bacecd9d7badf680c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, root. Outputs/bindings: relative.
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:53`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:53`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:54`; AST `cb5aaaf42a08c91666ce0e4859112cf066cdeebf56910b462a58b24332914278`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: raw.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:54`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:55`; AST `14d1cbc39c65636461267a28fac89eae79afd1a9c3719f12ca278873c196fdb6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, raw, relative. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:55`; AST `1c71510402688fc66f9f18274201ccd890bc521b89fde860e421ef3d24826eab`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:56`; AST `a0409c055ff3c2a219199795d4be0eefb79f7d601517390cea92afd386e07a27`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, files, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: digest, files.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:56`; AST `7f92c1717b0088be29e549a5d013cc155b2cd545479363038b647d2821ae2646`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, files, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: digest, files.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:56`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `15c6440df8c5f19bea783323cf490d8707b0489ed136d30c695dc1ff39c1c9c0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ast, isinstance, n, sorted, tree. Outputs/bindings: a, imports, n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `519e357672fce79a71c99b7276463d101c90fd063e69cb8d9b649abf83d0af38`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, ast, isinstance, n, sorted, tree. Outputs/bindings: a, n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `4f768a0365389e1c92649eb94488efc3d781fc38fafda131ccc6c1c7e3b25514`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, tree. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[5].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value.args[0].left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[4].value.args[0].left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value.args[0].left.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:57`; AST `52edc674ca61c4e36a3426e46d14df197a6820006835ec8e49b980d7d0c36bea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[4].value.args[0].left.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value.args[0].right::SetComp

Source: `infra/agentinfra/roadmap_portability.py:58`; AST `22e12de18f55e3fd31d22c54a9483b6e1804179ee083152d6f65c44cb572f45e`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, ast, isinstance, n, tree. Outputs/bindings: a, n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[5].body[4].value.args[0].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value.args[0].right.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:58`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[4].value.args[0].right.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[4].value.args[0].right.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:58`; AST `496d46f79aca0b6694f6f8aa40d9d5327eabf2d2b3881871ee0407f17c12d937`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[4].value.args[0].right.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:60`; AST `5bdbc50af7807096b773b2137c8d37c0599416faa270dd359a6e766f4d8b8f86`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BLOCKS, PATTERNS, ast, calls, child, digest, effects, enumerate, field, fields, getattr, i, imports, invariant, isinstance, k, kind, len, lib, libraries, list, n, names_in, names_out, next_owner, node, override, overrides, owner, proposal, raw, relative, require, route, set, sorted, source, str, type, unit, units, v, value, visit. Outputs/bindings: calls, child, effects, field, fields, i, invariant, k, kind, lib, libraries, n, names_in, names_out, next_owner, override, proposal, source, unit, v, value.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, ast.unparse, ast.walk, digest, enumerate, getattr, isinstance, len, libraries.items, override.get, override.items, overrides['units'].get, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:61`; AST `aeb8c7294e40fa6069655169831da75e125397d372c5e046c7324cb842ac5a13`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner. Outputs/bindings: next_owner.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[1]::If

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `aeddaae2bf74b82a248ae1303ce72674dec481d2cac31ba4b4723badd34df959`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node, owner. Outputs/bindings: next_owner.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[1]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[1].test::Call

Source: `infra/agentinfra/roadmap_portability.py:62`; AST `03f4d863af03611234c7247b6ee125dada11915164b7ebf16339435bb5a26fde`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:63`; AST `47f667885c9b8cab2f2391ed7cb48151287e7738be5e34e3b73b26b9ec505c0d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, owner. Outputs/bindings: next_owner.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2]::If

Source: `infra/agentinfra/roadmap_portability.py:64`; AST `0cf709aa21ba3bd36a3730c761dc27a39dbca723aac4f6e43dbb4ec0fac16ca6`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: BLOCKS, PATTERNS, ast, calls, digest, effects, fields, getattr, imports, invariant, isinstance, k, kind, len, lib, libraries, n, names_in, names_out, next_owner, node, override, overrides, proposal, raw, relative, require, route, set, sorted, source, type, unit, units, v. Outputs/bindings: calls, effects, fields, invariant, k, kind, lib, libraries, n, names_in, names_out, override, proposal, source, unit, v.
Calls/effect boundaries: PATTERNS.get, ast.dump, ast.dump(node, include_attributes=False).encode, ast.unparse, ast.walk, digest, getattr, isinstance, len, libraries.items, override.get, override.items, overrides['units'].get, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace, require, set, sorted, type, unit.update, units.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[2]; no call, error or mutation may be omitted. Condition: isinstance(node, BLOCKS) or isinstance(node, ast.stmt)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].test.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:64`; AST `b995adca511acc0fdc2469d2378b0b07f22a9c53713efead10f373bb5c55c933`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BLOCKS, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].test.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:64`; AST `e2bf93f2a9fbb0ec1d60a97184ee8f38d6b9356ea52441475e25c1a753382661`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `376758b2e642b07775831af0b29699bdf85bf7ec83a7ecaee8437b472c5f273b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, type. Outputs/bindings: kind.
Calls/effect boundaries: type.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[0].value.value::Call

Source: `infra/agentinfra/roadmap_portability.py:65`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `5c2cbb8ee8b3b622c144e77188a1bda0da2fd2052f990d96d8ac50e9944a58da`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n, names_in.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `c9d09a0d3e566624b56c69ad100118af486759121aa0554e69f87ddfe2c5269c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[1].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `17afd473726c5a678c32adc3cc8a96a8b31e262e8021ccf924ac11383cf08c54`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[5].body[5].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[1].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[1].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `4ce1a533696addd77247fef745b07cd543b5c26836077f5c88931ecde16ee2a4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:66`; AST `59f0d4aa6f7a1a18af1d35baf29ff5cdef611b8ce7b9b2f0126a9598271fc62c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[1].value.args[0].generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:67`; AST `335acc0c40ceeed7848058ff4fe25b684b6700f5ee6f9f55c11d3f303569faa8`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n, names_out.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:67`; AST `940a93eabfa057790c473f67a142ecd50591b3beb1a71497a0ae634a7c9834db`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[2].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:67`; AST `eb7831f9922987a45b31c04d6ce7c3a0aade097c89a7241da28ca7f191ef6167`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[5].body[5].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[2].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:67`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[2].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:67`; AST `4ce1a533696addd77247fef745b07cd543b5c26836077f5c88931ecde16ee2a4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:67`; AST `5f001159691f54aea19f198a393bbdbfe698328fc76a38534361c7af35bc3ddd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[2].value.args[0].generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `a86e3420d469e4dbffb250abce2c9c563f5c76b337a3936ef5153abfa2437aa3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: calls, n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `8a7f514d6474230e891f4a4e86910c94e4a90221ef1c161990fd26e064ceb86d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[3].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `b28d31c16e535d7d6d83960a7a0b58226ee0b45fee19949fa9e731670bd978c1`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[5].body[5].body[2].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[3].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `d37398c81d3e6778e173e0fabe4b6a4f1ccdff3685fe8d32f06e0aa03e719370`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[3].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[3].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[3].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[3].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:68`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[3].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:69`; AST `ed72708867a1c6fc476ac17795e1df2c658dad0fd9deccc4e2bc887bbaf9331c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PATTERNS, kind. Outputs/bindings: proposal.
Calls/effect boundaries: PATTERNS.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:69`; AST `0695e0c1cb211fa7dcd91ccaac0c33145e2ce78a6b9f209014cb4e5d13688599`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PATTERNS, kind. Outputs/bindings: (none).
Calls/effect boundaries: PATTERNS.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:70`; AST `8048819bb13fa216be8b931209ed2587518272999ac993b40cd72c086662d426`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: effects, n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:70`; AST `52cdb3991ddaba7230122c8d524fa2e151aa72d4ea5917fce43e64ad5ae8140d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, node, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[5].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:70`; AST `45b74ddd3e455cbac6a5745e2e8f189d72cd3a13c79cfda24eac6542cfab12d6`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, ast.walk, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[5].body[5].body[2].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[5].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_portability.py:70`; AST `2b61e5decfd609e82d91ed65f92b014a281c19986d2bb625356b5e6a69a6ec6e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[5].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[5].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:70`; AST `3ca05a3618e74851bb20d84cdd424fcded5f763f3eaf3ba430b79196f4e42a00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[5].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[5].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:71`; AST `5b78f524d545185ae95c46ca9ec96e6c4f9394bfd7137b82122cd2a7a21e87ea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[5].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:73`; AST `3074d8635e8eebd9f572d8c5f1bc5a152ce7f0a767e75b1e9c350340d88a8a9a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: libraries.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[7]::Assign

Source: `infra/agentinfra/roadmap_portability.py:78`; AST `2b5f347c335fcaeea42147b66ba5b6acb2edd07340d8677eab01fe65bdb9b7d6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kind, route. Outputs/bindings: invariant.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[8]::If

Source: `infra/agentinfra/roadmap_portability.py:79`; AST `f3289b71d97c382fcb95e6df2a3525aa35a7a044be36cfdfaed4e8b26aceead8`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[2].body[8]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.If, ast.While))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[8].test::Call

Source: `infra/agentinfra/roadmap_portability.py:79`; AST `1927d8456fe888e91df9776a3bb4b2f16582ee1dd48e9f3d60d7af2d33a0dc90`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[8].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[8].body[0]::AugAssign

Source: `infra/agentinfra/roadmap_portability.py:80`; AST `41e9159d21fe1dfde7d298dde26d49c9a4f72d60c89d6719be1bc88397bad19c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered AugAssign evaluation at root.body[13].body[5].body[5].body[2].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[8].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_portability.py:80`; AST `c18b20fc6a931aa1203440f1f8b4c0265224667054888e8fa512b84ef0e52745`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[8].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[9]::If

Source: `infra/agentinfra/roadmap_portability.py:81`; AST `4590a674f66719cf34b95a9e7d3a90901c62b0906802df03f5f5fa761737d372`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse, isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[2].body[9]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.For, ast.AsyncFor))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[9].test::Call

Source: `infra/agentinfra/roadmap_portability.py:81`; AST `34e9b2cb8ebf80d43c80578f8e9262e62ecd98636232d0a1169061045b0d5d6c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[9].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[9].body[0]::AugAssign

Source: `infra/agentinfra/roadmap_portability.py:82`; AST `58deffa8bc2b492ad3162467fc60784ac3665ee24f7c210a17afa2f9bb60da25`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, node. Outputs/bindings: invariant.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered AugAssign evaluation at root.body[13].body[5].body[5].body[2].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[9].body[0].value.left.left.right::Call

Source: `infra/agentinfra/roadmap_portability.py:82`; AST `bc6add1b97d423a6645739f36aa98f7316ecc56a99043994541a5d45ce7cff7e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[9].body[0].value.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[9].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_portability.py:82`; AST `f9be1754c1227970de354dc4b31bbcdfcca3518fc52e79c548a9fc12de9f1dc8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[9].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10]::Assign

Source: `infra/agentinfra/roadmap_portability.py:83`; AST `8011d4582cca4f8781b7ea78d194a87e163d0f068c80808dc19dc50dcccb1add`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, calls, digest, effects, getattr, imports, invariant, kind, len, lib, libraries, names_in, names_out, next_owner, node, proposal, raw, relative, route, source. Outputs/bindings: lib, source, unit.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest, getattr, len, libraries.items, raw.splitlines, relative.removesuffix, relative.removesuffix('.py').replace.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:84`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[3]::Call

Source: `infra/agentinfra/roadmap_portability.py:84`; AST `7e015840e16c88c823dd5259f4b55423b299ef9fa3c5de015b0073b6888bb2fb`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[3].args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:84`; AST `62642a7f86696182149656fb0833b390cc3f67cf8dd17c2b5151717295dc243e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[3].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:84`; AST `3fb94b2b8e1dc6a1bc206dc19bca3c2e71190137190d141090f14ace7aaa9d73`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[3].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:85`; AST `ccefd2bb5e25c3c40bb9fccc5f34ff179c59a0845b3ae29f825ddcd9f81afbcd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, node. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:85`; AST `c331789f037f08c0f906694e60140e82b9e02ec9a8e33a91a8f245bc525c4185`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, len, node, raw. Outputs/bindings: (none).
Calls/effect boundaries: getattr, len, raw.splitlines.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[1].args[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:85`; AST `47e2ce18890fe3dce0f518f5b24f3b83f3042f750aaef69e50f25bc7af5d7d1d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len, raw.splitlines.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[1].args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[1].args[2].args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:85`; AST `cdbc843ce77bcc95a6c9708e311d0f275743d081107aed5c5b33b34b08a7178b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.splitlines.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[4].elts[1].args[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[11]::ListComp

Source: `infra/agentinfra/roadmap_portability.py:88`; AST `329ba7608484fee5442d961d9e9c030c589b18743b987c35c182a2b444f4841f`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: imports, lib, libraries, source. Outputs/bindings: lib, source.
Calls/effect boundaries: libraries.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[11].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:88`; AST `bbcad9c952da994d6bdad031f0425fac2a2a6a39ad6b745bfee5abf0abecda66`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: libraries. Outputs/bindings: (none).
Calls/effect boundaries: libraries.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[11].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[13]::Call

Source: `infra/agentinfra/roadmap_portability.py:89`; AST `35b73a3b161a22835375d116155b2c1ebea7855ee7ef79683dd86213e4cbb9ea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removesuffix, relative.removesuffix('.py').replace.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[10].value.values[13].func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:89`; AST `04012b32da117e0853b4f15077bb8158d9a58d0112f7993f469f181bfc80f38b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removesuffix.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[10].value.values[13].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[11]::Assign

Source: `infra/agentinfra/roadmap_portability.py:97`; AST `372e235dbe87bf361126a98c6dd517fc3b0c7b11308b5ba159fcf143a11d430e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides, unit. Outputs/bindings: override.
Calls/effect boundaries: overrides['units'].get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[11].value::Call

Source: `infra/agentinfra/roadmap_portability.py:97`; AST `66592063ae5d2b8e35a9b57f5d5f1912e54eb7f9e07468ad08202b66a601cb3f`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, unit. Outputs/bindings: (none).
Calls/effect boundaries: overrides['units'].get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12]::If

Source: `infra/agentinfra/roadmap_portability.py:98`; AST `0dbca37045cf548377b32929db10ac0df28c2c4cd589ef7376428dc922a8fa1a`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: fields, k, override, require, set, unit, v. Outputs/bindings: fields, k, v.
Calls/effect boundaries: override.get, override.items, require, set, unit.update.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[2].body[12]; no call, error or mutation may be omitted. Condition: override
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:99`; AST `d1119a31140eba9d5f90037cd177bd9485ef4da3cb94dcc61e04f0d4ada85b25`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: override, require, unit. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5].body[2].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:99`; AST `11cac8b4e0f7bf1f4525cb834fbb5b55462c8e33f1312043a42e5d173aa3f873`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override, require, unit. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:99`; AST `f944e5d0736f3756a4689fd2de598221b7aceb5821d5498f0cb75f540ca44157`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:99`; AST `d5123be86d221ada39cdd42a4e89583104d8d5c1f53af3bb4dd2e52de598b461`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:100`; AST `b3d816531a439e0353293a5dd7533e714b7a2365b388ac4fa7e99417e152ca5d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: fields.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[2]::Expr

Source: `infra/agentinfra/roadmap_portability.py:101`; AST `ab6693562eec34bf31d5633ff276726e7efcf7274704240b6e4cb8e863b03a40`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, override, require, set. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require, set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5].body[2].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:101`; AST `ae661d434af5b75015a26f2a850c3d0008dfddbe780971bb1516395b413a4c25`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, override, require, set. Outputs/bindings: (none).
Calls/effect boundaries: override.get, require, set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:101`; AST `cb1a7e686a5034da28ca1791a7d883bd58eba59e2368304b7b986f955c512b94`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:101`; AST `f9370e5d53318114203af0a6b83ef10439f7a552fd4b1ad214a6e62fba6b4804`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:102`; AST `8f8b24dc9167079078b4b8e0b2e7d3997f952e4c04c7d90e1e344d17495e6d6a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, k, override, unit, v. Outputs/bindings: k, v.
Calls/effect boundaries: override.items, unit.update.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5].body[2].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:102`; AST `0abe98663ebcbf7174dbbcc69f0e4090df79230c199eaffe33c653d93e259b28`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, k, override, unit, v. Outputs/bindings: k, v.
Calls/effect boundaries: override.items, unit.update.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[3].value.args[0]::DictComp

Source: `infra/agentinfra/roadmap_portability.py:102`; AST `91313c7928045c15f4b3b9fb77ff7b21754df8640767eaf17b15e047aea008f6`.

Rust module: `infra::agentinfra::roadmap_portability`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: fields, k, override, v. Outputs/bindings: k, v.
Calls/effect boundaries: override.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[5].body[5].body[2].body[12].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[3].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:102`; AST `3eede006f5d161df1d034bc8de3cff772ef59c52037817866699b65850d00108`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: override. Outputs/bindings: (none).
Calls/effect boundaries: override.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[12].body[3].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:103`; AST `b75049395c98da5c450286ef8f50b9890bf87ff14db0f7bd47a2b85999424e2e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: override, unit. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[5].body[2].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[13]::Expr

Source: `infra/agentinfra/roadmap_portability.py:104`; AST `80a859dc4d7d22fe0d0ffdc8cf8e95938089d12d68e0a29d4c42dcf2be53a383`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unit, units. Outputs/bindings: (none).
Calls/effect boundaries: units.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5].body[2].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[2].body[13].value::Call

Source: `infra/agentinfra/roadmap_portability.py:104`; AST `1d22c0d6d427ef708f23cb2bc1822fd2339d707f6b48e16181a065d37d130474`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit, units. Outputs/bindings: (none).
Calls/effect boundaries: units.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[2].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3]::For

Source: `infra/agentinfra/roadmap_portability.py:105`; AST `7dbbdf94540821b6ca8608d25ebb9ee63fa2ec8585d502683d385d3400b7ce8d`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, child, enumerate, field, i, isinstance, list, next_owner, node, route, value, visit. Outputs/bindings: child, field, i, value.
Calls/effect boundaries: ast.iter_fields, enumerate, isinstance, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[5].body[5].body[3]; no call, error or mutation may be omitted. Iteration: (field, value) in ast.iter_fields(node)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:105`; AST `09b6e3b003896a4fa601486a87b76cab47e19e25562c99483afd9a0fa4af0043`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.iter_fields.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_portability.py:106`; AST `237cb01ad52ff4d173955e4350bc5131265c652f9b80dcdbcffc70cf01b21a5a`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, enumerate, field, i, isinstance, list, next_owner, route, value, visit. Outputs/bindings: child, i.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[3].body[0]; no call, error or mutation may be omitted. Condition: isinstance(value, ast.AST)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].test::Call

Source: `infra/agentinfra/roadmap_portability.py:106`; AST `518ae0204e0bc2a7a9a0fdeab27cd350bacc9a97c1a593b3402c0f44457a4dd2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:107`; AST `26cdc8a92d058e8db75544ff1f8d156f045e07b344bb1caa53aa52ae1ea3d2c4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, next_owner, route, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:107`; AST `41b2481bb0f92b2d99e7d1b14c9c88acca2bed6718d95909d8e278967e2bf55d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, next_owner, route, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `ca27472712279a088ffe26f4a3855408006880c6ae8ffee9146fa76a54a98b9f`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, enumerate, field, i, isinstance, list, next_owner, route, value, visit. Outputs/bindings: child, i.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(value, list)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_portability.py:108`; AST `f5635b2e334fb6e97f358f32dbb2b0086496303066699278ebd49fcf85562492`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0]::For

Source: `infra/agentinfra/roadmap_portability.py:109`; AST `9f101e75a9617e84d44a85e08e487a7770d138f83b4b500bfc48db3f63c6322c`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, child, enumerate, field, i, isinstance, next_owner, route, value, visit. Outputs/bindings: child, i.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0]; no call, error or mutation may be omitted. Iteration: (i, child) in enumerate(value)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:109`; AST `7319a75af29aa16ce29cee5b47f4824c2eea50c99daf127db96a63b65622d4e7`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, value. Outputs/bindings: (none).
Calls/effect boundaries: enumerate.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_portability.py:110`; AST `2de338419d1104614497ad306df94ac11e0435abf2cdedffa607a1f316a059b1`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, field, i, isinstance, next_owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(child, ast.AST)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0].test::Call

Source: `infra/agentinfra/roadmap_portability.py:110`; AST `bfd7a1d88fedbb3dac987f7a025d0b34fc3cab5882e0033352cecaa2e8492640`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, child, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:111`; AST `6d0d2b285266d5532492c616356135e1a2f3830e05f4733a6169c5a6437ed8ab`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child, field, i, next_owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::visit::root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:111`; AST `2fddc1348ad25f6f859d43c16388ee1946a9f5d9c4cd4f42090e8e1d7a94452e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child, field, i, next_owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].body[3].body[0].orelse[0].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[6]::Expr

Source: `infra/agentinfra/roadmap_portability.py:112`; AST `cf5b7f268e71083a292c249902b2e7f6ba9bde87d724e00a88b2abc89ec1e85d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[5].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:112`; AST `54d9837e7b8ee2da2a44fcc7b0d9ac2e34afef27ad26515c17ea2951989f198a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_portability.py:113`; AST `2aeed883cea2019bd96dbc9ad811c0c7dc1e44ebe026b9619d4304bed075431f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, u, units. Outputs/bindings: u.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:113`; AST `99f74107437faaa8878cbb7591c5a2dadb7d600d4353900327c8f56aaee8a54b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, u, units. Outputs/bindings: u.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[6].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:113`; AST `8fab30b6203427492d68560cbbe1bcc928799e0969ddeafe764ac4c92e3adca2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, u, units. Outputs/bindings: u.
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[6].value.args[0].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:113`; AST `9d44ba12a05af66e1da558a6a35bb4bf799ffc3eb26e7af15f3ccaf003bdccf4`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[6].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[6].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:113`; AST `d334ac4951312a2e5ce0e7d19e1cf4c4a0351088858089c704b81b4d02ed725c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, units. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[7]::Expr

Source: `infra/agentinfra/roadmap_portability.py:114`; AST `e257ce6d86c5c86320a2b6c7ddc69a9352ea46589a2abe56a75fb3aee4bc955d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overrides, require, set, u, units. Outputs/bindings: u.
Calls/effect boundaries: require, set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap_portability.py:114`; AST `0a3e0a8674a80468c5ab08237b635c595a65a5473df3d813bd51033fa14ba814`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, require, set, u, units. Outputs/bindings: u.
Calls/effect boundaries: require, set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[7].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:114`; AST `65a14c580ddf50b1dd6ee2b51204520784cb5edb1d49bc8e77ee97982b56bbde`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: overrides, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[7].value.args[0].comparators[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:114`; AST `9d44ba12a05af66e1da558a6a35bb4bf799ffc3eb26e7af15f3ccaf003bdccf4`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[7].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[8]::Assign

Source: `infra/agentinfra/roadmap_portability.py:115`; AST `8caeb31f120d0a9582a164de0ae8dbb83691214ee52ee2e06339c4eb5e3e9a19`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, files, raw_overrides, units. Outputs/bindings: record.
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[8].value.values[4]::Call

Source: `infra/agentinfra/roadmap_portability.py:116`; AST `f446143c5c08ab2b81ba051b93df3be743c4b494c9196d900dbfa98768d1b6aa`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, files, units. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[8].value.values[5].values[0].body::Call

Source: `infra/agentinfra/roadmap_portability.py:117`; AST `4ce2e06cfff0395ad8c1249bc4d803ae5a8d979d922734df030d402338ad541b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw_overrides. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.values[5].values[0].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[9]::Expr

Source: `infra/agentinfra/roadmap_portability.py:118`; AST `6942af7609acf3dd5cb355575971e15ed8f16988e677a47d9558aa3d38395e73`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[9].value::Call

Source: `infra/agentinfra/roadmap_portability.py:118`; AST `fd63307d6092b7b03a93b01d00ef0d4cc90e586d0aa2e0cd6a5383e681af5092`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::inventory::root.body[13].body[10]::Return

Source: `infra/agentinfra/roadmap_portability.py:119`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:122`; AST `94bce2652d975ddfeb01cfbfa802512dd038725dbbaec8468898b41105dc852c`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, len, lines, record, str, unit. Outputs/bindings: lines, unit.
Calls/effect boundaries: ', '.join, '; '.join, '\n'.join, len, lines.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:123`; AST `d0eb5455745bbf4c80aa843a7f618906fabc298a7642c0f1c477d3c60af530ed`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record. Outputs/bindings: lines.
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[0].value.elts[4].values[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:125`; AST `df46df88acf5e6ef901488c4610d14a5b71f816377a047e8ea3cd040d31bfe4e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.elts[4].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[0].value.elts[4].values[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:125`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.elts[4].values[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1]::For

Source: `infra/agentinfra/roadmap_portability.py:127`; AST `77a62c393e6c915f44bcb6c30dc0f1015e65da910cc2acc3af49ef923439ec33`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: lines, record, unit. Outputs/bindings: unit.
Calls/effect boundaries: ', '.join, '; '.join, lines.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[14].body[1]; no call, error or mutation may be omitted. Iteration: unit in record['units']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:128`; AST `7214c7ce317834d6cbe4b960b79b5d796e3392d39ca0fa87d4d80375949cac1e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lines, unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join, '; '.join, lines.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:128`; AST `2f1e236c8398f68b266600a683dce712520e40f7173635fe4f096f0abb91dae5`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lines, unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join, '; '.join, lines.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[6].values[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:130`; AST `3aa75dfcd6cf2d291b6ec84458f21047b34b2f04bf0804e36248fda78c60ba78`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[6].values[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[6].values[3].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:130`; AST `7c3780615bb5771e4ca9f5d087ce504e83d0dd79897dffbb1140aaf0a363213c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[6].values[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[7].values[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:131`; AST `726fa29e3f627d9e668c1ad09509678d21692d5ba1e15adc192cffd096842a03`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[7].values[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[8].values[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:132`; AST `d79bc397e6a9ef3e4311a110e7c7ff8ee0a8612018f2bb343e54ea0fb5727365`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: ', '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[8].values[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[10].right::Call

Source: `infra/agentinfra/roadmap_portability.py:133`; AST `a30df28dce224c0c9b901371b5549363fbffb5cb321af3076afc461dcf537390`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[10].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[11].right::Call

Source: `infra/agentinfra/roadmap_portability.py:134`; AST `f2928483541b170613d9c1ea7ce91addc0f1d24fe94957326a7bf64fa21dee39`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[11].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[12].right::Call

Source: `infra/agentinfra/roadmap_portability.py:135`; AST `d47f35417844d1e678c0f992bb2cf326884e436dfd849df789635a9cd2b36bcb`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[12].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[1].body[0].value.args[0].elts[18].left.right::Call

Source: `infra/agentinfra/roadmap_portability.py:137`; AST `957fbb11409ac5db1d3c88efc016095c3d41048da646a57d9d02824ccd9338ce`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: '; '.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.args[0].elts[18].left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[2]::Return

Source: `infra/agentinfra/roadmap_portability.py:138`; AST `183ef5d77c056458d553680b183e97de67803fa0aafc226ee5a655c9c44c4c28`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lines. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::markdown::root.body[14].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:138`; AST `4fffb99bc7d4169bb6278b954681e4ff82ab160a1898ea7351b0ad0db5c4cbd1`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lines. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:141`; AST `cbff0abc5e5f0b31ae655c329294aae75fd1df8d747b20b845ca18940ad60367`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: canonical, dict, digest, flush, group, index, int, isinstance, len, length, max_bytes, name, ordinal, ordinals, overhead, owner, parts, pending, record, require, size, str, tuple, type, unit, value. Outputs/bindings: group, index, length, name, ordinal, ordinals, overhead, owner, parts, pending, size, unit, value.
Calls/effect boundaries: canonical, digest, flush, group.encode, isinstance, len, ordinals.get, parts.items, pending.append, require, type, unit.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:142`; AST `2ac3e271c89c63736fd1555a96260bb7cf3e8118e753fab6a0f562b3ea37170e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:143`; AST `98975d602361a0e91087677e9f46b6c32db77945afb23b5426b1b55d52ba5e94`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, max_bytes, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:143`; AST `a1140d0ecd373cf63e3e5d2014e09948f45a9048d35b9dbd4ed939f3c47a383e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, max_bytes, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:143`; AST `c99ed4947b38c030b13015cab080bcc1db01a4478b079df565678d930d284956`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max_bytes, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:144`; AST `9194e782433b24b859fa402e8b8c1a7fce33f78ed273b2ec2d9c0082fe645e98`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: ordinals, parts, pending.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:145`; AST `b522a090d1f27a6fd49f6e6acac4faa84a3529f99e256ef8c850bf3b5008edc1`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: group.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:146`; AST `782f418b5c11d8a87d5a4c068ed7a14afcea1ed9e44465d94bc6f351f5c6f075`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, len. Outputs/bindings: overhead.
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[4].value.left::Call

Source: `infra/agentinfra/roadmap_portability.py:146`; AST `55e06e8c503e7c4aeae1469c3aaf1aad8a3b32856f071799c2df9a5bfa4c1c0d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[4].value.left.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:146`; AST `ce8cebaffdde5ef03235d1ab6505502282c6fbbc9f3bc1fa23824243baed23c7`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:147`; AST `dfb58974517c12c5b43017cd71d464fcfdcce45239db50342c947081f3ee4e0c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overhead. Outputs/bindings: size.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:149`; AST `f211b70b6b9ef384f4377f9284a9410f3619b28536d38a4be58cd10089b04364`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: canonical, digest, group, len, max_bytes, name, ordinal, ordinals, overhead, parts, pending, require, value. Outputs/bindings: name, ordinal, pending, size, value.
Calls/effect boundaries: canonical, digest, group.encode, len, ordinals.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[0]::Nonlocal

Source: `infra/agentinfra/roadmap_portability.py:150`; AST `2052d94f16cefd970e69734a00c0dcc2d5bd6d37f3e16db79b4ea437686422b5`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Nonlocal evaluation at root.body[15].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[1]::If

Source: `infra/agentinfra/roadmap_portability.py:151`; AST `64671b641ea636b177e8b5e5db2c70cddbfa0e5ca1be4c3d748295861d478c3d`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: pending. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[15].body[6].body[1]; no call, error or mutation may be omitted. Condition: not pending
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_portability.py:152`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[15].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:153`; AST `0bda719213f4f201b7048109c035bac9da89264d96666512b1abc8707b278710`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: group, ordinals. Outputs/bindings: ordinal.
Calls/effect boundaries: ordinals.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:153`; AST `efe6a2b799b25dbf62f32cbbd810afd916bab4f80d8c42c3d53354e982e3ebba`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group, ordinals. Outputs/bindings: (none).
Calls/effect boundaries: ordinals.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:154`; AST `9de30c4bf56785145a08a8adfb646e4b0d11ca5f710a7db7942c404d63f94ae1`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, group, ordinal. Outputs/bindings: name.
Calls/effect boundaries: digest, group.encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[3].value.values[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:154`; AST `346f99540ebace041b4c4ddd37addf263a13437f318a5bdf7a24db776d580559`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, group. Outputs/bindings: (none).
Calls/effect boundaries: digest, group.encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[3].value.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[3].value.values[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:154`; AST `46d42f2135254015f4885e2ff07904c1196f8ba0b525a7b7f101cfa964367265`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group. Outputs/bindings: (none).
Calls/effect boundaries: group.encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[3].value.values[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:155`; AST `58ba87c4a6b76d783e4f31db06e26d8cff2ef60c7e25b49d6693c1217a78f0c9`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending. Outputs/bindings: value.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[5]::Expr

Source: `infra/agentinfra/roadmap_portability.py:156`; AST `9cf5f6ece661a808558260701e1f574be0e00b6e0f66670183bf9e86882c2f7b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, len, max_bytes, name, parts, require, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:156`; AST `4570747c6766e7d9f4a77cbf11c9cca52c37601e10c06a58e9951d3c6818c9ea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, max_bytes, name, parts, require, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[5].value.args[0].values[1].left.left::Call

Source: `infra/agentinfra/roadmap_portability.py:156`; AST `0c02cdf8d7d616c4e492156ffb6bfb747d31ab07ecc8ecedaaa9c2bedde99607`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].value.args[0].values[1].left.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[5].value.args[0].values[1].left.left.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:156`; AST `1a07bd0abe50598ca6ed04aec23bd487f4b47a0fab4fc87670427f80c2369336`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].value.args[0].values[1].left.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:158`; AST `bda46d236d3950f1a4c4c23f7ba20a0e78bd09a2e6a4a232ea4f40fdf2de58d0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, parts, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[7]::Assign

Source: `infra/agentinfra/roadmap_portability.py:159`; AST `ecb56e15a0c97866671afb3652fa1e6dc1c2b026056a17e285750d6b81ed19cb`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: group, ordinal, ordinals. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::flush::root.body[15].body[6].body[8]::Assign

Source: `infra/agentinfra/roadmap_portability.py:160`; AST `d0cf581117b627c86078220de2e7059caad472deb26c91f1baeb2653786a1162`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: overhead. Outputs/bindings: pending, size.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7]::For

Source: `infra/agentinfra/roadmap_portability.py:162`; AST `0140219346a3edc0f4e03b0349937b78ac61dc6b2e9f08766a51c9f3bce86aaa`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: canonical, flush, group, isinstance, len, length, max_bytes, overhead, owner, pending, record, require, size, str, unit. Outputs/bindings: group, length, owner, size, unit.
Calls/effect boundaries: canonical, flush, isinstance, len, pending.append, require, unit.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[15].body[7]; no call, error or mutation may be omitted. Iteration: unit in record['units']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:163`; AST `ee877722aa4a9eb842bd680aec214f55b6e20af4c5b4986c9f2745136a12a0ce`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unit. Outputs/bindings: owner.
Calls/effect boundaries: unit.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:163`; AST `66837749b65ac6756dc3deeea9441a8f2007847f93a00a16fbe020825da6e92a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unit. Outputs/bindings: (none).
Calls/effect boundaries: unit.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:164`; AST `b376fd22a42c27a251883590a91430f4ebf5107f71b5a07258e8dd45501b376f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, owner, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:164`; AST `9d185869084379f6fb785e34543af01cda48dfe314aa5d5f18e150d0da29a90a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, owner, require, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:164`; AST `acdfde606b036e42c15068116f8f839fdd00803d9a09b5466f39c2a4ec84c1d9`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, owner, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[2]::If

Source: `infra/agentinfra/roadmap_portability.py:165`; AST `71cfd0ff3f3eedcba219f1032f3e07c04182ae8e12cdace21115d9c51d8bebe6`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: flush, group, owner. Outputs/bindings: group.
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[15].body[7].body[2]; no call, error or mutation may be omitted. Condition: owner != group
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:166`; AST `44f655f988291d37ff5a12d3b1b4ca8bfb40d6998623e7c7f70cb2837c1487aa`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: flush. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:166`; AST `9a084bcff8de08709550ef48b3f123534afb77109fec8016318fecd179e71251`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: flush. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:167`; AST `2336b820d724369f2a36c84c4b2b6fd61ce5e81218aa9a9e295fb85b554e2304`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner. Outputs/bindings: group.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[7].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:168`; AST `0040d593e42c8089f4c56e6a5e4a12e4122ef238e946295e70deccb81c873f4b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, len, unit. Outputs/bindings: length.
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:168`; AST `190357797879b5c3468a911a0e4690cbb83ffe2fc7ee146cb112e2fa6c408172`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, unit. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:168`; AST `df4d83f2dfe250fd034b95293eb762500b931b51e045651dfd07ee8dd195d2c6`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, unit. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[4]::Expr

Source: `infra/agentinfra/roadmap_portability.py:169`; AST `41d750fa544d417ad25b4e85a669a5deddbc6e37b68acdf467a372ddb02860e2`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: length, max_bytes, overhead, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:169`; AST `6703ccb77e7434d90ef7619e66bf33404e687b2e14b30cd48515bff1b6ecccf3`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: length, max_bytes, overhead, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[5]::If

Source: `infra/agentinfra/roadmap_portability.py:170`; AST `c3f6afa812fe320d32a8c27a86d8653bca77c48fde1b427f09659239f9cdba13`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: flush, length, max_bytes, pending, size. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[15].body[7].body[5]; no call, error or mutation may be omitted. Condition: pending and size + length + 1 > max_bytes
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:171`; AST `44f655f988291d37ff5a12d3b1b4ca8bfb40d6998623e7c7f70cb2837c1487aa`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: flush. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:171`; AST `9a084bcff8de08709550ef48b3f123534afb77109fec8016318fecd179e71251`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: flush. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[6]::AugAssign

Source: `infra/agentinfra/roadmap_portability.py:172`; AST `7becdaa36bd027881833713b4f883cbfc9f4eea87721d2294e162eef553f944e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: length, pending. Outputs/bindings: size.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered AugAssign evaluation at root.body[15].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[7]::Expr

Source: `infra/agentinfra/roadmap_portability.py:173`; AST `3032c119739567217ee6562abdd56c2a33c22c2571176b0a2b13ce9792d92037`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending, unit. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[7].body[7].value::Call

Source: `infra/agentinfra/roadmap_portability.py:173`; AST `e7b38fe3839fdca844a1a3b32b8cebcfff2db2040db1703639efa945c0567860`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending, unit. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[8]::Expr

Source: `infra/agentinfra/roadmap_portability.py:174`; AST `44f655f988291d37ff5a12d3b1b4ca8bfb40d6998623e7c7f70cb2837c1487aa`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: flush. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[8].value::Call

Source: `infra/agentinfra/roadmap_portability.py:174`; AST `9a084bcff8de08709550ef48b3f123534afb77109fec8016318fecd179e71251`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: flush. Outputs/bindings: (none).
Calls/effect boundaries: flush.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9]::Assign

Source: `infra/agentinfra/roadmap_portability.py:175`; AST `34ca8a2c5a9a02cec18ff8b4e8af73dbefb74fbf3b36f758cdf72989210801dd`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, digest, len, max_bytes, name, parts, record, value. Outputs/bindings: index, name, value.
Calls/effect boundaries: canonical, digest, len, parts.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[7]::Call

Source: `infra/agentinfra/roadmap_portability.py:177`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9]::ListComp

Source: `infra/agentinfra/roadmap_portability.py:178`; AST `a5f406228977ebb2a81107388260547f947306d736e539d06a8904505d1ffcfb`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: canonical, digest, len, name, parts, value. Outputs/bindings: name, value.
Calls/effect boundaries: canonical, digest, len, parts.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[9].value.values[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].elt.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:178`; AST `f5478a66fd3247b8968c1306f6cc686ba6a06ab0db4348065f96da8baff25481`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, value. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].elt.values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:178`; AST `713329791aec59f53add5caf311c586cba099b711d44eb59dd19773ebb41188f`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].elt.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].elt.values[3]::Call

Source: `infra/agentinfra/roadmap_portability.py:179`; AST `903fcc31ca621787ebaa9d4887c2be80548e3de40753d18342472c2f483a0e89`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, digest, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].elt.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].elt.values[3].args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:179`; AST `1a07bd0abe50598ca6ed04aec23bd487f4b47a0fab4fc87670427f80c2369336`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].elt.values[3].args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].elt.values[4].left::Call

Source: `infra/agentinfra/roadmap_portability.py:179`; AST `0c02cdf8d7d616c4e492156ffb6bfb747d31ab07ecc8ecedaaa9c2bedde99607`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].elt.values[4].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].elt.values[4].left.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:179`; AST `1a07bd0abe50598ca6ed04aec23bd487f4b47a0fab4fc87670427f80c2369336`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].elt.values[4].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[9].value.values[9].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:180`; AST `2141119718c6153bf438d761a03d90f528922a00b6347b49ce2232dc5bc7f360`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.values[9].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::shards::root.body[15].body[10]::Return

Source: `infra/agentinfra/roadmap_portability.py:181`; AST `621d0d10fd5acd4378f7bca76335de4bbc01b31f0b1dbcdab94b30cbb24f08e4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, parts. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[15].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:184`; AST `2773444044e2fda45f5b682e65ad2a498bfc76cbb8beebe6dae92264f4ca8eab`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bindings_current, dict, digest, expected, f, maintained_python, p, path, record, require, root. Outputs/bindings: expected, f, p, path.
Calls/effect boundaries: bindings_current, digest, maintained_python, p.relative_to, p.relative_to(root).as_posix, path.exists, path.read_bytes, record.get, record.get('configuration', {}).get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `79a042d5b1a7c244476dbe44f46ca9275729f9e0221a8f896c1db666bc2cf1f8`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, f, maintained_python, p, record, require, root. Outputs/bindings: f, p.
Calls/effect boundaries: bindings_current, maintained_python, p.relative_to, p.relative_to(root).as_posix, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `a1872ecbd9350265a7a931dcd98472f5dd0e3b949e80d9576182e8083ce9cf5d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, f, maintained_python, p, record, require, root. Outputs/bindings: f, p.
Calls/effect boundaries: bindings_current, maintained_python, p.relative_to, p.relative_to(root).as_posix, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value.args[0].values[0].left::ListComp

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `ac9219935382215e432fd2328e4bed430f4d9ed8209bb510c87ecad2f9f0b199`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: maintained_python, p, root. Outputs/bindings: p.
Calls/effect boundaries: maintained_python, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[16].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value.args[0].values[0].left.elt::Call

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.args[0].values[0].left.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value.args[0].values[0].left.elt.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.args[0].values[0].left.elt.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value.args[0].values[0].left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `ebe3343fcce41557451c3ee0c98810e3fb3b8c363ee8f3dc1f06b697298b0596`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: maintained_python, root. Outputs/bindings: (none).
Calls/effect boundaries: maintained_python.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.args[0].values[0].left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value.args[0].values[0].comparators[0]::ListComp

Source: `infra/agentinfra/roadmap_portability.py:185`; AST `60211175427cf1b47c08ce14d3d3f14192e9c313e5f996d75b7ce92b284427e7`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: f, record. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[16].body[0].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[0].value.args[0].values[1].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:186`; AST `ae0651d900cd6c1ae84399a194827c3c6cd036917b3f5439a308e8b96c33fa71`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, record, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.args[0].values[1].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:188`; AST `f4568b66c64f40c5fe916b5a997b97ad2da804858025aa5651e19fb50bf1f5db`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:189`; AST `721b7c3329eb12fa7010d9e589a4200a98761833356b159485309c6732602feb`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: expected.
Calls/effect boundaries: record.get, record.get('configuration', {}).get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:189`; AST `99ea45fd5c551a867a7a10d9335108959673a7e6705e118746fc248bc1876a50`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get, record.get('configuration', {}).get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:189`; AST `659db165aab0cb6300d6bad564e36139a53fe0becba1125cd7007e57cf3c1f14`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[3]::Expr

Source: `infra/agentinfra/roadmap_portability.py:190`; AST `3c86b2d344a788c4e5c3e13849884d14427a45b267d81973f617c219a299093b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, expected, path, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.exists, path.read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:190`; AST `c57abf228cc1a8ce5d0062ffe4c71c1110c3551f542059fbc3252e6efe6fbcb8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, expected, path, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.exists, path.read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[3].value.args[0].left.test::Call

Source: `infra/agentinfra/roadmap_portability.py:190`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.args[0].left.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[3].value.args[0].left.body::Call

Source: `infra/agentinfra/roadmap_portability.py:190`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.args[0].left.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::assert_sources::root.body[16].body[3].value.args[0].left.body.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:190`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.args[0].left.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::file_record::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:194`; AST `f1c9dea8395558c920a737e9630a3c57b3be2b29d24508b06d3de135ee8f29a7`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, digest, record, source, u, units. Outputs/bindings: u, units.
Calls/effect boundaries: dict, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::file_record::root.body[17].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:195`; AST `2cbc6a685af61bdc304987fe82a1969899b2a8b40a792e255ce37e30f2eb07a1`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, source, u. Outputs/bindings: u, units.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::file_record::root.body[17].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_portability.py:195`; AST `8c3a41aa19526923efb80703034df2bb0908e38a152bb6f470320106bab452fd`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: record, source, u. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::file_record::root.body[17].body[1]::Return

Source: `infra/agentinfra/roadmap_portability.py:196`; AST `5cf14db9e42013a2841aa89cca83a704baeeeb425b2826dead105dadec2a571c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, digest, record, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::file_record::root.body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:196`; AST `d277e1a1a638cea0d4f3b7924ecfd5c3b46470cf01ccc7594bf5dd0b0a8fa2be`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, digest, record, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::file_record::root.body[17].body[1].value.keywords[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:196`; AST `c95052825cc0e785e32159cf039948b4ba911a3083114f2fce82a6cfbd6f38b9`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, source, units. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.keywords[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_document_path::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:199`; AST `b51177339b3805295f8adad0f84327a81ce815a0f3c6258fc4c0265786ddf62f`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: source, str. Outputs/bindings: (none).
Calls/effect boundaries: source.replace.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_document_path::root.body[18].body[0]::Return

Source: `infra/agentinfra/roadmap_portability.py:200`; AST `5b252ba37d6f9d14f9c40ca08b432e08b5f1491b38c350e966bf91a28583c314`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.replace.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_document_path::root.body[18].body[0].value.left::Call

Source: `infra/agentinfra/roadmap_portability.py:200`; AST `5455af5e4a9bbf31ec27313524f769853dd40c4fb776b901f8a12b23eeb344b1`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.replace.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:203`; AST `fcddab34c70950ebe9eac061ae2ab853da214adc6b21dc613eb1bfa093f9319a`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _document_path, bytes, canonical, dict, digest, documents, file_record, index, markdown, name, output, parts, path, raw, record, require, shards, source, str, tuple, value. Outputs/bindings: documents, index, name, output, parts, path, raw, source, value.
Calls/effect boundaries: _document_path, canonical, digest, documents.append, file_record, markdown, markdown(file_record(record, source)).encode, parts.items, record.get, require, shards.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:204`; AST `806d41510d2b87f0e2a670736c45f29bf811987a186e491dab8e2c48a6049c7f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, shards. Outputs/bindings: index, parts.
Calls/effect boundaries: shards.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:204`; AST `e993f6a2d7fa159b4f0163de851c48636bc8f18aed60f6bbd164da3c8a9a397e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, shards. Outputs/bindings: (none).
Calls/effect boundaries: shards.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:205`; AST `012e16fb3bd3aea4525638803e45ada9c9ec93e7288e53a286645be7cbd1e0f0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, name, parts, value. Outputs/bindings: name, output, value.
Calls/effect boundaries: canonical, parts.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[1].value::DictComp

Source: `infra/agentinfra/roadmap_portability.py:205`; AST `63af041ad4d6f69134fd7bd53d72323a102275a8061f9b77ad6766b717429b49`.

Rust module: `infra::agentinfra::roadmap_portability`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: canonical, name, parts, value. Outputs/bindings: name, value.
Calls/effect boundaries: canonical, parts.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered DictComp evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[1].value.value.left::Call

Source: `infra/agentinfra/roadmap_portability.py:205`; AST `1a07bd0abe50598ca6ed04aec23bd487f4b47a0fab4fc87670427f80c2369336`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value.value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[1].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:205`; AST `2141119718c6153bf438d761a03d90f528922a00b6347b49ce2232dc5bc7f360`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:206`; AST `9bc1cc1edc99b031cab0ebc2b6705536e597fd9052dbdc0c978d197cdafae0b4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: documents.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3]::For

Source: `infra/agentinfra/roadmap_portability.py:207`; AST `937a100a033a803f5eacf17693ade28bc3eac7a1f255075ebbdd3b0fa0197435`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _document_path, digest, documents, file_record, markdown, output, path, raw, record, require, source. Outputs/bindings: path, raw, source.
Calls/effect boundaries: _document_path, digest, documents.append, file_record, markdown, markdown(file_record(record, source)).encode, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[19].body[3]; no call, error or mutation may be omitted. Iteration: source in record['files']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:208`; AST `d2a819b4394b6b201c1cb25fcdcf8ac7f992ef437ce151dcf5800dedd64cf8be`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _document_path, source. Outputs/bindings: path.
Calls/effect boundaries: _document_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:208`; AST `50b1c36d4b7e7d960e60d0ffbff23f21043db13b0a828265479ef33cdfe8cbac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _document_path, source. Outputs/bindings: (none).
Calls/effect boundaries: _document_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:209`; AST `704bf8bb2892851617ae41adda6ad4457223d54ececb242d9b4e0b97e463d734`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, path, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:209`; AST `9bbc15dd3e58b520b5066f30b595fbda19e06b20e33f106271e98056927a5ca8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, path, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:210`; AST `f2b695ec4936833bb1892e2972e811caf0bf90a4004c1aa09f6ed941097d511d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_record, markdown, record, source. Outputs/bindings: raw.
Calls/effect boundaries: file_record, markdown, markdown(file_record(record, source)).encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:210`; AST `0735f4b55839d21a83a0a135fca42981e00b5d77bd458ee5e1c825389a416432`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_record, markdown, record, source. Outputs/bindings: (none).
Calls/effect boundaries: file_record, markdown, markdown(file_record(record, source)).encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:210`; AST `4a11232a69bd1f090b88f69937d00f71776f38daede0349be9a875a8de5e1456`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_record, markdown, record, source. Outputs/bindings: (none).
Calls/effect boundaries: file_record, markdown.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[2].value.func.value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:210`; AST `dfd72e993a0b03c574e7bb525b3d32a6f6eef2a76187a440eb0cc811f4973d12`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_record, record, source. Outputs/bindings: (none).
Calls/effect boundaries: file_record.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[2].value.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:211`; AST `5ec1f4c471efcaff8e05f55824a5d464ca596eeb08ea265cf64b1e9f29357255`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, path, raw. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_portability.py:212`; AST `1b4b5b7b59942bb5d93af8aa13970db1dd866ffbc5d53776eb2dc132856d2491`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, documents, path, raw, source. Outputs/bindings: (none).
Calls/effect boundaries: digest, documents.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:212`; AST `d09aca3ab7d5ee05b7c183438d710b6776599cb14c629339846e918d9e27abf1`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, documents, path, raw, source. Outputs/bindings: (none).
Calls/effect boundaries: digest, documents.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[3].body[4].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:212`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[4].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:213`; AST `5e9e57160d14f7f038619e722f9f2b38e79c4037781ebe624b16949bbd50cfb3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: documents, index. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:214`; AST `0e8fbe2c8a9cfc89df7f7e2600de0ee285936c0ceb5102e5ed45d887fbc9254d`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:214`; AST `659db165aab0cb6300d6bad564e36139a53fe0becba1125cd7007e57cf3c1f14`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:215`; AST `70d791d36b035b023678354c7a9e1b9b7e185dba7c31520a5de82d9f3daf751f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, index, output. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[6].value.left::Call

Source: `infra/agentinfra/roadmap_portability.py:215`; AST `f193c154bef9bf4c11e7b0622b0a0faf86f74509f7e3f7631e3c4b3c02ec6f41`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, index. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::artifacts::root.body[19].body[7]::Return

Source: `infra/agentinfra/roadmap_portability.py:216`; AST `fe03adef11842ab5414552bb2b156f3cc03f8b943f5515b7507380c324cc3be3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, output. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[19].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:219`; AST `2502fdf2455da0f830d40df89f754d19b89f63019c47886296cd020e1dcc615a`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _document_path, base, bytes, canonical, confined_path, dict, digest, expected, f, file_record, index, json, layout, len, loads, local, markdown, owned, path, previous, raw, raw_index, relative, require, shard, source, str, u, units, value. Outputs/bindings: expected, f, index, layout, local, owned, path, previous, raw, raw_index, relative, shard, source, u, units, value.
Calls/effect boundaries: (json.dumps(value, indent=2, sort_keys=True) + '\n').encode, _document_path, canonical, confined_path, confined_path(base, relative, must_exist=True).read_bytes, dict, digest, file_record, index.get, json.dumps, len, loads, markdown, markdown(local).encode, path.exists, path.read_bytes, raw.decode, raw_index.decode, relative.endswith, relative.startswith, require, units.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:220`; AST `2078c24ceb7dad6389f02c6ece2e75712b7585af9f2f3ad52de1aed1e13d203b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[1]::If

Source: `infra/agentinfra/roadmap_portability.py:221`; AST `7482ba787b9047f5257a77ceff815c1e420c561c8fb0f1f993d982e942b04c17`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[20].body[1]; no call, error or mutation may be omitted. Condition: not path.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[1].test.operand::Call

Source: `infra/agentinfra/roadmap_portability.py:221`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_portability.py:222`; AST `99539d16b3c55a78e0ab0338d294ed31e812ad2d3fb18d6983c893234f79bcb3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[20].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:223`; AST `24ef828429d8cdba366c2203ccad7e39e88567acfcc03fa79ffd47dcf0d5af8f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: raw_index.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:223`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:224`; AST `9d7a4c24df33166434dc8bef127e7adfa4407d940623765d454244addbac0e6a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, raw_index. Outputs/bindings: index.
Calls/effect boundaries: loads, raw_index.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:224`; AST `d4442c7f09976c25bbc22aa895ff87ce2a03c9485f411605d06dea073b3f2427`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, raw_index. Outputs/bindings: (none).
Calls/effect boundaries: loads, raw_index.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:224`; AST `953a6dd19c3aa302cf1fe68b65cf390aadc27c543b1446233a048b57c9f47390`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw_index. Outputs/bindings: (none).
Calls/effect boundaries: raw_index.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[4]::Expr

Source: `infra/agentinfra/roadmap_portability.py:225`; AST `9446d96dfca9a8dc647bab9f805219018a9dfbda5a36bdddc5a22d6d4ade034c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, require. Outputs/bindings: (none).
Calls/effect boundaries: index.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:225`; AST `09ce875f9c1d34efe3891977039c1e8aafa6ff63c5925350ed2791fee02e521c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index, require. Outputs/bindings: (none).
Calls/effect boundaries: index.get, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[4].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:225`; AST `0dfd72e4abbec17d2d9e43bb99ecd5ccdaf7c821b252e319e37552ccb06ca74a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index. Outputs/bindings: (none).
Calls/effect boundaries: index.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[4].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:225`; AST `1c149d4ddbafd5ba630a01b20b636bf0324b0c933e9de60ee7cf48dda4e7cfa7`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index. Outputs/bindings: (none).
Calls/effect boundaries: index.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:227`; AST `19973d548b4792d8117d81a2342429e82a20a3a6d8581977f139d7dcdf73f5a9`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index. Outputs/bindings: layout.
Calls/effect boundaries: index.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:227`; AST `68b1124d06ef897061bcbf4abacd315b0cd76ee0152dc0c37813a67d81bdb9e8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index. Outputs/bindings: (none).
Calls/effect boundaries: index.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[6]::Expr

Source: `infra/agentinfra/roadmap_portability.py:228`; AST `a3ba467c0b4711e0093ddb3a9f1c60821df2d1787293a3423ad58aa18b52101c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: layout, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:228`; AST `db8a5af6ae2488865c35c83336de6170ef5868270ae078ccdc1fd4615009ca74`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: layout, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[7]::Assign

Source: `infra/agentinfra/roadmap_portability.py:229`; AST `15f94318905b357c2dfcb5ebcc72d44746b08e71b5a6817b2abef4a607f8a870`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw_index. Outputs/bindings: owned, units.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8]::For

Source: `infra/agentinfra/roadmap_portability.py:230`; AST `fa256547638fd57dc3baebdb64d053f1e6e16af185e3503bc04524db376aead5`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: base, canonical, confined_path, digest, expected, index, json, layout, len, loads, owned, raw, relative, require, shard, units, value. Outputs/bindings: expected, raw, relative, shard, value.
Calls/effect boundaries: (json.dumps(value, indent=2, sort_keys=True) + '\n').encode, canonical, confined_path, confined_path(base, relative, must_exist=True).read_bytes, digest, json.dumps, len, loads, raw.decode, relative.endswith, relative.startswith, require, units.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[20].body[8]; no call, error or mutation may be omitted. Iteration: shard in index['shards']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:231`; AST `fd3c055d1711a7d273ff79fea72460a7cfe49b665d811d3775fde37fff7bfa37`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shard. Outputs/bindings: relative.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:232`; AST `6ad95f171e5f155c020abb7fe0282fca5b4e21b7ee1083764d59f7ec9965715b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owned, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: relative.endswith, relative.startswith, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:232`; AST `2b669bfa6bdb83b614036128f9b14723eab0a7ba62a2b4eb2b5e60023122105f`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owned, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: relative.endswith, relative.startswith, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[1].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:232`; AST `e72d467232566e03e080016862c651222855171bb7e434cc7ace6dc2c33d3fea`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.startswith.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[1].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:232`; AST `280cb609a5fbc80c867b1641ed23c58911339f6ea84823f5f75c4c8fc615fdca`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.endswith.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:234`; AST `26fc6396ba4b350f7aa2ad24ff11a95c26e417abe71c138d326d9267d3fd2bf0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, confined_path, relative. Outputs/bindings: raw.
Calls/effect boundaries: confined_path, confined_path(base, relative, must_exist=True).read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:234`; AST `025e402ad1260bafa683daebe76bf9cb425bb054cdadf827f862943690271230`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(base, relative, must_exist=True).read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:234`; AST `a994eefafc1cca8d3131cc4d6245b4575ca89c1a519a385eb6573ca39d2c5eeb`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:235`; AST `f704e32d4ea1247a795405e7bb7cf01ad2d67b3ab01dc66bf0cf679eb6dd393e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, raw. Outputs/bindings: value.
Calls/effect boundaries: loads, raw.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:235`; AST `3cd9d6689794920e55f390bde47f66ddf243c378516a5469daece740a88f9b01`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, raw. Outputs/bindings: (none).
Calls/effect boundaries: loads, raw.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:235`; AST `7e5976c358f689cbba4847a37b23914e4dfb23dfd1a0d1c4648c224ea0e5dc22`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.decode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[4]::Expr

Source: `infra/agentinfra/roadmap_portability.py:236`; AST `3d253935ed1d4d22469a5b07bf32285095e15b4fe14d41c3836398cd4f6455b3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, len, require, shard, value. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:236`; AST `0f3b4d07f02c0b7256eea8f7b004981974df279ce4edaace8604e1d9c733dbd9`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, len, require, shard, value. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[4].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:236`; AST `f5478a66fd3247b8968c1306f6cc686ba6a06ab0db4348065f96da8baff25481`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, value. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[4].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[4].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:236`; AST `713329791aec59f53add5caf311c586cba099b711d44eb59dd19773ebb41188f`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[4].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[5]::Assign

Source: `infra/agentinfra/roadmap_portability.py:238`; AST `de88105d47191babaafcf2416ca5ff1c1cfdc18d830f5a3a9126a4003c8e3c1f`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, json, layout, value. Outputs/bindings: expected.
Calls/effect boundaries: (json.dumps(value, indent=2, sort_keys=True) + '\n').encode, canonical, json.dumps.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[5].value.body.left::Call

Source: `infra/agentinfra/roadmap_portability.py:238`; AST `1a07bd0abe50598ca6ed04aec23bd487f4b47a0fab4fc87670427f80c2369336`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, value. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[5].value.body.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[5].value.orelse::Call

Source: `infra/agentinfra/roadmap_portability.py:238`; AST `225ba4c652be714d79e372dc0730fb4e143a811fdcceb73da1a09cd5810db136`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: (json.dumps(value, indent=2, sort_keys=True) + '\n').encode, json.dumps.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[5].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[5].value.orelse.func.value.left::Call

Source: `infra/agentinfra/roadmap_portability.py:238`; AST `577dafdacf77bead0d6ca77b1c6e85bb552e7f90218c5abfb0b81d492a0794e9`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[5].value.orelse.func.value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[6]::Expr

Source: `infra/agentinfra/roadmap_portability.py:239`; AST `a513e095b5bcb657007955b6f7c5e475714eb0cfbd177f55445dac82c25d1a4c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:239`; AST `209a81850854813230312546c346151d49eb5657a613b59b85a22dbbfdc7a2c8`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[7]::If

Source: `infra/agentinfra/roadmap_portability.py:240`; AST `504e94addeff122f435d136a45e8f6e1d1b9973157af667636494f86411e4f83`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: digest, index, layout, len, raw, require, shard. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[20].body[8].body[7]; no call, error or mutation may be omitted. Condition: layout
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:241`; AST `007791be7654efc0c2f477c3ef9de6e1163ca62e92a2fd79bd322f2d88209767`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, index, len, raw, require, shard. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[8].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:241`; AST `77a71489666e794c48875c3fbb1957b40a4453f7da01faa28d1141bef43961ec`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, index, len, raw, require, shard. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[7].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:241`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[7].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[7].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:241`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[7].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[7].body[0].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_portability.py:242`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[7].body[0].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[8]::Expr

Source: `infra/agentinfra/roadmap_portability.py:243`; AST `07a4c781a9a84a8761561af456cf328146d467fd6eebc58adc1505523ee3fd00`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: units, value. Outputs/bindings: (none).
Calls/effect boundaries: units.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[8].value::Call

Source: `infra/agentinfra/roadmap_portability.py:243`; AST `3e01b6ce0176430c31398b62b62747f645a95df42e044308f97e258b1cfa7b18`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: units, value. Outputs/bindings: (none).
Calls/effect boundaries: units.extend.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[8].body[9]::Assign

Source: `infra/agentinfra/roadmap_portability.py:244`; AST `aa73d26b3bee4d86e05072574024042122d2c82dc8a469456cf566328adf8fd4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owned, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[8].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9]::Expr

Source: `infra/agentinfra/roadmap_portability.py:245`; AST `9a89ca69e21ae4599d85b8b68e29ffff20cb55d9c9f80e046fa3ba422af6764b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, index, len, require, u, units. Outputs/bindings: u.
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9].value::Call

Source: `infra/agentinfra/roadmap_portability.py:245`; AST `df69a3143554a7b42a78c8454e2555fc1c8748f9d3e1f54aa25d927060984c15`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, index, len, require, u, units. Outputs/bindings: u.
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:245`; AST `d334ac4951312a2e5ce0e7d19e1cf4c4a0351088858089c704b81b4d02ed725c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, units. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:245`; AST `8fab30b6203427492d68560cbbe1bcc928799e0969ddeafe764ac4c92e3adca2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, u, units. Outputs/bindings: u.
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9].value.args[0].values[1].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:245`; AST `9d44ba12a05af66e1da558a6a35bb4bf799ffc3eb26e7af15f3ccaf003bdccf4`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[20].body[9].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:245`; AST `d334ac4951312a2e5ce0e7d19e1cf4c4a0351088858089c704b81b4d02ed725c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, units. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[9].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_portability.py:246`; AST `d8886895236ea53b1e4b44144775ee2dabc66f7fad953c17c8e330ab22cef205`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, index, units. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[10]::Expr

Source: `infra/agentinfra/roadmap_portability.py:248`; AST `70423f34603739f026b2405aabd0e9707a190f56705dbe887668e6aa019844f3`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, index, require, u, units. Outputs/bindings: f, u.
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[10].value::Call

Source: `infra/agentinfra/roadmap_portability.py:248`; AST `2713a02ac3f2593540f5814b9fb177921721f846a62e1abf70f336cad22ac08d`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, index, require, u, units. Outputs/bindings: f, u.
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[10].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap_portability.py:248`; AST `a6792201751306dec32bacace38cafab70b8749657d67c6348e222e5e4ea0203`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[20].body[10].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[10].value.args[0].comparators[0]::SetComp

Source: `infra/agentinfra/roadmap_portability.py:248`; AST `7ee4f40a23faf1a0552ba2c33a26e84b7174df5a04de908471e504bedf55faff`.

Rust module: `infra::agentinfra::roadmap_portability`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: f, index. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[20].body[10].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[11]::Assign

Source: `infra/agentinfra/roadmap_portability.py:249`; AST `decdaa05d1520124eb58acd68a16c61489b531f43fcbc40fc91e61af5fcf263b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, index, units. Outputs/bindings: previous.
Calls/effect boundaries: dict.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[11].value::Call

Source: `infra/agentinfra/roadmap_portability.py:249`; AST `ff00cd033a3896a7e1641a6a2fba6d73f53449035eef9f8a9d8eb8b820892451`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, index, units. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12]::For

Source: `infra/agentinfra/roadmap_portability.py:250`; AST `a967de59a99a64b69e214d32c5afad7fa7936e1ff1526adf562a672dbc49f53a`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _document_path, base, confined_path, dict, expected, file_record, index, layout, local, markdown, owned, previous, raw, relative, require, source, u, units. Outputs/bindings: expected, local, raw, relative, source, u.
Calls/effect boundaries: _document_path, confined_path, confined_path(base, relative, must_exist=True).read_bytes, dict, file_record, markdown, markdown(local).encode, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[20].body[12]; no call, error or mutation may be omitted. Iteration: source in index['files']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_portability.py:251`; AST `9cd5037e83fb7b6bb9a1f3d2c64d6ed8dc62db4ea8657a5249275bc37fe58988`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _document_path, source. Outputs/bindings: relative.
Calls/effect boundaries: _document_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:251`; AST `50b1c36d4b7e7d960e60d0ffbff23f21043db13b0a828265479ef33cdfe8cbac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _document_path, source. Outputs/bindings: (none).
Calls/effect boundaries: _document_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:252`; AST `1722130ca7072e88e499c40f21ea9e2fe990c1c60c9ff2392e70c968d4ff99c8`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owned, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:252`; AST `fb381445256a73d172518a08a140d70387a6ee02b4d6ae8e5ab9eeba0a506d05`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owned, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:253`; AST `64c939396b6ae86581d059878a8de54185d864beb4f32083b615160032e1e187`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, file_record, layout, previous, source, u, units. Outputs/bindings: local, u.
Calls/effect boundaries: dict, file_record.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[2].value.body::Call

Source: `infra/agentinfra/roadmap_portability.py:253`; AST `051908352b2961c5e90e90346add0fb676d93281ecc68b5486569758ea531639`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_record, previous, source. Outputs/bindings: (none).
Calls/effect boundaries: file_record.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[2].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[2].value.orelse::Call

Source: `infra/agentinfra/roadmap_portability.py:253`; AST `b4f96aa5b3016c1d56d25086e12863a73d36c41abd2c61fa2fe73e77542da0df`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, previous, source, u, units. Outputs/bindings: u.
Calls/effect boundaries: dict.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[2].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[2].value.orelse.keywords[1].value::ListComp

Source: `infra/agentinfra/roadmap_portability.py:253`; AST `49a76591c5c47c887f0b9d0dfe52a39fa8da8250da55b84243ac197dce487208`.

Rust module: `infra::agentinfra::roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: source, u, units. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[20].body[12].body[2].value.orelse.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:254`; AST `bfb03ba2e221aac2a3d8618341b341f1101b7132bbf2780647ae7cd1b222e1a4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: local, markdown. Outputs/bindings: expected.
Calls/effect boundaries: markdown, markdown(local).encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:254`; AST `8f709b49be1f246e2dc44df16412da2383518d22752cc50c0794a1ed36858a95`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: local, markdown. Outputs/bindings: (none).
Calls/effect boundaries: markdown, markdown(local).encode.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:254`; AST `dbf9e5722c8177ff78bdbe305e7d02bd9a18e883bee89f60a375c06647425bbd`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: local, markdown. Outputs/bindings: (none).
Calls/effect boundaries: markdown.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:255`; AST `26fc6396ba4b350f7aa2ad24ff11a95c26e417abe71c138d326d9267d3fd2bf0`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, confined_path, relative. Outputs/bindings: raw.
Calls/effect boundaries: confined_path, confined_path(base, relative, must_exist=True).read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:255`; AST `025e402ad1260bafa683daebe76bf9cb425bb054cdadf827f862943690271230`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(base, relative, must_exist=True).read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:255`; AST `a994eefafc1cca8d3131cc4d6245b4575ca89c1a519a385eb6573ca39d2c5eeb`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[5]::Expr

Source: `infra/agentinfra/roadmap_portability.py:256`; AST `1d1178113c70ab8a20abd0558119c6bce3d89e1c79dccf7762bf6f4df456d01c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:256`; AST `52c18fbf0b4ac304c9fad8b131489e9e948514a35e64562148ce623905491b41`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[12].body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:257`; AST `aa73d26b3bee4d86e05072574024042122d2c82dc8a469456cf566328adf8fd4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owned, raw, relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::_previous_artifacts::root.body[20].body[13]::Return

Source: `infra/agentinfra/roadmap_portability.py:258`; AST `7738d032dc33993df60aef5b916f358e1605e7b3ea4f085dec551c991cfb1690`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owned. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[20].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:261`; AST `2b9cffdddbd011e00c619740c61a762f8dec142c439176ed73d4d6280f420505`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, FileLock, FileTransaction, Mutation, Path, TransactionError, _previous_artifacts, after, artifacts, assert_sources, base, before, confined_path, dict, digest, exc, index, len, lock, mutations, old_index, output, path, previous, record, recover_named_transactions, relative, require, root, set, sorted, state. Outputs/bindings: after, base, before, index, lock, mutations, old_index, output, path, previous, relative, root, state.
Calls/effect boundaries: ContractError, FileLock, FileTransaction, FileTransaction(root, mutations, state_dir=state, name='aegis-portability').commit, Mutation, _previous_artifacts, artifacts, assert_sources, confined_path, digest, len, lock.acquire, lock.release, mutations.append, output.get, path.exists, path.read_bytes, previous.get, recover_named_transactions, require, root.resolve, set, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:262`; AST `5359fe675fe99d16ae4fda070d6cb77e26ffdd854f71545e29c59cadb805817b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:263`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:263`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:264`; AST `a761fb1ff993586397df76954202802d04f9aaa7055f9d1db68a87df1a3ef23b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: base.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:265`; AST `b0e0971c78034de4539d465a4d2d69f3ed56c4a712ce0203de722c5edd1aefc8`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:266`; AST `b6d2d75c8376b65162da62ff22eda51c10131a33d85bba5a1c73a3d6afb6abb2`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:266`; AST `c6d80851e1cf599eef0d59bd9aa25808b7e300c37405399d90e64e5214de9f62`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[5]::Expr

Source: `infra/agentinfra/roadmap_portability.py:267`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[5].value::Call

Source: `infra/agentinfra/roadmap_portability.py:267`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6]::Try

Source: `infra/agentinfra/roadmap_portability.py:268`; AST `cd9b0439fc321b769ca2a20a29ab1869e4b8289d16cf5c822720a3bdb0f7f1b6`.

Rust module: `infra::agentinfra::roadmap_portability`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ContractError, FileTransaction, Mutation, TransactionError, _previous_artifacts, after, artifacts, assert_sources, base, before, confined_path, digest, exc, index, len, lock, mutations, old_index, output, path, previous, record, recover_named_transactions, relative, require, root, set, sorted, state. Outputs/bindings: after, before, index, mutations, old_index, output, path, previous, relative.
Calls/effect boundaries: ContractError, FileTransaction, FileTransaction(root, mutations, state_dir=state, name='aegis-portability').commit, Mutation, _previous_artifacts, artifacts, assert_sources, confined_path, digest, len, lock.release, mutations.append, output.get, path.exists, path.read_bytes, previous.get, recover_named_transactions, require, set, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Try evaluation at root.body[21].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:269`; AST `e1c20f6f8d16eb2a94a2de749a976479a7ab6a46ba1359651e3581d36cbf94ce`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recover_named_transactions, root, state. Outputs/bindings: (none).
Calls/effect boundaries: recover_named_transactions.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:269`; AST `b404a24383abd6ed3b22511222114bf6a5c74c186d73e6c603185eb693fbb703`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recover_named_transactions, root, state. Outputs/bindings: (none).
Calls/effect boundaries: recover_named_transactions.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[1]::Expr

Source: `infra/agentinfra/roadmap_portability.py:270`; AST `6942af7609acf3dd5cb355575971e15ed8f16988e677a47d9558aa3d38395e73`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:270`; AST `fd63307d6092b7b03a93b01d00ef0d4cc90e586d0aa2e0cd6a5383e681af5092`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:271`; AST `888029456e3e311892aab257d5f3bcbe36005e0e5af0199406a964aa8786ec67`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _previous_artifacts, base. Outputs/bindings: previous.
Calls/effect boundaries: _previous_artifacts.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:271`; AST `7e0e124d0e45fbfe606210dee917a83048d864155451a1a09059f94c26507825`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _previous_artifacts, base. Outputs/bindings: (none).
Calls/effect boundaries: _previous_artifacts.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_portability.py:272`; AST `711bd7fc326435ee499cf67dc3bf0377b12da45660df8a20b10976fbe2e2b130`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, record. Outputs/bindings: index, output.
Calls/effect boundaries: artifacts.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[3].value::Call

Source: `infra/agentinfra/roadmap_portability.py:272`; AST `e871a7c4e4c56cc8b6474f468a3c079fab9a6680d054a5dc6c8086f418e23a35`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, record. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:273`; AST `8ee07de8e13d2693d7998cf58b3b780aa35391c1f14b9d647ef73d9dc97199f5`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: mutations.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5]::For

Source: `infra/agentinfra/roadmap_portability.py:274`; AST `9842464d58d5fbeb2e332f8d71267cbd9014b5541b27673e44a1873d3ceb9fca`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Mutation, after, base, before, confined_path, digest, mutations, output, path, previous, relative, require, root, set, sorted. Outputs/bindings: after, before, path, relative.
Calls/effect boundaries: Mutation, confined_path, digest, mutations.append, output.get, path.exists, path.read_bytes, previous.get, require, set, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[21].body[6].body[5]; no call, error or mutation may be omitted. Iteration: relative in sorted(set(previous) | set(output))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:274`; AST `c19e15ec5282d1c32e77cff7c44ace895e539d4eca81abc601851a6a6d528a36`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, previous, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].iter.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:274`; AST `5b62bef02906d93e30195dcb42e09285e0c1a393975ef3e1b839c02853cb02a5`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].iter.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].iter.args[0].right::Call

Source: `infra/agentinfra/roadmap_portability.py:274`; AST `d0c45725c296da04229c2c0e5aed10209b6239b7dd6aa5b01d11a1431e4e917b`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].iter.args[0].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[0]::If

Source: `infra/agentinfra/roadmap_portability.py:275`; AST `1ec7a4ff15c3d7bf7863c5d99d87d08dacb56d0b4d427db78e7f6d709e97e008`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[5].body[0]; no call, error or mutation may be omitted. Condition: relative == 'inventory.json'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[0].body[0]::Continue

Source: `infra/agentinfra/roadmap_portability.py:276`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Continue evaluation at root.body[21].body[6].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:277`; AST `59df9af85f58a2b89826e3e5f7787cb6f42df3c0e68a355e128e444a06a19dfd`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, confined_path, relative, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:277`; AST `aad517c482818a0dcd4d6d3cbf5fa2cf9daa161cca8e7407d5836398869f9ce5`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:278`; AST `5966f78746382297e52f4b53b3642ae113e6eef3a00ad32892f3cdd09827ad47`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous, relative. Outputs/bindings: before.
Calls/effect boundaries: previous.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_portability.py:278`; AST `b9c8b568366e71a1be1eefe2032303f7454cffb56b79207491f783df2411ca7e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, relative. Outputs/bindings: (none).
Calls/effect boundaries: previous.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3]::If

Source: `infra/agentinfra/roadmap_portability.py:279`; AST `bc0fc6879d3af2d52d2c6f8a9a781f697f4b6440f617096ed186ee996b3915f8`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: before, output, path, relative, require. Outputs/bindings: before.
Calls/effect boundaries: path.exists, path.read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[5].body[3]; no call, error or mutation may be omitted. Condition: before is None and path.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3].test.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:279`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[3].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:280`; AST `7fa673bb0d1bd0a8cbef503e7c5a123153a661c92226cc440e8729d455ef6172`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, path, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:280`; AST `db42007da247bf451af434f2c7d76803be6c38be1dcb68ced526c2aa47b966aa`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, path, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_portability.py:280`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[3].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:282`; AST `7be2c3931aa069b4d490b975d00dcc6fda3e361647bf2bec6a22f528d37d0897`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[5].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:282`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[4]::Assign

Source: `infra/agentinfra/roadmap_portability.py:283`; AST `dd349ee283fcb89b7d6c3e2ebe4a5efcc2c800c079a81b33135c1ef43b2831b4`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, relative. Outputs/bindings: after.
Calls/effect boundaries: output.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:283`; AST `15c6baaf308ddd15c914b804565295589c133fcbc3a3ddffb98dfc255878163a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, relative. Outputs/bindings: (none).
Calls/effect boundaries: output.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[5]::If

Source: `infra/agentinfra/roadmap_portability.py:284`; AST `d7610154cc927c8a012f5c84fb3d6283e119e1b43c81ead66739c346d13110a9`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: Mutation, after, before, digest, mutations, path. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, mutations.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[5].body[5]; no call, error or mutation may be omitted. Condition: before != after
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:285`; AST `457b4fde56ba04e29fe3fe88967d86b63e78594bb2349557e0842ccd494b0e46`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Mutation, after, before, digest, mutations, path. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, mutations.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:285`; AST `e70e880520b5745bbdf2a445eac71c49d135ddfb99909a5819efe5715eb17871`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, after, before, digest, mutations, path. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, mutations.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[5].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:285`; AST `8f04dbcaeb188a9abb0168f127b03dc0d292c4ffadb724db15950078d2592de5`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, after, before, digest, path. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[5].body[5].body[0].value.args[0].keywords[1].value.body::Call

Source: `infra/agentinfra/roadmap_portability.py:286`; AST `4a63ff00fb497e1d094ddb9e4f8ada535aacd403c14cfceee7fc8dd669fbee57`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].body[5].body[0].value.args[0].keywords[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[6]::Assign

Source: `infra/agentinfra/roadmap_portability.py:287`; AST `7046e34b9621606bd2a5bfbe7861fc774d0fbdea62bc9137af9dabfbb6392e5a`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous. Outputs/bindings: old_index.
Calls/effect boundaries: previous.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[6].value::Call

Source: `infra/agentinfra/roadmap_portability.py:287`; AST `f4e1d07a43bf66a9886358434161a0047117c6a95b8e2f0a9ca53934c8907ec5`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous. Outputs/bindings: (none).
Calls/effect boundaries: previous.get.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[7]::If

Source: `infra/agentinfra/roadmap_portability.py:288`; AST `0587101f91bf9e2f736469dcc58774bbefa1120215e5d1c6fc85b6cc840ea4eb`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: Mutation, base, digest, mutations, old_index, output. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, mutations.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[7]; no call, error or mutation may be omitted. Condition: old_index != output['inventory.json']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:289`; AST `2bbb8650b5bb4c2ec8022ace4f9aa709b9d34ad3289b0df5eee34cbea8689808`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Mutation, base, digest, mutations, old_index, output. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, mutations.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:289`; AST `27b3278a719d398d5e8c0b7acb987776579210f2aacc573024d0903ff76c7810`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, base, digest, mutations, old_index, output. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, mutations.append.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[7].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:289`; AST `0b22ea25b08761eac709057bb7c666402a70457dd4d26c6130cd5b70ffbcacf2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, base, digest, old_index, output. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[7].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[7].body[0].value.args[0].keywords[1].value.body::Call

Source: `infra/agentinfra/roadmap_portability.py:291`; AST `d555dc5e0768e5965e6acba6ccf81b9cc4fa55b3fd035708f310f091a215abcf`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, old_index. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[7].body[0].value.args[0].keywords[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[8]::Expr

Source: `infra/agentinfra/roadmap_portability.py:292`; AST `6942af7609acf3dd5cb355575971e15ed8f16988e677a47d9558aa3d38395e73`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[8].value::Call

Source: `infra/agentinfra/roadmap_portability.py:292`; AST `fd63307d6092b7b03a93b01d00ef0d4cc90e586d0aa2e0cd6a5383e681af5092`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[9]::If

Source: `infra/agentinfra/roadmap_portability.py:293`; AST `085799e03b301e30ee4e5a92ef0260b43138f3072491c3eb7ebf3f464be13e5d`.

Rust module: `infra::agentinfra::roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: FileTransaction, mutations, root, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, mutations, state_dir=state, name='aegis-portability').commit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[9]; no call, error or mutation may be omitted. Condition: mutations
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:294`; AST `66163988c048fee3d5cdf471101388e9402fd2043a1ea344d9d74a296d546435`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, mutations, root, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, mutations, state_dir=state, name='aegis-portability').commit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:294`; AST `80e41b844dba2194864941782deb80e440de5aedc7fae37a2bed17825b96de56`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, mutations, root, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, mutations, state_dir=state, name='aegis-portability').commit.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[9].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:294`; AST `9b6a46172857fec2af48693a5e3e393382ccc70990c3c9bc32fffbe4aa8bb732`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, mutations, root, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[9].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[10]::Expr

Source: `infra/agentinfra/roadmap_portability.py:295`; AST `6942af7609acf3dd5cb355575971e15ed8f16988e677a47d9558aa3d38395e73`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[10].value::Call

Source: `infra/agentinfra/roadmap_portability.py:295`; AST `fd63307d6092b7b03a93b01d00ef0d4cc90e586d0aa2e0cd6a5383e681af5092`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[11]::Return

Source: `infra/agentinfra/roadmap_portability.py:296`; AST `63cdeaad8c4ac1398fb6c5595c675729d60dc4ba05692fb17ae7ed5385e51069`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, len, mutations, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[6].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[11].value.values[0]::Call

Source: `infra/agentinfra/roadmap_portability.py:296`; AST `df46df88acf5e6ef901488c4610d14a5b71f816377a047e8ea3cd040d31bfe4e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[11].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[11].value.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:296`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[11].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[11].value.values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:296`; AST `fa4085b49df6c96630e23e7a5a559c1d9c50381e62bbc344bbd24c11a1794f7c`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[11].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].body[11].value.values[4]::Call

Source: `infra/agentinfra/roadmap_portability.py:297`; AST `8faa21adb46cfa2185f8218d8ee8b67eb6f641f36014b5666b9bf7170e7ff518`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, mutations. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[11].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_portability.py:299`; AST `e3ecbebadb4e181f42d69ba5790db54e79a4590ebb9fb1120809af6df4cdc919`.

Rust module: `infra::agentinfra::roadmap_portability`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ContractError, TransactionError, exc. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[21].body[6].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].handlers[0].body[0]::Raise

Source: `infra/agentinfra/roadmap_portability.py:300`; AST `2d4bae3e9b5b1a70d770ab76681f6cd8c497ecb39d2d5e1609e7f8ba7246175c`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, exc. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[6].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/roadmap_portability.py:300`; AST `b66d25fd9808eed185214d00f885f066bdb80e588d011a8cb6469c7e6604b596`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, exc. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:302`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::publish::root.body[21].body[6].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:302`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22]::FunctionDef

Source: `infra/agentinfra/roadmap_portability.py:305`; AST `945b9b89de7dfbbe843fba3226364dc4db9607627993f75e1edb99b737977fb4`.

Rust module: `infra::agentinfra::roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, artifacts, assert_sources, base, confined_path, dict, expected, len, raw, record, relative, require, root. Outputs/bindings: _, base, expected, raw, relative.
Calls/effect boundaries: artifacts, assert_sources, confined_path, confined_path(root, base / relative, must_exist=True).read_bytes, expected.items, len, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:306`; AST `6942af7609acf3dd5cb355575971e15ed8f16988e677a47d9558aa3d38395e73`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:306`; AST `fd63307d6092b7b03a93b01d00ef0d4cc90e586d0aa2e0cd6a5383e681af5092`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[1]::Assign

Source: `infra/agentinfra/roadmap_portability.py:307`; AST `b2f795c2ca78da9d1273883d85ab3accd75e764167797c3e87d6330fc9df00e6`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, record. Outputs/bindings: _, expected.
Calls/effect boundaries: artifacts.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[1].value::Call

Source: `infra/agentinfra/roadmap_portability.py:307`; AST `e871a7c4e4c56cc8b6474f468a3c079fab9a6680d054a5dc6c8086f418e23a35`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, record. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[2]::Assign

Source: `infra/agentinfra/roadmap_portability.py:308`; AST `a761fb1ff993586397df76954202802d04f9aaa7055f9d1db68a87df1a3ef23b`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: base.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[3]::For

Source: `infra/agentinfra/roadmap_portability.py:309`; AST `6ec6f634873a7eda667cee7058621ecbdd4eb082056036bd3e489ed6e1bbeee6`.

Rust module: `infra::agentinfra::roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: base, confined_path, expected, raw, relative, require, root. Outputs/bindings: raw, relative.
Calls/effect boundaries: confined_path, confined_path(root, base / relative, must_exist=True).read_bytes, expected.items, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[22].body[3]; no call, error or mutation may be omitted. Iteration: (relative, raw) in expected.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[3].iter::Call

Source: `infra/agentinfra/roadmap_portability.py:309`; AST `2638a7ca6e900ccf7a3e6146bd68b01e243a5b1ad0f817cbc2a1ddd6e81c0d4a`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected. Outputs/bindings: (none).
Calls/effect boundaries: expected.items.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_portability.py:310`; AST `d7aa9d5a6f49252314b5181736d68612f372d52cfe1af049c300dc6eed2d3a8e`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, confined_path, raw, relative, require, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, base / relative, must_exist=True).read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_portability.py:310`; AST `87b243c8155fcbf876c9d9388dcd91e6ffbe87f05c6fc954539599920eef64d9`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, raw, relative, require, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, base / relative, must_exist=True).read_bytes, require.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[3].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_portability.py:310`; AST `5ea4b7ecc6f47c8ae16e96ccb30f5c6b0cf608857d99fb3ef49fc92b59cd3dc2`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, base / relative, must_exist=True).read_bytes.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[3].body[0].value.args[0].left.func.value::Call

Source: `infra/agentinfra/roadmap_portability.py:310`; AST `f8bf0221d55c20f1a71d2ad99db9ac10e1e156efd72b2a2304ed4bee02126d00`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].body[0].value.args[0].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[4]::Expr

Source: `infra/agentinfra/roadmap_portability.py:312`; AST `6942af7609acf3dd5cb355575971e15ed8f16988e677a47d9558aa3d38395e73`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[4].value::Call

Source: `infra/agentinfra/roadmap_portability.py:312`; AST `fd63307d6092b7b03a93b01d00ef0d4cc90e586d0aa2e0cd6a5383e681af5092`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_sources, record, root. Outputs/bindings: (none).
Calls/effect boundaries: assert_sources.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[5]::Return

Source: `infra/agentinfra/roadmap_portability.py:313`; AST `6756fafdd70b48524e65932e80fa90066ba1be33989aba3e91465d64818bda96`.

Rust module: `infra::agentinfra::roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[22].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[5].value.values[1]::Call

Source: `infra/agentinfra/roadmap_portability.py:313`; AST `df46df88acf5e6ef901488c4610d14a5b71f816377a047e8ea3cd040d31bfe4e`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[5].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_portability.py::module::check::root.body[22].body[5].value.values[2]::Call

Source: `infra/agentinfra/roadmap_portability.py:313`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, json, locks, pathlib, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[5].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
