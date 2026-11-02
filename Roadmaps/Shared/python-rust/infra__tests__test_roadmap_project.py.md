# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 216. Inventory digest: `9e6b6b56ba71f43d45bd67f135ba9fd2e3d6949c0f6ab9830b3372e4ef1416c3`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_project.py::module::root::Module

Source: `infra/tests/test_roadmap_project.py:1`; AST `d6aa04b7165f230ff35457644094e545d224fbc49a497656e7c8093fe4f0c16b`.

Rust module: `infra::tests::test_roadmap_project`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AEGIS_RECORD_WRITER, BudgetLedger, ContractError, Path, ProjectAdapter, ROOT, WorkspaceLease, __file__, __name__, adapter, atomic_write_json, before, cases, changed, compiled, copy, current, digest, execution, inherited, lease, ledger, legacy, name, old, owner, path, project_into_record, read_json, recipe_scope, record, self, shared, shutil, stale, started, str, sys, tempfile, unittest, value. Outputs/bindings: ROOT, _, adapter, before, cases, changed, compiled, current, execution, inherited, lease, ledger, legacy, name, old, owner, path, record, shared, stale, started, value.
Calls/effect boundaries: BudgetLedger, Path, Path(__file__).resolve, ProjectAdapter, WorkspaceLease, adapter.describe, adapter.update, atomic_write_json, cases.append, copy.deepcopy, digest, lease.acquire, lease.release, ledger.close, ledger.reserve, path.read_bytes, project_into_record, read_json, recipe_scope, self.adapter.profile.path, self.adapter.read, self.adapter.update, self.assertEqual, self.assertFalse, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.current_hash, self.path.exists, self.path.read_bytes, self.root.resolve, self.subTest, self.temp.cleanup, shared.mkdir, shutil.copyfile, str, sys.path.insert, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[0]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[1]::Import

Source: `infra/tests/test_roadmap_project.py:3`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_project.py:5`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_project.py:6`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_project.py:7`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_project.py:8`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[7]::Assign

Source: `infra/tests/test_roadmap_project.py:10`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[7].value.value.value::Call

Source: `infra/tests/test_roadmap_project.py:10`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[7].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[7].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_project.py:10`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[7].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[8]::Expr

Source: `infra/tests/test_roadmap_project.py:11`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[8].value::Call

Source: `infra/tests/test_roadmap_project.py:11`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[8].value.args[1]::Call

Source: `infra/tests/test_roadmap_project.py:11`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:12`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:13`; AST `9811b540c3e37df2b3ccdff46e6f3e69321e812e6a1dfe5017d057b281daa1cb`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:14`; AST `7e9c3f5290a99e55259b83ed615988e11578a991178ada162c503777b0b68347`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[12]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:15`; AST `f7bc34fd234a6f0db93029ebb0217e32d52e51e92c2f20e1815c94600acf79fa`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:16`; AST `726513b649a2445134ce2ea1473d3c522e44a378bf22ac4db203cb55298d9338`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[14]::ImportFrom

Source: `infra/tests/test_roadmap_project.py:17`; AST `3367960b9408d9ad78b9ae529c9afc616ef20136b6286eb07310bc757747ba05`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::root.body[15]::ClassDef

Source: `infra/tests/test_roadmap_project.py:20`; AST `80747767a86106cf487cfd0d7ed853048470aee1967a71b7e8a66dddab8ab443`.

Rust module: `infra::tests::test_roadmap_project`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: AEGIS_RECORD_WRITER, BudgetLedger, ContractError, Path, ProjectAdapter, ROOT, WorkspaceLease, adapter, atomic_write_json, before, cases, changed, compiled, copy, current, digest, execution, inherited, lease, ledger, legacy, name, old, owner, path, project_into_record, read_json, recipe_scope, record, self, shared, shutil, stale, started, str, tempfile, unittest, value. Outputs/bindings: _, adapter, before, cases, changed, compiled, current, execution, inherited, lease, ledger, legacy, name, old, owner, path, record, shared, stale, started, value.
Calls/effect boundaries: BudgetLedger, Path, ProjectAdapter, WorkspaceLease, adapter.describe, adapter.update, atomic_write_json, cases.append, copy.deepcopy, digest, lease.acquire, lease.release, ledger.close, ledger.reserve, path.read_bytes, project_into_record, read_json, recipe_scope, self.adapter.profile.path, self.adapter.read, self.adapter.update, self.assertEqual, self.assertFalse, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.current_hash, self.path.exists, self.path.read_bytes, self.root.resolve, self.subTest, self.temp.cleanup, shared.mkdir, shutil.copyfile, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:21`; AST `e14c08e0399bc74974e66bff829fc165d3833390c955490e4170965aadf710c9`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ProjectAdapter, ROOT, name, self, shared, shutil, tempfile. Outputs/bindings: name, shared.
Calls/effect boundaries: Path, ProjectAdapter, self.adapter.profile.path, shared.mkdir, shutil.copyfile, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_project.py:22`; AST `76bde1458ae912172e4121d6d32a40d02cf372c4db6ead9b5af171facc2865c2`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:22`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_project.py:23`; AST `3fd62e96028b079a923df6e9a7c1c1df8b3ae2536d55ba9d4f31f162d4d5ddb5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:23`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_project.py:24`; AST `64a433e7d51b0c2105679a685168fb55724f404a1027a03a7b7c8dcbfe90317e`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: shared.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:25`; AST `d20d143f38d9b5d82545abe3ef1d2ca636f603d0a2b93ac41056e250c71735d1`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:25`; AST `99bcba72db0838f639a464854466bfa2acd0fe9e260d2d59c8e8247715d94a84`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[4]::For

Source: `infra/tests/test_roadmap_project.py:26`; AST `daa5ee34868098cf470b6dbc8dfcbc6da7171324fbe510773775e59b3c3ba1ba`.

Rust module: `infra::tests::test_roadmap_project`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ROOT, name, shared, shutil. Outputs/bindings: name.
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[15].body[0].body[4]; no call, error or mutation may be omitted. Iteration: name in ('registry.json', 'records.schema.json')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:27`; AST `db7d7a871703fd92e816bbfd9ff370a38e278f3f25d86eaf0c06e96abeb4120f`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, name, shared, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:27`; AST `fed25c609f0527a549ec132ad9975f1bed9ae48319462f7ae165e4cbea1ac3e0`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, name, shared, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_project.py:28`; AST `534bb1662e28906b4d410df73ba6fc977f75299f5d7ad669682234772ea7b8ff`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_project.py:28`; AST `767d6f36794c3ef9461405214ba86150746f9d6ecfb7f1eb0c21ae84aa981a57`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_project.py:29`; AST `46dc0a3054f72ebdd3be4ad66b32ad95dafa86a825385def0f4c1bcac56f7d5c`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.profile.path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::setUp::root.body[15].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_project.py:29`; AST `99483f4e69e377719c4bedca45ec623281a85be11581f48d0b5928d401b07916`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.profile.path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::tearDown::root.body[15].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:31`; AST `13fc628cded8f8def9f296b061b0d1b4f129ada0770d009511b176b914c63004`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::tearDown::root.body[15].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:32`; AST `03b3f025b568ce93e3252b0f1f4a5ce0348dbf2ecebaae9a0913927af51d7b24`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::tearDown::root.body[15].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:32`; AST `467d2c9d775dc88f51613c917ddb5ec5487d5c87293666d9c9c5f9a88375b66b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::current_hash::root.body[15].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:34`; AST `76ea5e2b7df61d6213382b3e9d9008a561b5199e7504a4980935ddaeadeba280`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::current_hash::root.body[15].body[2].body[0]::Return

Source: `infra/tests/test_roadmap_project.py:35`; AST `4db8d123c31fdf79de360a1e5fb683217b61479f161e9eca471eaa5bd80dca02`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Return evaluation at root.body[15].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::current_hash::root.body[15].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:35`; AST `6620dd0b96aea2e1bd9d1b3e73989f4a9a28f09fc774e55e775b07e4aad2a765`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::current_hash::root.body[15].body[2].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_project.py:35`; AST `4b44c8c8e79e5efbcbe2ba59516a92731c54aa12c3a732915c0fa3affe4e9071`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:37`; AST `852c5d016484c2589e7545b5ac4c4534778efa42c5dcd021bcb2e9cb60793648`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, project_into_record, self, str, value. Outputs/bindings: value.
Calls/effect boundaries: project_into_record, self.adapter.read, self.adapter.update, self.assertEqual, self.current_hash, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:38`; AST `20d9a9dfd57181fa6c6b78bb503f90aaefa6c7f6fbe1b652fad67461244f8fbc`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:38`; AST `91823e44c21c71811b931cac23fbaae74684e03d82985213f3ac74eacfe2d9da`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_project.py:40`; AST `411d74731fc4df4dc599d9f32f1b8442e077554c3bc7f3b9247d0c2d624bed27`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:40`; AST `23ee6f072b51531c41928e41bd3f2cf346045edcb52f0a0ce4a62c936badc37b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[1].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_project.py:40`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_project.py:41`; AST `360309b3802d7cc3abef3d3b56e531fdf77ac11072f74506d35511d43974fec9`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project_into_record, self. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_project.py:41`; AST `525a793dcf5941f4e43fc807540b9a8ec45b23b57c3303ea580e75df674f7078`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project_into_record, self. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[2].value.args[3]::Call

Source: `infra/tests/test_roadmap_project.py:41`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[2].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:42`; AST `f817b6caf30aea0de883909e4c643a8989d045d4cbcb217c794b711b4775d598`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project_into_record, self, str. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record, self.current_hash, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:42`; AST `7c12ac80125e39f4f3de1f7562ebca081e4d3bd9b7e1050eb23168d89eb1c16d`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project_into_record, self, str. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record, self.current_hash, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[3].value.args[1]::Call

Source: `infra/tests/test_roadmap_project.py:42`; AST `0b9fcf65d75e190233aaae3396b1367c4aa97289b2bbf6d07f1f628b3b2923c3`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[3].value.args[3]::Call

Source: `infra/tests/test_roadmap_project.py:42`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[3].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_project.py:43`; AST `767ed4cac815d46f8414cb90a65a5c2b18947f7fd84e5542242d474856210dd6`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_project.py:43`; AST `d8f09ddea4d208bafd3e1f01a30e4561b63363253234579f5f5b0a48c664eb40`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[4].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_project.py:43`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[4].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[5]::Assign

Source: `infra/tests/test_roadmap_project.py:44`; AST `7f9cdfbbc155d092cefae8db45504b6cd67f6928cb597dfb67a1957bd98a4a90`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: value.
Calls/effect boundaries: self.adapter.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[5].value::Call

Source: `infra/tests/test_roadmap_project.py:44`; AST `cc3a14ee850c8407800cb3622920c68c2cea9fe91d035b8b8f62089aaf19d1d4`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[6]::Expr

Source: `infra/tests/test_roadmap_project.py:45`; AST `4a5c70aa313096fe6220d778a50215a90b89a012459a7003bec554f2d1047755`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[6].value::Call

Source: `infra/tests/test_roadmap_project.py:45`; AST `a912bd50908051307000d85e81be84ce5b5b32393ecfea9dac3b70a48f1b781e`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[7]::Expr

Source: `infra/tests/test_roadmap_project.py:46`; AST `b696cd4c47ef540c6478114c3562c7e8de2b1dd9b9580fafe2b5b1b7cae06f65`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[7].value::Call

Source: `infra/tests/test_roadmap_project.py:46`; AST `ad04a60351852228a0b684827beaebeff8d9a5f5368104dffcf363a104ce44eb`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[8]::Expr

Source: `infra/tests/test_roadmap_project.py:47`; AST `4d07a1853bc082f17d2aa5711131af6e1ea35da2df64ab660ba9619b769d0451`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[8].value::Call

Source: `infra/tests/test_roadmap_project.py:47`; AST `d669cf76cbefddd9a2587893b68853a3095341c0d6e7e003dbffdd8bc48ff69b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[9]::Expr

Source: `infra/tests/test_roadmap_project.py:48`; AST `1c79133279f167ef307ee37481d003cd501ce91260a380c062deabced7be61bd`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_inventory_projection_and_execution_share_one_recovery_owner::root.body[15].body[3].body[9].value::Call

Source: `infra/tests/test_roadmap_project.py:48`; AST `bf28ddb021b42a9275af5600cdff33735c5daa9b596e5be89b6ab68d0b33c870`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:50`; AST `28cedadb572b10cfb3bda87cd79dd4d0aed6d0091900cc92873fd180291642c6`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, self, stale. Outputs/bindings: stale.
Calls/effect boundaries: self.adapter.read, self.adapter.update, self.assertEqual, self.assertRaisesRegex, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:51`; AST `18af4f7bb1b77373aebc5e630882e7d741036b81e8ce15e7e639b531f266bcef`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:51`; AST `0c4c93a1a0e2b10b78914141bd0c01495278c517918bd2972156df8d2741f092`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_project.py:52`; AST `6e9aca1c98846981ecebbc11414b05202434575b70d53020ded0f28f12000200`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: stale.
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:52`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_project.py:53`; AST `17a7b932aea9acca2f62765e7371d1a4970370ce83106187a00a65fc9c689fe2`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_project.py:53`; AST `502d993b3613d194b46941f9de75102a0f3aa4a2cd31c67d677cc7a87cfa1ea1`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[3]::With

Source: `infra/tests/test_roadmap_project.py:54`; AST `603a8386d4dac6f709108c46e3f74dc90e7b86887d11b74c04c43c1cbb4c0db9`.

Rust module: `infra::tests::test_roadmap_project`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:54`; AST `e16b6714be843557c632915c8a5e902f1a29362d048f78ea758c718edaebec84`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:55`; AST `de23c7c75531f305d2c191b765557e3b08ae8d7a05c236ebdb732260c6c4d655`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:55`; AST `4b31e43f7e0f77857a805ddad545c4eff33ba57051c29605e45f56bb4b996128`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[4]::Expr

Source: `infra/tests/test_roadmap_project.py:56`; AST `8fa0b51ae11952fb2faf9cd9335b91f3ff3ac7b329f80dedadde873d134f3530`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_project.py:56`; AST `df127cae3032c7cfaf9b31333f8b928d3fb2b04fbe3a4d11bfb3df07fe569249`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_stale_update_cannot_replace_concurrent_data::root.body[15].body[4].body[4].value.args[0].value::Call

Source: `infra/tests/test_roadmap_project.py:56`; AST `cc3a14ee850c8407800cb3622920c68c2cea9fe91d035b8b8f62089aaf19d1d4`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:58`; AST `db1309a4056ddbbd5d239f49345968448c66277695bc9b126373890d590bb4a5`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, atomic_write_json, before, record, self. Outputs/bindings: before, record.
Calls/effect boundaries: atomic_write_json, self.adapter.update, self.assertEqual, self.assertRaises, self.current_hash, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0]::For

Source: `infra/tests/test_roadmap_project.py:59`; AST `f2d37f130c9b9a8ea5c8090928a2a240eeeb9d2bb36df1ca7ea645888d40b513`.

Rust module: `infra::tests::test_roadmap_project`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, atomic_write_json, before, record, self. Outputs/bindings: before, record.
Calls/effect boundaries: atomic_write_json, self.adapter.update, self.assertEqual, self.assertRaises, self.current_hash, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[15].body[5].body[0]; no call, error or mutation may be omitted. Iteration: record in ({'schema': 99, 'project': 'Aegis'}, {'schema': True, 'project': 'Aegis'}, {'schema': 1, 'project': 'Aegis', 'canonical_writer_transaction_name': 'another-writer'})
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:61`; AST `4a1ffdad981f358df29062b688d596696064f922205ad07cfc341ca09ac62214`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:61`; AST `2907e6b4ab0b192b9b603d0f137f7229ba7432576195f1c558b792cffae12224`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_project.py:62`; AST `fb36c80292e088333513ded7843bebbff894f7c075cf63c25bd5d378dc76b6aa`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: before.
Calls/effect boundaries: self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:62`; AST `4b44c8c8e79e5efbcbe2ba59516a92731c54aa12c3a732915c0fa3affe4e9071`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[2]::With

Source: `infra/tests/test_roadmap_project.py:63`; AST `36591bca70182e956273b5278fc5847ea04b9b8a0a078a52b4d1c49ba7c44c13`.

Rust module: `infra::tests::test_roadmap_project`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.assertRaises, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[5].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:63`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:64`; AST `18a42deed706ae23a927b2825ec04fae3c5f99fb3a17d647d057afec77a9c4ed`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:64`; AST `396b71be28a15eccb00408f881896795635066b5d333cb1d97faf2332f33cdd5`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[2].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_project.py:64`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[2].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:65`; AST `309460a17f8181e6e48580dfa6450cf77c0c458fd896870962614bb389009a24`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:65`; AST `1da07d80395353e7f7ba38b75791166af3774f010aed01ffa7eaeddea1622cd7`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_unknown_version_or_changed_writer_requires_explicit_migration::root.body[15].body[5].body[0].body[3].value.args[1]::Call

Source: `infra/tests/test_roadmap_project.py:65`; AST `4b44c8c8e79e5efbcbe2ba59516a92731c54aa12c3a732915c0fa3affe4e9071`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:67`; AST `337741109ae2670c566d5e33b4931024100be51a56b726b2c5d085e20603c161`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, ProjectAdapter, adapter, self. Outputs/bindings: adapter.
Calls/effect boundaries: ProjectAdapter, adapter.describe, adapter.update, self.assertFalse, self.assertRaisesRegex, self.assertTrue, self.path.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_project.py:68`; AST `d33853eda43247156245cacef2d5420d6d2e65dbbc94616ca8c9e01c3b9d973b`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, self. Outputs/bindings: adapter.
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:68`; AST `c06326070b1c4cbaace830ad3a9730d710e074d86aa781085778d3d88edc3d61`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_project.py:69`; AST `24f16c76518351295f1e0c46a76ddaa5f54c71a83cdf3a937afbe2dc9deae163`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter, self. Outputs/bindings: (none).
Calls/effect boundaries: adapter.describe, self.assertTrue.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:69`; AST `9047f432712891725f65aecc90344131e5fb95982f8c8f46da09bd8e820d8489`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter, self. Outputs/bindings: (none).
Calls/effect boundaries: adapter.describe, self.assertTrue.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_project.py:69`; AST `5292e9f6bcd8f1d96f656b6f9b862840f4e9dde58f6935f6f5fafcb2bba725b1`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.describe.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[2]::With

Source: `infra/tests/test_roadmap_project.py:70`; AST `22f664e174cd1f709f049e68a84e0cb41826a6487c217bc8ffe79cda95322e10`.

Rust module: `infra::tests::test_roadmap_project`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, adapter, self. Outputs/bindings: (none).
Calls/effect boundaries: adapter.update, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:70`; AST `1943911189024f152ce839bd9c535e74e29547cccaf5475ffcd1830b0521f55c`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:71`; AST `1c7ae771012871eade9e7bed251f073ce8a213417b28af6ee06f95c67592a1d1`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:71`; AST `217d36ed44b016465d9c2368b2538a7be414edebbdff1c30878a5b14ec182068`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:72`; AST `0cc3230db6b9b869bc2a6998d1a7a8ce629c2f75624cc9ca3793d88fef25759d`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse, self.path.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:72`; AST `e4c63d4c47492c636d04bbfca8a46f70c78b1e672d465654ff1b2e187487b545`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse, self.path.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_foreign_profiles_do_not_create_a_competing_carbon_queue::root.body[15].body[6].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_project.py:72`; AST `5a0ab509baad619ec2a1ec684d6882dd1595eead8f620b398322ae10eeaa6916`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:74`; AST `0b962d2779b4ebd9ea16a0ce15118992a392d1c632058a0583b2c701df001041`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: atomic_write_json, digest, path, project_into_record, read_json, self. Outputs/bindings: path.
Calls/effect boundaries: atomic_write_json, digest, path.read_bytes, project_into_record, read_json, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[0]::Assign

Source: `infra/tests/test_roadmap_project.py:75`; AST `e270804353e184e08b113177f5741a45b50ca8b11320a7622a5b6008cd955b62`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_project.py:76`; AST `4e46c4e37b2b5ae9051b49e6d078d8d6acf385e9d571cc4c9927558e76ceb458`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:76`; AST `0749d9a4c0a53059da53e7e83b5bf395fb9e914a32ee9e84d6127d3b94388c33`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[2]::Expr

Source: `infra/tests/test_roadmap_project.py:77`; AST `d9709ef40a6407b57cd8a9e4de93f5e5c885a99607ca926c11efd9855da5ebfe`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, path, project_into_record, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, project_into_record.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_project.py:77`; AST `105ee9797ee5470fbbfa2b79c8cda9e2be5d5d68643eef9c8e3f86c2b9af4e75`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path, project_into_record, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, project_into_record.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[2].value.args[3]::Call

Source: `infra/tests/test_roadmap_project.py:77`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[2].value.args[3].args[0]::Call

Source: `infra/tests/test_roadmap_project.py:77`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].value.args[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:78`; AST `1a5e09c72297209c7302e1ea5154390f2e3d8d680a869f2e3d27aac46a2d2b13`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:78`; AST `d58a0310461dfb571ba5e81db63b038307c55c3605002e4b1014a60b65e61662`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_generic_projection_keeps_its_existing_nonproject_contract::root.body[15].body[7].body[3].value.args[0].value::Call

Source: `infra/tests/test_roadmap_project.py:78`; AST `ca2a99ec0b14545aba864c1e6b22415e5a02ad33955de7320b863aa9c805bfcd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:80`; AST `3a07e700ba8ca48c34279ba3afe68ca7e540223677fc236ad2eb49b4b7faa886`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, WorkspaceLease, cases, changed, copy, execution, lease, owner, self. Outputs/bindings: cases, changed, execution, lease, owner.
Calls/effect boundaries: WorkspaceLease, cases.append, copy.deepcopy, lease.acquire, lease.release, self.adapter.read, self.adapter.update, self.assertEqual, self.assertRaises, self.assertRaisesRegex, self.current_hash, self.subTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[0]::Assign

Source: `infra/tests/test_roadmap_project.py:81`; AST `412626dbce372a362795421fe3888ef6116ecd170c9caccf92a1ff296520a3bf`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, self. Outputs/bindings: lease.
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:81`; AST `408829ac552086ff1aa49ed525f89889a9374a77ff0f5e75e1759a09776c7b06`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[1]::Assign

Source: `infra/tests/test_roadmap_project.py:82`; AST `09395ad02d2d665903909cea0b3b837b660087ffcd7ffdd32020e73fa634f25c`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: owner.
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:82`; AST `863b20df2fe3a796c5e8389ca119063f61b97671173a0c0e534d8cb37182cbf8`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[2]::Assign

Source: `infra/tests/test_roadmap_project.py:83`; AST `f1195200c21fc0c54dcacbacc71977cab9ed51cbef1a2a87633fce1ce9fd263a`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner. Outputs/bindings: execution.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:86`; AST `53ce37d61f4e26cae51f154b77d9ef9fb4bf0b8782378c65f112fac29e036871`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:86`; AST `4c095ef6e775ced7a9a0c388ea627dd76af6f875702d865ab06cab04af8168aa`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[4]::Assign

Source: `infra/tests/test_roadmap_project.py:87`; AST `94b78388342bce9ce07ab9a0596bccbbeba71dfca30933684a6682ceab121dc3`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: cases.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[5]::Assign

Source: `infra/tests/test_roadmap_project.py:88`; AST `18886f99fba2b6518fad36ed8f102fd77860a66e7ff5e3f6a370a3e782ab12d5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, execution. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[5].value::Call

Source: `infra/tests/test_roadmap_project.py:88`; AST `f6248815ebb8988a975fb44c6516e1f448f1fbf9cc1bb15bddf5bd1c22a07837`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, execution. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[6]::Assign

Source: `infra/tests/test_roadmap_project.py:88`; AST `37f26591e72d64376964a1c868597a30727bcada28966626a4ddca43af191ba0`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[7]::Expr

Source: `infra/tests/test_roadmap_project.py:88`; AST `e4ea45dc3ed8e22a4c7153281b19c72698aca277efab34c044a873d5db138680`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[7].value::Call

Source: `infra/tests/test_roadmap_project.py:88`; AST `11b1ecc2b57e9a1656a7dd8749f6956ac612abe722672cc92f23e80af4b63d4b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[8]::Assign

Source: `infra/tests/test_roadmap_project.py:89`; AST `18886f99fba2b6518fad36ed8f102fd77860a66e7ff5e3f6a370a3e782ab12d5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, execution. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[8].value::Call

Source: `infra/tests/test_roadmap_project.py:89`; AST `f6248815ebb8988a975fb44c6516e1f448f1fbf9cc1bb15bddf5bd1c22a07837`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, execution. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[9]::Assign

Source: `infra/tests/test_roadmap_project.py:89`; AST `f62b0e5698ff7e3d403ea4fe4b1a6fecfc61fb7b6d7a70c0bd529b0e3650ca24`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[10]::Expr

Source: `infra/tests/test_roadmap_project.py:89`; AST `e4ea45dc3ed8e22a4c7153281b19c72698aca277efab34c044a873d5db138680`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[10].value::Call

Source: `infra/tests/test_roadmap_project.py:89`; AST `11b1ecc2b57e9a1656a7dd8749f6956ac612abe722672cc92f23e80af4b63d4b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[11]::Assign

Source: `infra/tests/test_roadmap_project.py:90`; AST `18886f99fba2b6518fad36ed8f102fd77860a66e7ff5e3f6a370a3e782ab12d5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, execution. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[11].value::Call

Source: `infra/tests/test_roadmap_project.py:90`; AST `f6248815ebb8988a975fb44c6516e1f448f1fbf9cc1bb15bddf5bd1c22a07837`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, execution. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[12]::Assign

Source: `infra/tests/test_roadmap_project.py:90`; AST `316ffb543b4ffee5ec0ae0c65be30e4a9b04e0978f4f75baab05873654280829`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[13]::Expr

Source: `infra/tests/test_roadmap_project.py:90`; AST `e4ea45dc3ed8e22a4c7153281b19c72698aca277efab34c044a873d5db138680`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[13].value::Call

Source: `infra/tests/test_roadmap_project.py:90`; AST `11b1ecc2b57e9a1656a7dd8749f6956ac612abe722672cc92f23e80af4b63d4b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[14]::Assign

Source: `infra/tests/test_roadmap_project.py:91`; AST `18886f99fba2b6518fad36ed8f102fd77860a66e7ff5e3f6a370a3e782ab12d5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, execution. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[14].value::Call

Source: `infra/tests/test_roadmap_project.py:91`; AST `f6248815ebb8988a975fb44c6516e1f448f1fbf9cc1bb15bddf5bd1c22a07837`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, execution. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[15]::Assign

Source: `infra/tests/test_roadmap_project.py:91`; AST `b60040148d0175477e1afc250c8d119323991a57346ec0e95d712cef40aad9ef`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[16]::Expr

Source: `infra/tests/test_roadmap_project.py:91`; AST `e4ea45dc3ed8e22a4c7153281b19c72698aca277efab34c044a873d5db138680`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[16].value::Call

Source: `infra/tests/test_roadmap_project.py:91`; AST `11b1ecc2b57e9a1656a7dd8749f6956ac612abe722672cc92f23e80af4b63d4b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[17]::Assign

Source: `infra/tests/test_roadmap_project.py:92`; AST `18886f99fba2b6518fad36ed8f102fd77860a66e7ff5e3f6a370a3e782ab12d5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, execution. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[17].value::Call

Source: `infra/tests/test_roadmap_project.py:92`; AST `f6248815ebb8988a975fb44c6516e1f448f1fbf9cc1bb15bddf5bd1c22a07837`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, execution. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[18]::AugAssign

Source: `infra/tests/test_roadmap_project.py:92`; AST `1842ea8b777013e908e14316242e61b704cf452aa427cdd84b6a35a08fbe4f85`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered AugAssign evaluation at root.body[15].body[8].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[19]::Expr

Source: `infra/tests/test_roadmap_project.py:92`; AST `e4ea45dc3ed8e22a4c7153281b19c72698aca277efab34c044a873d5db138680`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[19].value::Call

Source: `infra/tests/test_roadmap_project.py:92`; AST `11b1ecc2b57e9a1656a7dd8749f6956ac612abe722672cc92f23e80af4b63d4b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, changed. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20]::For

Source: `infra/tests/test_roadmap_project.py:93`; AST `0864bbc50fc4c7f671bceea20a49fe2a3941804df1f956b6c3c9f7d2a1d2f410`.

Rust module: `infra::tests::test_roadmap_project`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, cases, changed, self. Outputs/bindings: changed.
Calls/effect boundaries: self.adapter.update, self.assertRaises, self.current_hash, self.subTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[15].body[8].body[20]; no call, error or mutation may be omitted. Iteration: changed in cases
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20].body[0]::With

Source: `infra/tests/test_roadmap_project.py:94`; AST `7a272259b5f1a1530579eab99a81d569f9f187accbed5551dfedee1caf884939`.

Rust module: `infra::tests::test_roadmap_project`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, changed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.assertRaises, self.current_hash, self.subTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[8].body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:94`; AST `b1d6d69649e5c18ef0038764bd97988259162a36d176c295a19dba977c1862a7`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[20].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:94`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[20].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:95`; AST `c20e2ea51b24cf451d1e3096954a4f608c8782a17f0c39bd76ece325e12ba3e6`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[20].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:95`; AST `51b3a2105d25716a7504b0a530cfa28aaff2cfa43ee4d004ec66b7f0e61c5fbf`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[20].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[20].body[0].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_project.py:95`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[20].body[0].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[21]::Expr

Source: `infra/tests/test_roadmap_project.py:96`; AST `c3f71ce5a1f29d9daa0546ee074bd114bfbcbdc811dd962d04019a9968809eb8`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[21].value::Call

Source: `infra/tests/test_roadmap_project.py:96`; AST `8598bed91be8a178cc7f63b2b837b205bc6ca2a8b7fae312aca72b1d98abf9f7`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[21].value.args[0].value::Call

Source: `infra/tests/test_roadmap_project.py:96`; AST `cc3a14ee850c8407800cb3622920c68c2cea9fe91d035b8b8f62089aaf19d1d4`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[21].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[22]::Expr

Source: `infra/tests/test_roadmap_project.py:97`; AST `51f27f68f175f168410b03e01a99a5ea1f3fb4fdbaabb5089ed61194e587b993`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease, owner. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[22].value::Call

Source: `infra/tests/test_roadmap_project.py:97`; AST `33f08fcbe408cbac32de9bea021a3da8ca4bcd49c7ffbbd298f75e95301e8e07`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease, owner. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[23]::With

Source: `infra/tests/test_roadmap_project.py:98`; AST `59df3442d95c1d11179d337c0326e37bbb47387855382a3f22cf5904b396e67f`.

Rust module: `infra::tests::test_roadmap_project`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.assertRaisesRegex, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[8].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[23].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:98`; AST `77046068d37fb8ab9b2d52f29aab64d1250f108abf27d197523900dd45a6fd33`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[23].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[23].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:99`; AST `c002aba4132de650af85393ef3b39c9f8351c2cb81617e10f322874554347053`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[23].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[23].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:99`; AST `31eda0fbf85c3076eeb83c1f1a6fb05af33fe6a99b13b2b34c7077897e4be41f`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[23].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_native_identity_history_accounting_and_lease_are_not_replaceable::root.body[15].body[8].body[23].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_project.py:99`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[23].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_project.py:101`; AST `1824308061901329c01dcfc150429dbbda711c3305eb357591e99ed4a6df0449`.

Rust module: `infra::tests::test_roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, ContractError, WorkspaceLease, compiled, current, digest, execution, inherited, lease, ledger, legacy, old, owner, recipe_scope, self, started, str. Outputs/bindings: _, compiled, current, execution, inherited, lease, ledger, legacy, old, owner, started.
Calls/effect boundaries: BudgetLedger, WorkspaceLease, digest, lease.acquire, lease.release, ledger.close, ledger.reserve, recipe_scope, self.adapter.update, self.assertEqual, self.assertRaisesRegex, self.current_hash, self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[0]::Assign

Source: `infra/tests/test_roadmap_project.py:102`; AST `44b6a6fc5b2c659adf1e86e91cb163ea9b3c4db4fc998d7e3456f514a852cf7c`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, self. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:102`; AST `7284f87df770a43bb43b821afc3c980b7c14f951534180b5361ce68c7aef3690`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[1]::Assign

Source: `infra/tests/test_roadmap_project.py:103`; AST `c453ca2215bac7e1ef85e04c01b7387d09a95f784c62a79e80b78a11c1038df0`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self, str. Outputs/bindings: legacy.
Calls/effect boundaries: digest, self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[1].value::Call

Source: `infra/tests/test_roadmap_project.py:103`; AST `eff4c725c73c240e5230f9f70d6ccaf0ddc757c2e42761540e6352190ea8918f`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[1].value.args[0].values[1]::Call

Source: `infra/tests/test_roadmap_project.py:103`; AST `4ee36b166806517fbd2f36d9a8e9f3e30ee06e71f9dfd7f45fa62881238aa607`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[1].value.args[0].values[1].args[0]::Call

Source: `infra/tests/test_roadmap_project.py:103`; AST `c98bd2b06965f3c2bd46549c755a912bb5b25cd543d9c96bf693954ed94eb929`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.root.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[1].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[2]::Assign

Source: `infra/tests/test_roadmap_project.py:104`; AST `e10a7a4d20fe223625970b2bd9e89e763416af5c455e1e2ce9f53291ca2707b5`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ledger, legacy. Outputs/bindings: old.
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[2].value::Call

Source: `infra/tests/test_roadmap_project.py:104`; AST `b3e1d1858d4d18bfc7b03bcad5d446f57f07da5e6703a68be1a246a034878534`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger, legacy. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[3]::Expr

Source: `infra/tests/test_roadmap_project.py:105`; AST `bdbcb8a4d65fe10839e0e06afdf4d47187e2e060d2bb40781a0c56f5f57d1e3b`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ledger, old. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_project.py:105`; AST `78d00353acf41c00b48f59e5a4e0584944069ad06c09a63387a4733acfba29f1`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger, old. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[4]::Assign

Source: `infra/tests/test_roadmap_project.py:106`; AST `412626dbce372a362795421fe3888ef6116ecd170c9caccf92a1ff296520a3bf`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, self. Outputs/bindings: lease.
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[4].value::Call

Source: `infra/tests/test_roadmap_project.py:106`; AST `408829ac552086ff1aa49ed525f89889a9374a77ff0f5e75e1759a09776c7b06`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[5]::Assign

Source: `infra/tests/test_roadmap_project.py:106`; AST `058c57d9e9c4c3b491ef57fcc95945e9aff84ee2dde77a5a5be4cc9f8d6eaff7`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: owner.
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[5].value::Call

Source: `infra/tests/test_roadmap_project.py:106`; AST `a5852a7afd16130b87c995ddcda78330a729b88d5a5817dcd1049ed29b6d7e1f`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[6]::Assign

Source: `infra/tests/test_roadmap_project.py:107`; AST `a2b4f604e869078c3a1f7fafb998ea47aa8d5e71a3564f50f2710a3b9acb0902`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old. Outputs/bindings: started.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[7]::Assign

Source: `infra/tests/test_roadmap_project.py:108`; AST `6993b1a358d92d3f419455e6c40bf1b44a2fbd403f90cd6c2a27c8176ab49a85`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner. Outputs/bindings: execution.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[8]::Expr

Source: `infra/tests/test_roadmap_project.py:111`; AST `944c2150e5634079352d3bcce1fc17956f010eb5f8ef3bee82f0f5ea4283d0c1`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, self, started. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[8].value::Call

Source: `infra/tests/test_roadmap_project.py:111`; AST `09e20868d2d7d7a5aef6bf02e05d783dfe64b489f534c7d2290bda2b62d96bb3`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, self, started. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[9]::Assign

Source: `infra/tests/test_roadmap_project.py:113`; AST `351cff0c945e952b69c8ce080f2b8211082fdf09d942d876ceab3d78d5bd5abb`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: compiled.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[10]::Assign

Source: `infra/tests/test_roadmap_project.py:114`; AST `22e16a8f319d02eb3d163313eefef361699e0924b5dbed24a0ad58992e1dbcb6`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ledger, recipe_scope, self. Outputs/bindings: _, inherited.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[10].value::Call

Source: `infra/tests/test_roadmap_project.py:114`; AST `a9147b39b97393a432cb5186aab061015bb0ea3dc0e60a101adfb3c3691b9d3a`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, ledger, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[11]::Expr

Source: `infra/tests/test_roadmap_project.py:115`; AST `ae7bc6b6452522b6670d946e393d6e451f6d3e0c364968d0966b8529e1c708fc`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inherited, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[11].value::Call

Source: `infra/tests/test_roadmap_project.py:115`; AST `76de43e9f698802aa12267e16d2624e550e63a9ac48748839e7749b767b2d5c6`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inherited, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[12]::Assign

Source: `infra/tests/test_roadmap_project.py:116`; AST `ba76991645203a452802808c8daf550525e3f99b0e61a37ed171e46833eeaa51`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ledger, legacy. Outputs/bindings: current.
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[12].value::Call

Source: `infra/tests/test_roadmap_project.py:116`; AST `d1ce35217ee699a507dfb4e60eb4007b60a6d4228792ccd27247716bae7ea00e`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger, legacy. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[13]::Expr

Source: `infra/tests/test_roadmap_project.py:117`; AST `76289345752b664f3218da41aa2b27b167d04d3c88fc49eaabcff60ea2c6a59b`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[13].value::Call

Source: `infra/tests/test_roadmap_project.py:117`; AST `f4e9effdfef12808d3fbb88e790862475d80f7585e0584e2480fd330734b2a38`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[14]::Assign

Source: `infra/tests/test_roadmap_project.py:118`; AST `22e16a8f319d02eb3d163313eefef361699e0924b5dbed24a0ad58992e1dbcb6`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ledger, recipe_scope, self. Outputs/bindings: _, inherited.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[14].value::Call

Source: `infra/tests/test_roadmap_project.py:118`; AST `a9147b39b97393a432cb5186aab061015bb0ea3dc0e60a101adfb3c3691b9d3a`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, ledger, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[15]::Expr

Source: `infra/tests/test_roadmap_project.py:119`; AST `8abc240f5a6eb870c68dab7b683b18461d2ecb96672f84bd8e3a16128de6bb17`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, inherited, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[15].value::Call

Source: `infra/tests/test_roadmap_project.py:119`; AST `9fc5724730eb9adec1e5311f96e80cc183931447ddc0651c6eed2d4a8386eada`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, inherited, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[16]::Expr

Source: `infra/tests/test_roadmap_project.py:120`; AST `8d59d293304199bf12a3198f67b59dc268f6f7e1ee1ab977615a4ea03b5301a1`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[16].value::Call

Source: `infra/tests/test_roadmap_project.py:120`; AST `ed6f73126880b5c8c25a88afee39af2a8657e2eb21e717df29e459c6f48f1f2b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.adapter.update, self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[16].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_project.py:120`; AST `0072c1a6d1ad294a66253cdf3b273b69fb35b738c18a29c1a788f3c4273d13bd`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.current_hash.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[16].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[17]::With

Source: `infra/tests/test_roadmap_project.py:121`; AST `42e3727e18ca975e40f0581b0be1dbee74b86994b5ca857c2b78f55eab0edfb9`.

Rust module: `infra::tests::test_roadmap_project`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, compiled, ledger, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[9].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[17].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_project.py:121`; AST `72ca4cc12070417261311db5d0cd5af8e829c14e767832a57c704171ab40e4c8`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[17].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[17].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:122`; AST `f1aa2c2013cddbf30129bde2d3f2f973f033e2bdc067f6b213824ea2aeb42184`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ledger, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[17].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:122`; AST `a9147b39b97393a432cb5186aab061015bb0ea3dc0e60a101adfb3c3691b9d3a`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, ledger, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[18]::Expr

Source: `infra/tests/test_roadmap_project.py:123`; AST `3ef167ba66b494648731c2de445c0122308ba8736631a03da4604cd435da9620`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease, owner. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::ProjectAdapterTests::test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime::root.body[15].body[9].body[18].value::Call

Source: `infra/tests/test_roadmap_project.py:123`; AST `bfe95f424e2e8db7c07f9df086c84abe753f133ca3eac3bcc62600a835e5eb0b`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease, owner. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[16]::If

Source: `infra/tests/test_roadmap_project.py:126`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[16]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[16].body[0]::Expr

Source: `infra/tests/test_roadmap_project.py:127`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_project.py::module::root.body[16].body[0].value::Call

Source: `infra/tests/test_roadmap_project.py:127`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap, agentinfra.roadmap_lease, agentinfra.roadmap_project, agentinfra.roadmap_records, agentinfra.roadmap_runtime, copy, pathlib, shutil, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
