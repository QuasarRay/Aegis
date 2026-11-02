# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 304. Inventory digest: `268f12c238c40b5cdff308844ea34a8556f406d06b70ebf6af1ad871a63f752e`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_interfaces.py::module::root::Module

Source: `infra/agentinfra/roadmap_interfaces.py:1`; AST `4bec86d65e70b7f16c475158bf595621df1967e9cd21cea1853f71817a3a488a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: GitInventory, INTERFACE_VERSION, KEYWORDS, LAYERS, Path, _compatible, _exports, _module, _public, _schema_vocabulary, _signature, after, any, ast, baseline, baseline_ref, before, bool, bytes, candidate, changes, child, collection, compile, confined_path, constants, context, current, d, definition, dependencies, dependency, dict, digest, entry, exported, exports, field, fields, file_binding, getattr, git, guards, importlib, int, isinstance, k, key, layer, len, list, loads, m, method, methods, module, modules, n, name, names, next, node, now, observe_interfaces, old, old_schemas, owners, package, path, paths, predicates, previous, previous_protocols, raw, read_json, require, result, root, schema, schema_binding, schemas, set, signature, sorted, statements, str, sys, target, tree, tuple, type, v, value, version, visit, zip. Outputs/bindings: INTERFACE_VERSION, LAYERS, after, baseline, before, candidate, changes, child, collection, constants, context, current, d, definition, dependencies, dependency, entry, exported, exports, field, fields, git, k, key, layer, m, method, methods, module, modules, n, name, names, node, now, old, old_schemas, owners, package, path, paths, predicates, previous_protocols, result, root, schema, schema_binding, schemas, signature, target, tree, v, value, version.
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, GitInventory, LAYERS.items, Path, Path(sys.executable).read_bytes, _compatible, _exports, _module, _public, _schema_vocabulary, _signature, after.get, after.get('methods', {}).get, after.items, any, ast.dump, ast.iter_fields, ast.literal_eval, ast.parse, ast.unparse, ast.walk, before.get, before.items, before['methods'].items, bool, changes.append, compile, confined_path, confined_path(root, path, must_exist=True).read_bytes, current['record_protocols'].get, definition.get, definition.get('properties', {}).get, definition.get('properties', {}).get('schema', {}).get, dependencies.add, dependencies.update, dict, digest, entry['path'].endswith, entry['path'].startswith, exports.setdefault, exports.setdefault(node.name, []).append, file_binding, getattr, git.blob, git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline_ref + '^{commit}').strip, git.read('rev-parse', baseline + ':Roadmaps/Shared/records.schema.json').strip, git.tree, importlib.util.resolve_name, isinstance, key.endswith, key.removesuffix, len, list, loads, methods.setdefault, methods.setdefault(method.name, []).append, module['exports'].items, name.endswith, name.rpartition, name.startswith, next, now[name]['exports'].get, observe_interfaces, old.items, old_schemas.decode, package['declared_versions'].get, path.relative_to, path.relative_to(root).as_posix, path.removeprefix, path.removeprefix('infra/agentinfra/').removesuffix, path.removeprefix('infra/agentinfra/').removesuffix('.py').replace, previous_protocols.items, read_json, require, root.resolve, schema.get, schema.get(collection, {}).values, schemas['$defs'].items, set, sorted, type, visit, zip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:1`; AST `2fdbc63ac4ac074a619e8fa4ac406cb972ffb6e61e5238c76f41d4b28da36b38`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_interfaces.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_interfaces.py:9`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_interfaces.py:10`; AST `866a97c0a29d398dc2bf8a74409548dccd9bb5221f4bf0f58ad1a37ef83e5260`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_interfaces.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_interfaces.py:12`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_interfaces.py:14`; AST `0fc966ee6b50ec82c02899d679da760b485c6564141d0e00c5c6deb2950693ff`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_interfaces.py:15`; AST `e13837c8d9d31575c34dbd76e83b360f6c8bf9520da353e84d3d0bba4eb74f41`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_interfaces.py:16`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[9]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:19`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::root.body[10]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:20`; AST `66cbe245c38a38227baf1cab814da2eff8e25c7a89c82543c674f1c8e1b8b44c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: LAYERS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:36`; AST `211d102014f7f1b08fadb789b18720a692c45262f5db63a54e1b18091fa2781e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ast, d, dict, node, type. Outputs/bindings: d.
Calls/effect boundaries: ast.dump, ast.unparse, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11].body[0]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:37`; AST `cc6ad832bd490b8c95f8b5872114f45a127487b1dd2db2e975ab99e92b85d929`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, d, node, type. Outputs/bindings: d.
Calls/effect boundaries: ast.dump, ast.unparse, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11].body[0].value.values[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:37`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11].body[0].value.values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:37`; AST `a9d78e957fb87634fba581906a154ff6af377aa56a4ad86384b49bf03292d0e8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11].body[0].value.values[2].body::Call

Source: `infra/agentinfra/roadmap_interfaces.py:38`; AST `9e1cbf2442985cf16ca626538eada2131fb3bf038101a678bc158d7bfeb9d6ab`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.values[2].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11].body[0].value.values[3]::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:39`; AST `de38e679edd9229e802a376a2c0f67c3997ee565bb08b86247141da0bb22fb5f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, d, node. Outputs/bindings: d.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[0].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_signature::root.body[11].body[0].value.values[3].elt::Call

Source: `infra/agentinfra/roadmap_interfaces.py:39`; AST `960aec68e7ac7577aed5d4a1075592bd6959447af29813a91cf0365548fd7774`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, d. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.values[3].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_public::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:42`; AST `1a0d4bc9118d92557a9c8856f1f24d14bf3b6c6f36194073acaf3623e65219ea`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, method, name, str. Outputs/bindings: (none).
Calls/effect boundaries: name.endswith, name.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_public::root.body[12].body[0]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:43`; AST `c4c5072c6bdd8dadc55911b3639686cc3678e861bb8530abf88e4542c75b52cf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: method, name. Outputs/bindings: (none).
Calls/effect boundaries: name.endswith, name.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_public::root.body[12].body[0].value.values[0].operand::Call

Source: `infra/agentinfra/roadmap_interfaces.py:43`; AST `40ed6bb4c1c523a3e31a2ca9de0e1794e8fd2cdbd6fe31b50111881ad81df90e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_public::root.body[12].body[0].value.values[1].values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:43`; AST `7431de30ae0cce6151a501c2cfec30fa0c87eb775b8558fab7c1912e57ef9b8b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value.values[1].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_public::root.body[12].body[0].value.values[1].values[2]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:43`; AST `56872a583038e232e8220ee1194d5100ff54a3fe82a0524c7aa9fc9ee20ffbca`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.endswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value.values[1].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:46`; AST `840f0dcf243360acb733756ac73e377fe6f2df6ea35f6b5e23233161a9dcb92b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _public, _signature, ast, context, dict, exports, field, fields, getattr, guards, isinstance, key, list, method, methods, n, node, predicates, statements, str, tree, tuple, type, value, visit. Outputs/bindings: context, exports, field, fields, key, method, methods, n, node, predicates, value.
Calls/effect boundaries: _public, _signature, ast.dump, ast.iter_fields, ast.unparse, dict, exports.setdefault, exports.setdefault(node.name, []).append, getattr, isinstance, list, methods.setdefault, methods.setdefault(method.name, []).append, type, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::root.body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:47`; AST `90c1c1bf758623c3ab488740a42892e6dcdbd0bb1e99ccf9878182d7cf21e70f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: exports.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:49`; AST `a2b499945a2f6fe508ef6a6b2b4faade85c942d89e0a5e69bf21c15d24539c0d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _public, _signature, ast, context, dict, exports, field, fields, getattr, guards, isinstance, key, list, method, methods, n, node, predicates, statements, str, tuple, type, value, visit. Outputs/bindings: context, field, fields, key, method, methods, n, node, predicates, value.
Calls/effect boundaries: _public, _signature, ast.dump, ast.iter_fields, ast.unparse, dict, exports.setdefault, exports.setdefault(node.name, []).append, getattr, isinstance, list, methods.setdefault, methods.setdefault(method.name, []).append, type, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0]::For

Source: `infra/agentinfra/roadmap_interfaces.py:50`; AST `44be60428b9d775e1180e0e25edd31f4ba4e2f28a402f54a0f5cf1997f5e09c6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _public, _signature, ast, context, dict, exports, field, fields, getattr, guards, isinstance, key, list, method, methods, n, node, predicates, statements, type, value, visit. Outputs/bindings: context, field, fields, key, method, methods, n, node, predicates, value.
Calls/effect boundaries: _public, _signature, ast.dump, ast.iter_fields, ast.unparse, dict, exports.setdefault, exports.setdefault(node.name, []).append, getattr, isinstance, list, methods.setdefault, methods.setdefault(method.name, []).append, type, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[13].body[1].body[0]; no call, error or mutation may be omitted. Iteration: node in statements
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:51`; AST `1f671f95eeb09abec013869128f9bef4c4787eec4b6af77068b98001d21a7318`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _public, _signature, ast, context, dict, exports, field, fields, getattr, guards, isinstance, key, list, method, methods, n, node, predicates, type, value, visit. Outputs/bindings: context, field, fields, key, method, methods, n, predicates, value.
Calls/effect boundaries: _public, _signature, ast.dump, ast.iter_fields, ast.unparse, dict, exports.setdefault, exports.setdefault(node.name, []).append, getattr, isinstance, list, methods.setdefault, methods.setdefault(method.name, []).append, type, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:51`; AST `d523540114cb218c0baa8bed353866eefa83eeecc4510dc6dfe4652ce5cc8c32`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:52`; AST `a5f2304ff75e5b635bbfba6bd34606180b55084fe4eb592189931f187b827cfc`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _public, _signature, dict, exports, guards, list, node. Outputs/bindings: (none).
Calls/effect boundaries: _public, _signature, dict, exports.setdefault, exports.setdefault(node.name, []).append, list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0].body[0]; no call, error or mutation may be omitted. Condition: _public(node.name)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:52`; AST `fcaf27c2a1392cbf18cde9eec00a4d2e7ae39cc422a1f640f5c3f225bccfe15c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _public, node. Outputs/bindings: (none).
Calls/effect boundaries: _public.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:53`; AST `66f198627d44655d428fc5be0b13e7879d647f65953533c50ae1b9a96f139d36`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _signature, dict, exports, guards, list, node. Outputs/bindings: (none).
Calls/effect boundaries: _signature, dict, exports.setdefault, exports.setdefault(node.name, []).append, list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:53`; AST `a0fc7ee24683ad25d0a31feadda11efc362659c71288e765fd1c6aba2834c2e4`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _signature, dict, exports, guards, list, node. Outputs/bindings: (none).
Calls/effect boundaries: _signature, dict, exports.setdefault, exports.setdefault(node.name, []).append, list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:53`; AST `e891a9343424ea56d4fcfea5d1492b2952f4e128d2a11b602af22ef3ea387d90`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exports, node. Outputs/bindings: (none).
Calls/effect boundaries: exports.setdefault.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:53`; AST `6dda73ec5ef23922fbaaf977a7b6499ea8fc9969639d3cbfecd5f3762d42246f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _signature, dict, guards, list, node. Outputs/bindings: (none).
Calls/effect boundaries: _signature, dict, list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].body[0].value.args[0].args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:53`; AST `d89a8446306dc0cbd4fffa8061f98ecd9b106f1e9f9e60cc8afa26caf0c7a5e5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _signature, node. Outputs/bindings: (none).
Calls/effect boundaries: _signature.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].body[0].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].body[0].body[0].value.args[0].keywords[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:53`; AST `575e768b2571fe4a81ae12dfac22a3e34ae9435ba8414308b7368109d4c504a0`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: guards, list. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].body[0].body[0].value.args[0].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:54`; AST `36f12fc2cb1f4793b533a14b06f4426051d3f9f2285525a65b3b32c377f3839b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _public, _signature, ast, context, exports, field, fields, getattr, guards, isinstance, key, list, method, methods, n, node, predicates, type, value, visit. Outputs/bindings: context, field, fields, key, method, methods, n, predicates, value.
Calls/effect boundaries: _public, _signature, ast.dump, ast.iter_fields, ast.unparse, exports.setdefault, exports.setdefault(node.name, []).append, getattr, isinstance, list, methods.setdefault, methods.setdefault(method.name, []).append, type, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.ClassDef)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:54`; AST `f173a8d685cc2749ba14dc2c482a20216b571d6eae1d4f6f2706b464a903e72c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:55`; AST `0437471e3763d27c38336c41bc20a36e850a508d2299158b8d2ea0534f3950de`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _public, node. Outputs/bindings: (none).
Calls/effect boundaries: _public.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[0]; no call, error or mutation may be omitted. Condition: not _public(node.name)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[0].test.operand::Call

Source: `infra/agentinfra/roadmap_interfaces.py:55`; AST `fcaf27c2a1392cbf18cde9eec00a4d2e7ae39cc422a1f640f5c3f225bccfe15c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _public, node. Outputs/bindings: (none).
Calls/effect boundaries: _public.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[0].body[0]::Continue

Source: `infra/agentinfra/roadmap_interfaces.py:56`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Continue evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:57`; AST `d218fcfc7ccd3c3b677ca687a7f390b1fc4c582036f83e7006b2eba2c47132bb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: methods.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2]::For

Source: `infra/agentinfra/roadmap_interfaces.py:58`; AST `588ccb0f77a37961ec46cdd38315a81b5d0b9c7dff32ed2ab61ddcbe9d27152d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _public, _signature, ast, isinstance, method, methods, node. Outputs/bindings: method.
Calls/effect boundaries: _public, _signature, isinstance, methods.setdefault, methods.setdefault(method.name, []).append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2]; no call, error or mutation may be omitted. Iteration: method in node.body
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:59`; AST `c7b34b27cc16b1483f028091584b190fc5a164065a0f02a517df6dab8e932c9b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _public, _signature, ast, isinstance, method, methods. Outputs/bindings: (none).
Calls/effect boundaries: _public, _signature, isinstance, methods.setdefault, methods.setdefault(method.name, []).append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0]; no call, error or mutation may be omitted. Condition: isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) and _public(method.name, method=True)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:59`; AST `1c2b56f7acf401765c9dff0488372c7c4ea7e9cc4f9f4cf61c7011b6bce840af`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, method. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:59`; AST `67db542dd81f503eba8ba91b9447b22c091d74df6767ef63a76c41f42572d624`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _public, method. Outputs/bindings: (none).
Calls/effect boundaries: _public.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:60`; AST `c14e600f4c09eb51b09f7673c20d8d59ae6c1832380954ac47b323266bbe660a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _signature, method, methods. Outputs/bindings: (none).
Calls/effect boundaries: _signature, methods.setdefault, methods.setdefault(method.name, []).append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:60`; AST `72538918b3ed415588dd06a22475f85bb5bb75469adf0951bb5d6bcafca3da89`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _signature, method, methods. Outputs/bindings: (none).
Calls/effect boundaries: _signature, methods.setdefault, methods.setdefault(method.name, []).append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:60`; AST `556d8ebc7cd05e2e42439e7a5a17dac6e1edeadf9d9ea56e119a2679bdd00d51`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: method, methods. Outputs/bindings: (none).
Calls/effect boundaries: methods.setdefault.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:60`; AST `e49ac8f72b904e5681a1ed3e781a63d6342ec5d22642e95402117ce01b97f680`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _signature, method. Outputs/bindings: (none).
Calls/effect boundaries: _signature.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[2].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:61`; AST `466b51731c6712f13c368aaa6e3f1f80fb19c3d6cd06b5e3681966633c86a12a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _public, ast, isinstance, n, node. Outputs/bindings: fields, n.
Calls/effect boundaries: _public, ast.unparse, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3].value::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:61`; AST `1dc7e795df73b126ea1d76ec30e95f105972d4a21aecd7e29b2646b72be04bd2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _public, ast, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: _public, ast.unparse, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.elt.values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:61`; AST `1bf44fe8dc2f9828855d65c14376ab3a50d253279a50fc34a81db63214ecf688`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.elt.values[2].body::Call

Source: `infra/agentinfra/roadmap_interfaces.py:62`; AST `271cf047a723782eb2c36d77d36b1226a724474ed79f396857f6d96c5f59e24c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.elt.values[2].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:63`; AST `b190bd15e96dac146d899dde6b0421d03ffd16e633e4f35b1927d0c8f51c4934`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.generators[0].ifs[0].values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:64`; AST `fbdd66b1ae5113b3d8be43e5108dcf14721dacd15e543b117bb2bf340728afc8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.generators[0].ifs[0].values[2]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:64`; AST `778e1406bb2171cf93d41db7ff4be67fa416ae8601d27c1b9ea47f713b6a3196`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _public, n. Outputs/bindings: (none).
Calls/effect boundaries: _public.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[3].value.generators[0].ifs[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:65`; AST `402429232c616669f4786c12ded18ccb9803e0faf1e62c043096bbf8365754ce`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, exports, fields, guards, list, methods, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, exports.setdefault, exports.setdefault(node.name, []).append, list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:65`; AST `1ba5d7ebf164173cfc081c046c9743c8168908641e380d3f0ba91724f1dd8194`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, exports, fields, guards, list, methods, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse, exports.setdefault, exports.setdefault(node.name, []).append, list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:65`; AST `e891a9343424ea56d4fcfea5d1492b2952f4e128d2a11b602af22ef3ea387d90`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exports, node. Outputs/bindings: (none).
Calls/effect boundaries: exports.setdefault.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[1]::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:65`; AST `7d8073c899e8f0fe21816cafbd43e8e860efc34e63ef816a472456160d1e84f3`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[1].elt::Call

Source: `infra/agentinfra/roadmap_interfaces.py:65`; AST `2b61e5decfd609e82d91ed65f92b014a281c19986d2bb625356b5e6a69a6ec6e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[1].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[2]::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:66`; AST `6b07d87348084f4936859c134f0c4902caff3b6b4b1dd54c5a69542a12114c75`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, n, node. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[2].elt::Call

Source: `infra/agentinfra/roadmap_interfaces.py:66`; AST `2b61e5decfd609e82d91ed65f92b014a281c19986d2bb625356b5e6a69a6ec6e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[2].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[5]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:67`; AST `575e768b2571fe4a81ae12dfac22a3e34ae9435ba8414308b7368109d4c504a0`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: guards, list. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].body[4].value.args[0].values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:71`; AST `7888743aab152f5b45bfb543b0ef08dabbcccc75d5a6319aede9ea7e796c5f88`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, getattr, isinstance, key, node. Outputs/bindings: key, predicates.
Calls/effect boundaries: ast.dump, getattr, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value::DictComp

Source: `infra/agentinfra/roadmap_interfaces.py:71`; AST `6c9a12820ff78265f6a98d21d61f977e3b7d17b3ae681fd26a2425c38e67b2a7`.

Rust module: `infra::agentinfra::roadmap_interfaces`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: ast, getattr, isinstance, key, node. Outputs/bindings: key.
Calls/effect boundaries: ast.dump, getattr, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:71`; AST `d8c7146144659d1166744c1c5930066799a68962f99128ae46bdd36953e0bb89`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, getattr, key, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, getattr.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:71`; AST `6bce45aead92c8d19310b47308bcf731fdcd7ecb7f2e735dcb483bfa36d4c36d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, key, node. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:73`; AST `bf9aaf72aec4ab3534982f6ea5553a85891af3b3af107c08f98732d2ae599c2f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, getattr, isinstance, key, node. Outputs/bindings: (none).
Calls/effect boundaries: getattr, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.generators[0].ifs[0].args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:73`; AST `17fe9e744591aa575219365603fc2c4215f0148600b98e1f99af67a934c141bf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, key, node. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[0].value.generators[0].ifs[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1]::For

Source: `infra/agentinfra/roadmap_interfaces.py:74`; AST `b911ad5d09fd44f9f7ba74e837b77847f343eb9d97a5ab40ce6bbb9da8a8161b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, context, field, guards, isinstance, list, n, node, predicates, type, value, visit. Outputs/bindings: context, field, n, value.
Calls/effect boundaries: ast.iter_fields, isinstance, type, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1]; no call, error or mutation may be omitted. Iteration: (field, value) in ast.iter_fields(node)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:74`; AST `09b6e3b003896a4fa601486a87b76cab47e19e25562c99483afd9a0fa4af0043`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.iter_fields.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:75`; AST `745e3fdfc790186d06282280899b45366bc123d33dff3900669bed55d81e06ea`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, guards, node, predicates, type. Outputs/bindings: context.
Calls/effect boundaries: type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[0].value.right.elts[0].values[0].value.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:75`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[0].value.right.elts[0].values[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1]::If

Source: `infra/agentinfra/roadmap_interfaces.py:76`; AST `30906d344e29cfe2fc85b236d1ffff1ed2cf2d480399684fa88e0d9768304b6f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, context, isinstance, list, n, value, visit. Outputs/bindings: n.
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1]; no call, error or mutation may be omitted. Condition: isinstance(value, list)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:76`; AST `f5635b2e334fb6e97f358f32dbb2b0086496303066699278ebd49fcf85562492`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:77`; AST `d10fb552187bb05ea81e2a516407d217965546131b3acd5489c3d9ba17f191dc`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, context, isinstance, n, value, visit. Outputs/bindings: n.
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:77`; AST `21ea6106b1e3387fbc97abcd44a477fe5160325b75c8f881e92a6feef902ce74`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, context, isinstance, n, value, visit. Outputs/bindings: n.
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0].value.args[0]::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:77`; AST `e9e8c536967282e5c846db6aa0adc5d0a1ad2b8996b5bd3a26692a5d3a897d8a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, value. Outputs/bindings: n.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:77`; AST `34a7798f4c7a5faf84da0726c38571f069911ad19299d32af2f628183d309e78`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].body[0].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:78`; AST `12a7fea93717f84bd1f12cae9bbb0a8ed348a73e040b70754bf32b1d7809334f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, context, isinstance, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(value, (ast.stmt, ast.ExceptHandler, ast.match_case))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:78`; AST `9b54c01303f6ad1520e69902090ac94057706b1927bf116600858fec72f21fe4`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:79`; AST `e5dd153fcbf6705d4c2b94ea918ac9b38f7e03e6294d51f830a33c96e0a2bcbc`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::visit::root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:79`; AST `c4bb288dae56a27266afd4aee6ca08137c48a5dc529e4c69f5ef21e2b2c4e72c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].orelse[0].orelse[1].body[1].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::root.body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:81`; AST `a734915400522c293a6f16e9ec4c6deda3c87f419720f95f7476527109902b32`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::root.body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:81`; AST `30bcd87da2ef4baaf519de2933509709a3cef64585b4f81d3a10a419d969f65e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_exports::root.body[13].body[3]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:82`; AST `6996792ae2b0422ddf2868698734b97cdd07dbb805a468f6e2efa5a6499e6d8c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exports. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:85`; AST `b8608df7ff8b7ec2762ead46a413b95de21dc7ac1e7d244251beae0c61969493`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: LAYERS, _exports, ast, bytes, compile, constants, dependencies, dependency, dict, digest, importlib, isinstance, key, layer, len, n, name, names, node, owners, package, path, raw, require, set, sorted, str, target, tree. Outputs/bindings: constants, dependencies, dependency, key, layer, n, name, names, node, owners, package, target, tree.
Calls/effect boundaries: LAYERS.items, _exports, ast.literal_eval, ast.parse, ast.walk, compile, dependencies.add, dependencies.update, digest, importlib.util.resolve_name, isinstance, key.endswith, key.removesuffix, len, name.rpartition, path.removeprefix, path.removeprefix('infra/agentinfra/').removesuffix, path.removeprefix('infra/agentinfra/').removesuffix('.py').replace, require, set, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:86`; AST `e0e840b00b3f4941a44dc15ed9954832ad06721b1a7d860d297c8f3fe8fa1b85`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, path, raw. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:86`; AST `6f0a3e5a676de77d42e7269cacd8fa11956b298997c94949466137505643d348`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, path, raw. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[1]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:87`; AST `23d2ea4f2bc5ed60770104453241b143f69a3f15da74d6cf5bb5b03a97d17068`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile, path, tree. Outputs/bindings: (none).
Calls/effect boundaries: compile.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[1].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:87`; AST `fe971ed311588e5202e40f05a1c97580fbf0b785ec266ceaf56e223ff3e2a5ad`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile, path, tree. Outputs/bindings: (none).
Calls/effect boundaries: compile.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[2]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:88`; AST `1a01ceecb0306bf771e31623bd825ae25f1c9bb67c306bfea449659e3cda9c1d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: key.
Calls/effect boundaries: path.removeprefix, path.removeprefix('infra/agentinfra/').removesuffix, path.removeprefix('infra/agentinfra/').removesuffix('.py').replace.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[2].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:88`; AST `5a51974e4f407e9546df2529b287205773b5d1b10064de54c385af3dd81511cd`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.removeprefix, path.removeprefix('infra/agentinfra/').removesuffix, path.removeprefix('infra/agentinfra/').removesuffix('.py').replace.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:88`; AST `3b5c7f068b3b6eba67af7f67917dc8560cca4f6fd2a2305099f01e05d475f538`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.removeprefix, path.removeprefix('infra/agentinfra/').removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[2].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:88`; AST `dfeee18136b2b3ad97bd5321e3dcd81495b08634165c6e8428a2d4dbc71fe07f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.removeprefix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[3]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:89`; AST `c65d15b979a0a9fee4be5a74e37394bed95e1d2e7e86fb6bc37d37a83b98cfbb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LAYERS, key, layer, names. Outputs/bindings: layer, names, owners.
Calls/effect boundaries: LAYERS.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[3].value::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:89`; AST `96900cc807a19bb897076ce4bca3351fa326ecea82ed1a992826c90b12c43e84`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: LAYERS, key, layer, names. Outputs/bindings: layer, names.
Calls/effect boundaries: LAYERS.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[3].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:89`; AST `7264ffe149453e31f351341625db647e936ac93f69d4e8083b98e9d109b0b86f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LAYERS. Outputs/bindings: (none).
Calls/effect boundaries: LAYERS.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[4]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:90`; AST `f2b3c3aa49bd523a884ab9014ad00e98610ba266646f0f05de3417e255247528`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, owners, path, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[4].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:90`; AST `4f6af90ea66b796d8dd5280910a063b45353913fddc7f5b2906db4b432912b55`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, owners, path, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:90`; AST `facc6ff0abf5cb9b406ba28eb527853a6394dc62a5c79f04f348fc9e4ea80dce`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, owners. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[5]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:91`; AST `0f62493caabad435ce080b80c417a4c00b4f16a42132fe9463719ce735afa8e3`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key. Outputs/bindings: name.
Calls/effect boundaries: key.removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[5].value.orelse.right::Call

Source: `infra/agentinfra/roadmap_interfaces.py:91`; AST `2ada937ecd52cd0186f8b69a6269154d7e28b91cc0779477aae619ff0a7611f6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key. Outputs/bindings: (none).
Calls/effect boundaries: key.removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.orelse.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[6]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:92`; AST `f3b2bb1d2cefd5d6c624ffc9d2bbc9eb04e97544bc97f37bb189c6a0eb53480c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, name. Outputs/bindings: package.
Calls/effect boundaries: key.endswith, name.rpartition.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[6].value.test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:92`; AST `fce5cf8f88335c2f3a9551cd1cb1205d055f2311bd2194805b062acc8b1a8a97`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key. Outputs/bindings: (none).
Calls/effect boundaries: key.endswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[6].value.orelse.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:92`; AST `a1bbc766d672e89e92f18f4fccc0320bb9846a9c61eef32b69f50a72393d0ba1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.rpartition.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.orelse.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[7]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:93`; AST `73e68a4ab479f38d4762ef4dd53fb9f107b9b9c264270aa4c050098692b6b864`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: dependencies.
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[7].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:93`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8]::For

Source: `infra/agentinfra/roadmap_interfaces.py:94`; AST `76044061519d7378096591daf19288b932d292b573d29c768e48c47e3dd41f0e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, dependencies, dependency, importlib, isinstance, n, node, package, tree. Outputs/bindings: dependency, n, node.
Calls/effect boundaries: ast.walk, dependencies.add, dependencies.update, importlib.util.resolve_name, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[14].body[8]; no call, error or mutation may be omitted. Iteration: node in ast.walk(tree)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:94`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:95`; AST `7978192c4a2ae162b70f49d140d7d4c99cb4f23127674eddb24853009c91f233`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, dependencies, dependency, importlib, isinstance, n, node, package. Outputs/bindings: dependency, n.
Calls/effect boundaries: dependencies.add, dependencies.update, importlib.util.resolve_name, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[14].body[8].body[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.ImportFrom)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:95`; AST `590fb849ed19f160c1e37ff1ac642a8b6c15e24fbebaf71c0325db10ff5a8938`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:96`; AST `305021f8a02dbc9eaa90d3be24ef46410eed852b6ca82aa91bf3eadae710739e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: importlib, node, package. Outputs/bindings: dependency.
Calls/effect boundaries: importlib.util.resolve_name.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].body[0].value.body::Call

Source: `infra/agentinfra/roadmap_interfaces.py:96`; AST `72a9ac48ac44c0ba1bba516670d1a54d3b6e1dff90c41bdbde679f500cf4ecb8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: importlib, node, package. Outputs/bindings: (none).
Calls/effect boundaries: importlib.util.resolve_name.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].body[1]::If

Source: `infra/agentinfra/roadmap_interfaces.py:97`; AST `cb2a54c1166a75b5f7862b84fd12951c4cd5db388485c958b502f8936363a7b8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dependencies, dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[14].body[8].body[0].body[1]; no call, error or mutation may be omitted. Condition: dependency
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:98`; AST `1a348a6753ffc4ff6a3b1831eb80cd60db14f1d28b19b327b695515adec0cfcc`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:98`; AST `cc617346ce7e4620e79d798fe760a8b02deece3009c51554389d58026dc64c28`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:99`; AST `df8d60cb4b7444f4d7061d029cf64e182142fafa4b9fee7003b9a98b3819d6b8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, dependencies, isinstance, n, node. Outputs/bindings: n.
Calls/effect boundaries: dependencies.update, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[14].body[8].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.Import)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:99`; AST `bcf2d7bd24edff449cb512da4d3682a98eaf6a2051e4413b6cca0fa8da802d2a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:100`; AST `1b749bf86734e26ffbf67974cf1fc128e32111f88b90306294c637496f5e0347`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, n, node. Outputs/bindings: n.
Calls/effect boundaries: dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:100`; AST `049ac5fccba474433fca35713c462578e7ad1915a54b00a831ff235023da5600`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, n, node. Outputs/bindings: n.
Calls/effect boundaries: dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[8].body[0].orelse[0].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_interfaces.py:100`; AST `77245073f3af1bed31a2183e53a745f0c7632803a0ce65fe88c36c598a1ef6cd`.

Rust module: `infra::agentinfra::roadmap_interfaces`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: n, node. Outputs/bindings: n.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[14].body[8].body[0].orelse[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[9]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:101`; AST `3607400688594a5c6d6a1b11910e2e4ab0385653d42c51345f92ed5d495ef07e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: constants.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10]::For

Source: `infra/agentinfra/roadmap_interfaces.py:102`; AST `3110fdb69b0f91dd0c9ab72ef26cc819398841743925af62eb88411feca0f112`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, constants, isinstance, node, target, tree. Outputs/bindings: node, target.
Calls/effect boundaries: ast.literal_eval, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[14].body[10]; no call, error or mutation may be omitted. Iteration: node in tree.body
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:103`; AST `5cf116401c4717bb92bd56788eae39516f66f5d1964a4ce7e30ff1c654e84b66`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, constants, isinstance, node, target. Outputs/bindings: target.
Calls/effect boundaries: ast.literal_eval, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[14].body[10].body[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.Assign)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:103`; AST `40b4c50f6f9af47ab769457c0a20540babf1d580aa27604a83f6a606d10df146`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0].body[0]::For

Source: `infra/agentinfra/roadmap_interfaces.py:104`; AST `984427944281c9301db465b37a5eecefce70b41d06a77a1347a8aaa1214b11a2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, constants, isinstance, node, target. Outputs/bindings: target.
Calls/effect boundaries: ast.literal_eval, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[14].body[10].body[0].body[0]; no call, error or mutation may be omitted. Iteration: target in node.targets
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:105`; AST `5ce3958bfa401f2613b586f69f7156f16f6adc4a8b4491267b3bd9bc66468a08`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, constants, isinstance, node, target. Outputs/bindings: (none).
Calls/effect boundaries: ast.literal_eval, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[14].body[10].body[0].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(target, ast.Name) and target.id in {'INTERFACE_VERSION', '__version__'}
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0].body[0].body[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:105`; AST `bb49be11d75c8fcd42a45358a442a6076ab30a780e349c5febbf0eeae72dff7c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, target. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[0].body[0].body[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0].body[0].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:106`; AST `a261994125f41520b53590c1660c2f985156359ed46589d2db2ecac631207787`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, constants, node, target. Outputs/bindings: (none).
Calls/effect boundaries: ast.literal_eval.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[10].body[0].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:106`; AST `576a537dd9b91565b3d1f344357069543ef306dbb4518d3013803905e1eb26fb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.literal_eval.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[0].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[11]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:107`; AST `55bcd6d9708dc7cef38833e260c9861690a17b49b96a0e70d3bf0b7fc4e60083`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _exports, constants, dependencies, digest, name, owners, path, raw, sorted, tree. Outputs/bindings: (none).
Calls/effect boundaries: _exports, digest, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[14].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[11].value.values[3]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:107`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[11].value.values[4]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:108`; AST `de9450f7ecc63e128a339905361055304d93bcd7d296673070afc21c7705212d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _exports, tree. Outputs/bindings: (none).
Calls/effect boundaries: _exports.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_module::root.body[14].body[11].value.values[5]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:108`; AST `d445abe7b1aa9419fb5b51023a2fee45121d26e73f616829c0bf22d6dc6de0d5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:111`; AST `b366c8ae61ca6f953e7da5d92b00b41c4fc151e2993fd696d15c5d5b849c0a77`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: KEYWORDS, _schema_vocabulary, child, collection, dict, isinstance, key, require, schema, set. Outputs/bindings: child, collection, key.
Calls/effect boundaries: _schema_vocabulary, isinstance, require, schema.get, schema.get(collection, {}).values, set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:112`; AST `e42486b0fafdabe6328fdb727a430dcacfcc70de87196b73e63a78f43ff804d6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: KEYWORDS, dict, isinstance, require, schema, set. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require, set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:112`; AST `ac9abc5a018fd6d973c0129d418ff80f3907f24fab29ad436d61b96f0a02d5b1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: KEYWORDS, dict, isinstance, require, schema, set. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require, set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:112`; AST `04e64341579f7fca914b718d486fcf5fc891c39bd528362ab24831c79013f26f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, schema. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[0].value.args[0].values[1].operand.left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:112`; AST `2d5d33452a2343dcf62f2dcf8a264edd4845200678e47e005aa0c13516fa9b65`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0].values[1].operand.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[1]::For

Source: `infra/agentinfra/roadmap_interfaces.py:113`; AST `dbd839d17a38d36563f38a723cc944550ca929e5a25969a755aacc40492727ff`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _schema_vocabulary, child, collection, schema. Outputs/bindings: child, collection.
Calls/effect boundaries: _schema_vocabulary, schema.get, schema.get(collection, {}).values.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[15].body[1]; no call, error or mutation may be omitted. Iteration: collection in ('$defs', 'properties')
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[1].body[0]::For

Source: `infra/agentinfra/roadmap_interfaces.py:114`; AST `1fb1548d13d46cfc442c0f67854f56e3b78770d8df223cbaedfd7349e54fa707`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _schema_vocabulary, child, collection, schema. Outputs/bindings: child.
Calls/effect boundaries: _schema_vocabulary, schema.get, schema.get(collection, {}).values.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted. Iteration: child in schema.get(collection, {}).values()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[1].body[0].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:114`; AST `d008cfd416a18c20b3f2d1126a65db7d896033b6e048b8e4db8675e3b2299a90`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: collection, schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get, schema.get(collection, {}).values.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[1].body[0].iter.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:114`; AST `080041b77429829ac1960ecc8c9c142ee50317d70d49684c36e4931d7d181d10`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: collection, schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].iter.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:115`; AST `06438fcf8418c6bb6d3a1fdff2b7983ec6da2b0321525a04774eea917223fe77`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _schema_vocabulary, child. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:115`; AST `1ab2bb01a15ef5bf09aa7ea25078ed220420ff43dfeb9b38997830bf8960dcdb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _schema_vocabulary, child. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[2]::For

Source: `infra/agentinfra/roadmap_interfaces.py:116`; AST `a2cb6214e2c83dc9d480a2f15f039f56c1d8157d5205f41b036025a0698dc2f5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _schema_vocabulary, dict, isinstance, key, schema. Outputs/bindings: key.
Calls/effect boundaries: _schema_vocabulary, isinstance, schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[15].body[2]; no call, error or mutation may be omitted. Iteration: key in ('items', 'additionalProperties')
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:117`; AST `536af9b71f15a24c27b2a846a1b3bc43967c7d8e463d2e76bd24f419cef810b9`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _schema_vocabulary, dict, isinstance, key, schema. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary, isinstance, schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[15].body[2].body[0]; no call, error or mutation may be omitted. Condition: isinstance(schema.get(key), dict)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[2].body[0].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:117`; AST `fcf95e287b8869ffa67bf8d9eba3da65b05d61245ea849c72d19b6d5a0e32db1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, key, schema. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[2].body[0].test.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:117`; AST `235f0e91bb89109d8a2e4ddf29972c13fe5faebb7f615f43e0d3fa071a0e04eb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:118`; AST `91a1cd1fceea9c427c70f5c245f54b7018fa8530e769fc6b67321493e78ce9a4`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _schema_vocabulary, key, schema. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:118`; AST `a315ca875220255170ffc47ade075d76176894bcd5f0863120c2e52b17aece59`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _schema_vocabulary, key, schema. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[3]::For

Source: `infra/agentinfra/roadmap_interfaces.py:119`; AST `3887c8939f6b455ed652060da926931be68df6674479184a4ad02ac3cdc91b2d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _schema_vocabulary, child, schema. Outputs/bindings: child.
Calls/effect boundaries: _schema_vocabulary, schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[15].body[3]; no call, error or mutation may be omitted. Iteration: child in schema.get('anyOf', [])
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[3].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:119`; AST `0c53fe32329002cbef654dba6465d81f5ca3183a1123df7fec9b68641fbfb4db`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schema. Outputs/bindings: (none).
Calls/effect boundaries: schema.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:120`; AST `06438fcf8418c6bb6d3a1fdff2b7983ec6da2b0321525a04774eea917223fe77`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _schema_vocabulary, child. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_schema_vocabulary::root.body[15].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:120`; AST `1ab2bb01a15ef5bf09aa7ea25078ed220420ff43dfeb9b38997830bf8960dcdb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _schema_vocabulary, child. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:123`; AST `5c9e2676807217146cd90675091db3aadbf19765b1b0c5370ee2e8b6566f2293`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: INTERFACE_VERSION, Path, _module, _schema_vocabulary, bool, confined_path, definition, dict, digest, file_binding, int, m, module, modules, name, next, package, path, paths, read_json, require, result, root, schema_binding, schemas, sorted, sys, type, version. Outputs/bindings: definition, m, module, modules, name, package, path, paths, result, root, schema_binding, schemas, version.
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, Path, Path(sys.executable).read_bytes, _module, _schema_vocabulary, bool, confined_path, confined_path(root, path, must_exist=True).read_bytes, definition.get, definition.get('properties', {}).get, definition.get('properties', {}).get('schema', {}).get, digest, file_binding, next, package['declared_versions'].get, path.relative_to, path.relative_to(root).as_posix, read_json, require, root.resolve, schemas['$defs'].items, sorted, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:124`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:124`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[1]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:125`; AST `45fa8dcac8108c95c183f84736db4e14e5e739c8e0ec8304f73f942bd26e367e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, sorted. Outputs/bindings: paths.
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[1].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:125`; AST `ccc646b28a5c429ba81fb873cb9e6e09d32526c6b6ec9a3213fb328df566dc0b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:125`; AST `05e15ad63f351f2f75ccb5aac8df168637a8bf4a858d76d3dd89234a598221bf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/agentinfra').rglob.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[2]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:126`; AST `a978ec6c7196401b2a5cba0baac816d7a60db0a8be238f9669fccf0adb52b791`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, paths, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[2].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:126`; AST `7ebbe98034d36058216e01bec81d12cf958a75f3524369ebb2660256b22f737c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, paths, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:126`; AST `28c20a38faccf6f5e045e227bb6b6ca5fa9a19b283260ef7f5fb45752b7cabc5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, paths. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `a78433db9cf32d9746b16e0d76a4aa157ea3f8a58d6b346c28472b356529313e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _module, confined_path, path, paths, root. Outputs/bindings: modules, path.
Calls/effect boundaries: _module, confined_path, confined_path(root, path, must_exist=True).read_bytes, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3].value::ListComp

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `cee3e88120569c1854e05d0cb19d402b0bdcc9ce7a7e80e1ba6bf9facd67e2b6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _module, confined_path, path, paths, root. Outputs/bindings: path.
Calls/effect boundaries: _module, confined_path, confined_path(root, path, must_exist=True).read_bytes, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ListComp evaluation at root.body[16].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3].value.elt::Call

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `849d75e68b1299c80f7ed2da772dc3df4a2c361012e196a2512d1452ea925e47`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _module, confined_path, path, root. Outputs/bindings: (none).
Calls/effect boundaries: _module, confined_path, confined_path(root, path, must_exist=True).read_bytes, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3].value.elt.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `611316fc9c413c06d1c67518dafd3666c7787482d809a1ffdf9cf82d39e96a1c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, path, must_exist=True).read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.elt.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3].value.elt.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `1a2653ec25accb9a278bb87e89cd9252557b2d9244710b81ebb7d848b1237b3e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.elt.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3].value.elt.args[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[3].value.elt.args[1].func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:127`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value.elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[4]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:128`; AST `61013331c5f033a5317fb211961594f938efec4e9edd8f08a23d451c00642735`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: m, modules, next. Outputs/bindings: m, package.
Calls/effect boundaries: next.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[4].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:128`; AST `4df7fb9218da7f85b44da36e84ba7f9010e13bda9fdd1f92b699bc09c1c5a9a0`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m, modules, next. Outputs/bindings: m.
Calls/effect boundaries: next.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[4].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_interfaces.py:128`; AST `b521a82515c96f00cdbb6962da959922f3a90efc42958a0c01c850c403382f9f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: m, modules. Outputs/bindings: m.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[16].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[5]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:129`; AST `9ada8c2f677da2023e707f69b74f57c8bbf7b1657fc0e38b674d42365bd3852a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: INTERFACE_VERSION, int, package, require, type. Outputs/bindings: (none).
Calls/effect boundaries: package['declared_versions'].get, require, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[5].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:129`; AST `dea2994187f1572fb18edfbdffec22f23a86856ed0e69b82d86eb92a658eb4d2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: INTERFACE_VERSION, int, package, require, type. Outputs/bindings: (none).
Calls/effect boundaries: package['declared_versions'].get, require, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[5].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:129`; AST `b80dedeb0b6b40a0d93793cfc96d4ccb3ff5d0ffe498f51a8ba5a01ab8fb5cc0`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: package, type. Outputs/bindings: (none).
Calls/effect boundaries: package['declared_versions'].get, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[5].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:129`; AST `32e1731a177a5a59654bba05ccd48625389832f142658bbcb948396b1409506a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: package. Outputs/bindings: (none).
Calls/effect boundaries: package['declared_versions'].get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[6]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:132`; AST `ef7b26411f6c571444bd02abc75e4e96b976d834c6d8a76558d030da07f5a4bf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, root. Outputs/bindings: schema_binding.
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[6].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:132`; AST `6f441cc9003145b64752138a0d50c0ea344604a9a0def47e1b6c7c3e3868867f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[7]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:133`; AST `d6465099cc576dac85b719d3ce35820be321a1bcc685887a2cfa879cbd4bd0ec`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: schemas.
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[7].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:133`; AST `6f2c55d17b7369e826d8713c0fc8e4bbc3af424cc3167b3e99b60e706f713cd5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[8]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:134`; AST `684f0ab2af278bc068368de9598b7c38e3ff3eb94e77adb09cf529ef29a07827`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _schema_vocabulary, schemas. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[8].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:134`; AST `11f4ed57b6cb6f16d3f29830cb36ec074fd372e6bb85e3f14cc9f63fe4795873`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _schema_vocabulary, schemas. Outputs/bindings: (none).
Calls/effect boundaries: _schema_vocabulary.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9]::For

Source: `infra/agentinfra/roadmap_interfaces.py:135`; AST `0251d1903199bde952d96b67f59f54571e86fdacdbe567ffb38a0c461838b147`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: definition, int, name, require, schemas, type, version. Outputs/bindings: definition, name, version.
Calls/effect boundaries: definition.get, definition.get('properties', {}).get, definition.get('properties', {}).get('schema', {}).get, require, schemas['$defs'].items, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[16].body[9]; no call, error or mutation may be omitted. Iteration: (name, definition) in schemas['$defs'].items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:135`; AST `c4c7c0f052dda5984391c6f318217e37e3770405f7f6b3907cbb27a974c680fe`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: schemas. Outputs/bindings: (none).
Calls/effect boundaries: schemas['$defs'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:136`; AST `61beda9ebc40bef1913cf09a22462859e8cc1dc1b2a5cbd7792a25acf3e9a403`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: definition. Outputs/bindings: version.
Calls/effect boundaries: definition.get, definition.get('properties', {}).get, definition.get('properties', {}).get('schema', {}).get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:136`; AST `b43459baff1d783243c68645c10b588b2ba01cb04e0e2afa3871170219655272`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: definition. Outputs/bindings: (none).
Calls/effect boundaries: definition.get, definition.get('properties', {}).get, definition.get('properties', {}).get('schema', {}).get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:136`; AST `66622330d2e6fe1e55d702eaf16c68d155d18338c09f43cf06848bb8b54ba0d6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: definition. Outputs/bindings: (none).
Calls/effect boundaries: definition.get, definition.get('properties', {}).get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[0].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:136`; AST `cb5036afa8337faac3960c8e674c2255a2fb5f94ab4955a69f8952214ba39318`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: definition. Outputs/bindings: (none).
Calls/effect boundaries: definition.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[1]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:137`; AST `75f97b0a91e6f08b8a0114896e4c4e36c0086249a6de07042178ba50fe8b39eb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, name, require, type, version. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:137`; AST `fe00c96324ccd233b899181076afd879f8a382f4afc91590e225c612ea4600f2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, name, require, type, version. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[9].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:137`; AST `2fd59e97a000d6cc2dc799ab534b5dc009f3203b64d9ddfb5419e4cd01179ffe`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, version. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[10]::For

Source: `infra/agentinfra/roadmap_interfaces.py:139`; AST `a182b7a1bd032579c62218c08ad94e5e0deb2893e54bcbedf4a5304ac433123b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: file_binding, module, modules, require, root. Outputs/bindings: module.
Calls/effect boundaries: file_binding, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[16].body[10]; no call, error or mutation may be omitted. Iteration: module in modules
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:140`; AST `36c021fff321db2148c9e92aef933dbf9915687b59f03ab2338562630301e89d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, module, require, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:140`; AST `f47aeb4efd5d8b30c5d2d5c63b32e56631548e97ce00f6e47081422f1a54b8ad`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, module, require, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[10].body[0].value.args[0].left.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:140`; AST `5b69a3c9e9ca4b73a503223ba06d4bb002166d4da8dd94601eebc52dc44e8312`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, module, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[0].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[11]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:142`; AST `84432c2d8f83ed52f2db4ef7f7b8df123711430f7ae2422ca4ec710760737057`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: paths, require, root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, require, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[11].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:142`; AST `9f986141f733f3cb0a3c238a5f45481d6e732167764e9dd9a964b2ecb6065587`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: paths, require, root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, require, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[11].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:142`; AST `ccc646b28a5c429ba81fb873cb9e6e09d32526c6b6ec9a3213fb328df566dc0b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/agentinfra').rglob, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[11].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:142`; AST `05e15ad63f351f2f75ccb5aac8df168637a8bf4a858d76d3dd89234a598221bf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/agentinfra').rglob.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[12]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:143`; AST `c47257af4c6f9009e88345e18e2c5dc91af97fb7c1a9329460c9e897aca91ce7`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, require, root, schema_binding. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[12].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:143`; AST `05efa6b19b37e5e6c15664d2236623741ce0645bb5801f7766bfc00c5a131953`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, require, root, schema_binding. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[12].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:143`; AST `6f441cc9003145b64752138a0d50c0ea344604a9a0def47e1b6c7c3e3868867f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[13]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:145`; AST `390c6a5e3315e7379fa8f2562a3011917d63fab4dff52b01f9cd6cf2f23da32e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: INTERFACE_VERSION, Path, digest, modules, schema_binding, schemas, sys. Outputs/bindings: result.
Calls/effect boundaries: Path, Path(sys.executable).read_bytes, digest.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[13].value.values[3].values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:146`; AST `528ea3efa8d833443ff176961af24a64957faeab5035acec50efb249cc33cc26`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, digest, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).read_bytes, digest.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].value.values[3].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[13].value.values[3].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:146`; AST `6ba59d0cde0384f15a99107ebe91ed97a2207941295cc5fe8bd44d690ab106cf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].value.values[3].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[13].value.values[3].values[1].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:146`; AST `0dfff54cbeeb64407db17d4e6b154f3aff810a988368a772f2aaa5d71265f9f3`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].value.values[3].values[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[14]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:152`; AST `ea550629d25e1f9e71896bf31374af5bfddb3e00134f1ff852e05146c14aecd2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[14].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:152`; AST `9ddec37ebb871d950d3273f3c19aaf26231ea1c560172aa64604b6f8dc8f2faf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::observe_interfaces::root.body[16].body[15]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:153`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[16].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:156`; AST `1465e2ab304a7236199e4dba997f0086fdd8ab5f42ee287a2e034daced2d9895`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: after, any, before, bool, current, dict, k, len, list, methods, name, previous, v, zip. Outputs/bindings: after, before, k, methods, name, v.
Calls/effect boundaries: after.get, after.get('methods', {}).get, after.items, any, before.get, before.items, before['methods'].items, len, zip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:157`; AST `501ddb42a1c4d2320b73db3e55af3c729c4ce62948e6694df88cada2bf993bc2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, len, previous. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[17].body[0]; no call, error or mutation may be omitted. Condition: len(previous) != len(current)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[0].test.left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:157`; AST `deab7c15b2307413a6b501148b1134b68fbf5f9aeffce480444ff277ecf5a92e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, previous. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[0].test.comparators[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:157`; AST `19be6a122c41a8259f17edddc4d1e66432f7782d6fe745b671c80f66dc997058`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:158`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[17].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1]::For

Source: `infra/agentinfra/roadmap_interfaces.py:159`; AST `ae10ba0e69510772336c53116cbf76ac6886ff6f223f57dcc964bfaa4dc92547`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: after, any, before, current, k, methods, name, previous, v, zip. Outputs/bindings: after, before, k, methods, name, v.
Calls/effect boundaries: after.get, after.get('methods', {}).get, after.items, any, before.get, before.items, before['methods'].items, zip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[17].body[1]; no call, error or mutation may be omitted. Iteration: (before, after) in zip(previous, current)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:159`; AST `f0564f04aa065beff87322f89ecd9319fb07bb6472b440e4bc9f27cc0863e754`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, previous, zip. Outputs/bindings: (none).
Calls/effect boundaries: zip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:160`; AST `a7cf787888e58742d6c599acd7ec519ec98462381b3d2aa6dafdfef877748f8e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, any, before, k, methods, name, v. Outputs/bindings: k, methods, name, v.
Calls/effect boundaries: after.get, after.get('methods', {}).get, after.items, any, before.get, before.items, before['methods'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[17].body[1].body[0]; no call, error or mutation may be omitted. Condition: before.get('kind') != 'ClassDef'
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].test.left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:160`; AST `40c16b2ca9a5ee22e0dce1b3d0de97b80528d69ffcb237af8280447a61e17875`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:161`; AST `36b6dddf92e8b4e76eb57e32ce7951f39739c1c321ee5ac6bbf5fe5ebc14e135`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, before. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[17].body[1].body[0].body[0]; no call, error or mutation may be omitted. Condition: before != after
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:162`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:164`; AST `2da14f1af73243e7f797d8bb78a1224122d5c0669b8fa72928fba6e484facaaa`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, before, k, v. Outputs/bindings: k, v.
Calls/effect boundaries: after.items, before.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[17].body[1].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: {k: v for k, v in before.items() if k != 'methods'} != {k: v for k, v in after.items() if k != 'methods'}
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[0].test.left::DictComp

Source: `infra/agentinfra/roadmap_interfaces.py:164`; AST `cc03301751ecabbc7c33c2219d01cd13919b9839109592773055b4301e7a7093`.

Rust module: `infra::agentinfra::roadmap_interfaces`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: before, k, v. Outputs/bindings: k, v.
Calls/effect boundaries: before.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered DictComp evaluation at root.body[17].body[1].body[0].orelse[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[0].test.left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:164`; AST `31c1cc9834ed51185d8d6607a332e507345848db7d6ab894058368465ee6f677`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].orelse[0].test.left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[0].test.comparators[0]::DictComp

Source: `infra/agentinfra/roadmap_interfaces.py:164`; AST `b3b513e17d313612c761347be134082eaf2a3bca9251fc8cf68056573cf73bb1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: after, k, v. Outputs/bindings: k, v.
Calls/effect boundaries: after.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered DictComp evaluation at root.body[17].body[1].body[0].orelse[0].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[0].test.comparators[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:164`; AST `12fa4c8028fca3bd7c7afd0406c83459c208642d4457fe041d590c4231ee2b5f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after. Outputs/bindings: (none).
Calls/effect boundaries: after.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].orelse[0].test.comparators[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[0].body[0]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:165`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1]::If

Source: `infra/agentinfra/roadmap_interfaces.py:166`; AST `e2b7c8f57adf9171b7f331805dcf1a82f1cead5d9ed80c0440dad009db84b512`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, any, before, methods, name. Outputs/bindings: methods, name.
Calls/effect boundaries: after.get, after.get('methods', {}).get, any, before['methods'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[17].body[1].body[0].orelse[1]; no call, error or mutation may be omitted. Condition: any((after.get('methods', {}).get(name) != methods for name, methods in before['methods'].items()))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1].test::Call

Source: `infra/agentinfra/roadmap_interfaces.py:166`; AST `82bb893c75a0172ab25a50c1e8f4661f0bdcff1e96154ef97eea4f4bcc35d206`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, any, before, methods, name. Outputs/bindings: methods, name.
Calls/effect boundaries: after.get, after.get('methods', {}).get, any, before['methods'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].orelse[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1].test.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_interfaces.py:166`; AST `00f5c9ebacae268f7de84a9a82547c73a451f7bdcb45ee8cba41fbe4d40fafca`.

Rust module: `infra::agentinfra::roadmap_interfaces`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: after, before, methods, name. Outputs/bindings: methods, name.
Calls/effect boundaries: after.get, after.get('methods', {}).get, before['methods'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[1].body[0].orelse[1].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1].test.args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:166`; AST `205afb4b66f6bb78e19847d206c6311c867bf339588c7b942d46ad91a421517e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, name. Outputs/bindings: (none).
Calls/effect boundaries: after.get, after.get('methods', {}).get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].orelse[1].test.args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1].test.args[0].elt.left.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:166`; AST `dc1d875870667036cd7d24149a5c1bb2ace9e6c3fac8cc3d6a8f14c74a075759`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after. Outputs/bindings: (none).
Calls/effect boundaries: after.get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].orelse[1].test.args[0].elt.left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1].test.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:166`; AST `57859bc53129cbe2e1842e4a2747db677f492f58f6d12a2a942b2d2b49a6c07a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before['methods'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].orelse[1].test.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[1].body[0].orelse[1].body[0]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:167`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1].body[0].orelse[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::_compatible::root.body[17].body[2]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:168`; AST `4a8ef490a01d3017cb999fbea58c2adfb60a40ad736e0d23eceb176a236b14c3`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_interfaces.py:171`; AST `dd0b0e8b79793458a5c4bfd2d9c33a4b1690801ec27067b2a40620a113ba017c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GitInventory, INTERFACE_VERSION, Path, _compatible, _module, baseline, baseline_ref, bool, candidate, changes, current, dict, entry, exported, git, len, loads, m, module, name, now, observe_interfaces, old, old_schemas, previous_protocols, require, root, schema, set, signature, sorted, str, value. Outputs/bindings: baseline, candidate, changes, current, entry, exported, git, m, module, name, now, old, old_schemas, previous_protocols, schema, signature, value.
Calls/effect boundaries: GitInventory, _compatible, _module, bool, changes.append, current['record_protocols'].get, entry['path'].endswith, entry['path'].startswith, git.blob, git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline_ref + '^{commit}').strip, git.read('rev-parse', baseline + ':Roadmaps/Shared/records.schema.json').strip, git.tree, len, loads, module['exports'].items, now[name]['exports'].get, observe_interfaces, old.items, old_schemas.decode, previous_protocols.items, require, set, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:172`; AST `b5ffa0be1c1416af065b0e26c0e1735bb472b8f9f993633bef0c81beecad908a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_interfaces, root. Outputs/bindings: current.
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:172`; AST `e3b835733344cc4702b993e1dfafa68c05951883e31c5b65824bdf1022d38cb1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[1]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:173`; AST `6be60ecbd9492af5c5dd6b3f753a825879749c93ccb83967aa9f6d22383d5117`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GitInventory, root. Outputs/bindings: git.
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[1].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:173`; AST `c4f3e6818765e5df9cc7a91d7bfc9093ba441ac55f12b5153bb08ff3dd3b1703`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GitInventory, root. Outputs/bindings: (none).
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[2]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:174`; AST `55c4af011e350b6f34da4790a85d5acae4702aab90a2fecd6e9592a1d235f1b8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: baseline_ref, git. Outputs/bindings: baseline.
Calls/effect boundaries: git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline_ref + '^{commit}').strip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[2].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:174`; AST `1b9f79e073fd163a64101a9ec326a3b319bd8bca76f4c760b3566e1da035794d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline_ref, git. Outputs/bindings: (none).
Calls/effect boundaries: git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline_ref + '^{commit}').strip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:174`; AST `8f481090a4a2f8acdf34c0cd09e657ecfe449fc135a5e9af30d5ed5e32a05902`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline_ref, git. Outputs/bindings: (none).
Calls/effect boundaries: git.read.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[3]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:175`; AST `a3890756b0f8ff83790166443326dd5c1ad1c4538d05ad143eeae0d97ed51a11`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: old.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4]::For

Source: `infra/agentinfra/roadmap_interfaces.py:176`; AST `a2c70fae372a3fc1c8da3b4e6ed9f136423459a3a4e304cb0c991cd7e025f263`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _module, baseline, entry, git, old, require, value. Outputs/bindings: entry, value.
Calls/effect boundaries: _module, entry['path'].endswith, entry['path'].startswith, git.blob, git.tree, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[18].body[4]; no call, error or mutation may be omitted. Iteration: entry in git.tree(baseline)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:176`; AST `fe7b80b9d8e4cba5aa5a7749d783ba4e66e8b012ff3fff87fe6b74af60375c94`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline, git. Outputs/bindings: (none).
Calls/effect boundaries: git.tree.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:177`; AST `c862c85ac3e1f1a3d4eb8935bf604e8a9b48ff9cc696f690a3590509bbc229c6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _module, entry, git, old, require, value. Outputs/bindings: value.
Calls/effect boundaries: _module, entry['path'].endswith, entry['path'].startswith, git.blob, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[18].body[4].body[0]; no call, error or mutation may be omitted. Condition: entry['path'].startswith('infra/agentinfra/') and entry['path'].endswith('.py') and (entry['type'] == 'blob')
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:177`; AST `6fbb232c8c3f2369408b554bf1cdec2036e62f24bc82c55a1907dfd003e15aef`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry['path'].startswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:177`; AST `8abb863a5b1ee69fee160afa4714babc5755aca91161d451a2ad4a895c95a2e5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry['path'].endswith.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:178`; AST `db5943d6918819c4ca0339910ac983c5ecfeac2be26cbe355d4d7b624781dd41`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:178`; AST `989f567886a88d81f4e99f7022320ddcd6b3a60b01868d585dea160ffa18c18d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:179`; AST `729a8bca91d7788dc97e4dcf4b8cd78151a2687c3a19822eacea832c85ec1729`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _module, entry, git. Outputs/bindings: value.
Calls/effect boundaries: _module, git.blob.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:179`; AST `64e4f2416ad6f3b9d56196bdc645f270ed774b643064d5c3fa70150fa268d63a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _module, entry, git. Outputs/bindings: (none).
Calls/effect boundaries: _module, git.blob.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:179`; AST `250dcf5754423bca08c0d557665fe6b4076808045bd1867a32d86332ae2fb305`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, git. Outputs/bindings: (none).
Calls/effect boundaries: git.blob.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[4].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:180`; AST `3e18e1130e75fdd171ed93c3cac97d3e188c276be34c4be7d952de8334233b9d`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[5]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:181`; AST `1644569e49daaedf06815020c6eb31d4036e0a36d4ef599f43a12aa7341015e2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, old, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[5].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:181`; AST `fe504b5df096c148dd4ffb89c7cc0e442ae268a3bcb33ac271d82e8654379b2c`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, old, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:181`; AST `c24394fbd71e6a194e252489ff389c10cc9aa26cedc37c1799d372faab9e1c67`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, old. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[6]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:182`; AST `28ff756d46203f5b726705eb8e2bd4733c8159f01efc16b9b32e14f71763c52a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, m. Outputs/bindings: m, now.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[6].value::DictComp

Source: `infra/agentinfra/roadmap_interfaces.py:182`; AST `8fc1f38190b338bd08ab9be0d7a6ac39f7525413cc257e75e11a953aaf2b8744`.

Rust module: `infra::agentinfra::roadmap_interfaces`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: current, m. Outputs/bindings: m.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[7]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:183`; AST `4b5017bb8cbdeea06785ff34dfa08e442f3328576c0f16148be31c607b435e36`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: changes.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8]::For

Source: `infra/agentinfra/roadmap_interfaces.py:184`; AST `2aa24f87178a451170a9c92c42fc1bb9c074d997df301edcaf35698980dfb88b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _compatible, candidate, changes, exported, module, name, now, old, signature. Outputs/bindings: candidate, exported, module, name, signature.
Calls/effect boundaries: _compatible, changes.append, module['exports'].items, now[name]['exports'].get, old.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[18].body[8]; no call, error or mutation may be omitted. Iteration: (name, module) in old.items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:184`; AST `8fe2c43ce29720275afaa01eb97b597bf51fdebc00206db7fd28385292efa809`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:185`; AST `4594843d371e8164ffc53f42bf56ec09f9537876c46c06259b95a561e8036f7a`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: changes, name, now. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[18].body[8].body[0]; no call, error or mutation may be omitted. Condition: name not in now
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:186`; AST `0c2c3e61717baa63c1e6e69b423f09501e362c7eab2067cc761f748415de0b6e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changes, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:186`; AST `a5a1230f969b5b49407906ce0085c5bbee36b64ea2b5c50607513fd40917e897`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changes, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[0].body[1]::Continue

Source: `infra/agentinfra/roadmap_interfaces.py:187`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Continue evaluation at root.body[18].body[8].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1]::For

Source: `infra/agentinfra/roadmap_interfaces.py:188`; AST `a79499a798b36142ac739d96f1e23f1e02427ba5d26a215c21b15056a6ec5f6b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _compatible, candidate, changes, exported, module, name, now, signature. Outputs/bindings: candidate, exported, signature.
Calls/effect boundaries: _compatible, changes.append, module['exports'].items, now[name]['exports'].get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[18].body[8].body[1]; no call, error or mutation may be omitted. Iteration: (exported, signature) in module['exports'].items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:188`; AST `572aa641e6c105fe6cd2149c0e42e833c9efeb40b781b5632dad2090f43c70a4`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module. Outputs/bindings: (none).
Calls/effect boundaries: module['exports'].items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:189`; AST `4f04366dd39a3e97a7f2091a6acdd72ad53286ccb968eabd883b82f46c83d231`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exported, name, now. Outputs/bindings: candidate.
Calls/effect boundaries: now[name]['exports'].get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:189`; AST `c30b650357f7ec6b2543a3afb304567a7390855a02e9602818e77817fce966d6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exported, name, now. Outputs/bindings: (none).
Calls/effect boundaries: now[name]['exports'].get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_interfaces.py:190`; AST `2892abb59ad4f430dd472c972bf2a8b5078692fe1f9901aa072ca6ad02f8d8f1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _compatible, candidate, changes, exported, name, signature. Outputs/bindings: (none).
Calls/effect boundaries: _compatible, changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[18].body[8].body[1].body[1]; no call, error or mutation may be omitted. Condition: candidate is None
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:191`; AST `f1868a6ceb65919f889d3a5540ad49ff01afab992cc25dacca4c166502b0e0c8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changes, exported, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[8].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:191`; AST `f05501febcff8259409eaff2f050660eb25aab90a40c68957e9a0ae2b2dd961b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changes, exported, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1].orelse[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:192`; AST `265e8c2b08f88d3122efb7d694dd80defc987dc1cb3d23c41c811119756f9667`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _compatible, candidate, changes, exported, name, signature. Outputs/bindings: (none).
Calls/effect boundaries: _compatible, changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[18].body[8].body[1].body[1].orelse[0]; no call, error or mutation may be omitted. Condition: not _compatible(signature, candidate)
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1].orelse[0].test.operand::Call

Source: `infra/agentinfra/roadmap_interfaces.py:192`; AST `11fa0b6bfe7d3c8701505211537da0c9cfbad7ab01604ce757ede474194bfcf3`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _compatible, candidate, signature. Outputs/bindings: (none).
Calls/effect boundaries: _compatible.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[1].body[1].orelse[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:193`; AST `ecea497fe61853f9799511299d8f172d4a3c45a1f28f81246612f8e65fa20eb3`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changes, exported, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[8].body[1].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[8].body[1].body[1].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:193`; AST `dc62751a56db21b5b3f071cb8542f188b094fd20ccbb14e2a0d72ae8911250b5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changes, exported, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[1].body[1].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[9]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:194`; AST `0a5f37e59619b02b1b373b3eedbcc0da108d177b7ddbd572afb8db3ab9f8dbd5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: baseline, git. Outputs/bindings: old_schemas.
Calls/effect boundaries: git.blob, git.read, git.read('rev-parse', baseline + ':Roadmaps/Shared/records.schema.json').strip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[9].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:194`; AST `1c872b75b03a5a73668ea74bd13ceba7ceddd44a5925bf9d5d5422d992d5aac5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline, git. Outputs/bindings: (none).
Calls/effect boundaries: git.blob, git.read, git.read('rev-parse', baseline + ':Roadmaps/Shared/records.schema.json').strip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[9].value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:194`; AST `751ce353296cbcfbfd1d91ae7f289abb2892f0967fb9f98b0bb25fbbd7637963`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline, git. Outputs/bindings: (none).
Calls/effect boundaries: git.read, git.read('rev-parse', baseline + ':Roadmaps/Shared/records.schema.json').strip.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[9].value.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:194`; AST `81fef6d525984f2f6dc3a55619d69c812f59bff489642ce76047bb41257482f5`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline, git. Outputs/bindings: (none).
Calls/effect boundaries: git.read.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_interfaces.py:195`; AST `bf9783545a9d1e15fcbe04d054098fc8c576a703f83cf4f0a7e30dc030edaf47`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[18].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[11]::Assign

Source: `infra/agentinfra/roadmap_interfaces.py:196`; AST `2d6023aa0bf293ccd16a037bcfda741a9339d811a6f6dce13b9db48efe50521b`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, old_schemas. Outputs/bindings: previous_protocols.
Calls/effect boundaries: loads, old_schemas.decode.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[11].value.value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:196`; AST `ebefc99a73e30d8be779479d4933f2b20d7ca45f266d67435bd95835cbae8eb1`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, old_schemas. Outputs/bindings: (none).
Calls/effect boundaries: loads, old_schemas.decode.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[11].value.value.args[0]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:196`; AST `b1383e83b0125a5f04523eb97a471e210593a14193c5380cee34afa443da0de8`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old_schemas. Outputs/bindings: (none).
Calls/effect boundaries: old_schemas.decode.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[12]::For

Source: `infra/agentinfra/roadmap_interfaces.py:197`; AST `9d075ad98c766c8e89f9de13a9a06e7b41ae98f339d86cc7150be872ad6857cb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: changes, current, name, previous_protocols, schema. Outputs/bindings: name, schema.
Calls/effect boundaries: changes.append, current['record_protocols'].get, previous_protocols.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered For evaluation at root.body[18].body[12]; no call, error or mutation may be omitted. Iteration: (name, schema) in previous_protocols.items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[12].iter::Call

Source: `infra/agentinfra/roadmap_interfaces.py:197`; AST `1906af2881086584766ec21faf4151dc7a94b7b72d59c80eb984f3d0f2d7078e`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous_protocols. Outputs/bindings: (none).
Calls/effect boundaries: previous_protocols.items.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[12].body[0]::If

Source: `infra/agentinfra/roadmap_interfaces.py:198`; AST `d1b83ed2bbde2b1f2cdb0593ee9fc354b91785baec10b63b08b1d40e151a54da`.

Rust module: `infra::agentinfra::roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: changes, current, name, schema. Outputs/bindings: (none).
Calls/effect boundaries: changes.append, current['record_protocols'].get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered If evaluation at root.body[18].body[12].body[0]; no call, error or mutation may be omitted. Condition: current['record_protocols'].get(name) != schema
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[12].body[0].test.left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:198`; AST `14e5f81c30c0121469469868c4bab382e9b10cfbebcab5fe656d0cccebb69ff0`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, name. Outputs/bindings: (none).
Calls/effect boundaries: current['record_protocols'].get.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[12].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_interfaces.py:199`; AST `65411d932067ccfc5e2c2c50379924795d63eac6f4cc5b5ea27552fbf4d04532`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changes, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[12].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_interfaces.py:199`; AST `50a18b1340902ae1faa2291da736fa62aded59eceb5618043fe86f2989025bf2`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changes, name. Outputs/bindings: (none).
Calls/effect boundaries: changes.append.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[13]::Return

Source: `infra/agentinfra/roadmap_interfaces.py:200`; AST `6a47362372d3a92e9bbc99afabfb9d579a5e9fbab195c0b9ce243ecb3a4f8bb6`.

Rust module: `infra::agentinfra::roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: INTERFACE_VERSION, baseline, changes, current, len, now, old, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: len, set, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Return evaluation at root.body[18].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[13].value.values[4]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:201`; AST `b3720b73e42707ad9b300e9ca52f252134a94d0777a96462df2c014e67c318ae`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, old. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[13].value.values[5]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:202`; AST `dcccb2a0f51409382ee29c8a7739dfac2ffe70cd97d9b6553ac03c28dc4f05cb`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, now. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[13].value.values[8]::Call

Source: `infra/agentinfra/roadmap_interfaces.py:203`; AST `10d426f9faf5fee39dd6dba7a39f02f2fb3099f1682a7a7cbef2353d7b7e39bf`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: now, old, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[13].value.values[8].args[0].left::Call

Source: `infra/agentinfra/roadmap_interfaces.py:203`; AST `7554e2d056c7330d49d83219dc4c92835d4104d684c7dab245248107965b529f`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: now, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].value.values[8].args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_interfaces.py::module::compare_interfaces::root.body[18].body[13].value.values[8].args[0].right::Call

Source: `infra/agentinfra/roadmap_interfaces.py:203`; AST `126a9e051bb3ed50fa0970c79f4ee485eee5f457a09cb491ed6ecb5f11dd4b32`.

Rust module: `infra::agentinfra::roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, roadmap_inventory, roadmap_records, security, sys.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].value.values[8].args[0].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
