# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 432. Inventory digest: `f0c060b0f9727976de20e38c617a988d68eb36c9662ab4c0de8ddb63fe536676`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_python_catalog.py::module::root::Module

Source: `infra/agentinfra/roadmap_python_catalog.py:1`; AST `8296681b399fa76f315408c17b0851ab71e3f684c8e4f8d10dfc92354af37345`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, HOOKS, Path, SEMANTIC_FIELDS, _actual_test_details, _node, _role, a, actual, actual_rows, all, any, assertions, ast, attempt, attempts, b, base, binding, bindings, bindings_current, by_id, c, calls, candidate, classes, closure, closures, cls, compiled, contract, contracts, current, declarations, dependencies, details, dict, digest, effects, expected, external_bases, f, field, fields, file_binding, file_bindings, file_obligations, files, fixture, fixture_catalog, fixture_nodes, fixtures, h, helpers, hooks, isinstance, item, key, len, list, local, location, locations, m, matches, method, methods, milestone, module, module_closure, module_hooks, n, node, o, obligation, observations, op, original_ids, p, path, paths, pattern, pending, policy, policy_path, quantifiers, r, read_json, receipt, record, related, relative, require, root, row, rows, runtime_bindings, runtime_dependencies, runtime_receipt, scope, scope_files, seen, selected, set, shared_targets, sorted, source, source_closure, source_files, source_inventory, sources, spec, spec_inputs, status, str, suffix, target, targets, tree, tuple, type, u, unit, units, unresolved, validate_tool_receipt, value, verification_targets. Outputs/bindings: HOOKS, INTERFACE_VERSION, a, actual, actual_rows, assertions, attempt, attempts, b, base, binding, bindings, by_id, c, calls, classes, closure, closures, cls, contract, contracts, current, declarations, dependencies, details, effects, expected, external_bases, f, field, fields, file_bindings, file_obligations, files, fixture, fixture_nodes, fixtures, h, helpers, hooks, item, key, local, location, m, matches, method, methods, milestone, module, module_hooks, n, o, obligation, observations, op, original_ids, p, path, paths, pattern, pending, policy, policy_path, quantifiers, r, receipt, record, related, relative, row, rows, runtime_dependencies, runtime_receipt, scope, scope_files, seen, selected, shared_targets, source, source_files, sources, spec, spec_inputs, status, suffix, target, targets, tree, u, unit, units, unresolved, value, verification_targets.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read, _actual_test_details, _node, _role, a.get, a.get('receipt', {}).get, a['receipt'].get, all, any, ast.dump, ast.dump(node, include_attributes=False).encode, ast.parse, ast.unparse, ast.unparse(n.func).startswith, ast.walk, attempt.get, attempt.get('operation', {}).get, b['path'].endswith, bindings_current, by_id.setdefault, by_id.setdefault(fixture['runtime_id'], []).append, closures.update, compiled['milestones'].items, contracts.items, contracts.values, declarations.items, dependencies.values, details.get, dict, digest, external_bases.append, fields['fixture_setup'].update, fields['fixture_teardown'].update, fields['quantification'].update, file_binding, file_obligations.get, file_obligations.setdefault, file_obligations.setdefault(path, set()).add, fixture_catalog, fixture_nodes.append, fixtures.items, isinstance, len, list, module.replace, module_closure, n.name.startswith, obligation['id'].removeprefix, observations.get, p.is_file, p.relative_to, p.relative_to(root).as_posix, path.read_bytes, path.startswith, pending.extend, pending.pop, policy.get, policy['milestones'].items, read_json, relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, require, root.glob, rows.append, runtime_bindings, seen.add, selected.add, selected.update, set, shared_targets.values, sorted, source_closure, source_files.get, spec.get, spec_inputs.get, type, u['file'].startswith, units.append, unresolved.append, validate_tool_receipt.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:1`; AST `3813b24702aa9a529c74740ed6d8253f2e8dd492d11d2887268908dea4aad3e4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_python_catalog.py:9`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:10`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:12`; AST `1b22542a5d8254b998e802893bd947613e5f7aec9d2b761e4d9d153a42837eb7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:13`; AST `ce3fd1b0a440467dcd26cac5a2dde040752e9433843030db7985d570fff67d9a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:14`; AST `94f2ef7cfe57c7bfab987ff333d99818aa195b2b2e4f09c3d8608a99d87b2cad`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[7]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:17`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::root.body[8]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:18`; AST `3bc612a942d99d61b0b3cec8a54c7697cc5d3e933d36bcf4cb3e0b539bb73a0f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: HOOKS.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:21`; AST `55d60404c1d3222d182cc03ed65a8772cdc341f570a433e0e027f331be00e24c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: path.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[0]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:22`; AST `caa3ee4fac724841a21d61eb20e54b04db30e3c196e8189f7ec1f997be169527`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[9].body[0]; no call, error or mutation may be omitted. Condition: path.startswith('infra/tests/')
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[0].test::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:22`; AST `9676bb865bc6787e8f6feece3508c80126e2c6750f0565f1fc5421068148ba64`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:23`; AST `508e4e9c9bce06a12603a5cce83e5068e5082402b476bcf9deed4097f38a1b53`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[1]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:24`; AST `ec166713407b6bc838ea78c28c1e40dcdc833bc44171f2735363dc9fd2bc0a39`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[9].body[1]; no call, error or mutation may be omitted. Condition: path.startswith('verification/roadmap/')
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[1].test::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:24`; AST `de0f12eeed3398b959e1633c27364a8e9877f6d6982ddeb6bfb0ff6b59e7b881`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:25`; AST `227f52c1fa52cc16284fb883098fde35d91072590d4cd688595ff87936e766da`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[9].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_role::root.body[9].body[2]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:26`; AST `1aa1f6ffc16a1ddb1bfbbe08713242cb2fd5feac050a6565a6ad3f083ea8f75b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:29`; AST `79da7d5d20708b872871330418be223d2e3b036d4547ccf532e47835bda2ce56`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ast, dict, digest, isinstance, node, record, type. Outputs/bindings: record.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, ast.unparse, digest, isinstance, type.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:30`; AST `de41dd42df1f4a8b224ff608620a324f7d142bd2a81cc0e696c1bbd012228f61`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, digest, node, type. Outputs/bindings: record.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest, type.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[0].value.values[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:30`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[0].value.values[2]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:31`; AST `7e015840e16c88c823dd5259f4b55423b299ef9fa3c5de015b0073b6888bb2fb`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[0].value.values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:31`; AST `62642a7f86696182149656fb0833b390cc3f67cf8dd17c2b5151717295dc243e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[0].value.values[2].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:31`; AST `3fb94b2b8e1dc6a1bc206dc19bca3c2e71190137190d141090f14ace7aaa9d73`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value.values[2].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[1]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:32`; AST `d71429501c272e436a6654a646ce1530b2aad6cd6e97107c85a0a6e417c08b99`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, isinstance, node, record. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[10].body[1]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[1].test::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:32`; AST `03f4d863af03611234c7247b6ee125dada11915164b7ebf16339435bb5a26fde`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:33`; AST `5e1239e16b5b10ea3935d81719413b2370b5e23fff240140e13bfcf578011327`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[1].orelse[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:35`; AST `48d9a503372df21c9ff0bf2d705b25ba7237e1eadb8b1c931d3019fbf1e8b710`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, node, record. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[1].orelse[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:35`; AST `4cd8f7dced90f779b836dc9a2d0b8689c57e72589b1542deeab922967aa0e075`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_node::root.body[10].body[2]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:36`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:39`; AST `463695b564efa8c616949d55c67471d3c6ea3a134e257fe60343092ece25746a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: HOOKS, Path, SEMANTIC_FIELDS, _node, a, any, assertions, ast, base, bindings_current, c, calls, classes, closure, closures, cls, current, dict, digest, effects, external_bases, field, fields, fixture_nodes, h, helpers, hooks, isinstance, key, len, list, local, location, locations, matches, method, methods, module, module_closure, module_hooks, n, op, path, pending, quantifiers, record, relative, require, root, rows, seen, set, sorted, sources, tree, tuple, unresolved. Outputs/bindings: a, assertions, base, c, calls, classes, closure, closures, cls, current, effects, external_bases, field, fields, fixture_nodes, h, helpers, hooks, key, local, location, matches, method, methods, module, module_hooks, n, op, path, pending, quantifiers, record, relative, rows, seen, sources, tree, unresolved.
Calls/effect boundaries: _node, any, ast.dump, ast.parse, ast.unparse, ast.unparse(n.func).startswith, ast.walk, bindings_current, digest, external_bases.append, fields['fixture_setup'].update, fields['fixture_teardown'].update, fields['quantification'].update, fixture_nodes.append, isinstance, len, module_closure, n.name.startswith, path.read_bytes, pending.extend, pending.pop, relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, require, seen.add, set, sorted, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:40`; AST `12f40e907ab6e9ef931a3a083cb32795164b525bd8e183076258067770a9daf0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:45`; AST `5922fbd2d8201e16f2cef3195df86d357fee1c8da48ae7c1b33e49e47a853715`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: closures, rows, sources.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:46`; AST `7de1d7a9a999bb6ef4e59665bf7ae6c4a79f95e9184c21a5637c622a9a0659b1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: HOOKS, SEMANTIC_FIELDS, _node, a, any, assertions, ast, base, bindings_current, c, calls, classes, closure, closures, cls, current, digest, effects, external_bases, field, fields, fixture_nodes, h, helpers, hooks, isinstance, key, len, local, location, locations, matches, method, methods, module, module_closure, module_hooks, n, op, path, pending, quantifiers, record, relative, require, root, rows, seen, set, sorted, sources, tree, unresolved. Outputs/bindings: a, assertions, base, c, calls, classes, closure, cls, current, effects, external_bases, field, fields, fixture_nodes, h, helpers, hooks, key, local, location, matches, method, methods, module, module_hooks, n, op, path, pending, quantifiers, record, relative, seen, tree, unresolved.
Calls/effect boundaries: _node, any, ast.dump, ast.parse, ast.unparse, ast.unparse(n.func).startswith, ast.walk, bindings_current, digest, external_bases.append, fields['fixture_setup'].update, fields['fixture_teardown'].update, fields['quantification'].update, fixture_nodes.append, isinstance, len, module_closure, n.name.startswith, path.read_bytes, pending.extend, pending.pop, relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, require, seen.add, set, sorted, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[11].body[2]; no call, error or mutation may be omitted. Iteration: location in locations
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:47`; AST `e7594743e05560c834429bc379a8d3cbcd410e92008b00878d05a0b5802731f4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: location. Outputs/bindings: relative.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:48`; AST `f330b09edc339bb478a4604ecc62c652796482fa772edc70288b4cbe9984a61b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, bindings_current, closure, closures, location, module, module_closure, path, relative, require, root, sources, tree. Outputs/bindings: closure, module, path, tree.
Calls/effect boundaries: ast.parse, bindings_current, module_closure, path.read_bytes, relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[1]; no call, error or mutation may be omitted. Condition: relative not in sources
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:49`; AST `6736d7161a223eeaf58b4df3ee62d8b279c980b361e1ba0cd0a93776b192c6aa`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, location, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:49`; AST `c6873cdc375bdafc987e35f8d7a5c1cc4adb70823e242467023e4b155c7ac007`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, location, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:49`; AST `8cf11dd7696ace1ffe5cbe3ee4f81a7678c22b2c20aa71f85974f2c5e9680d7e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, location, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:50`; AST `bb688c43f012bbb11b1830790cf9c34ff05e96895b8bc56fab2f2105b53129fa`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, root. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:51`; AST `909a958acdb48960e264f6ff9cb988dd15d6c33b44b31b3a14a16eba4a7a95c7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, path, relative. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:51`; AST `67537485f475d118833b444d0c543289a0b717cd6e77cfec6a7f66c408daf6ad`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, path, relative. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, path.read_bytes.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:51`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[3]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:52`; AST `daefad1eef791c12c50e8591f413e638f9ef46fbeed1d50c5794b9615befe06b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative. Outputs/bindings: module.
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:52`; AST `e3c8b31c01d6b2ad919a14880c57828c45197b694f381dae31ed1a40f4e7444c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:52`; AST `5e4a206b58cdebe0a9f3cfbe3c42e661cc3f31899c470277746612dadeb7b375`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[3].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:52`; AST `76236f9e85124a22ccddc476b067cc0b599d2cd22a783bfbc51362afb76de198`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[3].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[4]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:53`; AST `a089f093bdc65538484be20170b830e42856797226c46e5472cf1dd54dc12007`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: module, module_closure, root. Outputs/bindings: closure.
Calls/effect boundaries: module_closure.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[4].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:53`; AST `19dcbe56cf4c2ea9ae42883bb87029694138e46145fd726e23464793ff199a98`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module, module_closure, root. Outputs/bindings: (none).
Calls/effect boundaries: module_closure.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[5]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:54`; AST `65d7f63825d4f54826379635c49853500ae2bd07358b0e9ca750dab4ee010e83`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: closure, closures. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[1].body[6]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:55`; AST `532362393f7176622667c3ed1fcb4ccfd81874e699beb8b1b016c46af49dd9a3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: closure, relative, sources, tree. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[2]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:56`; AST `7605d8404ce7f3102e4d5186b411b92782e177b90716b156a6e674437a57736f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, sources. Outputs/bindings: closure, tree.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[3]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:57`; AST `c59add41c44b776d2b09b6dc8d57bb24b6e360b9a4f627439deca20e768d5cde`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, tree. Outputs/bindings: classes, n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[3].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:57`; AST `dcf92ea1eb46916909482f96ef8c24d741ccf024bfc50675ef05e7c49778f235`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, tree. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[3].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:57`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[3].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[3].value.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:57`; AST `de43fdf9b87001eb0040ffca2ae92940581d5214fd1e73f96f1b4942c9e5ef50`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[3].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[4]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:58`; AST `9186988d9b4196e7a4fac6d86da544088651798fae63c7341a52b8b35d0abd89`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, classes, cls, isinstance, location, method. Outputs/bindings: cls, matches, method.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[4].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:58`; AST `0d4759dca93fbbb3dc57fd5e73ec252ff6fff8d556257ff84738c15faba24d1e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, classes, cls, isinstance, location, method. Outputs/bindings: cls, method.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[4].value.generators[1].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:59`; AST `1c2b56f7acf401765c9dff0488372c7c4ea7e9cc4f9f4cf61c7011b6bce840af`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, method. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[4].value.generators[1].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[5]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:61`; AST `cc3e57b5f3ea5f9a0cb93935f818c59fce7bf9a9e1f0105d95115b356d630aab`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[5].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:61`; AST `8e3afe9f31e526e8ed18c62393752c07f168b47b91bdbc4943deada8b5ea6cb4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:61`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[6]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:62`; AST `4fdd0714e9f5759b04a46a504efa7a5319f3272c53f4781c4c78c6ef8d4a72f5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches. Outputs/bindings: cls, method.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[7]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:63`; AST `0db2f30a77875d77a3c0b96839841822cc4a4c4284757f16fb9b607a4d022c27`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, location, method, require. Outputs/bindings: (none).
Calls/effect boundaries: _node, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[7].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:63`; AST `d5bf4e4b635852e9af4bccbad32a0bafb6c5c801a8ded94dfba0b1c98cbfecef`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, location, method, require. Outputs/bindings: (none).
Calls/effect boundaries: _node, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[7].value.args[0].left.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:63`; AST `851af9f30699a758fe3f9c907fcd8b09713011e6535dc0ddeb81afbbe1a8b9af`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, method. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[7].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[8]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:64`; AST `07638634f5b5b69691a6206d1007d3c4fd17d491362ee90ba26c95c3e2ac6258`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: external_bases, fixture_nodes, pending, unresolved.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[9]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:65`; AST `fde76ccb6e703aceb55911cba8e9aa7c43527f31cdcf5a70cd4497e4d6ea1d92`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: seen.
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[9].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:65`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10]::While

Source: `infra/agentinfra/roadmap_python_catalog.py:66`; AST `7390b452970983a10a595fc79defb0e9d43475fee26e1359643aff1e4b246512`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: ast, base, c, classes, current, external_bases, fixture_nodes, isinstance, key, len, local, pending, seen, unresolved. Outputs/bindings: base, c, current, key, local.
Calls/effect boundaries: ast.unparse, external_bases.append, fixture_nodes.append, isinstance, len, pending.extend, pending.pop, seen.add, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered While evaluation at root.body[11].body[2].body[10]; no call, error or mutation may be omitted. Condition: pending
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:67`; AST `c8e071253eee689aae835b493fd4422d56b5011d087902d49656988285295fb9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending. Outputs/bindings: current.
Calls/effect boundaries: pending.pop.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:67`; AST `b59b504ea575e0473ea0b5cc17902585c9dde56c94712f38bdafbec0ce738e98`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.pop.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:68`; AST `541af6f77a8dad1121775cb33cc7d77ec18b0e714f50bdac9bceacc79d2e6358`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current. Outputs/bindings: key.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[2]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:69`; AST `c26e32fd548892d710dcad964a94b33abd43eec75ad60d2b6f1a2266891549d8`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: key, seen. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[10].body[2]; no call, error or mutation may be omitted. Condition: key in seen
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[2].body[0]::Continue

Source: `infra/agentinfra/roadmap_python_catalog.py:70`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Continue evaluation at root.body[11].body[2].body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[3]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:71`; AST `d22693deda34a0162a49b3c5707b3d36ad5dbd298b1426cfde942eddb5205d3b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[3].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:71`; AST `09a23fdc00a32b9cb9beee691bfac3e436189f9f0e75cbd75174d497f025afb8`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[4]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:72`; AST `b7942bbfc4e692372c3e060ca9a1c3e56b42b4dd88ab4a086b1aec1a1ff13794`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, fixture_nodes. Outputs/bindings: (none).
Calls/effect boundaries: fixture_nodes.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[4].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:72`; AST `4d5da00bf17fc30dbc77bee88f5b9187ba32213deaaebdfa802cadde1c506cfe`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, fixture_nodes. Outputs/bindings: (none).
Calls/effect boundaries: fixture_nodes.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:73`; AST `89a8416614fcdf6e3d8c62ad71417e972c9bfd43d4a65e2b5e506d1e09735459`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, base, c, classes, current, external_bases, isinstance, len, local, pending, unresolved. Outputs/bindings: base, c, local.
Calls/effect boundaries: ast.unparse, external_bases.append, isinstance, len, pending.extend, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[11].body[2].body[10].body[5]; no call, error or mutation may be omitted. Iteration: base in current.bases
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:74`; AST `a24d000d1d81bcb043b010c63c3404641ad8a9ab99394227f73e42f8b1449cfc`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, base, c, classes, isinstance. Outputs/bindings: c, local.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[10].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:74`; AST `91b9c70e10c52ed6a8880467eb5c2deae60f1d29a189f658a55a622393c1416e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, base, c, classes, isinstance. Outputs/bindings: c.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[10].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[0].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:74`; AST `63d0392b32ad0154dfe382feaf2f87a0548489e88f1c183dcf0a94d5b38e383d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, base, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[0].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:75`; AST `3e400b857bc153d676f127dbf45608067711a3ec3a263c52ea9849d09dd88cc7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, base, external_bases, len, local, pending, unresolved. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, external_bases.append, len, pending.extend, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[10].body[5].body[1]; no call, error or mutation may be omitted. Condition: local
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:76`; AST `93a71d827b9877ecf322a24b93b16727d7946c81426d08523e3b4837b87d965c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: local, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.extend.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[10].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:76`; AST `78c43b7799b2369ac6a389c1ca3cbccb45f3ed95ee8ac212b304f5f85395c7f9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: local, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.extend.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:77`; AST `4ceab60e17ce46fc7226e845b39334ca2f6fd022a272053a273daf4120d9fe2f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, base, len, local, unresolved. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, len, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[10].body[5].body[1].body[1]; no call, error or mutation may be omitted. Condition: len(local) != 1
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:77`; AST `6a23297ed5c5f90695896851846cdf390cfa808fbefae4847d80f6d083c94392`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, local. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[1].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:78`; AST `5da79aa261e2206713c6710385a4ffa97d0c3dc9c1c561a985542a0f36c50860`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, base, unresolved. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[10].body[5].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:78`; AST `f307625ad706d47838698d0923fd3ad457243b2d46ef28fd3744bf0dbe644a2c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, base, unresolved. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, unresolved.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].body[1].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:78`; AST `cff6ced96c9b5623f50b58b7b7755ac331d83f6529fd77ec3c2c61705ec8ca8a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, base. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[1].body[1].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].orelse[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:80`; AST `3c22f86d14cde31e2c1423df0efa7b29191da8036c308501a68f9939740113a7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, base, external_bases. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, external_bases.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[10].body[5].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].orelse[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:80`; AST `b0ad5bf856a9598dc6bc4d55ecb2166d0ae270ff194abedc9c82322046fe2a0f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, base, external_bases. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, external_bases.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[1].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[10].body[5].body[1].orelse[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:80`; AST `cff6ced96c9b5623f50b58b7b7755ac331d83f6529fd77ec3c2c61705ec8ca8a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, base. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[10].body[5].body[1].orelse[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[11]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:81`; AST `a2e0007275e725298923ef01cce4c908986154f0d7951fc08ecb61e7249d69b7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, c, fixture_nodes, isinstance, n. Outputs/bindings: c, methods, n.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[11].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:81`; AST `e160dcce1ed690bab4567cdf83c4fe33970ca0c978ad7a40511a5cd60dfb2bce`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, c, fixture_nodes, isinstance, n. Outputs/bindings: c, n.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[11].value.generators[1].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:81`; AST `d04c558a279b937a8a228f5bac6bda16ba2c5c46a43b366517972268ef09bb4f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[11].value.generators[1].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[12]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:82`; AST `abca6c0297b6458ee60fb887325d65417ef727d954d4d3935e7ab8b2f6c014fb`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, method, n, sorted. Outputs/bindings: calls, n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[12].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:82`; AST `0d40c8fefd9c408b9ae4dc9ae612f620aa5401c8a3a9f1af81f643dfb55466fd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, method, n, sorted. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[12].value.args[0]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:82`; AST `a333f6a61d7585041b1190799e31079c838e398a39e7f494774bcae196d4e3d6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, method, n. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[12].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:82`; AST `a23776d2296b4907600c9826b41aad7f84cfc4ec1c12c9696d61786d6a7bb862`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[12].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[12].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:82`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[12].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[12].value.keywords[0].value::Lambda

Source: `infra/agentinfra/roadmap_python_catalog.py:82`; AST `def9d8e23df01c3e551609cca87883fff5619986750efd836759596d4048d097`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: n. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Lambda evaluation at root.body[11].body[2].body[12].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:83`; AST `220384a0734e33568e4d66b7c2d67ce5743ecf842db5b59a5433068094adbf0f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: assertions, n.
Calls/effect boundaries: _node, ast.unparse, ast.unparse(n.func).startswith, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:83`; AST `064ba2153a69820157074112c736e5854c21143f646645670f1446539d7982ce`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: n.
Calls/effect boundaries: _node, ast.unparse, ast.unparse(n.func).startswith, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:83`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:83`; AST `a23776d2296b4907600c9826b41aad7f84cfc4ec1c12c9696d61786d6a7bb862`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:83`; AST `ec459fe7660e2311b9d6374445e99c314277891140df6f9795bcc3affd02ce37`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:83`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[1].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:84`; AST `edd19603f660a98cd70e9215c82e1cbfc488a0f9aefed24eaca147e199016db4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse, ast.unparse(n.func).startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[1].values[0].func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:84`; AST `d37398c81d3e6778e173e0fabe4b6a4f1ccdff3685fe8d32f06e0aa03e719370`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[1].values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[1].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:84`; AST `d37398c81d3e6778e173e0fabe4b6a4f1ccdff3685fe8d32f06e0aa03e719370`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[13].value.generators[0].ifs[0].values[1].values[1].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:85`; AST `5db5562500805172da36b1abefc9709fa2690234fee456cbd72a077aab4ec50f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: n, quantifiers.
Calls/effect boundaries: _node, ast.unparse, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:85`; AST `c31cf05032f867f16df7b3e697a1c1601e9d1a8b4d776bc8a14e6e830dcd4791`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: n.
Calls/effect boundaries: _node, ast.unparse, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:85`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[14].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:85`; AST `a23776d2296b4907600c9826b41aad7f84cfc4ec1c12c9696d61786d6a7bb862`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[14].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:85`; AST `bf2b50adf8e1899934b08847176f39db03f458fcef1135417fdaa8110c163601`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[14].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14].value.generators[0].ifs[0].values[1].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:86`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[14].value.generators[0].ifs[0].values[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[14].value.generators[0].ifs[0].values[1].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:86`; AST `d37398c81d3e6778e173e0fabe4b6a4f1ccdff3685fe8d32f06e0aa03e719370`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[14].value.generators[0].ifs[0].values[1].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[15]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:87`; AST `fdd3903a0324ff8bce830923b6bca7d76a28c7a4985ad2f6c43d42d255d735ff`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: effects, n.
Calls/effect boundaries: _node, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[15].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:87`; AST `e31455a18ec44e5420348c0022be641fd2f15ca06515529933c31d2ba84d103c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: n.
Calls/effect boundaries: _node, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[15].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:87`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[15].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[15].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:87`; AST `a23776d2296b4907600c9826b41aad7f84cfc4ec1c12c9696d61786d6a7bb862`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[15].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[15].value.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:87`; AST `b0c1eb756d7600e1bcb9cecd1cb554b93d36517fd2cab028d53059b0be7a4283`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[15].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[16]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:88`; AST `1cd4b9c8b826c06491a576be6ca7a854cca195e83a5d8dd19fffa44854530364`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: HOOKS, _node, methods, n. Outputs/bindings: hooks, n.
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[16].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:88`; AST `eb47a1689075e09dfdbbbcb0fcc2aad4d911187c102ecec4513b4def57399b1a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: HOOKS, _node, methods, n. Outputs/bindings: n.
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[16].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:88`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[16].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[17]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:89`; AST `eea11ea4b94b0486b97f8e9d586d399f33ab22266cc2407c00ce5359b1c526ba`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: HOOKS, _node, methods, n. Outputs/bindings: helpers, n.
Calls/effect boundaries: _node, n.name.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[17].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:89`; AST `c31b3d5caff8be05e186212b6d7e09bd4ff70b31686003110e098c7437d7ba62`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: HOOKS, _node, methods, n. Outputs/bindings: n.
Calls/effect boundaries: _node, n.name.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[17].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:89`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[17].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[17].value.generators[0].ifs[0].values[0].operand::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:89`; AST `d237e13467bcd227720fb2d601d24e409c368f85845e0283a5704be5af7808b1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: n. Outputs/bindings: (none).
Calls/effect boundaries: n.name.startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[17].value.generators[0].ifs[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[18]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:90`; AST `aa8e1596fee564327d18cffd1f0168cb1e40185c784a226e0dfbc5b64cdd3367`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, ast, isinstance, n, tree. Outputs/bindings: module_hooks, n.
Calls/effect boundaries: _node, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[18].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:90`; AST `7e36378aa7780fc24601c7e2e07073b9c55435c49883fda3129037700a335e71`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, ast, isinstance, n, tree. Outputs/bindings: n.
Calls/effect boundaries: _node, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[18].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:90`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[18].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[18].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:90`; AST `d04c558a279b937a8a228f5bac6bda16ba2c5c46a43b366517972268ef09bb4f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[18].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[19]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:91`; AST `df054d7f12f17bc0989aac836a4aa36c1dc7baa611f57c62920ff3e05d393364`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SEMANTIC_FIELDS, field, location. Outputs/bindings: field, fields.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[19].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:91`; AST `bf311e8188493cc5ad90e090db521249ae0e7fbb26da8dc8f137031f2f5fd094`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: SEMANTIC_FIELDS, field, location. Outputs/bindings: field.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[2].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[20]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:93`; AST `2f8cd01b7b8dbf44a7c7ea87eabeed73893d0b625862f7c2920491b2e8ead924`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, h, hooks, module_hooks. Outputs/bindings: h.
Calls/effect boundaries: fields['fixture_setup'].update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[20].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:93`; AST `8d0890f3fa4211bebcef4765696e4beb8b5fc0ad3a62c3a6c81a94120f591848`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, h, hooks, module_hooks. Outputs/bindings: h.
Calls/effect boundaries: fields['fixture_setup'].update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[20].value.keywords[0].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:93`; AST `b5bd1f461d66be981e5ec47838ec9c4c3a9ec1ac65ed9b106932ab1e04ce3759`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: h, hooks. Outputs/bindings: h.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[20].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[21]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:94`; AST `f37fd57dbeaf43094417a85c51da0ed6539de64596d05f712512f7b6e40c7120`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, h, hooks, module_hooks. Outputs/bindings: h.
Calls/effect boundaries: fields['fixture_teardown'].update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[21].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:94`; AST `e43002a07f1ad0ae0364454bb5088b7b2119341d80f30eadfac1eb67263bb07d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, h, hooks, module_hooks. Outputs/bindings: h.
Calls/effect boundaries: fields['fixture_teardown'].update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[21].value.keywords[0].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:94`; AST `96c5ec3f356e469fb59872f9edbd91f76d97d1bcb1ec7e4a6a61ab5f729c19e6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: h, hooks. Outputs/bindings: h.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[21].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[22]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:95`; AST `892cce3391d44f8e683946be22a76555224490da547eec2e99b866c09d286f3b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, helpers. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[23]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:96`; AST `dd5129128309794e662c3d5488042c04577f64c6ed9cf70d9ee358d0ac8ff591`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, calls, fields, n. Outputs/bindings: n.
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[23].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:96`; AST `ec56f56dc76c48a2f21d9852a406e58093ff51255adefe75dfdcd441e70232c2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, calls, n. Outputs/bindings: n.
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[23].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:96`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[23].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[24]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:97`; AST `fdd91fb12765f61f7cc2e6557188ec2b2b8fa478e53c4d47b65e68158d1f5c46`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertions, fields. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[25]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:98`; AST `f8e5186a295872e528e61616306920284b1f72b1dfc95b98c5e8e0038a700dad`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, quantifiers. Outputs/bindings: (none).
Calls/effect boundaries: fields['quantification'].update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[25].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:98`; AST `508100520d5f9d5ce19da32db042f228448e3aedbefc52edf30c40ece18e6af6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, quantifiers. Outputs/bindings: (none).
Calls/effect boundaries: fields['quantification'].update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[26]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:99`; AST `e8de2a846f0fe41570f82c8a409500ce53c2008f85dcf20f1998743df5ca2b00`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: effects, fields. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[26]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[27]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:100`; AST `acb77e640d3faac2c048f7acf5f7042f9f5b23f7f55d911ddaceb6b7293b96d1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, a, assertions, ast, fields, isinstance, method, n. Outputs/bindings: a, n.
Calls/effect boundaries: _node, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[27]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[27].value.left::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:100`; AST `482c486a9028d03d2756992918f9817a6628d8d730346fdbffd985fd70275d86`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, assertions. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[27].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[27].value.right::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:100`; AST `fb9b2f4ad415513aaf29755402c0d5270d723d4c77ee67f5fefdd792289d0be0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, ast, isinstance, method, n. Outputs/bindings: n.
Calls/effect boundaries: _node, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[27].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[27].value.right.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:100`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[27].value.right.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[27].value.right.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:100`; AST `a23776d2296b4907600c9826b41aad7f84cfc4ec1c12c9696d61786d6a7bb862`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[27].value.right.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[27].value.right.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:100`; AST `f1d58581931a56e640411cc291ba1549fd974d87a449b63ab365ec886b57a20b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[27].value.right.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[28]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:101`; AST `3e09c2316ccec3255c92e3a61b8bbfafbe5bf58f28bda15f6f4aa8f89b9f6d77`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, assertions, fields. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[28].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:101`; AST `cd8a26183cc59221e99da875f5e8d904a056648ee2d86bd35952c8e5db731191`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, assertions. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[29]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:102`; AST `cb66b1c05be28e16a383478cdd1e4d321ac8cc5b01821e09f8fa3cc366446bd1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, cls, fields, method, n. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[29]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[29].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:102`; AST `b1e779f4acf4f5b7d88ad656dde855117e82fd6bc32dd602d1a88d7fc51844ea`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, cls, method, n. Outputs/bindings: n.
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[29].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:102`; AST `2b61e5decfd609e82d91ed65f92b014a281c19986d2bb625356b5e6a69a6ec6e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.unparse.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[29].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `44a705714048d6bfaaf03edfc159f14915b51ed74b805af7423ad98d60d63dcb`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, any, ast, fields, isinstance, method, n, op. Outputs/bindings: n, op.
Calls/effect boundaries: _node, any, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[30]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `6ae70aa79a559d2911eca3578fd4caac4559ccf117a24d58808a8c7f8965f388`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, any, ast, isinstance, method, n, op. Outputs/bindings: n, op.
Calls/effect boundaries: _node, any, ast.walk, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[30].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value.elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[30].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `a23776d2296b4907600c9826b41aad7f84cfc4ec1c12c9696d61786d6a7bb862`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[30].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value.generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `11852503a8defa23d358c7b191a957a1efa4a298b44d19d6b81bc9b050dad5f3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[30].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value.generators[0].ifs[0].values[1]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `370436d4cfebef9b19bbb673ef1b6cb355d87b7cb05e8d0a0f27d788f738f4a5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, ast, isinstance, n, op. Outputs/bindings: op.
Calls/effect boundaries: any, isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[30].value.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value.generators[0].ifs[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `e5031d94fcb75dd272419694f79b240b10292fce601a6470d36d27a091a9d0f3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: ast, isinstance, n, op. Outputs/bindings: op.
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[2].body[30].value.generators[0].ifs[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[30].value.generators[0].ifs[0].values[1].args[0].elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:103`; AST `5c7d5773769fe9c439d09cbe27fb993516312a47775995bfd73c0c28978cc3e0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, op. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[30].value.generators[0].ifs[0].values[1].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[31]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:104`; AST `c3f3b20d44e2fa18712480274cd1ca447ad43d8a73e2bda69351307a45c5dd9c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, fields, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[31]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[31].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:104`; AST `c86f7cd32e74ede7563a1b84c99414bebcad84e24224a00461d920771a7fe27a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, method. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[31].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[32]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:105`; AST `544df5ead642c60c9c2add79481ce8fd0ed2d4155140258d1f98ffd5a212104d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[32]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:106`; AST `50557a70328adc202b3e678669cfd99ede841083959f484b5f34749152a33326`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _node, closure, cls, external_bases, fields, fixture_nodes, location, method, n, relative, set, sorted, unresolved. Outputs/bindings: n, record.
Calls/effect boundaries: _node, relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace, set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[33]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[3]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:107`; AST `a945692abbbc339c8e2a0b7f4b00c7ae213860d137498c1775f6eaad1172ec02`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _node, fixture_nodes, n, sorted. Outputs/bindings: n.
Calls/effect boundaries: _node, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[33].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[3].elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:107`; AST `ff405372acb9c3c8716db6104edc01a70e7e4625aad9c8394d7c45d961b3cd90`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _node, n. Outputs/bindings: (none).
Calls/effect boundaries: _node.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[3].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[3].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:107`; AST `91d1f363cf7ef86ede2552ed6940e6ccdd01632de988e90fa466ea5aa5d41a6e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture_nodes, n, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[3].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[3].generators[0].iter.keywords[0].value::Lambda

Source: `infra/agentinfra/roadmap_python_catalog.py:107`; AST `fc257e7843757ad5b0159710869edb55b268d980c19040cf7fe3ceaf324ff968`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: n. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Lambda evaluation at root.body[11].body[2].body[33].value.values[3].generators[0].iter.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[4]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:108`; AST `879e6d1236eacc453b843919eed9cb859bca2afa1a2eaf2cd401e1e8472276ab`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: external_bases, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[4].args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:108`; AST `30e986608ebe2a2f664c29948c6056ecfc38e9bc7e9e4b64fbadf67a69f0fcde`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: external_bases, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[7].left.left.left.left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:109`; AST `e3c8b31c01d6b2ad919a14880c57828c45197b694f381dae31ed1a40f4e7444c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix, relative.removeprefix('infra/tests/').removesuffix('.py').replace.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[7].left.left.left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[7].left.left.left.left.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:109`; AST `5e4a206b58cdebe0a9f3cfbe3c42e661cc3f31899c470277746612dadeb7b375`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix, relative.removeprefix('infra/tests/').removesuffix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[7].left.left.left.left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[33].value.values[7].left.left.left.left.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:109`; AST `76236f9e85124a22ccddc476b067cc0b599d2cd22a783bfbc51362afb76de198`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative. Outputs/bindings: (none).
Calls/effect boundaries: relative.removeprefix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[33].value.values[7].left.left.left.left.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[34]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:111`; AST `2cd571b5f223c91bf0c2b7adc8375639657e29aeb0946de69040a188919c46fd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[34]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[34].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:111`; AST `459942b3b031c512f2c84b1ead1f069f2c56349cbb6bb8b33eba095d39132ca1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[34].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[2].body[35]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:112`; AST `8c5ada080498885be0881fdbb5ec8b0886a26463f4c4e29c64e07433120223ce`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: location, record, rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[35]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::fixture_catalog::root.body[11].body[3]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:113`; AST `4c430762259e323786432040dcf07f7ed516acda46ab1659ada97cc7f5da04ef`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: closures, rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:116`; AST `3b8d3e2a60753c2e38dbbd95b83141e012de291e5290a4dac2841affd512b8c0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, actual, actual_rows, b, bindings_current, by_id, details, dict, fixture, fixtures, key, len, observations, r, require, root, rows, set, sorted, source, source_files, status. Outputs/bindings: actual, actual_rows, b, by_id, fixture, key, observations, r, rows, source, source_files, status.
Calls/effect boundaries: bindings_current, by_id.setdefault, by_id.setdefault(fixture['runtime_id'], []).append, details.get, fixtures.items, len, observations.get, require, set, sorted, source_files.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:117`; AST `fc4597f33450008782df58e2c9d81e2a91cbe64ff069ad49d9d3cd29e6c42240`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:118`; AST `a9f9b268866c76c2e98ab6874f0b0d87e8226c185e1940a77deffa2362d7466d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: by_id.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[2]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:119`; AST `add058955156ab616eecc7a7ae3ea24a4e65e73f62b06a486816b45dc3b2322a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: by_id, fixture, fixtures, key. Outputs/bindings: fixture, key.
Calls/effect boundaries: by_id.setdefault, by_id.setdefault(fixture['runtime_id'], []).append, fixtures.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[12].body[2]; no call, error or mutation may be omitted. Iteration: (key, fixture) in fixtures.items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[2].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:119`; AST `a99a41db1c567786c4d9b9d14e898919607e646cbed9c0b1a367e921aedb5951`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:120`; AST `220e3c5cbe30861b1c94c4d40222c7d1016107c40d92c5cea0711562362534f3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, fixture, key. Outputs/bindings: (none).
Calls/effect boundaries: by_id.setdefault, by_id.setdefault(fixture['runtime_id'], []).append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:120`; AST `6344a5f16d61b6de4f6ef9dbd3b73e3b45bdad190c0a142f7f479b111eb97b40`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, fixture, key. Outputs/bindings: (none).
Calls/effect boundaries: by_id.setdefault, by_id.setdefault(fixture['runtime_id'], []).append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[2].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:120`; AST `32629ca9dc51a68e3af36244c8b6ab5e97db8032a98062f56be08c0a82d15c23`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, fixture. Outputs/bindings: (none).
Calls/effect boundaries: by_id.setdefault.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[3]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:121`; AST `e8c450330daaa13fa87d0cfff0367a005880e61b719be4ea74449ae719b1947a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: details. Outputs/bindings: actual_rows.
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[3].value.body::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:121`; AST `ee66e841ab22ec61b1b6306527276221bf19091a091b65a221496b3d91b74eb0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details. Outputs/bindings: (none).
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[4]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:122`; AST `89d190683842cde96e41b62a99d1bb76028dd82065b435347df92f7070e18836`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual_rows, len, r, require. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:122`; AST `de9d6c68bd2a781870a97fb5c0906aa9e67a9a834396ca992c5e4f75a0da199d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual_rows, len, r, require. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:122`; AST `dfe7f0e37a8882c77a836f3ec1a82da35ac18ee24d4332245652f918f27a0195`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual_rows, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[4].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:122`; AST `722bc47293c1038b2fd00c7681e308700936fddf05d83538df38ca0af93c2143`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual_rows, len, r. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[4].value.args[0].comparators[0].args[0]::SetComp

Source: `infra/agentinfra/roadmap_python_catalog.py:122`; AST `24e73150686bc3f616a598beab16e64f8400c2a448105cf488720b862779ecae`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: actual_rows, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[4].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[5]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:123`; AST `d18cca813cfe0b2b005a2cd3725dbdc1a80237c5b7a81fb9fbca76372540dfd8`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual_rows, r. Outputs/bindings: observations, r.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[5].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:123`; AST `5f6756d3b13c4e0ad48fe53104467cd2a4229e7406b149bb5c117c2e4f9147a6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: actual_rows, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[6]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:124`; AST `289db5d4e0cdee9da2758ae4f7577db9a74b668aa939d5d23fe3d85f955b8813`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, details. Outputs/bindings: b, source_files.
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[6].value.body::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:124`; AST `755b1e83df5436c58305f5d6772a4ee3f55d2e5167b1c07a094aae5e9901b296`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: b, details. Outputs/bindings: b.
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[6].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[6].value.body.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:124`; AST `cda68a15f1a7b1e05efc22c9870d6a4cc200025fc19a3dc47e5e597f27bc79a6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details. Outputs/bindings: (none).
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value.body.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[7]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:125`; AST `df4673da866e41173fddde9b63f602bd87c25cde758b62448a23926237b8df16`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:126`; AST `e278d5bd877ab5e24cbd5444f799d6b5cd957e9ed3b621e63043129fbaedb686`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: actual, bindings_current, by_id, fixture, fixtures, key, len, observations, root, rows, source, source_files, status. Outputs/bindings: actual, fixture, key, source, status.
Calls/effect boundaries: bindings_current, fixtures.items, len, observations.get, source_files.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[12].body[8]; no call, error or mutation may be omitted. Iteration: (key, fixture) in fixtures.items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:126`; AST `a99a41db1c567786c4d9b9d14e898919607e646cbed9c0b1a367e921aedb5951`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:127`; AST `efb52b87caae677465d5576fdb5562101675badde9ab9f2d4593d57f2a228c06`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, observations. Outputs/bindings: actual.
Calls/effect boundaries: observations.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:127`; AST `df24979b50071afd80848739064f98c3c53214ee5f40a8ca3d67198fdd91189a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, observations. Outputs/bindings: (none).
Calls/effect boundaries: observations.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:128`; AST `9746cd2fc00f0128674f512a3fb67a90abf47cd78d838322327b7bdb0ec02b39`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture. Outputs/bindings: source.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:129`; AST `dd0184d1ff9918c2e65f57102f7c69bb34c59fd5e543681d7e70d5b6c8db7872`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: actual, bindings_current, by_id, fixture, len, root, source, source_files. Outputs/bindings: status.
Calls/effect boundaries: bindings_current, len, source_files.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[12].body[8].body[2]; no call, error or mutation may be omitted. Condition: len(by_id[fixture['runtime_id']]) != 1
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].test.left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:129`; AST `1aa09602be27aa8aad3bd4630b8b85bd97e22d17b2a2473fc4d93a6fab8afe53`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, fixture, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:130`; AST `b4bdbed0aa8b6aeae027b2a19b21c176d9050c85c985695242a85a2e0a2cb3ce`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:131`; AST `dea249ed6b155b4cc9a4a19db27c71bfec5ecf5f1c423888a93638e9d8806a5f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: actual, bindings_current, root, source, source_files. Outputs/bindings: status.
Calls/effect boundaries: bindings_current, source_files.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[12].body[8].body[2].orelse[0]; no call, error or mutation may be omitted. Condition: source_files.get(source['path']) != source or not bindings_current(root, [source])
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:131`; AST `76f1ba986ea0a1f03984f967edeccb4ee796ceed84b2338e018a766a4be13c17`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, source_files. Outputs/bindings: (none).
Calls/effect boundaries: source_files.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].orelse[0].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:131`; AST `2560b1f55ae492b210a0aee075032822ca6657216c85decee11d03ea96472229`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, source. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].orelse[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:132`; AST `1571fc95e36c9647f8b00e903cfb9ea5b121e59efa235d067e65a0c0eb60637f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[2].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:133`; AST `b887fdff04f9813588eb0d79f1cc3c96291bad7dddbebc06a3415359b2810e1a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: actual. Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[12].body[8].body[2].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: not actual
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:134`; AST `3dbf85ff865359095ddc7a654b177b23b97580be05a008a2ddcb89ca917c75c9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[2].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[2].orelse[0].orelse[0].orelse[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:136`; AST `6754256904eb8216a2353b38593dc75b301994ae32fac3953c0d3dd5b2f2ffa3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual. Outputs/bindings: status.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[2].orelse[0].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[8].body[3]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:137`; AST `c13989d36603e2293ddae7c00d7ff34dbeb695db945e587bc3cce53cbef35355`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, fixture, key, rows, status. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[9]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:139`; AST `2c1165fc4dd9b7d423ce78666bf0ad3d79d762fb8c3d35ada1f048ca839bc9f9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, observations, rows, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[9].value.values[1]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:139`; AST `3b21d863b81083104d582a4c78ff26db81590c9bf353f47dfcb3bbf1559d6c98`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, observations, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[9].value.values[1].args[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:139`; AST `ef670af76b768cfb8b169c82fd7f99d15ee562794bf1d9ff09cea2e9ca3b1261`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observations, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.values[1].args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::runtime_bindings::root.body[12].body[9].value.values[1].args[0].right::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:139`; AST `6890cd9a08554124849c1a279d8455d9ddd8732dd48e21435a6c24ec37f74a9b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.values[1].args[0].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:143`; AST `3eb3e4c3c6bc26f5b86ed808ac518182057b325d13284f4d6079547dc69f564e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, Path, a, any, attempt, attempts, b, binding, bindings, bindings_current, candidate, compiled, dependencies, details, dict, item, len, list, read_json, receipt, require, root, sorted, spec, spec_inputs, str, tuple, validate_tool_receipt. Outputs/bindings: a, attempt, attempts, b, binding, bindings, dependencies, details, item, receipt, spec, spec_inputs.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read, a.get, a.get('receipt', {}).get, a['receipt'].get, any, attempt.get, attempt.get('operation', {}).get, b['path'].endswith, bindings_current, dependencies.values, details.get, len, read_json, require, sorted, spec.get, spec_inputs.get, validate_tool_receipt.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:146`; AST `78e17dfe55d7fc70d3c6757906b88225e0003b67c382d61da76725efabb6f8ae`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_python_catalog.py:147`; AST `a7922dc8a0d82ef86d47d41024c804cc71a8264999535162870e84029b69ce01`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:150`; AST `57d930b4148aa1487ad95cb24787590baf25a0265a19ba5708d86c96624b54c2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, a, candidate, root. Outputs/bindings: a, attempts.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read, a.get, a.get('receipt', {}).get, a['receipt'].get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:150`; AST `567c4493126cd8781400574f3ce425a7739768030111b297d24fc7d7260b9d73`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: BudgetLedger, a, candidate, root. Outputs/bindings: a.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read, a.get, a.get('receipt', {}).get, a['receipt'].get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2].value.generators[0].iter.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:150`; AST `8464410ce9017bb079a82680ac5223945cba4d143cc08077c5f09c00053926d2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2].value.generators[0].iter.value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:150`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.generators[0].iter.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2].value.generators[0].ifs[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:151`; AST `773f4109c37d0b78ca38a6d58d6ed0d94a02395d78b43c74346ab2839e4075e7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get, a.get('receipt', {}).get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.generators[0].ifs[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2].value.generators[0].ifs[0].values[1].left.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:151`; AST `75581b1aaabd6631c6aa3b77866b15238db132ff961d75593a1f4402cb633f27`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.generators[0].ifs[0].values[1].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[2].value.generators[0].ifs[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:151`; AST `0a110b90c57c56387ca420cac9bf155a1ce8fb6028037930d4961e2ce384cd62`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a['receipt'].get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.generators[0].ifs[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[3]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:152`; AST `27f045113b8cf62e564abd394d00c8960ef5111744eb56acef82c674d197083e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: attempts. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[13].body[3]; no call, error or mutation may be omitted. Condition: not attempts
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:153`; AST `e49f608cf330397add69a29a5407d5b249ccad7da6e416e05e2829cd5e52586f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[13].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:154`; AST `fca64ccabe61da402949b4a3c0cc9e3c6cd8080802c5ed535b3344bc78beafd5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempts. Outputs/bindings: attempt.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[5]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:155`; AST `6dfb6cf8a0d9408c581773d599b16675876d164b4f5ced011a440d60c66b1980`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: binding.
Calls/effect boundaries: attempt.get, attempt.get('operation', {}).get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:155`; AST `045eb6db9bff7125a784c2a3a3c951a094a3ec1af2938eb703af032d922981bd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get, attempt.get('operation', {}).get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[5].value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:155`; AST `466051896d4e41d42d5822c25c60cfbbb7ac9f1ff06c930d8c5a32d6501f8708`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:156`; AST `9d41d85adfc5c5ec4d035da19f85c45666e728cd73b9f9a6f78cace51f7b0416`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, bindings_current, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:156`; AST `4c36ff1dc3c7d27e0d563372d27bd0a6744c85008f94bd13f6846ec6c43507ae`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[6].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:156`; AST `c257a7f2655cc69270fda2c99acf98c4ac7884fc49d5a5eefb6440b2a4ebcecb`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[7]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:157`; AST `574c3601ab27c8829eb5e7eaa6e707829ec2f254a22907599de9edc118d352a2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, read_json, root. Outputs/bindings: spec.
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:157`; AST `631a2b1f203d3ae75b408482821ceeb101d5c9c85fc09704908316cf58d8c278`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[8]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:158`; AST `a7c8544ab5579b445c3a3e39b59cd31a61112c89e1032eb2db733af1e436a6f3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, spec. Outputs/bindings: b, spec_inputs.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[8].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:158`; AST `1fb4809b18a48f5005cb479d6c673fd10c0ed0068943cb0d2f8e2d040c8349b8`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: b, spec. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:159`; AST `101dd3af01489f5d0f3c057b96818ad74274f3178822e6ae34a8ebf32ed2965b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, b, bindings_current, candidate, compiled, root, spec, spec_inputs. Outputs/bindings: b.
Calls/effect boundaries: any, bindings_current, spec.get, spec_inputs.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[13].body[9]; no call, error or mutation may be omitted. Condition: spec.get('candidate') != candidate or spec.get('contract_digest') != compiled['digest'] or any((spec_inputs.get(b['path']) != b for b in compiled['inputs'])) or (not bindings_current(root, spec['inputs']))
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:159`; AST `9277db9266c596f21669dd54eaea08d1b865bf9ef61522c68cbe84c2d9d333c6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:159`; AST `b967993284b98105a5aff29caadb9d9a79853cc55d8fdd9e014bd0def4bb2641`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].test.values[2]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:160`; AST `91b627d4a67f725f2ee673a2f149c56c59c5d8fde4be9790378bba6a04549021`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, b, compiled, spec_inputs. Outputs/bindings: b.
Calls/effect boundaries: any, spec_inputs.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].test.values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python_catalog.py:160`; AST `2d36f8cebef72c33d658cc306272e7dfd4c23e51e17a5b0e6aef7f7c60348c98`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: b, compiled, spec_inputs. Outputs/bindings: b.
Calls/effect boundaries: spec_inputs.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[9].test.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].test.values[2].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:160`; AST `435ea2967bab6c84da3dac0668da18f595c7dd61ca34f161e3a3fb2d9e613d5c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, spec_inputs. Outputs/bindings: (none).
Calls/effect boundaries: spec_inputs.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].test.values[2].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].test.values[3].operand::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:160`; AST `a0856e30a6594762ad02849fbd3ead77c8a4913f31e3fa6484db5aa00973fab3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, spec. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].test.values[3].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[9].body[0]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:161`; AST `e49f608cf330397add69a29a5407d5b249ccad7da6e416e05e2829cd5e52586f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[13].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[10]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:162`; AST `0b0cfe67e444feb3ea98473f66c6dca6437bb411f164e959d3669a38edb56e2e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[11]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:163`; AST `47f9e88f64472895f942aece84f3f15fe34455853e6c8e9ff0b8c43802b4b55b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, receipt, require, spec. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[11].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:163`; AST `80f58297f64148c2fd739a66a91f681b4bed4e13313e35e295fbaddbafa8b4bc`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, receipt, require, spec. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[12]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:164`; AST `bea1d513d8c1838e49ba88dfd428bf35ab466966cb7b9988084b513a4d8688fd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, root, spec, validate_tool_receipt. Outputs/bindings: (none).
Calls/effect boundaries: validate_tool_receipt.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[12].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:164`; AST `cfd9db3a38f9f5f522373afe44915146a40759b8c04aa17fc954f81c1c7d843d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, root, spec, validate_tool_receipt. Outputs/bindings: (none).
Calls/effect boundaries: validate_tool_receipt.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[13]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:165`; AST `8e7a27f3aa0973dc7c2a7e6324b9e849e10a877e5eafb136babd6a89390c98f0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, receipt. Outputs/bindings: b, bindings.
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[13].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:165`; AST `f61bdeb22744be21ba923544903e664c1bb2c6e8d925bff82a19f63146b807f9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, receipt. Outputs/bindings: b.
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[13].value.generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:165`; AST `db099b416ce409b0ddef0d0c9665accddf6e7368bf24c487faad035e07c73c72`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[13].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[14]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:166`; AST `428ed84c0b6af90403b53db74873557d30399b2bc4530a6980911d8d48ff7d8f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[14].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:166`; AST `a2d0c52cd4e8a5e4bed86565f881f83de737b3a12219186f3261d961d65b1c0a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[14].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:166`; AST `82943aa53759d5f1ea240a1d7eb297e9420b5430f1a37ff56ffef74ae09196fa`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[14].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[15]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:167`; AST `d7bd069d253d4d936f54f085920eb7c22afd9a0497aea77f1a31f6219afd04e5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings, read_json, root. Outputs/bindings: details.
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[15].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:167`; AST `0a79e79137858c28fbf7ef60046940bbc76add9d378d57e0c62bd33981b49aec`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[16]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:168`; AST `d63a28e86cec9e24de385d96f9860a966b3ce789f23b09c7f245fcca49eb87b7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, details, require. Outputs/bindings: (none).
Calls/effect boundaries: details.get, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[16].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:168`; AST `d37fecedb7551cb70395366b0881dbc5a55a40893acfc3140d4ce2253c5ee896`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, details, require. Outputs/bindings: (none).
Calls/effect boundaries: details.get, require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[16].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:168`; AST `3a51b701e45893ed657b0da354a92b1745d9749d7202a5e0d4d2a3d2a1c0be64`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details. Outputs/bindings: (none).
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[16].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[16].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:168`; AST `0ee6869294b72e11ecc4239c65c8266253c2522b6228afc747ac5282d737bc0a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details. Outputs/bindings: (none).
Calls/effect boundaries: details.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[16].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[17]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:169`; AST `f6f820f164f7c48d160a9f8cfbd27dada1be8722a7c8a2270bce7c051f111de5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dependencies.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[18]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:170`; AST `a59874b6adca634834799227f995e44832e63289f98e169cb779557b9a0c04af`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, dependencies, item, receipt, require. Outputs/bindings: item.
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[13].body[18]; no call, error or mutation may be omitted. Iteration: item in [binding, *receipt['artifacts']]
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[18].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:171`; AST `0dc2300846181a9fdad3f7ece0c8acb9bd21d54f3b42c440882de4bd40d348c8`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, item, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:171`; AST `242b6f3f1cc75d51a4eb80840d5c1e1881d862a821f0f52029d80c6d6d42ac13`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, item, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[18].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:172`; AST `174c267b95a7eb150a910a33ed9321ee2982b76a915a84c6c13bd68282cbf507`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, item. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[19]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:173`; AST `c2cf4f79dee550186f9e5703f8d31855f513fcb572907ad47d3878a072bfb2ef`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, bindings, dependencies, details, sorted. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.values, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[13].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[19].value.elts[2]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:173`; AST `0c92dcc8193e07b01c55fdcfcf6bd8ff73a2776d61096400805fb08b5794c057`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, dependencies, sorted. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.values, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[19].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[19].value.elts[2].args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:173`; AST `1f0a1f8ada8033f507f1e8ac925585718247758ca71aad47f1a6fc11028449fd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[13].body[19].value.elts[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::_actual_test_details::root.body[13].body[19].value.elts[2].keywords[0].value::Lambda

Source: `infra/agentinfra/roadmap_python_catalog.py:173`; AST `10552bb4b453c48baad30da0d42657f44c1f0b25d33ce1f7c87527d13f5dd537`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Lambda evaluation at root.body[13].body[19].value.elts[2].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::test_receipt_dependencies::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:176`; AST `c4380790e2b5cc97c091839f76f5c44d68bc63d1ffefddfb575fe10715a59b67`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _actual_test_details, candidate, compiled, dict, list, root, str. Outputs/bindings: (none).
Calls/effect boundaries: _actual_test_details.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::test_receipt_dependencies::root.body[14].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:177`; AST `55bf8d6d81e933d58ebc7f10dbeb313a4361b2501092fddabe2b267bb523e146`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::test_receipt_dependencies::root.body[14].body[1]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:178`; AST `b2ae5d18806855cd4125e439efb26454cba56d59a2369dd43f1784440f810c21`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _actual_test_details, candidate, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: _actual_test_details.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::test_receipt_dependencies::root.body[14].body[1].value.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:178`; AST `735bc9ab05c8a691d52d5fd6f84275107daf4c87a24a378349337080021b6680`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _actual_test_details, candidate, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: _actual_test_details.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_python_catalog.py:181`; AST `87efb9f19209a5bd990605490536c77481cdae5fc9c569b3978a992ad57930ed`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _actual_test_details, _role, all, b, c, candidate, closures, compiled, contract, contracts, declarations, details, dict, digest, expected, f, file_binding, file_bindings, file_obligations, files, fixture_catalog, fixtures, key, len, list, locations, m, milestone, module, o, obligation, original_ids, p, path, paths, pattern, policy, policy_path, r, read_json, related, relative, require, root, row, rows, runtime_bindings, runtime_dependencies, runtime_receipt, scope, scope_files, selected, set, shared_targets, sorted, source_closure, source_inventory, str, suffix, target, targets, u, unit, units, value, verification_targets. Outputs/bindings: b, c, closures, contract, contracts, declarations, details, expected, f, file_bindings, file_obligations, files, fixtures, key, m, milestone, module, o, obligation, original_ids, p, path, paths, pattern, policy, policy_path, r, related, relative, row, rows, runtime_dependencies, runtime_receipt, scope, scope_files, selected, shared_targets, suffix, target, targets, u, unit, units, value, verification_targets.
Calls/effect boundaries: _actual_test_details, _role, all, closures.update, compiled['milestones'].items, contracts.items, contracts.values, declarations.items, dict, digest, file_binding, file_obligations.get, file_obligations.setdefault, file_obligations.setdefault(path, set()).add, fixture_catalog, fixtures.items, len, list, module.replace, obligation['id'].removeprefix, p.is_file, p.relative_to, p.relative_to(root).as_posix, policy.get, policy['milestones'].items, read_json, require, root.glob, rows.append, runtime_bindings, selected.add, selected.update, set, shared_targets.values, sorted, source_closure, u['file'].startswith, units.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:182`; AST `53618f5097cfad6c99c97155431c93c918ac446c82e7de80ffda05328f954beb`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: policy_path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[1]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:183`; AST `7143092bbc3cccb25a58ade4893031dedc103dda8c5d6720ff076c46866da532`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy_path, read_json, root. Outputs/bindings: policy.
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[1].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:183`; AST `afc9245725092ce976e97407354ff4acb8e24ce6d97df815c214ec1691d49144`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy_path, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[2]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:184`; AST `2f6b266295150b3bed7e381d1e5b0835ad4cc21af21c27d832344ec7b9db05f3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, compiled, m. Outputs/bindings: c, contracts, m.
Calls/effect boundaries: compiled['milestones'].items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[2].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:184`; AST `f44d2d4a7b7f787b9ae862a7024ead8d70e7ecdb344eb5c4bb8db1e8071f1d72`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: c, compiled, m. Outputs/bindings: c, m.
Calls/effect boundaries: compiled['milestones'].items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[2].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:184`; AST `752f4a73b8c3044ae754a3009f757c4e7e03060bdfe02cc0899de4711f3326d6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled. Outputs/bindings: (none).
Calls/effect boundaries: compiled['milestones'].items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[3]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:185`; AST `e7f2d120734469047f344c7765d5d7204d824a3322173f339c563bee2a0209b3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contracts, policy, require, set. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[3].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:185`; AST `fc86861db45880ac55af892331fa221526826a44426fe69938a9ab4f460b0fc4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contracts, policy, require, set. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:185`; AST `4f4917a694d078dcde9a0b2b3f36334ce31176634b9e12cecc4a86db64cf7e07`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:185`; AST `94c9fdfd2a3a54a81ff51947e4c2ca4ed23161118987752d2cb889aa429b14e5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[3].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:185`; AST `84c74cfe8d6d6e09288203902dc607d0705f99caa0d7fa1166ca4a31812a1171`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contracts, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[4]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:186`; AST `921797b82d56aa1f8e09faf2e02f846ab0fcdce027f03d21785e1ee1e4192370`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture_catalog, locations, root. Outputs/bindings: closures, fixtures.
Calls/effect boundaries: fixture_catalog.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[4].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:186`; AST `fcb364079fe7074c0edf206402ebbf72fc8c0d5c89d89806fed3833bf2bb087c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture_catalog, locations, root. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[5]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:187`; AST `e78c8a31b24a47773e979f0c3bfdde5a93d6d1c26ac13114fb00722f1a92a865`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _actual_test_details, candidate, compiled, root. Outputs/bindings: details, runtime_dependencies, runtime_receipt.
Calls/effect boundaries: _actual_test_details.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[5].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:187`; AST `735bc9ab05c8a691d52d5fd6f84275107daf4c87a24a378349337080021b6680`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _actual_test_details, candidate, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: _actual_test_details.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[6]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:188`; AST `fa9636d3d5b8a9eac50680203ea7b1c51f13c693a37874af52960d0365e9d57e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, root, source_closure, target. Outputs/bindings: shared_targets, target.
Calls/effect boundaries: source_closure.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[6].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:188`; AST `721021946063b76dadf063ac7e30609fd41f5831618fb68fce547bd97dca5e9a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: policy, root, source_closure, target. Outputs/bindings: target.
Calls/effect boundaries: source_closure.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[6].value.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:188`; AST `37eafd9fdd3b3f73c61d78db96f74aa01fdaefd3e002058c8d44e8eeb8004ebc`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source_closure, target. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[7]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:189`; AST `829b8ebf5c2f8a5ed49b902d2b2b9a0e0fe2590b8ca8d74b8b0a9bd54ed32a05`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: closures, shared_targets, value. Outputs/bindings: value.
Calls/effect boundaries: closures.update, shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[7].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:189`; AST `b1449151cda6b6735fc9a91545292a6d01b98f4829cae1e03715e32b1654b03b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: closures, shared_targets, value. Outputs/bindings: value.
Calls/effect boundaries: closures.update, shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[7].value.args[0]::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:189`; AST `62eb94f6c036fc3cc7c5e82301e432dda4cbc475b8787c461a2038bda8b08e0a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: shared_targets, value. Outputs/bindings: value.
Calls/effect boundaries: shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[7].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:189`; AST `901d5931952c73958542a21b056d5508842753cef6ebb4e2cd276b10a4f6f51d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared_targets. Outputs/bindings: (none).
Calls/effect boundaries: shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[8]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:190`; AST `6268e60c1ce80b0cec0cc29ff316b412550e99959ead1f0199a53f7e68b4fb39`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, source_inventory. Outputs/bindings: b, file_bindings.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[8].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:190`; AST `49f9dce06d86e6b53774ba540c79b804c786b01b47561c3b903bfeecd3364eda`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: b, source_inventory. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[9]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:191`; AST `33665da6c36e30273ca6be0cc47c1fd947bff52d0e3b01c616a8876f96cc3545`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: scope_files.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:192`; AST `f2ab349e4c7a7ca00432369f8933ec40371e344f3d6616867ae34810e2c3108c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: file_bindings, milestone, module, p, pattern, policy, relative, require, root, scope, scope_files, selected, set. Outputs/bindings: milestone, module, p, pattern, relative, scope, selected.
Calls/effect boundaries: module.replace, p.is_file, p.relative_to, p.relative_to(root).as_posix, policy['milestones'].items, require, root.glob, selected.add, selected.update, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[10]; no call, error or mutation may be omitted. Iteration: (milestone, scope) in policy['milestones'].items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:192`; AST `f4e7e43ac23220d5d06f3fe79d7d425f5130e55e00cd9db0073b235afa3bdf80`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy['milestones'].items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:193`; AST `4c2122a8558936951780f95e675d564c5a3c1b4506332af27d697b0499e6fca8`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: selected.
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:193`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:194`; AST `06269d6acd6750132881e6fddd118e4b6b5abca485639889904d91519c05b17c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: file_bindings, module, relative, require, scope, selected. Outputs/bindings: module, relative.
Calls/effect boundaries: module.replace, require, selected.add.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[10].body[1]; no call, error or mutation may be omitted. Iteration: module in scope['production_modules']
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:195`; AST `5f5cfd53b3fe4a7d0206e7642d3b9aa6fb2f41d30f807d24de06bedcc9f41965`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: module. Outputs/bindings: relative.
Calls/effect boundaries: module.replace.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[0].value.left.right::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:195`; AST `e88e703772b75004eb4954cf71620439fc214359c4f038620546880320a2365f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: module. Outputs/bindings: (none).
Calls/effect boundaries: module.replace.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[1].body[0].value.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_python_catalog.py:196`; AST `44aa65c3c92ac9942e3c3b6d8ad99f99ce92f9b2a7b6c5c6a2db70f7ec2da350`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: module. Outputs/bindings: relative.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered If evaluation at root.body[15].body[10].body[1].body[1]; no call, error or mutation may be omitted. Condition: module == 'agentinfra'
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:197`; AST `6e1d008379e74d3ce1c9cb3a3d7b2b791e416c4dc307d5608a0c1c80bec85942`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: relative.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:198`; AST `5954db7ac101855296eb39156f2ae8455bf4f4085fff961844e5cb44523233cd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_bindings, module, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:198`; AST `af0c7742023b451e8e1ac929a361597ed062fe1def14049f45ccd5f95b94e306`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_bindings, module, relative, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:199`; AST `5c1fa3344c42172f7de49770e82681dbb801b7c77b0d5fed33e64053af2ba2fa`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:199`; AST `becb53e6e275fb7aee84901d742a80950ba77cad4b6346a275b140ae8efe34f2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:200`; AST `bb12f409782860432c8621f132526372253df8dfcc4dd807f57b79d544bb09dc`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: file_bindings, p, pattern, root, scope, selected. Outputs/bindings: p, pattern.
Calls/effect boundaries: p.is_file, p.relative_to, p.relative_to(root).as_posix, root.glob, selected.update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[10].body[2]; no call, error or mutation may be omitted. Iteration: pattern in scope['maintained_source_patterns']
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `63b24911c31d0e829de6ad5d23159dab66499c265d50fd05dd8cea72ef37b52b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_bindings, p, pattern, root, selected. Outputs/bindings: p.
Calls/effect boundaries: p.is_file, p.relative_to, p.relative_to(root).as_posix, root.glob, selected.update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `2647e88a63c71e7896841d8f80906d0312555db4feaf371d998d64d186ebddd7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_bindings, p, pattern, root, selected. Outputs/bindings: p.
Calls/effect boundaries: p.is_file, p.relative_to, p.relative_to(root).as_posix, root.glob, selected.update.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `18d3966b0b97eba2a22323a505f25b57507237a3d2ecf6c2fd0233a29a8037e6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: file_bindings, p, pattern, root. Outputs/bindings: p.
Calls/effect boundaries: p.is_file, p.relative_to, p.relative_to(root).as_posix, root.glob.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[10].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0].elt.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value.args[0].elt.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `259c59db5f2f06edc0bbd00d8d9e1098ac333049b126b4450815db1c45cac849`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pattern, root. Outputs/bindings: (none).
Calls/effect boundaries: root.glob.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0].generators[0].ifs[0].values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value.args[0].generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0].generators[0].ifs[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value.args[0].generators[0].ifs[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[2].body[0].value.args[0].generators[0].ifs[0].values[1].left.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:201`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].value.args[0].generators[0].ifs[0].values[1].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[10].body[3]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:202`; AST `25c2968aaed2c88627fb1bfe6c415944526ff4442f3bea5a959957af360f7f08`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: milestone, scope_files, selected. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[11]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:203`; AST `ac5dc778d890ac7d3fe32248966b866f064c4894b141595ccc25455eb29f5366`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:204`; AST `80108af9f6bac2bba21ab0dc1add0d4a8fff24cfb8366e073ea1e92d25ad0232`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _role, b, c, closures, contract, contracts, dict, digest, f, file_bindings, files, fixtures, key, list, milestone, obligation, original_ids, p, policy, require, rows, scope_files, shared_targets, sorted, source_inventory, suffix, targets, u. Outputs/bindings: b, c, contract, f, files, key, milestone, obligation, original_ids, p, suffix, targets, u.
Calls/effect boundaries: _role, contracts.items, dict, digest, fixtures.items, list, obligation['id'].removeprefix, require, rows.append, shared_targets.values, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[12]; no call, error or mutation may be omitted. Iteration: (milestone, contract) in contracts.items()
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:204`; AST `194cbbafb8658fc92174f260adc20a0927247172cf511fb63942c34126fea87d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contracts. Outputs/bindings: (none).
Calls/effect boundaries: contracts.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:205`; AST `36c9bc2185c0ad22a7935963c80586a52143814e43b08e04af394b7dc3af3106`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _role, b, c, closures, contract, dict, digest, f, file_bindings, files, fixtures, key, list, milestone, obligation, original_ids, p, policy, require, rows, scope_files, shared_targets, sorted, source_inventory, suffix, targets, u. Outputs/bindings: b, c, f, files, key, obligation, original_ids, p, suffix, targets, u.
Calls/effect boundaries: _role, dict, digest, fixtures.items, list, obligation['id'].removeprefix, require, rows.append, shared_targets.values, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[12].body[0]; no call, error or mutation may be omitted. Iteration: obligation in contract['proof_obligations']
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:206`; AST `4f4272189d3ed92b5ad241522f1142a6f0161da3f98346df81041f41c3d4cc3a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: milestone, obligation. Outputs/bindings: suffix.
Calls/effect boundaries: obligation['id'].removeprefix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:206`; AST `bbb68eaa2eefd7678e7c97bd28668f9368c19369b139520d38a651f48db6387f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestone, obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation['id'].removeprefix.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:207`; AST `9290005806fab79d6ee0e3fb0fd9ef7ab102a6c804eccca4acbbd21c71eb4150`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: milestone, require, suffix. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:207`; AST `6703d42447c266e0076c393f347161d0bed47fc86988c458f1944cd60769deac`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestone, require, suffix. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:208`; AST `1dd4df203499b50b6673e6a0c15af26bd88c0c4dcf4f295b3dbd38655720b0fc`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, c, milestone, scope_files, shared_targets, suffix. Outputs/bindings: b, c, files.
Calls/effect boundaries: shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[2].value.orelse::SetComp

Source: `infra/agentinfra/roadmap_python_catalog.py:208`; AST `b76103f4e532aa170a120f424aaa81887d262a7462e489d75ce58c5e2326198b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, c, shared_targets. Outputs/bindings: b, c.
Calls/effect boundaries: shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered SetComp evaluation at root.body[15].body[12].body[0].body[2].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[2].value.orelse.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:208`; AST `901d5931952c73958542a21b056d5508842753cef6ebb4e2cd276b10a4f6f51d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared_targets. Outputs/bindings: (none).
Calls/effect boundaries: shared_targets.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[2].value.orelse.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[3]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:209`; AST `2b82f9ae8730412235afb3cf75fcdc9e10fa493d01908ed3860c1d0c11ad3702`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: files, source_inventory, u. Outputs/bindings: targets, u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[3].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:209`; AST `a448621449c73c809b3d0aab6c6449f6459565d625c9ffedfde1d223dd75dace`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: files, source_inventory, u. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[4]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:210`; AST `3526612b8eeb432ad8405d92a222382cd430c93f0f0f1fc4e07dfa73db5a43b9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, closures, f, files, fixtures, key, milestone, suffix. Outputs/bindings: b, f, key, original_ids.
Calls/effect boundaries: fixtures.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[4].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:210`; AST `cbb8f2402e370efd73395ef3787c1ff71e83e2280a405ad12a71118e6a9c776d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, closures, f, files, fixtures, key, milestone, suffix. Outputs/bindings: b, f, key.
Calls/effect boundaries: fixtures.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[4].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:210`; AST `a99a41db1c567786c4d9b9d14e898919607e646cbed9c0b1a367e921aedb5951`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[4].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[4].value.generators[0].ifs[0].values[1].right::SetComp

Source: `infra/agentinfra/roadmap_python_catalog.py:210`; AST `54caf8651a2972ddb755e25d12ce7cb46f2257614e620bb289253eb5840a66ec`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, closures, f. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered SetComp evaluation at root.body[15].body[12].body[0].body[4].value.generators[0].ifs[0].values[1].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:211`; AST `756c2e45b73b56e95af83730841bd9701b0b66b3058ebad108c1b1fbe16a9bd0`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _role, contract, dict, digest, file_bindings, files, list, milestone, obligation, original_ids, p, policy, rows, shared_targets, sorted, suffix, targets, u. Outputs/bindings: p, u.
Calls/effect boundaries: _role, dict, digest, list, rows.append, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:211`; AST `a55b36882a04bc35461ceef88f56e55c98516e2a71fefcd4d44da27c4fb65082`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, contract, dict, digest, file_bindings, files, list, milestone, obligation, original_ids, p, policy, rows, shared_targets, sorted, suffix, targets, u. Outputs/bindings: p, u.
Calls/effect boundaries: _role, dict, digest, list, rows.append, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[5]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:212`; AST `1253f0f07ad69eba5dc7892142a2e1dca56b8de30947ef3013ae84aeb4801584`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[6]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:213`; AST `53d551f8eabf28b1b22096f53ccb767d5600c9bed6e7d66534730d896316ee24`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _role, dict, file_bindings, files, p, sorted. Outputs/bindings: p.
Calls/effect boundaries: _role, dict, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[6].elt::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:213`; AST `d90b6591e73e62990b40cd66eb763e6ec0b4c83380ace5402975314d6c6a497e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, dict, file_bindings, p. Outputs/bindings: (none).
Calls/effect boundaries: _role, dict.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[6].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[6].elt.keywords[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:213`; AST `5be8dcba6f5ecfd15de1da33597edeec70ba1689221bdfceae002af92ab26c43`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, p. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[6].elt.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[6].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:213`; AST `05cb7a0a2a5d8121e7823f0a1fb8c974bc335b007b204b6bd26fdf9a6644637f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[6].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[7]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:214`; AST `47bf3aed017cc2df72dabaeff1557868383b1494706af42e65af6502135c7ed7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _role, file_bindings, files, p, sorted. Outputs/bindings: p.
Calls/effect boundaries: _role, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[7].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:214`; AST `05cb7a0a2a5d8121e7823f0a1fb8c974bc335b007b204b6bd26fdf9a6644637f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[7].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[7].generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:214`; AST `5be8dcba6f5ecfd15de1da33597edeec70ba1689221bdfceae002af92ab26c43`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, p. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[7].generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[8]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:215`; AST `73c5b627d30262a00e94b39eed1289da718470b60797a77ecae631a9adb56ec3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _role, file_bindings, files, p, sorted. Outputs/bindings: p.
Calls/effect boundaries: _role, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[8].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:215`; AST `05cb7a0a2a5d8121e7823f0a1fb8c974bc335b007b204b6bd26fdf9a6644637f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[8].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[8].generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:215`; AST `5be8dcba6f5ecfd15de1da33597edeec70ba1689221bdfceae002af92ab26c43`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, p. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[8].generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[9]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:216`; AST `e00942e4c96db7c31de85f7d4c33b811fb662e19e3f8fc55b8b44c101111b4e1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _role, targets, u. Outputs/bindings: u.
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[9].generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:216`; AST `c6ba34afdb0f94c7ee97b84d5240c5fe8e693d5327b1449c319ccc0dcc5850ef`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, u. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[9].generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[10]::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:217`; AST `2e30947866f89260b86096d348304f1806c5185dc09c8b056cec43397a516ff9`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _role, targets, u. Outputs/bindings: u.
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[10].generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:217`; AST `c6ba34afdb0f94c7ee97b84d5240c5fe8e693d5327b1449c319ccc0dcc5850ef`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, u. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[10].generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[12].body[0].body[5].value.args[0].values[12].body::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:218`; AST `17518ca1ed3ff56624c4e6d238e96dbc735ccd7e0e3024782af5cb906764d7f4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, shared_targets. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].body[5].value.args[0].values[12].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[13]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:223`; AST `4875d1dd54e38d58c311efaa7a33b2af1db4cbfb15d7066cff379bcef636ab61`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: file_obligations.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:224`; AST `8790f8020416e6296d00aadc65faef79e2ff38fb004bc533d5d15e81aed33e17`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: b, file_obligations, fixtures, key, path, paths, row, rows, set. Outputs/bindings: b, key, path, paths, row.
Calls/effect boundaries: file_obligations.setdefault, file_obligations.setdefault(path, set()).add, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[14]; no call, error or mutation may be omitted. Iteration: row in rows
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:225`; AST `fd4379240d358e03c66afde47011410a14b5ff49ed19b7cf64924fc7b5e9cdb4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, fixtures, key, row. Outputs/bindings: b, key, paths.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[0].value.left::SetComp

Source: `infra/agentinfra/roadmap_python_catalog.py:225`; AST `cdd3b91640a4c9766a38d6dd0a484d53c41db9680499007ea1a7776094017dbf`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, row. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered SetComp evaluation at root.body[15].body[14].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[0].value.right::SetComp

Source: `infra/agentinfra/roadmap_python_catalog.py:225`; AST `d75a8bcd25f6c529e8d54e4d7555c217b8158905c1f85423ef6eedc34301a1d5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: fixtures, key, row. Outputs/bindings: key.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered SetComp evaluation at root.body[15].body[14].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[1]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:226`; AST `50827491b627216b313b7c04da471512c096dd42ef93f5579636109fb76ca107`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: file_obligations, path, paths, row, set. Outputs/bindings: path.
Calls/effect boundaries: file_obligations.setdefault, file_obligations.setdefault(path, set()).add, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[14].body[1]; no call, error or mutation may be omitted. Iteration: path in paths
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:227`; AST `e37fea0088a7469f1d82623b830352cd13cd36769873b1ef5b0a55fd8703157a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_obligations, path, row, set. Outputs/bindings: (none).
Calls/effect boundaries: file_obligations.setdefault, file_obligations.setdefault(path, set()).add, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:227`; AST `c0acf46d42ce7a098615f17002561118a86020031ca54a304eac7aa30884057b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_obligations, path, row, set. Outputs/bindings: (none).
Calls/effect boundaries: file_obligations.setdefault, file_obligations.setdefault(path, set()).add, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[1].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:227`; AST `c3ff4a22b7b44a0a649a08bbe35d8e4d6d9c37fd0f2c338d1849f6cb613b51a7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_obligations, path, set. Outputs/bindings: (none).
Calls/effect boundaries: file_obligations.setdefault, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[1].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[14].body[1].body[0].value.func.value.args[1]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:227`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[1].body[0].value.func.value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[15]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:228`; AST `263a15b8cce53eee8cb579999c1dccffacf60ae773eb5753ea991b2a92af637a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: units.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16]::For

Source: `infra/agentinfra/roadmap_python_catalog.py:229`; AST `01d624cd3b529b82a252c13cb0e89ae15693d8fc9cba89ab2e8ccb61d9852fc5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _role, file_obligations, related, require, set, sorted, source_inventory, unit, units. Outputs/bindings: related, unit.
Calls/effect boundaries: _role, file_obligations.get, require, set, sorted, units.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered For evaluation at root.body[15].body[16]; no call, error or mutation may be omitted. Iteration: unit in source_inventory['units']
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:230`; AST `721e3880878471e7d5d1a7cadbb9840bc2409a2795847ef247d73f496ef579de`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_obligations, set, sorted, unit. Outputs/bindings: related.
Calls/effect boundaries: file_obligations.get, set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:230`; AST `69ca3f97851c6c2d4dc22dd47f15ba957c0a5065adffc10964971e0e037948ed`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_obligations, set, sorted, unit. Outputs/bindings: (none).
Calls/effect boundaries: file_obligations.get, set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:230`; AST `468517af327d1ba3a3ab9e1649929f14dc89bdbb188b64074f25a7d534d43c3a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_obligations, set, unit. Outputs/bindings: (none).
Calls/effect boundaries: file_obligations.get, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[16].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[0].value.args[0].args[1]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:230`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[16].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[1]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:231`; AST `77eaa62a97ef26d9829d8534bcca95000c9dfacaa1ecf7f366400a2005722e36`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: related, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[1].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:231`; AST `104215f4d739c9eb36ba9cd6342a28e52f997362316ff7fc1ecd4acd3793c715`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: related, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[2]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:232`; AST `37d5102fe784da47f0f0adaab0788abc2f6110fe8a44d6c12dbdf9edeb113066`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _role, related, unit, units. Outputs/bindings: (none).
Calls/effect boundaries: _role, units.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[2].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:232`; AST `afe3bba3b414504f95106b23c5c29030a2e165bf7a09337ea50a6cbf561cfe63`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, related, unit, units. Outputs/bindings: (none).
Calls/effect boundaries: _role, units.append.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[16].body[2].value.args[0].values[6]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:233`; AST `e1f43631fdfa9fcd6e45f5988994458fa3fca0b151cb94a78d5132c4a1ab5acb`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, unit. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[16].body[2].value.args[0].values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[17]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:235`; AST `808d5be7ac0a166d1dabb81df92aaa297a3873c908aeefdbdef7eb210a7aa86a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _role, file_bindings, len, source_inventory, u. Outputs/bindings: declarations, u.
Calls/effect boundaries: _role, len, u['file'].startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[17].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:235`; AST `1d2bfefce06665b424fbb348e6479031b7afaeaf7826d57d328b23ce9d5ff003`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: _role, file_bindings, len, source_inventory, u. Outputs/bindings: u.
Calls/effect boundaries: _role, len, u['file'].startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[17].value.value.values[3]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:235`; AST `c6ba34afdb0f94c7ee97b84d5240c5fe8e693d5327b1449c319ccc0dcc5850ef`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _role, u. Outputs/bindings: (none).
Calls/effect boundaries: _role.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[17].value.value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[17].value.value.values[7]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:237`; AST `c60c39d072b7c384ddf4295b69a275045ad529085b3893fdd5180968383f7e9c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, u. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[17].value.value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[17].value.generators[0].ifs[0].values[1].operand::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:241`; AST `06c0480e019584c4962f07a1b344390944524f306f06fa91135cbd10e3ee3a9f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: u. Outputs/bindings: (none).
Calls/effect boundaries: u['file'].startswith.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[17].value.generators[0].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[18]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:242`; AST `7c7f844b80442b081f7eccb5f2bfc4427a1af3bd1b42491ff275e6665c03915f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: declarations, key, value. Outputs/bindings: key, targets, value.
Calls/effect boundaries: declarations.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[18].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:242`; AST `74c673259468536b8045b73e15e90575dc6f848822b001388a6609617e541174`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: declarations, key, value. Outputs/bindings: key, value.
Calls/effect boundaries: declarations.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[18].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:242`; AST `01eaf35638ae74a15b5b7c7b018b63a2e9c5e0b3410a9e56be05d58b11136228`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: declarations. Outputs/bindings: (none).
Calls/effect boundaries: declarations.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[18].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[19]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:243`; AST `24c944c44e9c3914417a332a861be5a0f17cc1c62c8d9901868d86738cd4aec7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: declarations, key, value. Outputs/bindings: key, value, verification_targets.
Calls/effect boundaries: declarations.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[19].value::DictComp

Source: `infra/agentinfra/roadmap_python_catalog.py:243`; AST `3104806899eeabe2b8f5834c207cb2de55ad70dce1f934875092c419304b303d`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: declarations, key, value. Outputs/bindings: key, value.
Calls/effect boundaries: declarations.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[19].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:243`; AST `01eaf35638ae74a15b5b7c7b018b63a2e9c5e0b3410a9e56be05d58b11136228`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: declarations. Outputs/bindings: (none).
Calls/effect boundaries: declarations.items.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[19].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[20]::Assign

Source: `infra/agentinfra/roadmap_python_catalog.py:244`; AST `ff70b97ff2ad16e3a4394412f3e99cb8bd975d40673b2b1ca1f467d1429342fd`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, contracts, o. Outputs/bindings: contract, expected, o.
Calls/effect boundaries: contracts.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[20].value::ListComp

Source: `infra/agentinfra/roadmap_python_catalog.py:244`; AST `26a74ddd0397ef3d086a82528fe0adaa69f3be101fdbc45b1ff2641478573878`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: contract, contracts, o. Outputs/bindings: contract, o.
Calls/effect boundaries: contracts.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[20].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:244`; AST `ead2696b3f9b9f68fe7019593bed9e88783f3bb113027c1c5d97340104be159e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contracts. Outputs/bindings: (none).
Calls/effect boundaries: contracts.values.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[20].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `7b726cdaee4760cad94febe5d110bc3f12ff05eb28becf0467fa4d00586b627f`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, len, r, require, rows, set, sorted. Outputs/bindings: r.
Calls/effect boundaries: len, require, set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `460a382fd94d39ac15ec98744ab7b493d8228212d3206dc15f54aa4b020a9389`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len, r, require, rows, set, sorted. Outputs/bindings: r.
Calls/effect boundaries: len, require, set, sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `c2d06b163e3f45e9d7be910cb5ac5a89b21e57724763b4159be61fb15e2f5005`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[21].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `92c7b105ab8208e6c0d99003aa501423395c1925384705c62d883a1c21cf675e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[21].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value.args[0].values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[21].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `ce496e131ed1c30321cd73f9d72367282de4cde60997f5322f3ffdf066b2645a`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[21].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `e59ae0b9bc1ccc6b98738bce5bdcaf5f886a65d8fe9df9c37890583ca5525f94`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, rows, sorted. Outputs/bindings: r.
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[21].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[21].value.args[0].values[2].comparators[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python_catalog.py:245`; AST `8de0d01ce146bdbb123b597fb32be67c88816b3e28e927ab3161373eaa03596e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[21].value.args[0].values[2].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[22]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:247`; AST `b7a3207da45211109028ec27f4e149aadb802e529b8a401823adab0cbf3623f5`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, r, require, rows, set, targets. Outputs/bindings: r.
Calls/effect boundaries: all, require, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[22].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:247`; AST `0ccd8df6c226ad24148cdfef773a34bed9ce921c353f85bab8ef34fa6b55e703`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, r, require, rows, set, targets. Outputs/bindings: r.
Calls/effect boundaries: all, require, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[22].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:247`; AST `1e73a2073329c3f0e59f5784bf63f0d52b3c14d0442b6b92213884c597839a89`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, r, rows, set, targets. Outputs/bindings: r.
Calls/effect boundaries: all, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[22].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[22].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python_catalog.py:247`; AST `4e026134a9cfde1745b9f6a65c8f666fee8ea741765601e60251d3320b518365`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, rows, set, targets. Outputs/bindings: r.
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[22].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[22].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:247`; AST `28f037d707c936e02d43a08094dc39e5aa5b6d4be7db4aaff6abffd1ecc8932c`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[22].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[22].value.args[0].args[0].elt.comparators[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:247`; AST `8942adca9fcadeb50e227a08d09d2198deda26d90437dff8bd0bda057c14c7d2`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, targets. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[22].value.args[0].args[0].elt.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[23]::Expr

Source: `infra/agentinfra/roadmap_python_catalog.py:248`; AST `0354636ff73c3b71d08adcd7cccea6bd7d0bb6be8965b75a6428822f012c75a4`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, r, require, rows, set, verification_targets. Outputs/bindings: r.
Calls/effect boundaries: all, require, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[23].value::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:248`; AST `4a3127d5c7acd496f3e6ccb95fc6165ab0bb7b38dade1b9c66b2bc74783a4fc6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, r, require, rows, set, verification_targets. Outputs/bindings: r.
Calls/effect boundaries: all, require, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[23].value.args[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:248`; AST `273cc243942c8348cb8b8ee519e47ed2f2b97c2c29fa58092c8caaa4f1e45594`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, r, rows, set, verification_targets. Outputs/bindings: r.
Calls/effect boundaries: all, set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[23].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[23].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_python_catalog.py:248`; AST `6820f7175866b74c6acd0e625a845dce60c6f8517747273cb434789b2f69e7b1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, rows, set, verification_targets. Outputs/bindings: r.
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[23].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[23].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:248`; AST `79800a1fca8c974ef65a6010acf12c14f98c47bb22a8361530eac0c8a22064d1`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[23].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[23].value.args[0].args[0].elt.comparators[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:248`; AST `0b069f28bf69a6c5f104b3616a137811420766cba520ebb5a6488f14dff442b3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, verification_targets. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[23].value.args[0].args[0].elt.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[24]::Return

Source: `infra/agentinfra/roadmap_python_catalog.py:249`; AST `76cb7d2af9cd4a853018b83323919e1c7483ced53b01958193f29a94525e806e`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: closures, details, file_binding, fixtures, policy_path, root, rows, runtime_bindings, runtime_dependencies, runtime_receipt, targets, units, verification_targets. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, runtime_bindings.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Return evaluation at root.body[15].body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[24].value.values[0]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:249`; AST `204b89cb9b4a277fd8acc43fe9c975bae097102940c5eb3e6a0e474fa95dbbf3`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, policy_path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[24].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_python_catalog.py::module::obligation_catalog::root.body[15].body[24].value.values[9]::Call

Source: `infra/agentinfra/roadmap_python_catalog.py:253`; AST `8c004f620786695cacd9935f98e00a08ca2d72dcd5c6455ba898f3b449a59df6`.

Rust module: `infra::agentinfra::roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details, fixtures, root, runtime_bindings. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, ast, pathlib, roadmap_policy, roadmap_python, roadmap_records, roadmap_runtime, roadmap_work.

Invariants: Preserve ordered Call evaluation at root.body[15].body[24].value.values[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
