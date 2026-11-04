# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 411. Inventory digest: `5985aaa4805e653a178ac25b2a7931044bd862f01a041aa9445fcf03d2d23915`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_python.py::module::root::Module

Source: `infra/agentinfra/roadmap_python.py:1`; AST `eee9a33ca665336238d9a9ea979f09eaef47b6f89795e5ac6e243828c3d1e9e6`.

Rust module: `infra::agentinfra::roadmap_python`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: DYNAMIC, EFFECT_MODULES, OSError, Path, RuntimeError, _modules, a, all, any, archive, argv, ast, b, backend, binding, bindings_current, bool, c, calls, candidate, catalog, chapter, chapters, claims, closure, cls, compiled, confined_path, count, declarations, dependencies, dependency, dict, digest, disposition, entry, errors, esbmc_arguments, expected, external, external_rows, file_binding, files, fixture, functions, h, hazards, importlib, include_tests, inventory, isinstance, key, kind, legacy, len, list, locations, maintained_python, module, module_closure, modules, n, name, next, node, obligation, obligation_catalog, observation, observed, original_occurrences, output, package, parent, path, pending, producer_inputs_current, proof, qualification, qualification_reports, r, range, raw, re, read_json, recommendations, record, relative, release, require, research_sources, result, root, row, rows, run, safe, separator, set, sorted, source_closure, source_inventory, str, symbol, target, toolchain, tree, type, visited, zipfile. Outputs/bindings: BACKENDS, DYNAMIC, EFFECT_MODULES, INTERFACE_VERSION, a, archive, argv, b, backend, binding, c, calls, catalog, chapter, chapters, closure, cls, count, declarations, dependencies, dependency, disposition, entry, errors, expected, external, external_rows, files, functions, hazards, key, legacy, locations, module, modules, n, name, node, observed, output, package, parent, path, pending, proof, qualification, r, raw, recommendations, record, relative, release, result, row, rows, safe, separator, source_inventory, symbol, tree, visited.
Calls/effect boundaries: '.'.join, (root / 'infra/tests').glob, Path, _modules, all, any, archive.namelist, archive.read, argv.append, ast.dump, ast.dump(declarations[0], include_attributes=False).encode, ast.dump(node, include_attributes=False).encode, ast.parse, ast.unparse, ast.walk, bindings_current, bool, c.get, confined_path, dependencies.add, dependencies.update, digest, entry.get, errors.append, esbmc_arguments, external.add, external_rows.append, file_binding, files.append, hazards.append, importlib.util.resolve_name, inventory, isinstance, len, maintained_python, module_closure, modules[module].read_bytes, name.removesuffix, name.rpartition, name.split, next, node.name.startswith, obligation.get, obligation_catalog, observation.get, original_occurrences, parent.is_relative_to, path.is_symlink, path.read_bytes, path.readlink, path.readlink().as_posix, path.relative_to, path.relative_to(root).as_posix, path.resolve, path.resolve(strict=True).is_relative_to, pending.append, pending.pop, proof.get, qualification.get, qualification_reports, range, re.search, read_json, read_json(root / 'Roadmaps/Shared/python-backends.json').get, record.pop, record.update, relative.is_absolute, relative.removeprefix, relative.removeprefix('infra/').removesuffix, relative.removeprefix('infra/').removesuffix('.py').replace, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, relative.startswith, require, research_sources, result.get, rows.append, run.get, set, sorted, source_closure, str, target.partition, toolchain.get, type, visited.add, zipfile.ZipFile.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:1`; AST `c15af44d7238bd18cc61df4c83d73e4c3111ee4940ae0bec2f0d34305113be99`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_python.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_python.py:9`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_python.py:10`; AST `866a97c0a29d398dc2bf8a74409548dccd9bb5221f4bf0f58ad1a37ef83e5260`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_python.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_python.py:12`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[6]::Import

Source: `infra/agentinfra/roadmap_python.py:13`; AST `4123c8e546e07497699149dda363dc8539207c3974a8a7d70400f73212c30178`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_python.py:15`; AST `edbc37de842252529389a4446732fc56dad43cd0db247d08c1a9a528f9db72a1`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_python.py:16`; AST `94f2ef7cfe57c7bfab987ff333d99818aa195b2b2e4f09c3d8608a99d87b2cad`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_python.py:17`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[10]::Assign

Source: `infra/agentinfra/roadmap_python.py:20`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[11]::Assign

Source: `infra/agentinfra/roadmap_python.py:21`; AST `bf471ff7b64fb5a76dcbcd24e8cafe1c02441647b738fa2915e9341aa730a195`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: BACKENDS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[12]::Assign

Source: `infra/agentinfra/roadmap_python.py:22`; AST `5f4dd3230a5dba2409be525ac1e40643bfcf5e3f7598856658818591707ca1db`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: DYNAMIC.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::root.body[13]::Assign

Source: `infra/agentinfra/roadmap_python.py:23`; AST `30fa6bb5934f05942732e36e39a9c8a5b4dfa76fad61259d2721bf9fad6c729a`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: EFFECT_MODULES.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:26`; AST `463ac7a213ab069b1729355a28a3a03dada0493add7da3391d7e44c07155908f`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, backend, read_json, require, root, str. Outputs/bindings: backend.
Calls/effect boundaries: read_json, read_json(root / 'Roadmaps/Shared/python-backends.json').get, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:27`; AST `5e6fa0bf28de1c12a4774674de9a7e0af73137f836780faf13eafbf754609d28`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: backend.
Calls/effect boundaries: read_json, read_json(root / 'Roadmaps/Shared/python-backends.json').get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:27`; AST `5c482292b58e67148bdeaf2e4329ecbcc9e0e2fa4587298530e4a4306ca660f7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, read_json(root / 'Roadmaps/Shared/python-backends.json').get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:27`; AST `62f3cd8f69a1722e90a45ae3013dbfbf37c9dfc848e190da9e6b80375ae86ea1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14].body[1]::Expr

Source: `infra/agentinfra/roadmap_python.py:28`; AST `5f90576f68836ed662c7e252b9128f2bf1fa1ef2ab35c8b351f14410a5f98735`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:28`; AST `0923b3625564e86cd0e0b614524c33414375335f6ae11daa54beff90bdd49924`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::qualification_backend::root.body[14].body[2]::Return

Source: `infra/agentinfra/roadmap_python.py:29`; AST `e12bed1e67062320deee4c3a451f0155d06464724607e0568a2d03db989b17b5`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::backend_observation_key::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:32`; AST `e0087d8cfca8ef8564eb0d7c984bba6b1ea5ab96cd51436114fec0104c395e80`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: backend, kind, require, str. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::backend_observation_key::root.body[15].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:33`; AST `3be9980565bee7896d755add1f0604e7fb5df4b3dffb0d7852eee23428161726`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend, kind, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::backend_observation_key::root.body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:33`; AST `80f322ef06c8ac8f861e75e0cf039f76049a1a012916a0ab13cf713cb40d3b1d`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend, kind, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::backend_observation_key::root.body[15].body[1]::Return

Source: `infra/agentinfra/roadmap_python.py:34`; AST `6060117b8d37f8e1a63671b3236172d98d1e5686409959d197760dc77d8f656c`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend, kind. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:37`; AST `f9b8cb8fc3cc26f38b9cf6b37682505f95ef7f26cd272968fea32aaf8d9cdba4`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, argv, bool, claims, dict, fixture, functions, list, require, root, str, toolchain. Outputs/bindings: argv, functions.
Calls/effect boundaries: argv.append, require, str, toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:38`; AST `a5a4d3f9e3b756be74641779cac9c36a73586db58350a45bbf2456c62c7a89f2`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: functions.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[1]::Expr

Source: `infra/agentinfra/roadmap_python.py:40`; AST `bdb479d9257d93e4a5eaa18980082634e68424e6fdb1dbee631f9f08e54437ac`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, functions, require, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: require, toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:40`; AST `4c9876a513d28b4b32be73e3efb654d6244677ac247526ec130da9b61954943f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, functions, require, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: require, toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:40`; AST `a1570292a8fc75ba5ee5d3c375d6190adbc55c1d07ea99d6aa2674ae094cc85b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:41`; AST `53dcb07f33ba5a0912a95bfd76a7a9c61ad9c9ac2ecd4d85788ad2f68c10b725`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, functions, root, str, toolchain. Outputs/bindings: argv.
Calls/effect boundaries: str.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[2].value.elts[1]::Call

Source: `infra/agentinfra/roadmap_python.py:41`; AST `9d55f7e3cf15b3703add749bbcabdeb16f728bd38a95db40e23f2b1e6f4e64df`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[3]::If

Source: `infra/agentinfra/roadmap_python.py:43`; AST `3d0a9a53e46e0471bb0b4f68d4db06265c10cfc0b0bd9a060d09abb43447c5fa`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: argv, claims. Outputs/bindings: (none).
Calls/effect boundaries: argv.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[16].body[3]; no call, error or mutation may be omitted. Condition: claims
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:44`; AST `e582a8cecee5f37a080065b3bddba73c8776c408e206b73308a7183b4eaca912`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: argv.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:44`; AST `88a5268a3dfaf126be83db7f80837350d3b389035dec1c2487edcea1df4e7027`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: argv.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_arguments::root.body[16].body[4]::Return

Source: `infra/agentinfra/roadmap_python.py:45`; AST `7380e3840d109e347e2c95493f45df8297b1fbc0fddb142e625811bc85a9dbd1`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:48`; AST `73415717eb9a81f9066543d9c930f63973c0a56444c15ff560c6ec858f8fa06d`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, argv, bool, claims, dict, esbmc_arguments, expected, fixture, legacy, list, producer_inputs_current, require, root, str, toolchain. Outputs/bindings: expected, legacy.
Calls/effect boundaries: esbmc_arguments, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:50`; AST `178bc92424ac2531b9912c0264ce1153f4cab3080cd010b752a996aa1d866ca9`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:51`; AST `f22456f9b1d137c236070a38de0ea6dc7d27c3fab9e01fc9fdfc98648743fd91`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: claims, esbmc_arguments, fixture, root, toolchain. Outputs/bindings: expected.
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:51`; AST `1333249fbf55f886a4c8cdea92bd66afaec41fbf7b67f37fd6e48b74ad0562eb`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: claims, esbmc_arguments, fixture, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[2]::If

Source: `infra/agentinfra/roadmap_python.py:52`; AST `9de8d3bcea482bd1d21992d3662056573a8d512db998a266a57d3288f9afd008`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: argv, expected. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[17].body[2]; no call, error or mutation may be omitted. Condition: argv == expected
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:53`; AST `805e6c554582f9147d93e2ba255cf8638ba767d650bf0965f75119a1d05670e8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:54`; AST `cedfffe3cb520286d1490fcedde95ae1ab56c051ac44e1a79328b0a0fee549b8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: claims, expected. Outputs/bindings: legacy.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[4]::Expr

Source: `infra/agentinfra/roadmap_python.py:55`; AST `41a213601597a217731531cf45e20656e87fa394d4be328f3bc9bb900b3fda3d`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, legacy, producer_inputs_current, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[4].value::Call

Source: `infra/agentinfra/roadmap_python.py:55`; AST `47f9eacfd1f7ab173582b45f3c072ae2a295581a8dcbd981f13604d2c26b3f9e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, legacy, producer_inputs_current, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_command_policy::root.body[17].body[5]::Return

Source: `infra/agentinfra/roadmap_python.py:57`; AST `db7a6f5233f9f6199966bc3b390b871adc30cf9e6ea456f46a75ef95a43e4701`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:60`; AST `389ed2067ae4268f2e1f0fc0222e15a7edab5a94ee3a20cd7f02852bf5d02d6d`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, RuntimeError, bool, confined_path, dict, entry, list, observed, parent, path, relative, release, require, root, rows, safe, toolchain. Outputs/bindings: entry, observed, parent, path, relative, release, rows, safe.
Calls/effect boundaries: Path, bool, confined_path, parent.is_relative_to, path.is_symlink, path.readlink, path.readlink().as_posix, path.resolve, path.resolve(strict=True).is_relative_to, relative.is_absolute, require, rows.append, toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:61`; AST `9a4fb1c319eae220575ce99155a9b6e090ecc8e5494fd404501934a3a2a3d888`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:62`; AST `095f5e72e43802d0867c01f53bef4c248e5d16f7d0f59530b93b541bb85eb2c6`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root, toolchain. Outputs/bindings: release.
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:62`; AST `6b810c4dab3e2267f3c0fc6ec8025811862542518824a05e64dd0352c3c512b9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:63`; AST `ac5dc778d890ac7d3fe32248966b866f064c4894b141595ccc25455eb29f5366`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3]::For

Source: `infra/agentinfra/roadmap_python.py:64`; AST `104bc57c65a29557b5dd9dd92acb4287badd5360a9c0d4a9e649fced8968a144`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OSError, Path, RuntimeError, bool, confined_path, entry, observed, parent, path, relative, release, require, root, rows, safe, toolchain. Outputs/bindings: entry, observed, parent, path, relative, safe.
Calls/effect boundaries: Path, bool, confined_path, parent.is_relative_to, path.is_symlink, path.readlink, path.readlink().as_posix, path.resolve, path.resolve(strict=True).is_relative_to, relative.is_absolute, require, rows.append, toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[18].body[3]; no call, error or mutation may be omitted. Iteration: entry in toolchain.get('symlinks', [])
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].iter::Call

Source: `infra/agentinfra/roadmap_python.py:64`; AST `3b418e27e46825b6a6922866027ab0dbb2a4cff811cf5df83dc6c1b9e02b7410`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:65`; AST `310bc3b9c82561dd02d8e4920d6f3e914a7e95ebbf945e4d5fa4c3b7e13b7b79`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, entry. Outputs/bindings: relative.
Calls/effect boundaries: Path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:65`; AST `28fabc0ba2361f496981dc8dc691e48e4ae1dbda9bd20cf6d84784f86a3932c2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, entry. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_python.py:66`; AST `49180ae7c28abf874799cf9396e8d460db0c32fa3bd0af5d50e49335d5d755eb`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, require. Outputs/bindings: (none).
Calls/effect boundaries: relative.is_absolute, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:66`; AST `dd3708cb78b0e002080aaaeebf8c006c7799d36af4f0e40a6c2d8fc7a7468302`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative, require. Outputs/bindings: (none).
Calls/effect boundaries: relative.is_absolute, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[1].value.args[0].values[0].operand::Call

Source: `infra/agentinfra/roadmap_python.py:66`; AST `00aaffb80f28951a211c9100385d42ec5450aae288fb251b707aae97c7b776ff`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.is_absolute.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].value.args[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:67`; AST `fe8c92b4e18d3530be8a780ff22c141b822fe1ed52ea8f612f2fb1b71c916d04`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: parent.
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:67`; AST `5139dfd1961b7e810703103bac1b9ae31865b9c23a75fde1ba3210ecc2f520ee`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_python.py:68`; AST `ee0746aadf98527323c38b148f01a21b01d31bd61ff50b0068cf6888e80515f3`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parent, release, require. Outputs/bindings: (none).
Calls/effect boundaries: parent.is_relative_to, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_python.py:68`; AST `0a6a85e8eb88398089b99279339feedf51e4a75a1885b4787f8f1e1be0f1f431`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parent, release, require. Outputs/bindings: (none).
Calls/effect boundaries: parent.is_relative_to, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:68`; AST `f5735e63a169cf85227b73a9adecd60144ee499b5217cdae284b8d8082de92fa`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parent, release. Outputs/bindings: (none).
Calls/effect boundaries: parent.is_relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:69`; AST `9a254c9da2fbc1673a02491aeaf69e27df915b56e0ad06f60716a3083fe78934`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parent, relative. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[5]::Assign

Source: `infra/agentinfra/roadmap_python.py:70`; AST `c1dcab57fb18fedfdd48fd2b706cc6ff3c93205a8c941ae1c6b69ab64730eafc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: observed.
Calls/effect boundaries: path.is_symlink, path.readlink, path.readlink().as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[5].value.test::Call

Source: `infra/agentinfra/roadmap_python.py:70`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[5].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[5].value.body::Call

Source: `infra/agentinfra/roadmap_python.py:70`; AST `593518a770212afd56ae63735f60671b201f20e0f0d2c213f59474ca0e5abbe0`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink, path.readlink().as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[5].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[5].value.body.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:70`; AST `be12d503fd54bd779d75ccf612bcdbf41e065e05b938e9dfedb0ec2536ee3343`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[5].value.body.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6]::Try

Source: `infra/agentinfra/roadmap_python.py:71`; AST `22d80fcb07db75ade6789e7090c788d401e1c730dbc4ef9de2e88ce3bc95cbec`.

Rust module: `infra::agentinfra::roadmap_python`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, RuntimeError, bool, observed, path, release. Outputs/bindings: safe.
Calls/effect boundaries: bool, path.resolve, path.resolve(strict=True).is_relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Try evaluation at root.body[18].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:72`; AST `db674739f1c74af6f4a117b1823359605311abdfc03e2977012f62d465e27cfd`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, observed, path, release. Outputs/bindings: safe.
Calls/effect boundaries: bool, path.resolve, path.resolve(strict=True).is_relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:72`; AST `21e8df57cea3c811bf02f4b92376f9c1dc87de937a5d3a9fbf6475edd7e39e32`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, observed, path, release. Outputs/bindings: (none).
Calls/effect boundaries: bool, path.resolve, path.resolve(strict=True).is_relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:72`; AST `afe7a5b07018118bb7f2b61409e77f2f7157fb58198488f4da24a82e3c2acc91`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, release. Outputs/bindings: (none).
Calls/effect boundaries: path.resolve, path.resolve(strict=True).is_relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6].body[0].value.args[0].values[1].func.value::Call

Source: `infra/agentinfra/roadmap_python.py:72`; AST `1a16b2bd53a983bcc5031f30a9a1dc7d5aac796d63f545cb3b1d99e954c660fc`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.resolve.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].body[0].value.args[0].values[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_python.py:73`; AST `e9fff3c3e69922b26464f91f9622d031d77878b02fd97847516c88aad141ecba`.

Rust module: `infra::agentinfra::roadmap_python`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, RuntimeError. Outputs/bindings: safe.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[18].body[3].body[6].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[6].handlers[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:74`; AST `100417f8077881dad959fd3668cf15b0679926b35a349dd89210a17112b57612`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: safe.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[6].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[7]::Expr

Source: `infra/agentinfra/roadmap_python.py:75`; AST `29198c2667e05c3b992f7a2ad976f8fc7c77280d5f7b67ebdd7ed48ff2438b36`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, observed, rows, safe. Outputs/bindings: (none).
Calls/effect boundaries: rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[3].body[7].value::Call

Source: `infra/agentinfra/roadmap_python.py:75`; AST `f314922cf3ae25729f8eb99a9703b814d85c11d0ecffadb543dd71ca269ce814`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, observed, rows, safe. Outputs/bindings: (none).
Calls/effect boundaries: rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::esbmc_link_state::root.body[18].body[4]::Return

Source: `infra/agentinfra/roadmap_python.py:76`; AST `e8d62c7bb685945ea0a81e6d4c73e7fe86bcf8b904a9d5c35c30d98b70af7c94`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:79`; AST `f062be2e2cdd3c2416022deef52a4c35982ccebd117024e563e40b1ff7871bd0`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, output, re, run. Outputs/bindings: output.
Calls/effect boundaries: re.search, run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:80`; AST `cf4b9c479f018d1c93c4fa589154988b63cac77f4c5ba7334988f108258ccb8a`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:81`; AST `a1488055fc81b7d75b793dce6719d43f9f07a22eddc69b3ead810b571fe21d10`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[19].body[1]; no call, error or mutation may be omitted. Condition: run.get('timed_out') or run.get('stdout_truncated') or run.get('stderr_truncated')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[1].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:81`; AST `bf9254dc6751673df54c8c8712c82a283034ab4c8b4a6805fbb0b1729d5e875a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[1].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:81`; AST `5b731948b6b950a0e7b3c608217c7665a30c59bbf52d5d13a5406bf3844de3c7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[1].test.values[2]::Call

Source: `infra/agentinfra/roadmap_python.py:81`; AST `314424bb4502375fdd1fc0f147f592abed1ec99e39883f208e17f8d83b18fcf1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:82`; AST `e41522aaa386b237f36a6e0e358c1e07e623898f53c45a52ffea2e855b6ef44c`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:83`; AST `07f218db002279a6c880a297511f3acd78379edb4e548fe098f0a14b6507b84a`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: run. Outputs/bindings: output.
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[2].value.left.left::Call

Source: `infra/agentinfra/roadmap_python.py:83`; AST `6df5bbe6141d63abe7ef30f663e13a831cc2e4e7049b42f604970ca3fb4f8e96`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value.left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[2].value.right::Call

Source: `infra/agentinfra/roadmap_python.py:83`; AST `06f12d9f5c50db36ee1b352ebbd4fae1d9afd7de676e9883335584081938bed0`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[3]::If

Source: `infra/agentinfra/roadmap_python.py:84`; AST `c76f99f049c220dd801757296e6704b60f4268855bc168ae907e28b7be70cb74`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[19].body[3]; no call, error or mutation may be omitted. Condition: re.search('(?i)timed out|time limit exceeded|^TIMEOUT', output)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[3].test::Call

Source: `infra/agentinfra/roadmap_python.py:84`; AST `2108eb4e384fc219f5e109cea14e8d4ef2fd1b21381a3f540a192ec867eff8d2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:85`; AST `f6cc574b90b00df5a641c1a1396b5d010f5f13927d6539e848928dc74a6817da`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[4]::If

Source: `infra/agentinfra/roadmap_python.py:86`; AST `8c4b6986d8f4af1b62ae9b3717fa17c609a6a626caefc7f83db431760956051f`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[19].body[4]; no call, error or mutation may be omitted. Condition: re.search('(?i)traceback|unsupported|not supported|error:|parsing error|segmentation fault|terminate called|aborted', output)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[4].test::Call

Source: `infra/agentinfra/roadmap_python.py:86`; AST `23885a9d02bdef6347ea922cb6f02bb012a91653e9b357e28720af1caf039e26`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:87`; AST `8f8abd4243348491dd5cefb40f2d4f4c416ecd0f2429cf6658e46ffbf0ba19fa`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[5]::If

Source: `infra/agentinfra/roadmap_python.py:88`; AST `a63baf618d6fbff65df7ab8182dc5dbe786300b7238666e75d352899d84e9c29`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[19].body[5]; no call, error or mutation may be omitted. Condition: 'VERIFICATION SUCCESSFUL' in output and run.get('returncode') == 0
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[5].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:88`; AST `960fde0eb87025060b1e30c49da5835cd28c809c64d675e28ae074fd861900b6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[5].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:89`; AST `ccee43afadabf31c6a801d8b42552789ba809407b189142246e51b2ed911e7b6`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[6]::If

Source: `infra/agentinfra/roadmap_python.py:90`; AST `b7a5205228ce1ad4afd2d9402ba2eadfda59bb5c99d00b1775aea57d78843f62`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[19].body[6]; no call, error or mutation may be omitted. Condition: 'VERIFICATION FAILED' in output and run.get('returncode') not in {None, 0}
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[6].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:90`; AST `960fde0eb87025060b1e30c49da5835cd28c809c64d675e28ae074fd861900b6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[6].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:91`; AST `b0326436951d445d9262a19f8c53bd24c5dadcc096bb8522dee2f6db914d6fb7`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_esbmc::root.body[19].body[7]::Return

Source: `infra/agentinfra/roadmap_python.py:92`; AST `ebbfb9eaa0860009c3a551d3bf0bc22be76d76f3a671cf00f7aa2ed4d142cf39`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:95`; AST `07d96c1d2cfe41170e63a5c04121cb8a1faa0ca237fa04826fc98039c8c53398`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, any, c, calls, dict, observation, proof, run. Outputs/bindings: c, calls, proof.
Calls/effect boundaries: all, any, c.get, observation.get, proof.get, run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:96`; AST `ad3a836b557bd03c5449ccd93f05d2d3845701f4d3c0f7f84c661d13c1dafc65`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:97`; AST `1570e76e213418765791ac8c02676ff458ec08c71e558553630c7a54b9173c86`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[20].body[1]; no call, error or mutation may be omitted. Condition: run.get('timed_out') or run.get('stdout_truncated') or run.get('stderr_truncated')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[1].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:97`; AST `bf9254dc6751673df54c8c8712c82a283034ab4c8b4a6805fbb0b1729d5e875a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[1].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:97`; AST `5b731948b6b950a0e7b3c608217c7665a30c59bbf52d5d13a5406bf3844de3c7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[1].test.values[2]::Call

Source: `infra/agentinfra/roadmap_python.py:97`; AST `314424bb4502375fdd1fc0f147f592abed1ec99e39883f208e17f8d83b18fcf1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:98`; AST `710435a22ef28f5300dfdd84b1d1e729b3acb97b050fbad720456a0d1b3d55a9`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[20].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[2]::If

Source: `infra/agentinfra/roadmap_python.py:99`; AST `cdad7efc7aab2337652a2a61bd7a6b6f2b871b30a29aa35da28818d827047e7e`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: observation, run. Outputs/bindings: (none).
Calls/effect boundaries: observation.get, run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[20].body[2]; no call, error or mutation may be omitted. Condition: run.get('returncode') != 0 or observation.get('error') or observation.get('status') != 'OBSERVED_UNQUALIFIED'
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[2].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:99`; AST `960fde0eb87025060b1e30c49da5835cd28c809c64d675e28ae074fd861900b6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[2].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:99`; AST `a842b32d241f6d7a84453d9e41ae7459d09801025c07b445b2d341941b9e9a22`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[2].test.values[2].left::Call

Source: `infra/agentinfra/roadmap_python.py:99`; AST `00cc91bd6eb8c39870f5f32b31c9c2953866f91cd253c55830cdb92494f85553`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].test.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:100`; AST `3bfa4314bab4dca1ed6fedfb88d5dd47c9c7fec39246e8fd2a598eb0f7d1d89c`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[20].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:101`; AST `ce930f573652afdafbca94e9f525c437ece92d2aa63d367fec6c961c3842233b`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: proof.
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[3].value::Call

Source: `infra/agentinfra/roadmap_python.py:101`; AST `95a90182778b76d76c5be883bc180bb3320406c830479e168ed8076762312915`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:102`; AST `8e0d8b63d0cd754c68bd0fb191d744467a1fb11d916e2bd02d688a359f6ca20b`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: calls.
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[4].value::Call

Source: `infra/agentinfra/roadmap_python.py:102`; AST `f0436a51a2e06b991547b846b3d613ce96fd8a2fbba4d54334aa27cfb9dda1b6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[5]::If

Source: `infra/agentinfra/roadmap_python.py:103`; AST `fffaa47a1866e4247607c730185678d53e8f39f4557b851fa98789b7b96f2f2a`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: calls, observation, proof. Outputs/bindings: (none).
Calls/effect boundaries: observation.get, proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[20].body[5]; no call, error or mutation may be omitted. Condition: observation.get('skips') or proof.get('conclusion') in {'SKIP', 'PARTIAL'} or (not calls) or (proof.get('description') == 'nothing to prove')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[5].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:103`; AST `6cba289bad185edef68bc0ae19b79a753afda52f8926dad3909e5267e274f03f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[5].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:103`; AST `459b116c28211ca0e27c2349fc316ad547eedff2d805d6e7e73abc83ce414c39`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[5].test.values[3].left::Call

Source: `infra/agentinfra/roadmap_python.py:104`; AST `a2dfafaf4bb89742583e766c9a7e09f8d325eac53c7dd90f91334d3693852c6e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].test.values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[5].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:105`; AST `b8d79b1eacb9d6d96cae4e0f41fe3755efa28136f3260bc2f13f3cb3aa8ce00f`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[20].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[6]::If

Source: `infra/agentinfra/roadmap_python.py:106`; AST `e41f3621a004ba9b1012d0a525fcc881be2e3e9de1810237267aa18184289aa4`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: all, c, calls, proof. Outputs/bindings: c.
Calls/effect boundaries: all, c.get, proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[20].body[6]; no call, error or mutation may be omitted. Condition: proof.get('conclusion') == 'OK' and all((c.get('conclusion') == 'OK' for c in calls))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[6].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:106`; AST `459b116c28211ca0e27c2349fc316ad547eedff2d805d6e7e73abc83ce414c39`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[6].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:106`; AST `80f3ac43b7b9a399991cf9ec78ea2cffcd314d24fc380503213e86c452f22c61`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, calls. Outputs/bindings: c.
Calls/effect boundaries: all, c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[6].test.values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python.py:106`; AST `21f2c8bc5504b8552301667fe18d4604a99950f6c8fc9d06fa43b20893a78611`.

Rust module: `infra::agentinfra::roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, calls. Outputs/bindings: c.
Calls/effect boundaries: c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[20].body[6].test.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[6].test.values[1].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_python.py:106`; AST `af7d8a3c8b8928f5ef9e8656cdfe0fcdb3c62de844995bcf3b865767db5c370b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].test.values[1].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[6].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:107`; AST `4cdcf49efcca6c4b5ce19f2ed5091496773d311916c73fbd8f3ad51027775013`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[20].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7]::If

Source: `infra/agentinfra/roadmap_python.py:108`; AST `2fc17188917340482a12add0997aef8de484d552b14b31ed5fbc4b7b5e278e0b`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, c, calls, proof. Outputs/bindings: c.
Calls/effect boundaries: any, c.get, proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[20].body[7]; no call, error or mutation may be omitted. Condition: proof.get('conclusion') == 'FAIL' and any((c.get('conclusion') == 'FAIL' and c.get('description') == 'assertion' for c in calls))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:108`; AST `459b116c28211ca0e27c2349fc316ad547eedff2d805d6e7e73abc83ce414c39`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: proof.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:108`; AST `16e035fd9fe69adbf4f584dde176d1720c3142998e83116f4f1e9ea86444c01e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, c, calls. Outputs/bindings: c.
Calls/effect boundaries: any, c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7].test.values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python.py:108`; AST `e99edc6bd1f15ff2dc9a18b6a6e964319f794c60c6af459846905c396c743546`.

Rust module: `infra::agentinfra::roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, calls. Outputs/bindings: c.
Calls/effect boundaries: c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[20].body[7].test.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7].test.values[1].args[0].elt.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:108`; AST `af7d8a3c8b8928f5ef9e8656cdfe0fcdb3c62de844995bcf3b865767db5c370b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].test.values[1].args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7].test.values[1].args[0].elt.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:108`; AST `a58f90518aa6fd1b56a21a75146bee99c4312a2eb947da610ed2a550d9a95d1a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].test.values[1].args[0].elt.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:109`; AST `cb81e6e46605549cfd3014e1b0d0308508911f2f6534de793d46088d9e9fa3f8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[20].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_deal::root.body[20].body[8]::Return

Source: `infra/agentinfra/roadmap_python.py:110`; AST `9e69b76bbede32cbdbcb1b466811a9c52dcef3cfedfcb43ae7cc27770d974df2`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[20].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:113`; AST `ccafb44fe580d21e38a61710e24304aee27d4c34754f4370934a2f204fded598`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bool, dict, include_tests, key, maintained_python, name, path, relative, require, result, root, str. Outputs/bindings: key, name, path, relative, result.
Calls/effect boundaries: maintained_python, name.removesuffix, path.relative_to, path.relative_to(root).as_posix, relative.removeprefix, relative.removeprefix('infra/').removesuffix, relative.removeprefix('infra/').removesuffix('.py').replace, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, relative.startswith, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:114`; AST `2c435ecac12c985901bb8025f4efe5e5ad7e200542d8b36f3e0370612550a391`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1]::For

Source: `infra/agentinfra/roadmap_python.py:115`; AST `cd0107b1121071998c666c5ab5ec9179d26e16f96b553353f8e1b26396ffc51b`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: include_tests, key, maintained_python, name, path, relative, require, result, root. Outputs/bindings: key, name, path, relative.
Calls/effect boundaries: maintained_python, name.removesuffix, path.relative_to, path.relative_to(root).as_posix, relative.removeprefix, relative.removeprefix('infra/').removesuffix, relative.removeprefix('infra/').removesuffix('.py').replace, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, relative.startswith, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[21].body[1]; no call, error or mutation may be omitted. Iteration: path in maintained_python(root)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].iter::Call

Source: `infra/agentinfra/roadmap_python.py:115`; AST `ebe3343fcce41557451c3ee0c98810e3fb3b8c363ee8f3dc1f06b697298b0596`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: maintained_python, root. Outputs/bindings: (none).
Calls/effect boundaries: maintained_python.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:116`; AST `c9a5d02444369221b50b662c72fded4efbbded9a1bf01f8bacecd9d7badf680c`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, root. Outputs/bindings: relative.
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:116`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:116`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:117`; AST `e2adb0e7edb9817ccd3521a782ff90cdd2435a12d16fee91c6dc66e79bb00666`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: include_tests, key, name, path, relative, require, result. Outputs/bindings: key, name.
Calls/effect boundaries: name.removesuffix, relative.removeprefix, relative.removeprefix('infra/').removesuffix, relative.removeprefix('infra/').removesuffix('.py').replace, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, relative.startswith, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[1]; no call, error or mutation may be omitted. Condition: relative.startswith('infra/agentinfra/')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].test::Call

Source: `infra/agentinfra/roadmap_python.py:117`; AST `1e468eec55ec16b2560984ee15380e612f297a651d97e490cf2dd255c4ff1017`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:118`; AST `47a59fd67f2a5e8237f4b0f7cf86d12d531a1eae08468b750d7ee69b08ed1227`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative. Outputs/bindings: name.
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/').removesuffix, relative.removeprefix('infra/').removesuffix('.py').replace.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:118`; AST `b0ddfe1016de4a52ca0b869275070dfbf1c854b8e4542d47b8d498fb70a6fa2b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/').removesuffix, relative.removeprefix('infra/').removesuffix('.py').replace.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:118`; AST `5ad70cd03cd0d5d35d1e04f6015c394da3309182acf94aea9bd19c957ec351af`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/').removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].body[0].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:118`; AST `ca5efa0c9f6b8ea57acc6940e7b2ef2937f989dbdec1c047a7a279c17139747e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].body[0].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:119`; AST `4894957cf2f3f87eff13bb97c241e628f385adddb33e34258127d91033596936`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, path, result. Outputs/bindings: (none).
Calls/effect boundaries: name.removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].body[1].targets[0].slice::Call

Source: `infra/agentinfra/roadmap_python.py:119`; AST `f4b0c69bb849b314b144b5c26aa0d1709c85d9eb909640148b059fed8c04f858`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].body[1].targets[0].slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0]::If

Source: `infra/agentinfra/roadmap_python.py:120`; AST `ebcabc68211558ca7747130ecd258b4c053e5b8c4fbe63b025dbc14b904ba399`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: include_tests, key, name, path, relative, require, result. Outputs/bindings: key, name.
Calls/effect boundaries: name.removesuffix, relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, relative.startswith, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[1].orelse[0]; no call, error or mutation may be omitted. Condition: include_tests and relative.startswith('infra/tests/')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:120`; AST `fd5fad1a27222d41e08615b0583e20b9a736cf05859fae139679c2174f10a81b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].orelse[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:121`; AST `2b7987cdf4eced9b9ed560bb2fc4d6e363fcb74d2dd109fe7cd81b3e0ef34ac6`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative. Outputs/bindings: name.
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:121`; AST `e3c8b31c01d6b2ad919a14880c57828c45197b694f381dae31ed1a40f4e7444c`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:121`; AST `5e4a206b58cdebe0a9f3cfbe3c42e661cc3f31899c470277746612dadeb7b375`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].orelse[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[0].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:121`; AST `76236f9e85124a22ccddc476b067cc0b599d2cd22a783bfbc51362afb76de198`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].orelse[0].body[0].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:122`; AST `5cc2e5061f90166203229784c8249871d98227fb222717af6e933c6e83971b70`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name. Outputs/bindings: key.
Calls/effect boundaries: name.removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[1].orelse[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:122`; AST `f4b0c69bb849b314b144b5c26aa0d1709c85d9eb909640148b059fed8c04f858`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.removesuffix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].orelse[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[2]::Expr

Source: `infra/agentinfra/roadmap_python.py:123`; AST `5ceadbe2feb2225a506859da97b990aebabd58f24657257d32d365510751927f`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[1].body[1].orelse[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:123`; AST `5f3d566e5776a6a5bdc139d1bfbd9a33e2a58737fd821726e29712a8b337f7c7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].orelse[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[1].body[1].orelse[0].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:124`; AST `a81f944630dd9a5e21a4f373dbcdfd942485e6b0bdcf3c78b358455f65108b7b`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, path, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[1].orelse[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::_modules::root.body[21].body[2]::Return

Source: `infra/agentinfra/roadmap_python.py:125`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:128`; AST `2d3dc4124491d09ba4ecdb3f8e94d418971b9f5761f36165bd278788924e92d6`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: DYNAMIC, EFFECT_MODULES, Path, _modules, a, ast, b, bool, count, dependencies, dependency, dict, digest, external, external_rows, file_binding, files, h, hazards, importlib, include_tests, isinstance, len, module, modules, name, node, package, parent, path, pending, range, record, relative, require, root, set, sorted, str, tree, type, visited. Outputs/bindings: a, count, dependencies, dependency, external, external_rows, files, hazards, modules, name, node, package, parent, path, pending, record, relative, tree, visited.
Calls/effect boundaries: '.'.join, _modules, ast.parse, ast.unparse, ast.walk, dependencies.add, dependencies.update, digest, external.add, external_rows.append, file_binding, files.append, hazards.append, importlib.util.resolve_name, isinstance, len, name.rpartition, name.split, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, pending.append, pending.pop, range, require, set, sorted, type, visited.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:129`; AST `5db52268bd5fce705a14f5a34c842a6d57e23a9d944be55532b7b8a2c13e9c08`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:135`; AST `446fa0ad587b33604c3a66e13a4e5c0d02294c1d3ca103cf16dc371d1f07eccd`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _modules, include_tests, root. Outputs/bindings: modules.
Calls/effect boundaries: _modules.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:135`; AST `4e642e8a4b4c5eae6c671cf21e3d1c78342a6c8c26ccfc8f4bba777f3e1d00ae`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _modules, include_tests, root. Outputs/bindings: (none).
Calls/effect boundaries: _modules.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[2]::Expr

Source: `infra/agentinfra/roadmap_python.py:136`; AST `01d260d2d5635be69b4da52a0c0df46197e0f36482de7d1f49e38e203590e754`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: module, modules, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:136`; AST `bca7eaf9da3d6e8dfb2e6fce92104ddd88a6b2120dac7471d04a3e3f81068813`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module, modules, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:137`; AST `4a67ecff99d8b848b82e85a134b8a29c3f148c101a4c4c2e1f87baff49d4d4a2`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: module, set. Outputs/bindings: external, files, hazards, pending, visited.
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[3].value.elts[1]::Call

Source: `infra/agentinfra/roadmap_python.py:137`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[3].value.elts[3]::Call

Source: `infra/agentinfra/roadmap_python.py:137`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[3].value.elts[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4]::While

Source: `infra/agentinfra/roadmap_python.py:138`; AST `fc7cebcb93164c826e6b43506c21e88de1f327d5b6ff7049323ed8bf3c4abb5b`.

Rust module: `infra::agentinfra::roadmap_python`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: DYNAMIC, a, ast, count, dependencies, dependency, external, file_binding, files, hazards, importlib, isinstance, len, modules, name, node, package, parent, path, pending, range, relative, root, set, tree, type, visited. Outputs/bindings: a, count, dependencies, dependency, name, node, package, parent, path, relative, tree.
Calls/effect boundaries: '.'.join, ast.parse, ast.unparse, ast.walk, dependencies.add, dependencies.update, external.add, file_binding, files.append, hazards.append, importlib.util.resolve_name, isinstance, len, name.rpartition, name.split, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, pending.append, pending.pop, range, set, type, visited.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered While evaluation at root.body[22].body[4]; no call, error or mutation may be omitted. Condition: pending
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:139`; AST `79a5064181d8b093c604343b55bb720b127ce55e16ab09b54072679e44e78873`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending. Outputs/bindings: name.
Calls/effect boundaries: pending.pop.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:139`; AST `b59b504ea575e0473ea0b5cc17902585c9dde56c94712f38bdafbec0ce738e98`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.pop.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:140`; AST `cfe0978b3d813d3e6a449e4c705e3c590f7599cd86091a607f25ad9bfd21bbd8`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: name, visited. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[1]; no call, error or mutation may be omitted. Condition: name in visited
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[1].body[0]::Continue

Source: `infra/agentinfra/roadmap_python.py:141`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Continue evaluation at root.body[22].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[2]::Expr

Source: `infra/agentinfra/roadmap_python.py:142`; AST `02335b9788b9a5d9b32cec0f4ca62ab69642213324e34a2cf78208dcf40e553a`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, visited. Outputs/bindings: (none).
Calls/effect boundaries: visited.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:142`; AST `ee93f5d990c895f275dc0524fd37216e2daf9d340375b638e3e5c7053758fc77`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, visited. Outputs/bindings: (none).
Calls/effect boundaries: visited.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:143`; AST `2f95153b3f8c72af02dedd25d35315c9e34e8df7d857a36745c81bc4fb210dd0`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: modules, name. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:144`; AST `c9a5d02444369221b50b662c72fded4efbbded9a1bf01f8bacecd9d7badf680c`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, root. Outputs/bindings: relative.
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_python.py:144`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:144`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[5]::Expr

Source: `infra/agentinfra/roadmap_python.py:145`; AST `5bb8c7e2c18fc3be463234888df63a79031d2f02b35d5e5cbbd029aaebaa37a2`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, files, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, files.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[5].value::Call

Source: `infra/agentinfra/roadmap_python.py:145`; AST `a8f89555b031de103d2637f55f0f004ffcfdfeeba6fd4af3b6457bc48ef6afe6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, files, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, files.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:145`; AST `e8457929e4b469f5fb6798717852b1b34d5ad1a0970999a9e33bb237cecc4b61`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[6]::Assign

Source: `infra/agentinfra/roadmap_python.py:146`; AST `909a958acdb48960e264f6ff9cb988dd15d6c33b44b31b3a14a16eba4a7a95c7`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, path, relative. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_python.py:146`; AST `67537485f475d118833b444d0c543289a0b717cd6e77cfec6a7f66c408daf6ad`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, path, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[6].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:146`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[7]::Assign

Source: `infra/agentinfra/roadmap_python.py:147`; AST `460e57179c69ac383848440c3a7f6d6fd3aeb7ca15503efbf3045b4a126246cc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, path. Outputs/bindings: package.
Calls/effect boundaries: name.rpartition.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[7].value.orelse.value::Call

Source: `infra/agentinfra/roadmap_python.py:147`; AST `a1bbc766d672e89e92f18f4fccc0320bb9846a9c61eef32b69f50a72393d0ba1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.rpartition.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[7].value.orelse.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[8]::Assign

Source: `infra/agentinfra/roadmap_python.py:148`; AST `73e68a4ab479f38d4762ef4dd53fb9f107b9b9c264270aa4c050098692b6b864`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: dependencies.
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[8].value::Call

Source: `infra/agentinfra/roadmap_python.py:148`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9]::For

Source: `infra/agentinfra/roadmap_python.py:149`; AST `5738c1e224204b32128795cef3111c4370e1157f2455be8384d496c716a6451b`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: count, dependencies, len, modules, name, parent, range. Outputs/bindings: count, parent.
Calls/effect boundaries: '.'.join, dependencies.add, len, name.split, range.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[22].body[4].body[9]; no call, error or mutation may be omitted. Iteration: count in range(1, len(name.split('.')))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].iter::Call

Source: `infra/agentinfra/roadmap_python.py:149`; AST `7da63f115a11f2da2ae74002567097f73673ac53f6a6c5e44454ab1412f92074`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, name, range. Outputs/bindings: (none).
Calls/effect boundaries: len, name.split, range.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[9].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].iter.args[1]::Call

Source: `infra/agentinfra/roadmap_python.py:149`; AST `26292ef1c3c398bdd85ab03decdc7be62f164068ee6422c889fa18dc63f831c0`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, name. Outputs/bindings: (none).
Calls/effect boundaries: len, name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[9].iter.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].iter.args[1].args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:149`; AST `b3dec83a02904bd005345bc09fb30cf7950897d72cf03866de759d3a9df59cd9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[9].iter.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:150`; AST `b54f2da7ce19fdb58959f5be48551f5b8eaaa2c67aeb6bdb685e721a847f07c2`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, name. Outputs/bindings: parent.
Calls/effect boundaries: '.'.join, name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:150`; AST `0c1690f18fb848118cbac568bda3a7da2d9a4c7c731908b1d6c4f0dc2d8c4a33`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, name. Outputs/bindings: (none).
Calls/effect boundaries: '.'.join, name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].body[0].value.args[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:150`; AST `b3dec83a02904bd005345bc09fb30cf7950897d72cf03866de759d3a9df59cd9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[9].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:151`; AST `1bba2ac2654637a1ba6fec7d806d6680718300b12fcf62d49616fe87e8dbdd71`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dependencies, modules, parent. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[9].body[1]; no call, error or mutation may be omitted. Condition: parent in modules
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:152`; AST `a915e855909e16931944f7ca25465d7a936046f5638f1bf8b5a891ed94c22518`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, parent. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[9].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[9].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:152`; AST `c7694fb3e0fb07591d89ef9f724ddbbfb7a4e96322223de0a55e32d8d9150d06`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, parent. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[9].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10]::For

Source: `infra/agentinfra/roadmap_python.py:153`; AST `07954e3db6bdccf7f6d898bcbe53f30eb515e42b4a0c8633654b761541693a10`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: DYNAMIC, a, ast, dependencies, dependency, hazards, importlib, isinstance, modules, node, package, relative, tree, type. Outputs/bindings: a, dependency, node.
Calls/effect boundaries: ast.unparse, ast.walk, dependencies.add, dependencies.update, hazards.append, importlib.util.resolve_name, isinstance, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[22].body[4].body[10]; no call, error or mutation may be omitted. Iteration: node in ast.walk(tree)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].iter::Call

Source: `infra/agentinfra/roadmap_python.py:153`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0]::If

Source: `infra/agentinfra/roadmap_python.py:154`; AST `18468c0ffd5fbdf911b9db8525c93503c3e5445810f54b6d9c04bd867c48445a`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: DYNAMIC, a, ast, dependencies, dependency, hazards, importlib, isinstance, modules, node, package, relative, type. Outputs/bindings: a, dependency.
Calls/effect boundaries: ast.unparse, dependencies.add, dependencies.update, hazards.append, importlib.util.resolve_name, isinstance, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[10].body[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.Import)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].test::Call

Source: `infra/agentinfra/roadmap_python.py:154`; AST `bcf2d7bd24edff449cb512da4d3682a98eaf6a2051e4413b6cca0fa8da802d2a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:155`; AST `6b6838e9cb10bc189c66dfcc9ddae944e679776dee9da8af7a5633e769297425`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, dependencies, node. Outputs/bindings: a.
Calls/effect boundaries: dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:155`; AST `87e255ba2770dfa9c6dfd224afb3459c7f319310e98d16db70f7cf9055ed899e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, dependencies, node. Outputs/bindings: a.
Calls/effect boundaries: dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python.py:155`; AST `56869e058338adfb03a22f6055bf7186493bf511601a7b311d8eeecaf6755170`.

Rust module: `infra::agentinfra::roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, node. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[22].body[4].body[10].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_python.py:156`; AST `635c80083edb252ee8af768b585e835fe37a1ef89583f5c869618b44d74abdef`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: DYNAMIC, a, ast, dependencies, dependency, hazards, importlib, isinstance, modules, node, package, relative, type. Outputs/bindings: a, dependency.
Calls/effect boundaries: ast.unparse, dependencies.add, dependencies.update, hazards.append, importlib.util.resolve_name, isinstance, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[10].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.ImportFrom)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_python.py:156`; AST `590fb849ed19f160c1e37ff1ac642a8b6c15e24fbebaf71c0325db10ff5a8938`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:157`; AST `305021f8a02dbc9eaa90d3be24ef46410eed852b6ca82aa91bf3eadae710739e`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: importlib, node, package. Outputs/bindings: dependency.
Calls/effect boundaries: importlib.util.resolve_name.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[0].value.body::Call

Source: `infra/agentinfra/roadmap_python.py:157`; AST `72a9ac48ac44c0ba1bba516670d1a54d3b6e1dff90c41bdbde679f500cf4ecb8`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: importlib, node, package. Outputs/bindings: (none).
Calls/effect boundaries: importlib.util.resolve_name.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:158`; AST `21bde3014933f830644d82a27ff367aed7fb44c1698a78f283fb63f314648f9c`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, dependencies, dependency, modules, node. Outputs/bindings: a.
Calls/effect boundaries: dependencies.add, dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[1]; no call, error or mutation may be omitted. Condition: dependency
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:159`; AST `1a348a6753ffc4ff6a3b1831eb80cd60db14f1d28b19b327b695515adec0cfcc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:159`; AST `cc617346ce7e4620e79d798fe760a8b02deece3009c51554389d58026dc64c28`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_python.py:160`; AST `a3c117e7254755015e72163fae3e05a5d501f0e97244f04fb484927614067b5d`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, dependencies, dependency, modules, node. Outputs/bindings: a.
Calls/effect boundaries: dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:160`; AST `8791f4681dda82040a3caaf9a0a014f5931bf73f2a006486c6c05694bb1d2eaf`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, dependencies, dependency, modules, node. Outputs/bindings: a.
Calls/effect boundaries: dependencies.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[1].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python.py:160`; AST `27e797e885677ca6dc69af2282aa99b24055b5e23bf5840589c54a7eca0ac9f8`.

Rust module: `infra::agentinfra::roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, dependency, modules, node. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[22].body[4].body[10].body[0].orelse[0].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_python.py:161`; AST `5b1489b44057cae13ca94e54a844a12ca732e0a754ebab5acf90325c68ba7fbf`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: DYNAMIC, ast, hazards, isinstance, node, relative, type. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, hazards.append, isinstance, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(node, ast.Call) and ast.unparse(node.func) in DYNAMIC
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:161`; AST `4997081ff906c8796f106ce8f6260f1dfd36debc1ad1c0ac789544985a119802`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:161`; AST `8c39eebfc87e80849e11fdc7cd52549192cf2cc20a3ac5b8ad905d4587343e4e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:162`; AST `1df127a03591abb337fd9a634bf3df46284ee7b268f7365a68da40721b795edc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, hazards, node, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, hazards.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:162`; AST `9fc8b2b576e4424b3eaebbe5b9179fb5053ced1bd93b07a01569b82d62513ad4`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, hazards, node, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, hazards.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].body[0].value.args[0].values[3]::Call

Source: `infra/agentinfra/roadmap_python.py:162`; AST `8c39eebfc87e80849e11fdc7cd52549192cf2cc20a3ac5b8ad905d4587343e4e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].body[0].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_python.py:163`; AST `2b3d038f73bf90ea4d377797e0b0f4ed1ec9214130baef9c532e9160dd07620e`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, hazards, isinstance, node, relative, type. Outputs/bindings: (none).
Calls/effect boundaries: hazards.append, isinstance, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.AsyncFunctionDef, ast.Await, ast.Yield, ast.YieldFrom))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_python.py:163`; AST `152663888dae7d823d7da4e29b4f3e54207a86d19c7d71df0c85b81a1fe738dc`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:164`; AST `0e479d83bb9589a04397ec424874e8496b622fda0b213a8a446a37810c498cba`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hazards, node, relative, type. Outputs/bindings: (none).
Calls/effect boundaries: hazards.append, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:164`; AST `e0856b63666610055f6295e27824219e467695cd030ae3ba9394989869153abd`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hazards, node, relative, type. Outputs/bindings: (none).
Calls/effect boundaries: hazards.append, type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].body[0].value.args[0].values[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:164`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[10].body[0].orelse[0].orelse[0].orelse[0].body[0].value.args[0].values[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11]::For

Source: `infra/agentinfra/roadmap_python.py:165`; AST `21d4cc00878465e63a85d495f7af4565972b0eb28ff9b6919a5368d26807a6d2`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: dependencies, dependency, external, modules, pending. Outputs/bindings: dependency.
Calls/effect boundaries: external.add, pending.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[22].body[4].body[11]; no call, error or mutation may be omitted. Iteration: dependency in dependencies
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11].body[0]::If

Source: `infra/agentinfra/roadmap_python.py:166`; AST `ed079abbd7f2929f0ef0edc24db27742886b2ee325fd877bf427e00e68293a01`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dependency, external, modules, pending. Outputs/bindings: (none).
Calls/effect boundaries: external.add, pending.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[11].body[0]; no call, error or mutation may be omitted. Condition: dependency in modules
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:167`; AST `b11569782bdcd1dd1c42876e073338f91b629d15866d988156de36123f328bc8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[11].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:167`; AST `70887ce054ecbdc449b819b48fc0e4b8f6650730001f16cc422cb98e654e0350`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[11].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_python.py:168`; AST `c2bcb451be1eb8a179a8c2cba5d927f169f038db8ddb939b22775d068a197851`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dependency, external. Outputs/bindings: (none).
Calls/effect boundaries: external.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[22].body[4].body[11].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: dependency != '__future__'
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11].body[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:169`; AST `f332433789dcf27b5c461bfb5d80bb92bd0207466f61c8b31008650ece755a9d`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency, external. Outputs/bindings: (none).
Calls/effect boundaries: external.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[11].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[4].body[11].body[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:169`; AST `eeeed21e7213b47e021ab8c171572070bedbd2cf150c71183d2eddc70c0af5d0`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, external. Outputs/bindings: (none).
Calls/effect boundaries: external.add.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[11].body[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[5]::Assign

Source: `infra/agentinfra/roadmap_python.py:170`; AST `ced836cb7e0f84873acbd3fd65a4013c18f32d82b190230a9d1b6b8bd0956d0b`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: external_rows.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[6]::For

Source: `infra/agentinfra/roadmap_python.py:171`; AST `22e8d14749e7ee14d48815420eaedbd5f8effdca59157a113fb46428a6e238f1`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: EFFECT_MODULES, external, external_rows, name, sorted. Outputs/bindings: name.
Calls/effect boundaries: external_rows.append, name.split, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[22].body[6]; no call, error or mutation may be omitted. Iteration: name in sorted(external)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[6].iter::Call

Source: `infra/agentinfra/roadmap_python.py:171`; AST `003aff05069180b2dcdd0adedf124a7455120050ff9ac4678032b8be026af3a9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: external, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:173`; AST `562ac7857c479087d6022dc6b1905c278c4285a6aab79b24f708d02440153024`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: EFFECT_MODULES, external_rows, name. Outputs/bindings: (none).
Calls/effect boundaries: external_rows.append, name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:173`; AST `c90d34c0c114e5cabebdd9725894af1b06860bcc80293360e919b1a1850595d9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: EFFECT_MODULES, external_rows, name. Outputs/bindings: (none).
Calls/effect boundaries: external_rows.append, name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[6].body[0].value.args[0].values[2].left.value::Call

Source: `infra/agentinfra/roadmap_python.py:174`; AST `b3dec83a02904bd005345bc09fb30cf7950897d72cf03866de759d3a9df59cd9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.split.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].body[0].value.args[0].values[2].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[7]::Assign

Source: `infra/agentinfra/roadmap_python.py:175`; AST `90268365f15b6ae0b87875c402e8b061a7596087978f79cea1d876c64597fc7f`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, external_rows, files, h, hazards, module, sorted. Outputs/bindings: record.
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[7].value.values[2]::Call

Source: `infra/agentinfra/roadmap_python.py:175`; AST `a5616fd6a71280cc0021ec98e0e0aa0aaf2df557f2242b1ce25a206fc8069837`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[7].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[7].value.values[2].keywords[0].value::Lambda

Source: `infra/agentinfra/roadmap_python.py:175`; AST `10552bb4b453c48baad30da0d42657f44c1f0b25d33ce1f7c87527d13f5dd537`.

Rust module: `infra::agentinfra::roadmap_python`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Lambda evaluation at root.body[22].body[7].value.values[2].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[7].value.values[4]::Call

Source: `infra/agentinfra/roadmap_python.py:176`; AST `f0ad58b8ac5451e12007918c6283395ed68776fe3e09a204d6e6ad22dd16ed0f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: h, hazards, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[7].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[7].value.values[4].keywords[0].value::Lambda

Source: `infra/agentinfra/roadmap_python.py:176`; AST `ba6a1776d57d9bb9cc959aab1e7e263d85ce1f4d160eb55064246559189e6100`.

Rust module: `infra::agentinfra::roadmap_python`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: h. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Lambda evaluation at root.body[22].body[7].value.values[4].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[8]::Assign

Source: `infra/agentinfra/roadmap_python.py:179`; AST `2cd571b5f223c91bf0c2b7adc8375639657e29aeb0946de69040a188919c46fd`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[8].value::Call

Source: `infra/agentinfra/roadmap_python.py:179`; AST `459942b3b031c512f2c84b1ead1f069f2c56349cbb6bb8b33eba095d39132ca1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[22].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::module_closure::root.body[22].body[9]::Return

Source: `infra/agentinfra/roadmap_python.py:180`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[22].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:183`; AST `99080d9205d986fe0943e0b5e4c34a385e691003bcc88ab372f2a403b9bb37a4`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _modules, ast, declarations, dict, digest, isinstance, len, module, module_closure, modules, n, record, require, root, separator, str, symbol, target, tree. Outputs/bindings: declarations, module, modules, n, record, separator, symbol, tree.
Calls/effect boundaries: _modules, ast.dump, ast.dump(declarations[0], include_attributes=False).encode, ast.parse, digest, isinstance, len, module_closure, modules[module].read_bytes, record.pop, record.update, require, target.partition.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:184`; AST `1b740c267d12944c01d5e012aa8ad75593b3c4f8b982280f14dd8fac47d2b40f`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:185`; AST `870e022a2b17f2940615955ca541c27a3b8365d737bc0613dadfb01853072ccb`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _modules, root. Outputs/bindings: modules.
Calls/effect boundaries: _modules.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:185`; AST `b70161fc056a2a6204c36ac15bfafbd58c36250373a85baa6edd2cb5471ee3c2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _modules, root. Outputs/bindings: (none).
Calls/effect boundaries: _modules.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:186`; AST `79df4b5d8061ab75c54f01aa59c6daa68365f9bab1b7352ee04ec46c05247811`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: module, separator, symbol.
Calls/effect boundaries: target.partition.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:186`; AST `96b0397a70070dcf485ba63ea78a3d542e84f9a2254fa8a0ba78efdb9a051134`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.partition.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[3]::Expr

Source: `infra/agentinfra/roadmap_python.py:187`; AST `5a26a97b5e9455bbf1ceac7997e42fa2bfe75c45387dcf92e8f7a166068cec13`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: module, modules, require, separator, symbol. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[3].value::Call

Source: `infra/agentinfra/roadmap_python.py:187`; AST `068f3d1eee6ee8974a2a637c405633d6cb76229cb6a47ef01f3b9a5b3bfc2154`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module, modules, require, separator, symbol. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:188`; AST `71722a79cdd639e8f1750180e538f00524416e3d5e50ad45d324e9aa70b2b2bb`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, module, modules. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse, modules[module].read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[4].value::Call

Source: `infra/agentinfra/roadmap_python.py:188`; AST `ef684d19bf2258df692fbc742c443b88c2e33b1e4ecbee1681cb23c9e0e64322`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, module, modules. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, modules[module].read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:188`; AST `5142147f53eb161e573d3b09f9229bba0cb047923dcc5dbe4edd55d8c3213956`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module, modules. Outputs/bindings: (none).
Calls/effect boundaries: modules[module].read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[5]::Assign

Source: `infra/agentinfra/roadmap_python.py:189`; AST `c730245e9f1fcc229c455e90de9d3092fce60e3b2772a91388d8f1601a0676d0`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, symbol, tree. Outputs/bindings: declarations, n.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[5].value::ListComp

Source: `infra/agentinfra/roadmap_python.py:189`; AST `743891da556a17bcd914836497cd8a2bc8f5fc87d4609755077848dde6cee84f`.

Rust module: `infra::agentinfra::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, symbol, tree. Outputs/bindings: n.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[23].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[5].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:189`; AST `1bfd0947f77036bd703871e082921a90106285abdb2ea9bec9d2bc7c3e176b43`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[5].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[6]::Expr

Source: `infra/agentinfra/roadmap_python.py:190`; AST `b29250e32c68ab3af2e6e013f10b1b8773b6b0a52ca644a1b1946e7fd7256de8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: declarations, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[6].value::Call

Source: `infra/agentinfra/roadmap_python.py:190`; AST `17f292296b74c7b3532234ded026305f086cb4b7c57452b1b8b7ba5c2da6cf31`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: declarations, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[6].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:190`; AST `b6a6fa8bf6202eb2301f64174d501c001767c86365f4548489819a4713e78aa8`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: declarations, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[7]::Assign

Source: `infra/agentinfra/roadmap_python.py:191`; AST `5a8a2cfbbdd3e22bd03615a688354f2175930cfeaaa6a48ba0ee2e6781d7be8a`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: module, module_closure, root. Outputs/bindings: record.
Calls/effect boundaries: module_closure.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[7].value::Call

Source: `infra/agentinfra/roadmap_python.py:191`; AST `e5b423e6120ca286cf155874375210dced80c42599449276941d05c067ab43a7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module, module_closure, root. Outputs/bindings: (none).
Calls/effect boundaries: module_closure.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[8]::Expr

Source: `infra/agentinfra/roadmap_python.py:192`; AST `1a2c48e82537ff77025ea14dfc8ba44b084a210de3f87480aab8e05451b44078`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.pop.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[8].value::Call

Source: `infra/agentinfra/roadmap_python.py:192`; AST `c39c8d8abddf1093bdbbc46638f733092039f8051cb687058c468b70e7d62dc6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.pop.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[9]::Expr

Source: `infra/agentinfra/roadmap_python.py:193`; AST `4ff6da901f9b1b4e1d81a9dc02da16e24c66456fbe110a1ee1756bb01bf823dc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, declarations, digest, record, target. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(declarations[0], include_attributes=False).encode, digest, record.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[9].value::Call

Source: `infra/agentinfra/roadmap_python.py:193`; AST `8401d251c9a8daf2cb0f1085188897776582dbed7a6d1b68c07690e62a537e9d`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, declarations, digest, record, target. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(declarations[0], include_attributes=False).encode, digest, record.update.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[9].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:193`; AST `58f1a998539773ff287c34d434f5cf3de6ff7cebe77ebda64dbe50e0dd35007b`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, declarations, digest. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(declarations[0], include_attributes=False).encode, digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[9].value.keywords[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:193`; AST `7f0799cfe04e3f551540ae3efb3357c1765aceb7ae41f7d52a1f280f57e2f8be`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, declarations. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(declarations[0], include_attributes=False).encode.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].value.keywords[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[9].value.keywords[1].value.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_python.py:193`; AST `148db243047fc0596252fdabcea960f0b7d5fb66ab7d7a54f5f8f075a54e5bbd`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, declarations. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].value.keywords[1].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[10]::Assign

Source: `infra/agentinfra/roadmap_python.py:194`; AST `2cd571b5f223c91bf0c2b7adc8375639657e29aeb0946de69040a188919c46fd`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[10].value::Call

Source: `infra/agentinfra/roadmap_python.py:194`; AST `459942b3b031c512f2c84b1ead1f069f2c56349cbb6bb8b33eba095d39132ca1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[23].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::source_closure::root.body[23].body[11]::Return

Source: `infra/agentinfra/roadmap_python.py:195`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[23].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:198`; AST `7e0d814795f8ca16e9191fb1110278e35735321a1026b0b0d43b3fc02bc7ca11`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, archive, bindings_current, c, chapter, chapters, confined_path, dict, digest, disposition, file_binding, len, r, raw, read_json, recommendations, require, root, sorted, zipfile. Outputs/bindings: archive, c, chapter, chapters, disposition, r, raw, recommendations.
Calls/effect boundaries: archive.namelist, archive.read, bindings_current, confined_path, digest, file_binding, len, read_json, require, sorted, zipfile.ZipFile.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:199`; AST `7d7f2f9e954bbdcb3b5083a5d0a478f05abf315c31575bca337809c9ac60bbf0`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: disposition.
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:199`; AST `02b8ff8b48a5022a65e79556a99b980e4aaaefd32deb111cd4d74324b1c3427e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[1]::Expr

Source: `infra/agentinfra/roadmap_python.py:200`; AST `aa5ff7e07f22420bbbd25ae8956d315a1be7deea4dc16342b3ea1d464a615ce8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, disposition, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:200`; AST `138d706ad08395a0b6be6a7d96c508d0c912650b116625fad3b33da129c3ab3d`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, disposition, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:200`; AST `d3f84615954dfda2d9b0733e35612d59734a72c83769baf6595cd3cd0958ca2f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, disposition, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:201`; AST `4e843be16f30baa96a20cc73b371fd6a594e70bd461043e146835d993e707e67`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: disposition. Outputs/bindings: chapters.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3]::With

Source: `infra/agentinfra/roadmap_python.py:202`; AST `eee84c4d8c3e6d3e52889eacea30b665824bb2ffd6034b0507f42919d0fd9d20`.

Rust module: `infra::agentinfra::roadmap_python`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: archive, c, chapter, chapters, confined_path, digest, disposition, len, raw, require, root, sorted, zipfile. Outputs/bindings: archive, c, chapter, raw.
Calls/effect boundaries: archive.namelist, archive.read, confined_path, digest, len, require, sorted, zipfile.ZipFile.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered With evaluation at root.body[24].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_python.py:202`; AST `60a02ce14cc8e7f2404b039ebac36a40e17fe14dfe3a36439d879576d8be4dd2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, disposition, root, zipfile. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, zipfile.ZipFile.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].items[0].context_expr.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:202`; AST `466245728d0ebcb59622c729e9ad1cba79fb3bbfeedb24faa753f4a454084223`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, disposition, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].items[0].context_expr.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:203`; AST `acec9e136829e32db65ea1c29dc8475062684e12ad247b07b3c3e205a072cfa6`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, c, chapters, require, sorted. Outputs/bindings: c.
Calls/effect boundaries: archive.namelist, require, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:203`; AST `a72c7d90e502385851e579be15cb13316c7d913e77e4e7905b8d08868655a1dc`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, c, chapters, require, sorted. Outputs/bindings: c.
Calls/effect boundaries: archive.namelist, require, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:203`; AST `5101e225b5004e9605c7cd9fa0067e8a2dcc7ddddaed2a8b9c73d199f79dc26a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, sorted. Outputs/bindings: (none).
Calls/effect boundaries: archive.namelist, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[0].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:203`; AST `0604e8fe30240315c386fa717f20eb8bc250c5047830b9016717981f5cbd313e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive. Outputs/bindings: (none).
Calls/effect boundaries: archive.namelist.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[0].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_python.py:203`; AST `4208ffdc06e21c01883eacb7c73b8962fc7682519bd9ce8c2062d993b03b8280`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, chapters, sorted. Outputs/bindings: c.
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[0].value.args[0].comparators[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python.py:203`; AST `140eda09a7c75ddcf5f73f2c00af265ef7e3eae8f21206810557497021be7184`.

Rust module: `infra::agentinfra::roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, chapters. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[24].body[3].body[0].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1]::For

Source: `infra/agentinfra/roadmap_python.py:204`; AST `5c1c5b86be44103f8200399f4b6337a55a4316a0e0cb6a740575682b13cb08b9`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: archive, chapter, chapters, digest, len, raw, require. Outputs/bindings: chapter, raw.
Calls/effect boundaries: archive.read, digest, len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[24].body[3].body[1]; no call, error or mutation may be omitted. Iteration: chapter in chapters
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:205`; AST `80e70ac847eb641529308a95f323c68a6ed4d8693a7114d104f0442dc960ac22`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, chapter. Outputs/bindings: raw.
Calls/effect boundaries: archive.read.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:205`; AST `45cd1fafb64d4727969d70a854285b6e1a8421fa8fd79e3d6f62a38beed13cc4`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, chapter. Outputs/bindings: (none).
Calls/effect boundaries: archive.read.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_python.py:206`; AST `1fad4248005160a52d5b5ea2a0e4af928fc9b0a5df21e47a4b2ee0f63e43df2d`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chapter, digest, len, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[3].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:206`; AST `f39f4c544971d5765b4dd8c1d41174acc9e65971db21ecf8e231cdf50d3f70ba`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chapter, digest, len, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:206`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[1].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[3].body[1].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:206`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].body[1].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:207`; AST `0e6ff4324825f99802c5d263ae51d55b054b9ef72d182c85971377bc67d70eb8`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: disposition. Outputs/bindings: recommendations.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[5]::Expr

Source: `infra/agentinfra/roadmap_python.py:208`; AST `f36804c64870d5e95c3051c045a2aaa6b448a7e0f060f8293159476e762479b5`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, r, recommendations, require. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[5].value::Call

Source: `infra/agentinfra/roadmap_python.py:208`; AST `b2be52915390249de8e6564f855cde6f6fbc2ef8a25e0976fe7f6535496ea9d8`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, r, recommendations, require. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[5].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:208`; AST `94b9f1b8bc294d01465971207ff60ab9984ba9fdb4847c741af993cd2b8e4399`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, recommendations. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:208`; AST `bfb318cc176864f1a7e18f73bdd7fccc06cd24959c504119f9c6ce183948c700`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, r, recommendations. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[5].value.args[0].values[1].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_python.py:208`; AST `7f20bf15997805136f4a7a27dbd53bf0a7be7ba1f38cdbc303a346b17d076842`.

Rust module: `infra::agentinfra::roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, recommendations. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered SetComp evaluation at root.body[24].body[5].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[6]::Return

Source: `infra/agentinfra/roadmap_python.py:209`; AST `2dd188dc357d49fcd091af120f85a55df5781695ef8afad83d947648c656a303`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chapters, disposition, file_binding, recommendations, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[24].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::research_sources::root.body[24].body[6].value.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:209`; AST `2d703e6757ac22c692e6e13db445740b713b67942aefcee05b1f9d51a7a7e3fb`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[24].body[6].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:214`; AST `b391e15997970835efc006e6729e8deaea8336e8dd2406f8860d8532061fd07b`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ast, cls, dict, digest, file_binding, isinstance, list, n, node, path, relative, root, row, rows, sorted, tree. Outputs/bindings: cls, n, node, path, relative, row, rows, tree.
Calls/effect boundaries: (root / 'infra/tests').glob, ast.dump, ast.dump(node, include_attributes=False).encode, ast.parse, ast.walk, digest, file_binding, isinstance, node.name.startswith, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, rows.append, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:215`; AST `f314ccd872cf53bab93ba495c5f928b72c8a12c69bf3ffecd7cc5717eee74446`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:220`; AST `ac5dc778d890ac7d3fe32248966b866f064c4894b141595ccc25455eb29f5366`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2]::For

Source: `infra/agentinfra/roadmap_python.py:221`; AST `0ff532732bc90059808f9438bd2af8305dcba232058459f399661fa7644d4ccb`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, cls, digest, file_binding, isinstance, n, node, path, relative, root, row, rows, sorted, tree. Outputs/bindings: cls, n, node, path, relative, row, tree.
Calls/effect boundaries: (root / 'infra/tests').glob, ast.dump, ast.dump(node, include_attributes=False).encode, ast.parse, ast.walk, digest, file_binding, isinstance, node.name.startswith, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, rows.append, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[25].body[2]; no call, error or mutation may be omitted. Iteration: path in sorted((root / 'infra/tests').glob('test*.py'))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].iter::Call

Source: `infra/agentinfra/roadmap_python.py:221`; AST `1696a11350aa24bb1d3fcee22b747d8501081a0538b3169947f173d4195ba9ba`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/tests').glob, sorted.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].iter.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:221`; AST `ba096cd5307fa540b82b6e325ead0970251beaf5c34ecbc24e7cca37813624b7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra/tests').glob.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:222`; AST `c9a5d02444369221b50b662c72fded4efbbded9a1bf01f8bacecd9d7badf680c`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, root. Outputs/bindings: relative.
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:222`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python.py:222`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:223`; AST `660192fc53c6f93e7cfa2feb231162ebf361612b9ccb6a803fc559988dfbfebb`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, path. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:223`; AST `672642bf24fe00484a0ac69002dec258fe1ab1a2a4a56b8f4cd760426642741d`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, path. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:223`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2]::For

Source: `infra/agentinfra/roadmap_python.py:224`; AST `20ae650f5b0e2f0dca83add639a47a90415bd30daf620dc37c2fc4a66fbd36da`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, cls, digest, file_binding, isinstance, n, node, relative, root, row, rows, tree. Outputs/bindings: cls, n, node, row.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, ast.walk, digest, file_binding, isinstance, node.name.startswith, rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[25].body[2].body[2]; no call, error or mutation may be omitted. Iteration: cls in [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].iter::ListComp

Source: `infra/agentinfra/roadmap_python.py:224`; AST `dcf92ea1eb46916909482f96ef8c24d741ccf024bfc50675ef05e7c49778f235`.

Rust module: `infra::agentinfra::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, tree. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[25].body[2].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].iter.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python.py:224`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].iter.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].iter.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python.py:224`; AST `de43fdf9b87001eb0040ffca2ae92940581d5214fd1e73f96f1b4942c9e5ef50`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].iter.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0]::For

Source: `infra/agentinfra/roadmap_python.py:225`; AST `257a287bb16d7e0394fb5701c5d579a9d98d0f02d966b623c697b35176713b74`.

Rust module: `infra::agentinfra::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, cls, digest, file_binding, isinstance, node, relative, root, row, rows. Outputs/bindings: node, row.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest, file_binding, isinstance, node.name.startswith, rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered For evaluation at root.body[25].body[2].body[2].body[0]; no call, error or mutation may be omitted. Iteration: node in cls.body
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_python.py:226`; AST `5da8aae278f3226b07a26fbadc86523b80634a057e26c5a78a5028ca3c3e5f94`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, cls, digest, file_binding, isinstance, node, relative, root, row, rows. Outputs/bindings: row.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest, file_binding, isinstance, node.name.startswith, rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[25].body[2].body[2].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith('test')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:226`; AST `d523540114cb218c0baa8bed353866eefa83eeecc4510dc6dfe4652ce5cc8c32`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:226`; AST `05031cb0c50b15b678336582a445af6d2f8e5cbb12354da0984ff4693187f80f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node. Outputs/bindings: (none).
Calls/effect boundaries: node.name.startswith.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python.py:227`; AST `85a1a9a966dff418067baaff96516afdc47e7e906e9e90381de305e2baae65ed`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, cls, digest, file_binding, node, relative, root. Outputs/bindings: row.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest, file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[2].body[2].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:227`; AST `e8457929e4b469f5fb6798717852b1b34d5ad1a0970999a9e33bb237cecc4b61`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[4]::Call

Source: `infra/agentinfra/roadmap_python.py:229`; AST `7e015840e16c88c823dd5259f4b55423b299ef9fa3c5de015b0073b6888bb2fb`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[4].args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:229`; AST `62642a7f86696182149656fb0833b390cc3f67cf8dd17c2b5151717295dc243e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[4].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_python.py:229`; AST `3fb94b2b8e1dc6a1bc206dc19bca3c2e71190137190d141090f14ace7aaa9d73`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].body[0].value.values[4].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:231`; AST `383a5c9b98019bb2ac19d79f2b2b4b5577ba3d3a64dc396bab8670879c815f6f`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, row. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[2].body[2].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:231`; AST `8765e7e907fad8dd380c79aab2778b538e259bee766146c3a3fa600737969aaf`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, row. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[2]::Expr

Source: `infra/agentinfra/roadmap_python.py:232`; AST `9623b8dff4f8ad8e2932407abc5d704e39c464f8abadd5dd962af1a60f413ae0`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, rows. Outputs/bindings: (none).
Calls/effect boundaries: rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[2].body[2].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[2].body[2].body[0].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:232`; AST `beaefb5e65b631efcc82945814b4162e477628b3023bd19e88f3920d2def0f27`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row, rows. Outputs/bindings: (none).
Calls/effect boundaries: rows.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[2].body[0].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::original_occurrences::root.body[25].body[3]::Return

Source: `infra/agentinfra/roadmap_python.py:233`; AST `e8d62c7bb685945ea0a81e6d4c73e7fe86bcf8b904a9d5c35c30d98b70af7c94`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[25].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:236`; AST `71ecdc3f710654a94e5ff0f3936f9e4c437415fcef855c61d0573df0e44f9bc8`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, candidate, catalog, closure, compiled, dict, inventory, locations, obligation_catalog, original_occurrences, qualification_reports, read_json, research_sources, root, source_closure, source_inventory, str. Outputs/bindings: catalog, closure, locations, source_inventory.
Calls/effect boundaries: inventory, obligation_catalog, original_occurrences, qualification_reports, read_json, research_sources, source_closure.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[26]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_python.py:237`; AST `d2eb98c986c0cb745aea657ee1ec69f9ccd92b0fa8610602759dceed6617d28e`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[26].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[1]::Assign

Source: `infra/agentinfra/roadmap_python.py:238`; AST `0f2bdee81d47f442b04bba6e84f7aee69a41e166a9c5c71d7195bb2fd8580e8e`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, root. Outputs/bindings: source_inventory.
Calls/effect boundaries: inventory.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[1].value::Call

Source: `infra/agentinfra/roadmap_python.py:238`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:239`; AST `cdef9a7c5ea45d7369622f33024a1dec0a146788fd2fc05ba28cedfbb0b15155`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original_occurrences, root. Outputs/bindings: locations.
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:239`; AST `2f2a8691bb8c587e5b7b3386ccf5e1399a670c3bb4db48cca6d6e6121297dba6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original_occurrences, root. Outputs/bindings: (none).
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:240`; AST `2ea8018faaf7260c0a6e66782880f3f601c364ffc98bbde79ee88aab0661a88b`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, compiled, locations, obligation_catalog, root, source_inventory. Outputs/bindings: catalog.
Calls/effect boundaries: obligation_catalog.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[3].value::Call

Source: `infra/agentinfra/roadmap_python.py:240`; AST `cf67dd78ffcfc35102df5dd4c1374324c2c8f1d1a4d088b5a4ab6498034a4235`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, compiled, locations, obligation_catalog, root, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: obligation_catalog.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:241`; AST `7209064fae95bd09f27a46397ff604b352035c12ec662c14c1b71c46a738b8c5`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, source_closure. Outputs/bindings: closure.
Calls/effect boundaries: source_closure.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[4].value::Call

Source: `infra/agentinfra/roadmap_python.py:241`; AST `9541f4c9d8dff7d7ff3112bf1ab4deb4b2305a0241438b75b655ce54f3816385`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[5]::Return

Source: `infra/agentinfra/roadmap_python.py:242`; AST `69d968b0ded492819b47d71eda5c6501793060917aa4d57b8dd23468dbc62258`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, catalog, closure, locations, qualification_reports, read_json, research_sources, root, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: qualification_reports, read_json, research_sources.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[26].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[5].value.values[3]::Call

Source: `infra/agentinfra/roadmap_python.py:243`; AST `d6464c7060dfe7a64deb8729c133d334d56a0a59b60f399c2b2f7ca37c69cec4`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: research_sources, root. Outputs/bindings: (none).
Calls/effect boundaries: research_sources.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[5].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[5].value.values[4]::Call

Source: `infra/agentinfra/roadmap_python.py:243`; AST `62f3cd8f69a1722e90a45ae3013dbfbf37c9dfc848e190da9e6b80375ae86ea1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[5].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::route::root.body[26].body[5].value.values[7]::Call

Source: `infra/agentinfra/roadmap_python.py:244`; AST `986c40247fb90a74f786b8b7a095aba2f46e323f2bbeb20a9e7cd468236b8562`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, catalog, qualification_reports, root. Outputs/bindings: (none).
Calls/effect boundaries: qualification_reports.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[26].body[5].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:256`; AST `7f52fb16b11f563abc8887f2d603b11ad3a5a817a72c80006e9c4eb1465e2c67`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, output, re, run. Outputs/bindings: output.
Calls/effect boundaries: re.search, run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[27]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:257`; AST `e4e0b6deedf4271c30f361d4544dc66abc96fd50376b96dfe12309574d6413a9`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[27].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:258`; AST `0d5737830d5282a4d01691f4efd2c73393fbb677e342f72bfd4e94c78124ec22`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[27].body[1]; no call, error or mutation may be omitted. Condition: run.get('timed_out') or run.get('stdout_truncated') or run.get('stderr_truncated')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[1].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:258`; AST `bf9254dc6751673df54c8c8712c82a283034ab4c8b4a6805fbb0b1729d5e875a`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[1].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:258`; AST `5b731948b6b950a0e7b3c608217c7665a30c59bbf52d5d13a5406bf3844de3c7`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[1].test.values[2]::Call

Source: `infra/agentinfra/roadmap_python.py:258`; AST `314424bb4502375fdd1fc0f147f592abed1ec99e39883f208e17f8d83b18fcf1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:259`; AST `556a6c2b16cda061f3560e9ddd3608b5b104fd7a855a22a53f1fcd4f9b523041`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[27].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:260`; AST `07f218db002279a6c880a297511f3acd78379edb4e548fe098f0a14b6507b84a`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: run. Outputs/bindings: output.
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[27].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[2].value.left.left::Call

Source: `infra/agentinfra/roadmap_python.py:260`; AST `6df5bbe6141d63abe7ef30f663e13a831cc2e4e7049b42f604970ca3fb4f8e96`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].value.left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[2].value.right::Call

Source: `infra/agentinfra/roadmap_python.py:260`; AST `06f12d9f5c50db36ee1b352ebbd4fae1d9afd7de676e9883335584081938bed0`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3]::If

Source: `infra/agentinfra/roadmap_python.py:261`; AST `7333bbfdc7ac52522f6ffee7c77ce7affcb25f6ca1886c68dca39c890d544852`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, re, run. Outputs/bindings: (none).
Calls/effect boundaries: re.search, run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[27].body[3]; no call, error or mutation may be omitted. Condition: re.search('Verification successful[.!]', output) and run.get('returncode') == 0
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3].test.values[0]::Call

Source: `infra/agentinfra/roadmap_python.py:261`; AST `a305d0ed47ea086403a3db0d298c0dd78dfa218e7051fc36f7523460ae53c290`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[3].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:261`; AST `960fde0eb87025060b1e30c49da5835cd28c809c64d675e28ae074fd861900b6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[3].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_python.py:262`; AST `f1620b6e8d5065165fe3c49fe627b16c8be754f42bdda4720d898e0b5cc0edb8`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[27].body[3].body[0]; no call, error or mutation may be omitted. Condition: re.search('(?i)traceback|not supported|unsupported|verification failed|type error', output)
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3].body[0].test::Call

Source: `infra/agentinfra/roadmap_python.py:262`; AST `4d53a3ecaa30b959e82306849502180a629b9b68b5adcc793689716afd9fe982`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[3].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:263`; AST `e51f43788cb8b3ba537907b1e5f3c1ff6eeb0183fe64a84bbffac27c851b6c86`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[27].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[3].body[1]::Return

Source: `infra/agentinfra/roadmap_python.py:264`; AST `6b369e9940c400e5bad8fa1bca2e01043d9b13c314fbd52ea6854d5bbf07cd53`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[27].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[4]::If

Source: `infra/agentinfra/roadmap_python.py:265`; AST `4907c07673419208ea956de4e3566cd397c7d035475fdc281a4f02b30cb832ab`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output, re, run. Outputs/bindings: (none).
Calls/effect boundaries: re.search, run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[27].body[4]; no call, error or mutation may be omitted. Condition: run.get('returncode') not in {None, 0} and re.search('Verification failed[.!]', output) and re.search('assert.failed|assertion.false', output) and (not re.search('(?i)traceback|type error|unsupported', output))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[4].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:265`; AST `960fde0eb87025060b1e30c49da5835cd28c809c64d675e28ae074fd861900b6`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[4].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[4].test.values[1]::Call

Source: `infra/agentinfra/roadmap_python.py:265`; AST `176f078c484d07cca9ea94f09f8a769f75525b4204e8c67d9fb3c7b063479953`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[4].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[4].test.values[2]::Call

Source: `infra/agentinfra/roadmap_python.py:266`; AST `6f63651350dfb5f9a643c4f09e855ce8d6d0095616d9695fed8856cc97f2a99e`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[4].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[4].test.values[3].operand::Call

Source: `infra/agentinfra/roadmap_python.py:266`; AST `b4f5a7bb55246c2d564a53a1e049e9af97a728eeec9345bf27410440a11e9aed`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[27].body[4].test.values[3].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:267`; AST `5a9574abbee5476333995e0d83733c626d6de43e4b3284abd0641caa25273790`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[27].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::classify_nagini::root.body[27].body[5]::Return

Source: `infra/agentinfra/roadmap_python.py:268`; AST `748ee14ae507f0b87f48a733fb5a12910e18cf4935b2787347cbb90abb2949cb`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[27].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28]::FunctionDef

Source: `infra/agentinfra/roadmap_python.py:271`; AST `62ea45067f58ef01de793d42ec6a58a079775886a28f448162dfbbc1fc7c44d3`.

Rust module: `infra::agentinfra::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, b, binding, bindings_current, catalog, confined_path, dict, entry, errors, key, list, next, obligation, qualification, read_json, result, root, str. Outputs/bindings: b, binding, catalog, entry, errors, key, qualification.
Calls/effect boundaries: bindings_current, confined_path, entry.get, errors.append, next, obligation.get, qualification.get, read_json, result.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:272`; AST `890ec8750521b2cfa91438e5d964a7a30c648acd88e2d3048fbc136c3643990d`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[1]::If

Source: `infra/agentinfra/roadmap_python.py:278`; AST `dbb15e0b4a72c07b6d42b1f13d71cc26eb7e93c824e796afda3709be19c1ee98`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[28].body[1]; no call, error or mutation may be omitted. Condition: obligation.get('backend') not in {'nagini', 'esbmc-python', 'deal'}
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_python.py:278`; AST `7614d3295bf703996d9ce200241d4c3f05990802a7977e7ad36d430a69c69148`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:279`; AST `b98d3492e7d9cf3ad08a6755e4ee962ff6b89d6d238688050439ce1c9205f710`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[28].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[2]::Assign

Source: `infra/agentinfra/roadmap_python.py:280`; AST `00c6032e1c62eb566926d672794ef11e0b44cedbc1259207c69b9a8401b67944`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: catalog.
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[2].value::Call

Source: `infra/agentinfra/roadmap_python.py:280`; AST `62f3cd8f69a1722e90a45ae3013dbfbf37c9dfc848e190da9e6b80375ae86ea1`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[3]::Assign

Source: `infra/agentinfra/roadmap_python.py:281`; AST `e38b3deb4197759b501f99ea57eb1687bf38ac1b8701c358becf86253c5b8929`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation. Outputs/bindings: key.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[4]::Assign

Source: `infra/agentinfra/roadmap_python.py:282`; AST `677a2abad77e561c721d7b0bca6d4f9554d4566dc8f3e86dc1d3d3a203e4f6fa`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, catalog, key, next. Outputs/bindings: b, entry.
Calls/effect boundaries: next.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[4].value::Call

Source: `infra/agentinfra/roadmap_python.py:282`; AST `8a2f88645871f17b28e32f89a1887e2a3056eafe9347c3dc6078d33a8f9b0fd9`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, catalog, key, next. Outputs/bindings: b.
Calls/effect boundaries: next.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[4].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python.py:282`; AST `38a9321564233632bdabbcd74f81d9b45894ba32a77ec2fdaf8261c3a5e989dc`.

Rust module: `infra::agentinfra::roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: b, catalog, key. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[28].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[5]::Assign

Source: `infra/agentinfra/roadmap_python.py:283`; AST `77905525b1838757d9a36638b843bc37695d709437ca6ae4dd4e7b7ff74949e3`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: errors.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[6]::Assign

Source: `infra/agentinfra/roadmap_python.py:284`; AST `df222e89e24d6d204c98955a7998d85fcd2473bf3ae3dff524b1e57e4f52823e`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: binding.
Calls/effect boundaries: entry.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[6].value::Call

Source: `infra/agentinfra/roadmap_python.py:284`; AST `106559ee0335728488168f25f2711b08269f0a6ee4bde97576a00b0eee6d7452`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[7]::If

Source: `infra/agentinfra/roadmap_python.py:285`; AST `cde911d31e601c13f230efd4c76718d7e2ff23d740fd66fcab58af2d2b671c20`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, bindings_current, entry, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, entry.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[28].body[7]; no call, error or mutation may be omitted. Condition: entry.get('status') != 'QUALIFIED' or not binding or (not bindings_current(root, [binding]))
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[7].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:285`; AST `d5d807e1d0b6c641342078867592654f37dca2bc8415720808fa246351a5b339`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[7].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[7].test.values[2].operand::Call

Source: `infra/agentinfra/roadmap_python.py:285`; AST `c257a7f2655cc69270fda2c99acf98c4ac7884fc49d5a5eefb6440b2a4ebcecb`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[7].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_python.py:286`; AST `ad37c5fc732b06beb1ad6aa0275fec62e3b8cfd44e86db0b5ca722af5f75ebc1`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[28].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[8]::Assign

Source: `infra/agentinfra/roadmap_python.py:287`; AST `d1062fb79d0257b3ddc16aeb16ac1d7b91052939ad830679205c1dc42c88a916`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, confined_path, read_json, root. Outputs/bindings: qualification.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[8].value::Call

Source: `infra/agentinfra/roadmap_python.py:287`; AST `781ed7c69901254e631e8887a4f061f9d90e073a5136e5b4001231bf8ac0a69f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[8].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python.py:287`; AST `3cff76a4f8621efeac41053a9b6ce3e8ef8e5f85141b5ec2ef8724821ea6b41f`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[9]::Expr

Source: `infra/agentinfra/roadmap_python.py:290`; AST `c808b3a282aaa85b640e801fa6668eddb041eafb272255d702727135adfee218`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[9].value::Call

Source: `infra/agentinfra/roadmap_python.py:290`; AST `13239d799d40280d9dd8f3bd30044367a64669261b2e0408a36b3bfc84d7b9dc`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[10]::If

Source: `infra/agentinfra/roadmap_python.py:291`; AST `36de3dbca066c53fef8a4a799984b0a82b0ec626ddb405a15d38b6f6c91fd660`.

Rust module: `infra::agentinfra::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, errors, obligation, qualification, result. Outputs/bindings: (none).
Calls/effect boundaries: errors.append, obligation.get, qualification.get, result.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered If evaluation at root.body[28].body[10]; no call, error or mutation may be omitted. Condition: result.get('python_qualification') != binding or qualification.get('toolchain') != obligation.get('toolchain')
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[10].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python.py:291`; AST `08140e8097553e580c7e5de2f9c07c57e6fc5eb2400ae1e92d124becaf38daf0`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[10].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[10].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python.py:291`; AST `52b59f12459eb5b89f91c6187620f505bd23f6b12dee837690c336828a1e1ccc`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification. Outputs/bindings: (none).
Calls/effect boundaries: qualification.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[10].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[10].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_python.py:291`; AST `d9d397ce9bd42bcf2277a4e74dc94861dadc48122defb9f7da381097d891184c`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[10].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_python.py:292`; AST `cc68871a454739c3864ab65153570fc81c0935a4f684be480f0f4f33cf4c8cfa`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_python.py:292`; AST `816c69a8ea4717b4f67cdfadabd4175d09666bcc542839cec5a55869f0eade44`.

Rust module: `infra::agentinfra::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[28].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python.py::module::python_proof_errors::root.body[28].body[11]::Return

Source: `infra/agentinfra/roadmap_python.py:293`; AST `95659ec2764e1068e57db3e38e5a541ca59148b7402bfb0198a0ccf386555978`.

Rust module: `infra::agentinfra::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, importlib.util, pathlib, re, roadmap_portability, roadmap_python_catalog, roadmap_records, security, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[28].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
