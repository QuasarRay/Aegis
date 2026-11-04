# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 280. Inventory digest: `ca1aeb860eb8cc17333e3ea5a824c64df40b64acf2920237bd106e4104d7d31d`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_acceptance.py::module::root::Module

Source: `infra/agentinfra/roadmap_acceptance.py:1`; AST `abba2c8bb9aeb85f3f803ca383b4ee738191651fcc73fff4c7ebb6a71b6e8763`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, GitInventory, Path, ProjectAdapter, _assemble, _immutable, _unique, a, adapter, all, all_inputs, any, artifacts, attempts, audit, audit_evidence, b, base, baseline, bind_goal, binding, bindings, bindings_current, bool, by_path, candidate, case, check, commit, common, compare_interfaces, compatibility, compatibility_binding, compile_roadmaps, compiled, compiled_binding, complete_current, confined_path, contract, current, current_success, dict, digest, disposition, dispositions, entry, evidence, evidence_binding, execution, expected, file_binding, gate, generated, generation, git, history, interfaces, inventory, isinstance, item, k, list, m, mapping, migration_bindings, migration_index, milestone, n, name, names, native, native_binding, next, observe_interfaces, observed, originals, originals_binding, owner, p, partial, passing, path, prior_binding, qualify_execution, r, read_json, receipt, receipts, require, review, review_binding, review_path, reviewed_artifacts, root, run, runs, scope, selected, selected_work_milestones, set, sorted, spec, str, test_details, tests, through, unchanged_originals, validate_compatibility_disposition, validate_record, validate_tool_receipt. Outputs/bindings: INTERFACE_VERSION, _, a, adapter, all_inputs, attempts, audit, b, base, binding, by_path, candidate, case, commit, common, compatibility, compatibility_binding, compiled, compiled_binding, contract, current, disposition, dispositions, entry, evidence, evidence_binding, execution, expected, gate, generated, generation, git, history, interfaces, item, k, m, mapping, migration_bindings, migration_index, milestone, n, name, names, native, native_binding, observed, originals, originals_binding, owner, p, partial, passing, path, prior_binding, r, receipt, receipts, review, review_binding, reviewed_artifacts, root, run, runs, scope, selected, spec, test_details, tests.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read, GitInventory, ProjectAdapter, _assemble, _immutable, _unique, adapter.profile.path, adapter.profile.path().read_bytes, adapter.read, adapter.update, all, any, artifacts, audit_evidence, b['path'].endswith, bind_goal, bindings_current, bool, check, compare_interfaces, compile_roadmaps, confined_path, current.get, current_success, dict, dict.fromkeys, digest, dispositions.append, entry['path'].endswith, entry['path'].startswith, execution.get, expected.append, file_binding, git.blob, git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline + '^{commit}').strip, git.tree, history.append, inventory, isinstance, item.get, list, next, observe_interfaces, observed.get, observed['implementation_units'].values, observed['outputs'].values, partial.get, qualify_execution, read_json, receipts.append, require, review.get, reviewed_artifacts.extend, root.resolve, runs.items, runs.values, selected_work_milestones, set, sorted, tests.get, unchanged_originals, validate_compatibility_disposition, validate_record, validate_tool_receipt.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:1`; AST `a35fdcc58eceab5d2b3eabd570e1065b61230d67208b4029c7921ca75bdcd84c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:9`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:11`; AST `35659e841c72c1c95daa9ff298aea04e55736d16fc43d44605e80617df2ed0d7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:12`; AST `636534e2245736b0b6e7173b1574c2c9c9350c49ffeb6396e41cc4d5423b0e2b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:13`; AST `ca9d5a029471fc522b9b57025e634cc805aa2619c361c5db84b63672593768df`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:14`; AST `0fc966ee6b50ec82c02899d679da760b485c6564141d0e00c5c6deb2950693ff`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:15`; AST `3811621fdd2e34bc60f6d4b40253aefa193d7cdd11073d4188d52620c73aa081`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:16`; AST `06018155a23f1f83c82d139847669324993143354a3dd3b3aaf896059cf1187a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:17`; AST `f311a9ccf1409d242c9c82d6a924616e9255b9f1563a36c36a1510d33b803d67`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:18`; AST `78e17dfe55d7fc70d3c6757906b88225e0003b67c382d61da76725efabb6f8ae`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:19`; AST `e9852fcb169ab44c75b6f6ffe1ad4329a1251bcd2b9453fbd2a97abd94a8b49a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[12]::ImportFrom

Source: `infra/agentinfra/roadmap_acceptance.py:20`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::root.body[13]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:23`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_acceptance.py:26`; AST `766c40920e4f9776b7fee35e7e2f747ef9e705fd704833cd1795af110056b3d9`.

Rust module: `infra::agentinfra::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: binding, bindings, by_path, dict, list, p, require, sorted. Outputs/bindings: binding, by_path, p.
Calls/effect boundaries: require, sorted.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:27`; AST `2ef8194491de53856f64ce0c11cc237a2b0a4decc1a8006463dc7c657c12659d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: by_path.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[1]::For

Source: `infra/agentinfra/roadmap_acceptance.py:28`; AST `e23a2cd3d149f8d1176692d4978ab03852eb42aa5989269f9d1541897f50210b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, bindings, by_path, require. Outputs/bindings: binding.
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered For evaluation at root.body[14].body[1]; no call, error or mutation may be omitted. Iteration: binding in bindings
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:29`; AST `3ec671ff7a6cd1983bb9a1088518db70a9e21d8e9d3d21ea2dae16b2de4a4639`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, by_path, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:29`; AST `b4b9b6f4421586689641adff08acb922773f0a54f9b09f33e024d501f1e18735`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, by_path, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:30`; AST `5ab5bfe48193bb75ee11184d17a55291cb4027dc4f6b92162f0e66c202027b93`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, by_path. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[2]::Return

Source: `infra/agentinfra/roadmap_acceptance.py:31`; AST `029538c4e978372a02f1ad3123497372aed6c7dd8b136860990b02ae4feb8c57`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_path, p, sorted. Outputs/bindings: p.
Calls/effect boundaries: sorted.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_acceptance.py:31`; AST `ea8763d979c1f3dc417d1949e7df30f16ac0bce5cf9007a427f31157051ffbd3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: by_path, p, sorted. Outputs/bindings: p.
Calls/effect boundaries: sorted.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ListComp evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_unique::root.body[14].body[2].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_acceptance.py:31`; AST `f83acede9672ff9d2096d2e5fdd56222582bf7c544ffe5d7723bbae64a2c6ae0`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_path, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_acceptance.py:34`; AST `006c4155e7688e875813471377b631d385b60ee93e7698c275f3b1c39ac79b90`.

Rust module: `infra::agentinfra::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GitInventory, Path, baseline, binding, bindings_current, bool, commit, dict, digest, entry, expected, git, require, root, str. Outputs/bindings: binding, commit, entry, expected, git.
Calls/effect boundaries: GitInventory, bindings_current, bool, digest, entry['path'].endswith, entry['path'].startswith, expected.append, git.blob, git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline + '^{commit}').strip, git.tree, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:35`; AST `6be60ecbd9492af5c5dd6b3f753a825879749c93ccb83967aa9f6d22383d5117`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GitInventory, root. Outputs/bindings: git.
Calls/effect boundaries: GitInventory.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:35`; AST `c4f3e6818765e5df9cc7a91d7bfc9093ba441ac55f12b5153bb08ff3dd3b1703`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GitInventory, root. Outputs/bindings: (none).
Calls/effect boundaries: GitInventory.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:36`; AST `5c0f635bdc3b82aac370cc3411eecb0d6b37dd63f05f34a466831a922159a054`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: baseline, git. Outputs/bindings: commit.
Calls/effect boundaries: git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline + '^{commit}').strip.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:36`; AST `56a9422d16413fbd7828ec26f18ebb3d31788e4ba4f0f4b747fbb4ddd45d6f0d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline, git. Outputs/bindings: (none).
Calls/effect boundaries: git.read, git.read('rev-parse', '--verify', '--end-of-options', baseline + '^{commit}').strip.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[1].value.func.value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:36`; AST `def82450416f33d2eda55c094f5564ccc5e7d0451fdb07722ee2a0ececbd00de`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: baseline, git. Outputs/bindings: (none).
Calls/effect boundaries: git.read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[2]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:37`; AST `a949725fe544ef5cf140e8b3b75a375e877da15f1697c674dbf9f0a49b39733f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: expected.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3]::For

Source: `infra/agentinfra/roadmap_acceptance.py:38`; AST `de5f5aba5d1380fbb4e7104b633185811fb9a1f6f9cbc658f6089a1e116be140`.

Rust module: `infra::agentinfra::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, bindings_current, commit, digest, entry, expected, git, require, root. Outputs/bindings: binding, entry.
Calls/effect boundaries: bindings_current, digest, entry['path'].endswith, entry['path'].startswith, expected.append, git.blob, git.tree, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered For evaluation at root.body[15].body[3]; no call, error or mutation may be omitted. Iteration: entry in git.tree(commit)
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].iter::Call

Source: `infra/agentinfra/roadmap_acceptance.py:38`; AST `e951d5d1dae14dca00104331d571822820c46d1bdbd957df66ef6d2f5c4efd2a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commit, git. Outputs/bindings: (none).
Calls/effect boundaries: git.tree.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_acceptance.py:39`; AST `fa795fb8fc46fe895152d9c4bc09a5242a009573a612a676f395f099aa03e25b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, bindings_current, digest, entry, expected, git, require, root. Outputs/bindings: binding.
Calls/effect boundaries: bindings_current, digest, entry['path'].endswith, entry['path'].startswith, expected.append, git.blob, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered If evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted. Condition: entry['path'].startswith('infra/tests/') and entry['path'].endswith('.py')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:39`; AST `af07d81dea7f9916aba22c0b7b99b2e74ad5a23118544cd9c314940bba45087c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry['path'].startswith.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:39`; AST `8abb863a5b1ee69fee160afa4714babc5755aca91161d451a2ad4a895c95a2e5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry['path'].endswith.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:40`; AST `327f34618fccf48f62033458737fd37a45279f96c267af49f800a704efdf0c21`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:40`; AST `d43398dc13d937ddaa6aadcc9dbb2d197f139c7fe5e58d6c8f24bb367e7b93d4`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:41`; AST `61be3a754c357967df364e609d9d0e4e7b225c16b5c9c7ca0a0e1bba931fdd49`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, entry, git. Outputs/bindings: binding.
Calls/effect boundaries: digest, git.blob.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[1].value.values[1]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:41`; AST `02809aa7a8757e72ac979cdcbe68aaacd3e10aaeff654d6f339d7b8fd8fc4939`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, entry, git. Outputs/bindings: (none).
Calls/effect boundaries: digest, git.blob.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[1].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[1].value.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:41`; AST `250dcf5754423bca08c0d557665fe6b4076808045bd1867a32d86332ae2fb305`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, git. Outputs/bindings: (none).
Calls/effect boundaries: git.blob.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[1].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[2]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:42`; AST `61b2c3deb08379d3e55b613332f2339e246059e1f4ae56d5c287ba1ebd4d4ff7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, bindings_current, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:42`; AST `0e1eb848636fa13f080dc04b8cef107fcb51df622c931d1298e4f161137a77a6`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:42`; AST `c257a7f2655cc69270fda2c99acf98c4ac7884fc49d5a5eefb6440b2a4ebcecb`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bindings_current, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[3]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:43`; AST `6ecfef690565b1e6ca65fc0d79bff6793ea0cd03aea0d9913e0c00c8e079c8c0`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, expected. Outputs/bindings: (none).
Calls/effect boundaries: expected.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[3].body[0].body[3].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:43`; AST `68aaaea0bd556b041abace850432fa4b9492f46a9166adb6f4ee1a055c4e103c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, expected. Outputs/bindings: (none).
Calls/effect boundaries: expected.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[4]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:44`; AST `fcd56421ad962b9c6c2c0d2b622833eaeccca749ee0c07176350813e0a764cd8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, expected, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[4].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:44`; AST `1d25e36650de06c22c3bf6f58dd8cf1a735d3179cb4a38bc9d5c610ac8b334d8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, expected, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:44`; AST `8d1d2ee4fa1bf4be7289761f56da64f1412743b10882123358b5a30f31d3762e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, expected. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::unchanged_originals::root.body[15].body[5]::Return

Source: `infra/agentinfra/roadmap_acceptance.py:45`; AST `1876a1502082707e6bf9c5f66087b33861c42634ebc00b5af134ef84c63fdf06`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: commit, expected. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Return evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::assemble_implementation::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap_acceptance.py:48`; AST `99cdb3e7a7b8ed1d21bf9e65ab19187d0868dffd418f61727a6eaafea1a6d83e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _assemble, dict, review_path, root, str, through. Outputs/bindings: (none).
Calls/effect boundaries: _assemble.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::assemble_implementation::root.body[16].body[0]::Return

Source: `infra/agentinfra/roadmap_acceptance.py:49`; AST `e4a2b6f175e2cae9b1ef681b72164fa003351ba93175dffa38d6b484da292135`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _assemble, review_path, root, through. Outputs/bindings: (none).
Calls/effect boundaries: _assemble.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Return evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::assemble_implementation::root.body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:49`; AST `02d94bda76ae74d1b89cf1a217f484d8c0eb7635bf1c8b06e3f49ee15cc02afc`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _assemble, review_path, root, through. Outputs/bindings: (none).
Calls/effect boundaries: _assemble.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::refresh_implementation_dependencies::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_acceptance.py:52`; AST `e26089bc023769e5b493f448059f614a733cf6e984ed0fb300f6852189194b02`.

Rust module: `infra::agentinfra::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _assemble, dict, review_path, root, str, through. Outputs/bindings: (none).
Calls/effect boundaries: _assemble.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::refresh_implementation_dependencies::root.body[17].body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:53`; AST `84042bc4a395ba75d1b694f26b3f796939d62418e67a30b882c34dba99480dc8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::refresh_implementation_dependencies::root.body[17].body[1]::Return

Source: `infra/agentinfra/roadmap_acceptance.py:54`; AST `ad29559dace5d899e6d3b75adb1183d370079d03d94ea0701d5d627dd65f1269`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _assemble, review_path, root, through. Outputs/bindings: (none).
Calls/effect boundaries: _assemble.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::refresh_implementation_dependencies::root.body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:54`; AST `205ccaa41293614d8ef56e94cf1fd822ad9e87bb83aaaf3e9d0d0951430445ed`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _assemble, review_path, root, through. Outputs/bindings: (none).
Calls/effect boundaries: _assemble.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_acceptance.py:57`; AST `9b072aef9c2523a71ac87e08bc507f46922737ab2b31b37fb52001abd5d3122b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, Path, ProjectAdapter, _immutable, _unique, a, adapter, all, all_inputs, any, artifacts, attempts, audit, audit_evidence, b, base, bind_goal, bindings_current, bool, candidate, case, check, common, compare_interfaces, compatibility, compatibility_binding, compile_roadmaps, compiled, compiled_binding, complete_current, confined_path, contract, current, current_success, dict, digest, disposition, dispositions, evidence, evidence_binding, execution, file_binding, gate, generated, generation, history, interfaces, inventory, isinstance, item, k, list, m, mapping, migration_bindings, migration_index, milestone, n, name, names, native, native_binding, next, observe_interfaces, observed, originals, originals_binding, owner, partial, passing, path, prior_binding, qualify_execution, r, read_json, receipt, receipts, require, review, review_binding, review_path, reviewed_artifacts, root, run, runs, scope, selected, selected_work_milestones, set, spec, str, test_details, tests, through, unchanged_originals, validate_compatibility_disposition, validate_record, validate_tool_receipt. Outputs/bindings: _, a, adapter, all_inputs, attempts, audit, b, base, candidate, case, common, compatibility, compatibility_binding, compiled, compiled_binding, contract, current, disposition, dispositions, evidence, evidence_binding, execution, gate, generated, generation, history, interfaces, item, k, m, mapping, migration_bindings, migration_index, milestone, n, name, names, native, native_binding, observed, originals, originals_binding, owner, partial, passing, path, prior_binding, r, receipt, receipts, review, review_binding, reviewed_artifacts, root, run, runs, scope, selected, spec, test_details, tests.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read, ProjectAdapter, _immutable, _unique, adapter.profile.path, adapter.profile.path().read_bytes, adapter.read, adapter.update, all, any, artifacts, audit_evidence, b['path'].endswith, bind_goal, bindings_current, bool, check, compare_interfaces, compile_roadmaps, confined_path, current.get, current_success, dict, dict.fromkeys, digest, dispositions.append, execution.get, file_binding, history.append, inventory, isinstance, item.get, list, next, observe_interfaces, observed.get, observed['implementation_units'].values, observed['outputs'].values, partial.get, qualify_execution, read_json, receipts.append, require, review.get, reviewed_artifacts.extend, root.resolve, runs.items, runs.values, selected_work_milestones, set, tests.get, unchanged_originals, validate_compatibility_disposition, validate_record, validate_tool_receipt.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:58`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:58`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:59`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:59`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[2]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:60`; AST `0903c8e0543af79f0dcc2db143222c7f639446c3b806ff4eac4afed1aa1b72cc`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, root. Outputs/bindings: adapter.
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[2].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:60`; AST `a885979b048414ab9ab482a4aaa51e20efe2db175d6aaf5096c07c6e15434558`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[3]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:61`; AST `86f972f909f7202210d3de94b6fed67edaa338c07e78c557335930084da868a4`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: current.
Calls/effect boundaries: adapter.read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[3].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:61`; AST `475d5be5efd9ec4a3dca0b74c9a7534e6fc14081f5396d86007b06bd7a2ef8b1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[4]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:62`; AST `3c46484e30aa460ba871433570319addfe05dee860c923469181a8053ef426b7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, require, through. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[4].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:62`; AST `662ea754b749a9f462559229cb23cf325e75aed657df8c8e0f42b26a830acee6`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, require, through. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[5]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:63`; AST `74a034ca05671387910627824063c543d6ca9dafbef60d266102f1a24c236106`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, qualify_execution, root, through. Outputs/bindings: _, native, owner.
Calls/effect boundaries: qualify_execution.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[5].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:63`; AST `3f331087f3c602123133c3471827c11a828f9a8d230cb297c6fc0e8c4a0fe176`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, qualify_execution, root, through. Outputs/bindings: (none).
Calls/effect boundaries: qualify_execution.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[6]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:64`; AST `d18f91c5ed22701ccf3af3e866e4b488d5d4cfaf354e132adc503021f25c7492`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, root. Outputs/bindings: attempts.
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[6].value.value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:64`; AST `8464410ce9017bb079a82680ac5223945cba4d143cc08077c5f09c00053926d2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger, BudgetLedger(root).read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[6].value.value.func.value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:64`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[7]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:65`; AST `64046e4c573f56ef7bc3e73c566954b2910026a7e0dfef6a07bf7484cf7bc644`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, attempts, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[7].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:65`; AST `3417005b589f7460f5ce8bbf8cba489c9a263f6c77f9a5228af3a7439a2c019f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, attempts, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[7].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_acceptance.py:65`; AST `25c96cb979138392fdf2c2a1b04ca742960967fc7b7db7456eec85614925d23a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, attempts. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[7].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_acceptance.py:65`; AST `6888807d7a92c26844a84ae7ef0f1a3976c04db8422f6566e2cdf131609354f9`.

Rust module: `infra::agentinfra::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, attempts. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[7].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[8]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:66`; AST `44fc79c19a2550b6dae574fb088d3426102b8cf5152382be44640bc99c443f7f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: runs.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[9]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:67`; AST `1f0b5a3d6a71b61d5a54ca3518b44296ce1ccc1a39bbbdb095476b88e382b0b5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, current, selected_work_milestones, through. Outputs/bindings: selected.
Calls/effect boundaries: selected_work_milestones.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[9].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:67`; AST `dfe1d737e7258c0d5ce3a2161172c8f017dd21ee369473ca31233c79a98b484e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, current, selected_work_milestones, through. Outputs/bindings: (none).
Calls/effect boundaries: selected_work_milestones.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[10]::If

Source: `infra/agentinfra/roadmap_acceptance.py:68`; AST `02bc917cb0f786d5b21fb5768d69e5efacf6ed4f4817eb9122eb353ae870fb22`.

Rust module: `infra::agentinfra::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, complete_current, m, require, selected, through. Outputs/bindings: m, selected.
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[10]; no call, error or mutation may be omitted. Condition: not complete_current
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:69`; AST `75562d64284ca82d320d965ef159451caedebf973575860246d0ab3a85ed27be`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: m, selected, through. Outputs/bindings: m, selected.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[10].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_acceptance.py:69`; AST `ea84fea315311b218ed1c707a426ebc3ac2e24e1a3004c9a30880ae12e346deb`.

Rust module: `infra::agentinfra::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: m, selected, through. Outputs/bindings: m.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[10].body[1]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:70`; AST `de26adf0ac06bc8688de79bce75857dc86c7be0941f3d81acd063af138aa2dd2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, require, selected. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[10].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:70`; AST `7e269f3abe85d275a65d4d5913a872d2436b8b058929f23e21cadfa7b0bfe66f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, require, selected. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[10].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:70`; AST `b616cf6467e9365526318598f574278bb1f40b21032dd4328d4c900f08c71d7e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, selected. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[10].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[11]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:71`; AST `86de5cc9753fc530cdd89931d418569760816b37a4931d0d0c396d6cc33e4785`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, dict, list, m, name, selected. Outputs/bindings: m, name, names.
Calls/effect boundaries: dict.fromkeys, list.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[11].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:71`; AST `b5507e65031772c7f4734b0027bad50054278418116f91c917ec9eae6e725063`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, dict, list, m, name, selected. Outputs/bindings: m, name.
Calls/effect boundaries: dict.fromkeys, list.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[11].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:71`; AST `63d1d2abfd579ddb602d6e5131df4a7e5dabbc6a018f83a43c257d57ae795121`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, dict, m, name, selected. Outputs/bindings: m, name.
Calls/effect boundaries: dict.fromkeys.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[11].value.args[0].args[0].elts[4].value::ListComp

Source: `infra/agentinfra/roadmap_acceptance.py:72`; AST `c680c854d98f9a635b2984e0345c6a1755582a36a1803ce70edd65e9fb32c609`.

Rust module: `infra::agentinfra::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: compiled, m, name, selected. Outputs/bindings: m, name.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[11].value.args[0].args[0].elts[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12]::For

Source: `infra/agentinfra/roadmap_acceptance.py:73`; AST `a39a23a30e0440b92706c52b769a05b301b3e83a48b20e02c7f6543c2ad64ef4`.

Rust module: `infra::agentinfra::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: attempts, bindings_current, compiled, current_success, name, names, receipt, require, root, run, runs, spec, through, validate_tool_receipt. Outputs/bindings: name, receipt, run, spec.
Calls/effect boundaries: bindings_current, current_success, require, validate_tool_receipt.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[12]; no call, error or mutation may be omitted. Iteration: name in names
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:74`; AST `12749db13602f3fad9e73376f7ab694bb4f46694a9ae73980df141563f81bb15`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempts, compiled, current_success, name, root, through. Outputs/bindings: run.
Calls/effect boundaries: current_success.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:74`; AST `d4845660602e37b90d9227313c7e9652c200299081591936ff89eb37ebeddb0d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, compiled, current_success, name, root, through. Outputs/bindings: (none).
Calls/effect boundaries: current_success.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:75`; AST `cf2816f4a24e0d9a31836bb2bd8eb415c7f634b7f9d624ed39c1b60dbfedb40a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: run. Outputs/bindings: receipt, spec.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[2]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:76`; AST `bea1d513d8c1838e49ba88dfd428bf35ab466966cb7b9988084b513a4d8688fd`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, root, spec, validate_tool_receipt. Outputs/bindings: (none).
Calls/effect boundaries: validate_tool_receipt.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:76`; AST `cfd9db3a38f9f5f522373afe44915146a40759b8c04aa17fc954f81c1c7d843d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, root, spec, validate_tool_receipt. Outputs/bindings: (none).
Calls/effect boundaries: validate_tool_receipt.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[3]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:77`; AST `ab3d0c5737ff71e57ad1c5fe0c845d079859d5970d5089eabbb50c1f1dffda54`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, receipt, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:77`; AST `1e7c2957ec02723e1aefc26feab617318d6a17fb265e657b0a7b18b4559f3479`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, receipt, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:77`; AST `4135bda17568f5f6bc1ed34100bacdbba6adfd6c3b68935a2af63ac5c70e6ee7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, receipt, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[4]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:78`; AST `e3e9ba784d744f329cc7d53dcf404a9c9a09832831448a46556e53c5c597de2e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:78`; AST `a238128fe7180881dcddd3bd46aabbfce2987ee612d0a729e6fdcc53e0622a64`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[12].body[5]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:80`; AST `3c69f2ba405a94dc611e8667932cfd5a6bc6279fca788cd983d98623caf71f40`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, run, runs. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[13]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:81`; AST `90047f077babafb7860b88e935ce18938eb6d433c837dcde0e44d7d91d7c4c86`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: runs. Outputs/bindings: candidate.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[14]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:82`; AST `3440c1ec25bfc2fc1fdf564a6c36d8cc7fc78dd0bc8acd41d0e92b63fee161dc`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, candidate, r, require, runs. Outputs/bindings: r.
Calls/effect boundaries: all, require, runs.values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[14].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:82`; AST `905c5c5a12f0fd6565ae3d4764e15a9764bb49c40db53185940ed8ba278733da`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, candidate, r, require, runs. Outputs/bindings: r.
Calls/effect boundaries: all, require, runs.values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[14].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:82`; AST `9f75628efc7341f952717e7da312a95b075503a7417ef54cc0b808f5013c9075`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, candidate, r, runs. Outputs/bindings: r.
Calls/effect boundaries: all, runs.values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[14].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_acceptance.py:82`; AST `09d139d2310476fd435f37a0352772432129ed58ebb135e18abe224b0bed7ff3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: candidate, r, runs. Outputs/bindings: r.
Calls/effect boundaries: runs.values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[14].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[14].value.args[0].args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_acceptance.py:82`; AST `9bc1f304419c05fc227d6da18dcdd2e0e61905ff2a984bcd07c4ad67e987aa20`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: runs. Outputs/bindings: (none).
Calls/effect boundaries: runs.values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[15]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:83`; AST `124b4523edf25c0412426c47d270d9605f82142842a771a6bbb316e45da19224`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, review_path, root. Outputs/bindings: review_binding.
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[15].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:83`; AST `32d72aeb3e26e22b657884a2df391d228c88a13df6b2f6cf6bc4e631ff9370dc`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, review_path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[16]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:84`; AST `0145dc7a277734a0b3de7ecce75a2b920210a9f096b47c249471411207c63165`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, read_json, review_path, root. Outputs/bindings: review.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[16].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:84`; AST `62e29c5c5e9296ff83c498705b4aa85762b730d6a4a2614740f5335876a5eef2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, read_json, review_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[16].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:84`; AST `b1595819485bf7f0dcc919fd8153139cafc345431f8e8fde7367187c7426893c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, review_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[16].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:85`; AST `38b12a6e69d6c585fe82525f489070d38cff6095146591c7dbfa3254cb3011ab`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, candidate, require, review. Outputs/bindings: (none).
Calls/effect boundaries: bool, require, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:85`; AST `b8491fd30596e4ff4cb52c470d45767ef7fcf8261d8ef7394d12940113e3e505`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, candidate, require, review. Outputs/bindings: (none).
Calls/effect boundaries: bool, require, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:85`; AST `4a3265213ca3d34e51a922053549618086df765d512296011da0cd6fdc8b41e8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:85`; AST `708d628bda40ad8854ca4f2417cd210a8846033fb36d473496fb9ee953426acc`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:86`; AST `d41ef9915d4ddf6e39391c494e658e6651f839513507f26e766f8925656fd74c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, review. Outputs/bindings: (none).
Calls/effect boundaries: bool, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:86`; AST `ec68aeaf833afc4bca63cd0df56f192e3270dd2a27322adac3e5444f6ae46a1f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[3]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:86`; AST `b5c3a5b9203928e89f77f97b466d6486d362260efa347336954bb72e05d741be`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, review. Outputs/bindings: (none).
Calls/effect boundaries: bool, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[3].args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:86`; AST `f3290eb74a567baef0faf2b9a820e9f7f437655b507eb726e650e0bb268ff3ec`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[17].value.args[0].values[4].operand::Call

Source: `infra/agentinfra/roadmap_acceptance.py:86`; AST `99ce2cb1673c2ae9aa0ee0e241c676179c98f71909de723d51e1c8e4c7685857`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].value.args[0].values[4].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[18]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:88`; AST `c519685e89bfc15d2826be15a3f90591f7e2c5ded7deaf3588a02c59e28cf29b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current. Outputs/bindings: scope.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[19]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:89`; AST `9a6d9bb40cf1f8975c269a5188ab26ce3ca1e15f1945eb12e124b049a1cd72a7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, scope, through. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[19].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:89`; AST `0cdca6374dfff0baca4f1e54207dc16b6b8f881e8abde96bb05859841be5558c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, scope, through. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[20]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:90`; AST `f3ac8d1cf6a62790dd12c566fe30adc0e9e495717ce2fb04d7896a4797982d98`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, review, selected, set. Outputs/bindings: (none).
Calls/effect boundaries: require, review.get, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[20].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:90`; AST `f9185fe682928eeb34b21639cf64f258c8663c1f54b5e1c066634611f34b0038`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, review, selected, set. Outputs/bindings: (none).
Calls/effect boundaries: require, review.get, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[20].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:90`; AST `b4abb177ab264da05579c110bd4922f22db7c6a9921eca0effcdbd228156471a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review, set. Outputs/bindings: (none).
Calls/effect boundaries: review.get, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[20].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:90`; AST `f8aa66644318b206c4e3b1e753c6f6e4870290c9f10448357cf899e0a503b282`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[20].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:90`; AST `e541c2f73caf451c363e9efe74ef3635e9ae7e5d1d4968c9c214a3f907f3a854`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: selected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21]::If

Source: `infra/agentinfra/roadmap_acceptance.py:91`; AST `3280c6f323fc3eb4faeb650b773e10ecddb45bc46ff45ac77f835beed0a7004c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: complete_current, partial, require, review, through. Outputs/bindings: partial.
Calls/effect boundaries: partial.get, require, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[21]; no call, error or mutation may be omitted. Condition: not complete_current
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:92`; AST `f62a7a74bd8103bc82164ee94b10e79a26dfcc9c45d326f035cfbff9a672d237`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: review. Outputs/bindings: partial.
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:92`; AST `522707816cb8ebcb4d5902d08f5ad6be61b1433e96ceae23507d8bdbe352378e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[21].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[1]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:93`; AST `b9d29a5de6c7b472a14d4397dbd7f820379aa897b935d0a0dba62d30f8bcfddd`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, require, through. Outputs/bindings: (none).
Calls/effect boundaries: partial.get, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:93`; AST `736aaa29dc51e49c891e029cfec96d556c9f2e5db90b9a9af12ee267c20face2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, require, through. Outputs/bindings: (none).
Calls/effect boundaries: partial.get, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:93`; AST `97873e8b7f937e33aba8aa598aec0b1c6e1ccf2cb49f5015d6684dfa24cf6bbe`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[21].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:93`; AST `1f9d29013f28569a26d3e4f407161bf9949fc25e6bc83fb2cbc7db1cb2ba97d2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[21].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[21].body[1].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:93`; AST `d66abe22ff1fdd09b97d9d81c2ed80c541687c780edc65cd667516eae422ccd9`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[21].body[1].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[22]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:95`; AST `8ecbfecf02ce1cc88bebeeedc7c53ba614e1f70d50a7cb90c68c5f12e194fcf7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: review, root, unchanged_originals. Outputs/bindings: originals.
Calls/effect boundaries: unchanged_originals.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[22].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:95`; AST `84fa5559f0b8c7f1e5f41e2029fc02b7720f1140829a43da55127e7a10868016`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review, root, unchanged_originals. Outputs/bindings: (none).
Calls/effect boundaries: unchanged_originals.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[23]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:96`; AST `2dbc2bef613ff2db3b4aa9bbe3acdc53944bccf790eab0496f9cd20768882bb7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, next, runs. Outputs/bindings: b, test_details.
Calls/effect boundaries: b['path'].endswith, next.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[23].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:96`; AST `fd149a16eaa5df0df2fb151dea5cf28b8054779533875f22b87a55e93e011e71`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, next, runs. Outputs/bindings: b.
Calls/effect boundaries: b['path'].endswith, next.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[23].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_acceptance.py:96`; AST `e67b134a5c569caeb09e914d2e680661be5a4a3976fadb9699c46cc42de32ac1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: b, runs. Outputs/bindings: b.
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[23].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[23].value.args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:96`; AST `db099b416ce409b0ddef0d0c9665accddf6e7368bf24c487faad035e07c73c72`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[23].value.args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[24]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:97`; AST `48e94490f38f89fa3c029162c656b3fa126c7e8bbb249748d1415a30f84212a7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, read_json, root, test_details. Outputs/bindings: tests.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[24].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:97`; AST `e73433420428080c5a8e0008913d746ad9095a4be80c6b3ad846d86801be5b75`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, read_json, root, test_details. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[24].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:97`; AST `63d60ab7117b15984c7872b2f8f3353a6e99e0301493da4e43867e1ffdb3212a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, test_details. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[24].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[25]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:98`; AST `1b6f8df1e8d919c596c5eb7b703f5d28c7de56f20603de60cf0205ebfaf903d8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, require, tests. Outputs/bindings: (none).
Calls/effect boundaries: require, tests.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[25].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:98`; AST `7060a7106bfaf16a9a01f465446cf93917547be7b4e530adacf6adb7edf00aa0`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, require, tests. Outputs/bindings: (none).
Calls/effect boundaries: require, tests.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[25].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:98`; AST `f76fcc19233f4d81d091fb27e7fc42c1671d3d4e07d55d43758b4a3261ef5b3b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tests. Outputs/bindings: (none).
Calls/effect boundaries: tests.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[25].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[26]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:99`; AST `3ad6158059bbd64c3241e8e561ff9e64f063b0938aef5903bfc5816a7d155718`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: case, tests. Outputs/bindings: case, passing.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[26]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[26].value::SetComp

Source: `infra/agentinfra/roadmap_acceptance.py:99`; AST `5fd27976f50484151745e32f9f40ed0144f9aca1ea2e9b2ac29bd94f09559486`.

Rust module: `infra::agentinfra::roadmap_acceptance`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: case, tests. Outputs/bindings: case.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered SetComp evaluation at root.body[18].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[27]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:100`; AST `0b43a95f61e5031f27acad42aab4668a4cf0eeeedb06d81cd17c8cde83acf8cd`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, originals, require, set, tests. Outputs/bindings: b.
Calls/effect boundaries: require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[27]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[27].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:100`; AST `982c6d4005cc11f014b7713419062458054f97ddb4782b22ba59bb3807d3c589`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, originals, require, set, tests. Outputs/bindings: b.
Calls/effect boundaries: require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[27].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[27].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:100`; AST `521198191a9a84fc30107b5c00b6f84debf0412efb6dba19e9ec3b9ec055fedd`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, originals, set. Outputs/bindings: b.
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[27].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[27].value.args[0].left.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_acceptance.py:100`; AST `aa4fe4fc2a01fdc32ef0411f24ab13c2abee4ebaca01532c9564417827e45519`.

Rust module: `infra::agentinfra::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: b, originals. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[27].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[27].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:100`; AST `771529cb08217c5ba980c26edf5325ca2d156df9a37af8c7ace8abc361ca85d2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, set, tests. Outputs/bindings: b.
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[27].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[27].value.args[0].comparators[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_acceptance.py:100`; AST `091d485577980391b7d1ae2f38e00eb9def841bcc085d80ad81cabed14f050a2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: b, tests. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[27].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[28]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:102`; AST `b506a36ab3b8ab16e6d61c3795de21e89be6ae6ac83193c2294f7e34bb4693fb`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, root. Outputs/bindings: mapping.
Calls/effect boundaries: inventory.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[28].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:102`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[29]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:103`; AST `37996d4decdd4cf09c4f977dba6b5dce26eda861743ce35ca79f5169b984be52`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: check, mapping, root. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[29]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[29].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:103`; AST `aca6d7804f7aa50d8a69fc4a23da9915c964f07b04eab36f24c356bd7c1fc9da`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, mapping, root. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[30]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:104`; AST `14e146ee4283b7747e99e6305150c7c6ec4d988b7638263908e8af713cfe0ee6`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, mapping. Outputs/bindings: _, generated.
Calls/effect boundaries: artifacts.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[30]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[30].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:104`; AST `be59702d454b64ba020f026d26bdcca3d702bf9e24b953671c5dc40da5e3badf`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, mapping. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[30].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[31]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:105`; AST `67aae97715c0bde4c42d2600a280b1857ae98cef16378bdd9bcea53ba43c48a7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, generated, path, root. Outputs/bindings: migration_bindings, path.
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[31]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[31].value::ListComp

Source: `infra/agentinfra/roadmap_acceptance.py:105`; AST `51845c293cb2bb0740816960e60d3430cccf0bf82d3836f95b7b0a950e2e4590`.

Rust module: `infra::agentinfra::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: file_binding, generated, path, root. Outputs/bindings: path.
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[31].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[31].value.elt::Call

Source: `infra/agentinfra/roadmap_acceptance.py:105`; AST `192184ea8321d34d40631933a8fafdc81e7e09cb8d86dc5a2b054a9aa268aaac`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[31].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[32]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:106`; AST `e40b064e1b38bbd452915b51d888b924256f416f437df23b22138227910c8fad`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, root. Outputs/bindings: migration_index.
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[32]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[32].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:106`; AST `46acd784cef9299ca126ca4a1876ff980bc946c4679343ee8ae16b18aba2e5a2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[32].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[33]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:107`; AST `c694be6310da13b8b54772d04c51c3bf8828902995f7d50b0302dc62a0f452ab`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, name, review_binding, run, runs. Outputs/bindings: generation, name, run.
Calls/effect boundaries: digest, runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[33]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[33].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:107`; AST `f54a6f8c4249b8f2452420f3a80629a8f789599cbbbe3dbbbcc26f739469be6c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, review_binding, run, runs. Outputs/bindings: name, run.
Calls/effect boundaries: digest, runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[33].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[33].value.args[0].values[1]::DictComp

Source: `infra/agentinfra/roadmap_acceptance.py:107`; AST `77f3896d9dfe086f4a6ba2e9e94c5d4d5b338eee38467077e185caf9090dd79e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: name, run, runs. Outputs/bindings: name, run.
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[33].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[33].value.args[0].values[1].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_acceptance.py:109`; AST `c3d9fecb80f3ad461c89a84698156864b8e8311a34cd6aed9778808625a0a140`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: runs. Outputs/bindings: (none).
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[33].value.args[0].values[1].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[34]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:110`; AST `dbaf76678fe6e5d9f821f18920432acc5858ccd9e8186342b5977ddd1e911aed`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, generation, through. Outputs/bindings: base.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[34]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[35]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:111`; AST `2e073201ddcc7e4fb41ec61a50176ee3606452fac75d935df7eeeeefa9cf5b57`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, observe_interfaces, root. Outputs/bindings: interfaces.
Calls/effect boundaries: _immutable, observe_interfaces.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[35]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[35].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:111`; AST `bd4efe363a54ebe258e255db0195c30398a97553b26d3d64649c9f7d65540fe5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, observe_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable, observe_interfaces.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[35].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[35].value.args[2]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:111`; AST `e3b835733344cc4702b993e1dfafa68c05951883e31c5b65824bdf1022d38cb1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[35].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[36]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:112`; AST `4c4bd8b41908c53480287bcc87676d90263ec11beb836c45b21f318adf6784d1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compare_interfaces, review, root. Outputs/bindings: compatibility.
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[36]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[36].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:112`; AST `715156a96f83a5170658c971951ffcf6ba8cfa716e194f198f5bb7e984d8c301`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, review, root. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[36].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[37]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:113`; AST `dd0c5fd3095ccecccfccfe26756760a58651e2af7e54fa5d55b91b6b94c32784`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dispositions.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[37]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38]::If

Source: `infra/agentinfra/roadmap_acceptance.py:114`; AST `1ea022ad92e13a363d126cfab8e759c293bfb1ba0fd403ff5a6b7f565dce3537`.

Rust module: `infra::agentinfra::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _immutable, base, compatibility, dict, disposition, dispositions, isinstance, require, review, root, validate_compatibility_disposition. Outputs/bindings: disposition.
Calls/effect boundaries: _immutable, dispositions.append, isinstance, require, review.get, validate_compatibility_disposition.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[38]; no call, error or mutation may be omitted. Condition: not compatibility['structural_compatible']
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:115`; AST `60bbae7c764d664f1c8170d2e3b4d0a16800dddf302e21a712caab5f22cbd0ef`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, require, review. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[38].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:115`; AST `0386c80e49750a8f5ac54936263bc1be59f016f80049b56080fea9e59f1b2a76`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, require, review. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[38].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:115`; AST `868832e480f8f6f444645c52f2ab35689a11fe9e0b833470fca90c43211a1e67`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, review. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[38].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[0].value.args[0].args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:115`; AST `4bf8be2b3aa3f27bbc8b592ebafe0898d563e4316cd97d79a90f6c22120a7394`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[38].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:117`; AST `cea7bf428db26b14a26a81ced8bb4a0820f01887b659bc6ae122087525b63a2f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compatibility, review, root, validate_compatibility_disposition. Outputs/bindings: disposition.
Calls/effect boundaries: validate_compatibility_disposition.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[38].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:117`; AST `17318f6cd5dd9ca533767c6dd0d610376b5bd5534e0e837541c7f7c13bb550be`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compatibility, review, root, validate_compatibility_disposition. Outputs/bindings: (none).
Calls/effect boundaries: validate_compatibility_disposition.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[38].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[2]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:118`; AST `7d9bb1b461affc96e12f9274aa34da7077419fa99185a626d5ac2869293b115c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, disposition, dispositions, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable, dispositions.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[38].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[2].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:118`; AST `fe5337f00f2ad53c60b52cbad067a0f2d018547617117ed69e12dd743e5350cd`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, disposition, dispositions, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable, dispositions.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[38].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[38].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:118`; AST `515e8b55392ff9692bdbb144ccbc01681f5be0c271cb99cdffe28d9643e408f3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, disposition, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[38].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[39]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:119`; AST `676eb3a3c872c2210d38f875141553cb61459f68fd1e61f0d4b38948b54e9a37`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, compatibility, root. Outputs/bindings: compatibility_binding.
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[39]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[39].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:119`; AST `9d7755094dbc967f874cbe14f50e7d88d369297c9c9d20f35e70e0ef0a3e3378`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, compatibility, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[39].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[40]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:120`; AST `1b4c5b1763ca47791e77b875809d64015a0390a6ec909def744d456025a50aa5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, originals, root. Outputs/bindings: originals_binding.
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[40]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[40].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:120`; AST `b11b7f79e11786637bef137d33cfb4495437fcc1b21aee038861d09ef68cde9f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, originals, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[40].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[41]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:121`; AST `78230e9ffeac45f638e16931ddd2173e92834cfa0619f3876026953b4b5a4c12`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, compiled, root. Outputs/bindings: compiled_binding.
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[41]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[41].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:121`; AST `6921202f50bbcce3d1e7b404dba9d86191068e11229d2fed756c89345546a190`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[41].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[42]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:122`; AST `d484c2832e00a265598d1ab950e4b318fc20b47c58724109cc42a9d586fc5a26`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, native, root. Outputs/bindings: native_binding.
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[42]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[42].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:122`; AST `208d562c6e92bab0d67fb11067cbe481b96b9fa90da4fd5cbeb91bdde2cb917e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, native, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[42].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[43]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:123`; AST `21708ad6ee68e47d92b6dc2b630d0fe2591126be440e51832f660ffba58ad74c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _unique, migration_bindings, runs. Outputs/bindings: all_inputs.
Calls/effect boundaries: _unique.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[43]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[43].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:123`; AST `287a7f3edfe3d90ab5d14561ea97914efbe3097494a55d7f1c5a91175021f527`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _unique, migration_bindings, runs. Outputs/bindings: (none).
Calls/effect boundaries: _unique.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[43].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[44]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:124`; AST `324396d791e2dc4d29fc13a6c9537f23b55fe96c7bd6e7770b86b0da63eecca4`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, compatibility_binding, compiled_binding, dispositions, interfaces, name, originals_binding, review_binding, run, runs. Outputs/bindings: b, common, name, run.
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[44]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[44].value.elts[6].value::ListComp

Source: `infra/agentinfra/roadmap_acceptance.py:125`; AST `0aa6a9ff44073643626f6ef9a68f9bfa5a490b7bfd649de488f53d80004a85e5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, name, run, runs. Outputs/bindings: b, name, run.
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[44].value.elts[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[44].value.elts[6].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_acceptance.py:125`; AST `c3d9fecb80f3ad461c89a84698156864b8e8311a34cd6aed9778808625a0a140`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: runs. Outputs/bindings: (none).
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[44].value.elts[6].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[45]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:127`; AST `e4b847b358a5e253757735e333d41f71516d71439ca2070d7f6e7d944628404b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: receipts.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[45]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46]::For

Source: `infra/agentinfra/roadmap_acceptance.py:128`; AST `29875e79308b321913827103de29f6f6d074de44f2c6366a4be04e68742216d3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _unique, all_inputs, b, bindings_current, candidate, common, compiled, contract, digest, gate, generation, item, milestone, n, name, observed, originals_binding, passing, r, receipt, receipts, require, review, reviewed_artifacts, root, run, runs, selected, set, through, validate_record. Outputs/bindings: b, contract, gate, item, milestone, n, name, observed, r, receipt, reviewed_artifacts, run.
Calls/effect boundaries: _unique, b['path'].endswith, bindings_current, digest, item.get, observed.get, observed['implementation_units'].values, observed['outputs'].values, receipts.append, require, reviewed_artifacts.extend, runs.items, set, validate_record.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[46]; no call, error or mutation may be omitted. Iteration: milestone in selected
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:129`; AST `2799d38a92f5e1f2145390bfed2ee0d4f85f6ae1ddfb40592912ae68521bdb3b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, milestone. Outputs/bindings: contract.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[46].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[1]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:130`; AST `f9caddc2478e0694214d1f7c7566b56931e48f6b89b92c4bbcb6ff6208b8dd65`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[46].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:130`; AST `cfb0f0af45c57f4cb8e530c93215890f1908c6c0d024a2c681603672f7c9462b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:130`; AST `667b0281782ac167fc2e5367fc5549364a09446c91c8958b05f7cd1b838bb333`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[2]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:132`; AST `642f96e12cf3b924d493b3f0e4b188d1e9f106ee25cafc6b5444b4ad662c6d1a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: milestone, review. Outputs/bindings: observed.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[46].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:133`; AST `5f0183e3e0cbaedc27a5edc299c3053d8ff5085ac87c7549544c99b6b8cd725d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, observed, require, set. Outputs/bindings: (none).
Calls/effect boundaries: observed.get, require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[46].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:133`; AST `a43606ff49775f0974f888bc796ed3b1b7e5987f6df99c44a96c1e790817cb4a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, observed, require, set. Outputs/bindings: (none).
Calls/effect boundaries: observed.get, require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:133`; AST `edfbdab40c08ea6d8c6adc5fe15cbc4ee89be1697761b9aefa5861ad754d0feb`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, set. Outputs/bindings: (none).
Calls/effect boundaries: observed.get, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:133`; AST `ed104138768777304d511aafe8181317ea2df97ce39bdfa6ffb7aafcd86b9eff`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed. Outputs/bindings: (none).
Calls/effect boundaries: observed.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:133`; AST `ceb213fadf1ec2f87591cd6a9fd16b75075beb341f8de1020f40517d92d19b93`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:134`; AST `246795320e5d56882afab264c2cc1517f6f649950e85c27f80b0e02666e4c0e1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, set. Outputs/bindings: (none).
Calls/effect boundaries: observed.get, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:134`; AST `e7d608a3e9f61f75265adf11473a525be702cff6442f7b450611f4c273e991d1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed. Outputs/bindings: (none).
Calls/effect boundaries: observed.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[3].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:134`; AST `e9a3aa3a88704c1c3901396b801eb54e5f349228ea91fb945deb9fff159e9a74`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[3].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[4]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:136`; AST `4074ca7e7c945d874b5a823157f22b0dde43c3519faef5f43922bcc6dfbecb3f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: reviewed_artifacts.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[46].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5]::For

Source: `infra/agentinfra/roadmap_acceptance.py:137`; AST `f0af4473c9cf3d56ddbb524c0ac22da0f6c04ba8111595cc205bcd65d987a5b8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: bindings_current, item, observed, passing, require, reviewed_artifacts, root, set. Outputs/bindings: item.
Calls/effect boundaries: bindings_current, item.get, observed['implementation_units'].values, observed['outputs'].values, require, reviewed_artifacts.extend, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[46].body[5]; no call, error or mutation may be omitted. Iteration: item in [*observed['outputs'].values(), *observed['implementation_units'].values()]
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].iter.elts[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:137`; AST `4ad0cf286e3704a6bffd657eb445b36d66e17b800952d69df4d8a471274a14bf`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed. Outputs/bindings: (none).
Calls/effect boundaries: observed['outputs'].values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].iter.elts[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].iter.elts[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:137`; AST `45d985603a5210849caa9468c231d834bd6c8fbc3f70a3bdef0e08eb0b5aabf3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed. Outputs/bindings: (none).
Calls/effect boundaries: observed['implementation_units'].values.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].iter.elts[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:138`; AST `59e284deffb1dd16cfd246ea8419685a2026a0217667b7759577ada2cabffb17`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, item, passing, require, root, set. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, item.get, require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[46].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:138`; AST `06cc593580daa01a553a07b72de41d9ad8036b4772aa30f72de1c94db7b53787`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, item, passing, require, root, set. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, item.get, require, set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:138`; AST `246d5dcdb595f01eb65f3b09ad04da4d54ce450421803e5e6b63ff185994a649`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:138`; AST `52a58297bdd94f74cc7bd867d9a9fba05b34d5d57293e5afc0aaa09df4f54d2f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:138`; AST `b160a41749fd8a9a305649a5884180c4cee2bd3f5d31b2ac370367d436c9ec27`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[0].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_acceptance.py:139`; AST `8cf35d41991ce0709eff13fec29727b5301cdcf36407c53f959777e1b19a5b0f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[0].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[0].value.args[0].values[4]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:139`; AST `5fa4c8f513201e279be2e663812e3cb84bb4664100e34a58bc305f88f8b8558b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, item, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[0].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[1]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:141`; AST `3e894bec26e9a38fce7d6af8893d7807761f240a3940f8ed163909f6bd0c8a95`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item, reviewed_artifacts. Outputs/bindings: (none).
Calls/effect boundaries: reviewed_artifacts.extend.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[46].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:141`; AST `d2285a12fd2ccbf7d6d6e191f1f9d7a3e05ca1177caa90c159d84ee30c9ff17d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, reviewed_artifacts. Outputs/bindings: (none).
Calls/effect boundaries: reviewed_artifacts.extend.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6]::For

Source: `infra/agentinfra/roadmap_acceptance.py:142`; AST `3276a73f6415659ef25d92c6e68c47c077d90e16d009ea63b91b618628b7c575`.

Rust module: `infra::agentinfra::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _unique, all_inputs, b, candidate, common, contract, digest, gate, generation, milestone, n, name, originals_binding, r, receipt, receipts, reviewed_artifacts, root, run, runs, through, validate_record. Outputs/bindings: b, gate, n, name, r, receipt, run.
Calls/effect boundaries: _unique, b['path'].endswith, digest, receipts.append, runs.items, validate_record.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[46].body[6]; no call, error or mutation may be omitted. Iteration: (gate, name) in (('source_correspondence', 'source.reconcile'), ('implemented_outputs', 'roadmap.validate'), ('production_build', 'production.build'), ('applicable_original_tests', 'original.tests'))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:144`; AST `6e6fded91e963d9ea893fc315ec85ec0c7e02faade6f9ab8f2a95e78b11b6daa`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, runs. Outputs/bindings: run.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[46].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:145`; AST `ee9fc870bf87443e2d6eca638fd19ff26f930b5dd148bb65a42f06396f4cf954`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _unique, all_inputs, b, candidate, common, contract, digest, gate, generation, milestone, n, originals_binding, r, reviewed_artifacts, run, runs, through. Outputs/bindings: b, n, r, receipt.
Calls/effect boundaries: _unique, b['path'].endswith, digest, runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[46].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1].value.values[6]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:147`; AST `1253f0f07ad69eba5dc7892142a2e1dca56b8de30947ef3013ae84aeb4801584`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[6].body[1].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1].value.values[8]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:148`; AST `c74d47d77406d2faf1a80650b5d615d26d1596f793051376213e43811250502c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _unique, common, reviewed_artifacts, run. Outputs/bindings: (none).
Calls/effect boundaries: _unique.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[6].body[1].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1].value.values[10].values[6]::DictComp

Source: `infra/agentinfra/roadmap_acceptance.py:151`; AST `3124899ca1d08eec8690f61630c1cf76a28d56411f75260a2b170696856c5d5a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: n, r, runs. Outputs/bindings: n, r.
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[46].body[6].body[1].value.values[10].values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1].value.values[10].values[6].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_acceptance.py:151`; AST `c3d9fecb80f3ad461c89a84698156864b8e8311a34cd6aed9778808625a0a140`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: runs. Outputs/bindings: (none).
Calls/effect boundaries: runs.items.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[6].body[1].value.values[10].values[6].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1].value.values[14]::ListComp

Source: `infra/agentinfra/roadmap_acceptance.py:156`; AST `eaf48c8108cbcfc50afc869c3a85a42118bb5c62f40cae11e7f16f8114e2a844`.

Rust module: `infra::agentinfra::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, run. Outputs/bindings: b.
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[46].body[6].body[1].value.values[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[1].value.values[14].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:156`; AST `1a6b272a6b055667455390724ce028beab541fdb9b09c7392c931a6a43a52e5b`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b['path'].endswith.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[6].body[1].value.values[14].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[2]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:157`; AST `c9b2f0103891b1cd42b7839dd114c406f24421dc914796e9cd4de891d190d258`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[46].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:157`; AST `ea4e054b22d82ce959d88540507f7d4dcae88502dbfbd701b7adfebe5531ccda`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[3]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:158`; AST `dcadd15fd2dbb958385bb84e5b5f753b267236642b2d4615860ec7bc6659c3d8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, receipts. Outputs/bindings: (none).
Calls/effect boundaries: receipts.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[46].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[46].body[6].body[3].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:158`; AST `de7704aae55cd23d4f34ed6577353a304a3bcbbef191f229a918dd39e5c5bb25`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, receipts. Outputs/bindings: (none).
Calls/effect boundaries: receipts.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[46].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[47]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:159`; AST `520d53db79eabe52658f8af577fbd7d1ac84550bff69ff356e5096a61c3340c3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, receipts. Outputs/bindings: evidence.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[47]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[48]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:160`; AST `5b9bb2d45a4363d27939471107c4f967c1c80ff0a1d43d1e67785198f647c140`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit_evidence, compiled, evidence, root. Outputs/bindings: audit.
Calls/effect boundaries: audit_evidence.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[48]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[48].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:160`; AST `15e12735a35059c13d4e0dfc2ee22d0526ab26ef50db74dcba2999220bbcfb0c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit_evidence, compiled, evidence, root. Outputs/bindings: (none).
Calls/effect boundaries: audit_evidence.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[48].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[49]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:161`; AST `cae02be23929fd4b0cd0b3deddc7a6bd229bdeec7b077848453934eeaca0e805`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, audit, m, require, selected. Outputs/bindings: m.
Calls/effect boundaries: all, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[49]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[49].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:161`; AST `1be1a26c0a860ae482f9f199d810e67ba46e2114eaeb4deaf3107d6b87b86b3d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, audit, m, require, selected. Outputs/bindings: m.
Calls/effect boundaries: all, require.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[49].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[49].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:161`; AST `8f36028e452ab9e99592fc08d8b0ede82e04030866695e49ffc2191e20c1ae8e`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, audit, m, selected. Outputs/bindings: m.
Calls/effect boundaries: all.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[49].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[49].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_acceptance.py:161`; AST `f667dd2a766e36e9a6cb19c0ddff6283e58ee1f9d2d111c623d707d84544f9f9`.

Rust module: `infra::agentinfra::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: audit, m, selected. Outputs/bindings: m.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[49].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[50]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:162`; AST `c480a849e90afa40231b547336cf7bec114b3fc78ef6697211246ef78afc0a1d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, base, evidence, root. Outputs/bindings: evidence_binding.
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[50]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[50].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:162`; AST `327789ceb2430ffd9e05c13cbc101c2e3920c5dc12d12b523915a920848e64c5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, base, evidence, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[50].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[51]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:163`; AST `480e43acc8f7f8586e5c10af8593af0f2bb5cca6ca019e30439a75539feb589d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _immutable, audit, base, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[51]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[51].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:163`; AST `99150aeea053abe67acb3c6ac547063bea1ecb5e8e70928baf7d57c5710b878a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _immutable, audit, base, root. Outputs/bindings: (none).
Calls/effect boundaries: _immutable.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[51].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[52]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:164`; AST `86f972f909f7202210d3de94b6fed67edaa338c07e78c557335930084da868a4`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: current.
Calls/effect boundaries: adapter.read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[52]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[52].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:164`; AST `475d5be5efd9ec4a3dca0b74c9a7534e6fc14081f5396d86007b06bd7a2ef8b1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.read.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[52].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[53]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:165`; AST `7a8f30ce5d96a70958c4d51d6673536dda323a70c68f0d252b988a9f488303d2`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, dict. Outputs/bindings: execution.
Calls/effect boundaries: dict.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[53]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[53].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:165`; AST `e39c7b831e0189875b7e6d4433b233e6500f14429dca59c4c8fc16fd6ac9446a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[53].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[54]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:166`; AST `7f1ddc32f66f08cfea2d4f761f360cafe537ebe48106b30a09553289ca8e2e8c`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: prior_binding.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[54]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[55]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:167`; AST `6fed326e74060216bf29b992a4c32395e9f6bb22daa69973856b4742994bf0b1`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[55]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[55].value.elts[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:167`; AST `4c152ba0ddcae5f021c961df5ea040b3875ac8b8553149025b4b23f7569366b6`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[55].value.elts[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[56]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:168`; AST `00442c95a584dfd374b7c4dc5a8fb0ddba7570540254e177c0faee47b37be1d5`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bind_goal, compiled, execution, native, owner, prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[56]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[56].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:168`; AST `4b020ebd628ea1cc1d32e3e2f73960684c4aad4d838b6bfde40a356a5dc6fc1d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bind_goal, compiled, native, owner, prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[56].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[57]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:170`; AST `95f620c65d2b70c79885a71d8628e7035d38e3156a53cead016c0c435994392a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, k, native. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[57]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[57].value::DictComp

Source: `infra/agentinfra/roadmap_acceptance.py:170`; AST `12d4cce81999c9c60f5863299d19a25d0b74183891dba1b715ada093642399db`.

Rust module: `infra::agentinfra::roadmap_acceptance`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, native. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[57].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[58]::Assign

Source: `infra/agentinfra/roadmap_acceptance.py:171`; AST `59103eaa021088ef0ed66bd25fca96bb55106b93c20781c994dafd9c182c6b20`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, list. Outputs/bindings: history.
Calls/effect boundaries: current.get, list.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[58]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[58].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:171`; AST `8581a440dea74e5dba683434ec7142a391e95e463028c8c120fca0007a5c92cf`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, list. Outputs/bindings: (none).
Calls/effect boundaries: current.get, list.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[58].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[58].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:171`; AST `28fa7b264936c4144986cc97e7820c013d77daefefb8205a81c504efd64bc5c7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[58].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[59]::If

Source: `infra/agentinfra/roadmap_acceptance.py:172`; AST `bf528882f73ec3cd60d879c568a34aad1687d152230061909ed7f83ac2ed2df3`.

Rust module: `infra::agentinfra::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, evidence_binding, history. Outputs/bindings: (none).
Calls/effect boundaries: current.get, history.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[59]; no call, error or mutation may be omitted. Condition: current.get('roadmap_evidence') and current['roadmap_evidence'] != evidence_binding
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[59].test.values[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:172`; AST `1333383b3fe3032b13c56791a0adf30c7d0d6450b600ed5d0308aba896ce85c8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[59].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[59].body[0]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:173`; AST `b4f8be97c0508ab39ac76a7d45d8ac5cc17225beff5767145053b0a653f38b09`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, history. Outputs/bindings: (none).
Calls/effect boundaries: history.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[59].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[59].body[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:173`; AST `000cf577ad436370e40575f0b242e0ad871d6a67bca6bafce675c6d9975d691f`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, history. Outputs/bindings: (none).
Calls/effect boundaries: history.append.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[59].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[60]::Expr

Source: `infra/agentinfra/roadmap_acceptance.py:174`; AST `0ef3ffe1ad4ddfe452d936f38434e72d80c0ccf7e592d8995b9e8245884d7643`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter, audit, compatibility_binding, complete_current, digest, evidence_binding, execution, history, interfaces, migration_index, review, review_binding. Outputs/bindings: (none).
Calls/effect boundaries: adapter.profile.path, adapter.profile.path().read_bytes, adapter.update, digest, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[60]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[60].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:174`; AST `363d6d4ba5fc294a701665b5acff229717965fcd28fa32bd1d4a64a368feb62d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter, audit, compatibility_binding, complete_current, digest, evidence_binding, execution, history, interfaces, migration_index, review, review_binding. Outputs/bindings: (none).
Calls/effect boundaries: adapter.profile.path, adapter.profile.path().read_bytes, adapter.update, digest, review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[60].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[60].value.args[0].values[8].body::Call

Source: `infra/agentinfra/roadmap_acceptance.py:178`; AST `acb6d6af6982866d233f2d520e295bd774dd93181922f7a76580a968cdd4a11a`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: review. Outputs/bindings: (none).
Calls/effect boundaries: review.get.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[60].value.args[0].values[8].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[60].value.keywords[0].value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:179`; AST `3f1faba7779a1640a9737c8dd9613b32b537b77ddb4aa95702b5cd7019dd569d`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter, digest. Outputs/bindings: (none).
Calls/effect boundaries: adapter.profile.path, adapter.profile.path().read_bytes, digest.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[60].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[60].value.keywords[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_acceptance.py:179`; AST `d17e350e65e00463e5c423c18b26b0401fd9debd1a9b2365e777451997f6ccf8`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.profile.path, adapter.profile.path().read_bytes.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[60].value.keywords[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[60].value.keywords[0].value.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_acceptance.py:179`; AST `927525f77bb177789ff98c6b0b191aecb990be874c5131819c07ab4a33f375ea`.

Rust module: `infra::agentinfra::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.profile.path.
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[60].value.keywords[0].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_acceptance.py::module::_assemble::root.body[18].body[61]::Return

Source: `infra/agentinfra/roadmap_acceptance.py:180`; AST `8e541b27163d75bcd49df0dc71f43c47ffe731327356420e48e98665f533fce7`.

Rust module: `infra::agentinfra::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, complete_current, evidence_binding, native_binding, selected, through. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, pathlib, roadmap, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_portability, roadmap_project, roadmap_records, roadmap_runtime, roadmap_work, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[61]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
