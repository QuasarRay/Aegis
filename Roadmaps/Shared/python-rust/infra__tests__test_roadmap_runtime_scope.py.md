# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 124. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_runtime_scope.py::module::root::Module

Source: `infra/tests/test_roadmap_runtime_scope.py:1`; AST `01e469759a41215887bdde3373a9910ae32fff2e6a9275bb2f6ef7c084880d8a`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, ContractError, Path, WorkspaceLease, __file__, __name__, a, ancestors, atomic_write_json, before, compiled, current, digest, lease, legacy, new, old, owner, path, recipe_scope, record, restarted, self, state, str, sum, sys, tempfile, unittest, work. Outputs/bindings: a, ancestors, before, compiled, current, lease, legacy, new, old, owner, path, record, restarted, state, work.
Calls/effect boundaries: BudgetLedger, Path, Path(__file__).resolve, WorkspaceLease, atomic_write_json, digest, lease.acquire, lease.release, recipe_scope, restarted.read, restarted.reserve, self.assertEqual, self.assertNotEqual, self.assertRaisesRegex, self.ledger.close, self.ledger.read, self.ledger.reserve, self.root.resolve, self.temp.cleanup, str, sum, sys.path.insert, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[0]::ImportFrom

Source: `infra/tests/test_roadmap_runtime_scope.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_runtime_scope.py:3`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_runtime_scope.py:4`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_runtime_scope.py:5`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_runtime_scope.py:6`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[5]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:8`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[5].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:8`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[5].value.args[1]::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:8`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[5].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:8`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[5].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:8`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_runtime_scope.py:9`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[7]::ImportFrom

Source: `infra/tests/test_roadmap_runtime_scope.py:10`; AST `7e9c3f5290a99e55259b83ed615988e11578a991178ada162c503777b0b68347`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_roadmap_runtime_scope.py:11`; AST `5b90894d096758c9f19f8600da372bc7cd3d8c63d0642e575f9761c8cc9880e1`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_runtime_scope.py:12`; AST `3367960b9408d9ad78b9ae529c9afc616ef20136b6286eb07310bc757747ba05`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::root.body[10]::ClassDef

Source: `infra/tests/test_roadmap_runtime_scope.py:15`; AST `95650d1f7f7dc96a7fb6fe25bf665fb9a8e42628e03e1467cd2c395df20ef384`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: BudgetLedger, ContractError, Path, WorkspaceLease, a, ancestors, atomic_write_json, before, compiled, current, digest, lease, legacy, new, old, owner, path, recipe_scope, record, restarted, self, state, str, sum, tempfile, unittest, work. Outputs/bindings: a, ancestors, before, compiled, current, lease, legacy, new, old, owner, path, record, restarted, state, work.
Calls/effect boundaries: BudgetLedger, Path, WorkspaceLease, atomic_write_json, digest, lease.acquire, lease.release, recipe_scope, restarted.read, restarted.reserve, self.assertEqual, self.assertNotEqual, self.assertRaisesRegex, self.ledger.close, self.ledger.read, self.ledger.reserve, self.root.resolve, self.temp.cleanup, str, sum, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_runtime_scope.py:16`; AST `3d83f452ebfa993f7b4614f4d9f68aaf3c9b6fab1d7b36483794612d296a6958`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, Path, self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger, Path, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:17`; AST `76bde1458ae912172e4121d6d32a40d02cf372c4db6ead9b5af171facc2865c2`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:17`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:18`; AST `3fd62e96028b079a923df6e9a7c1c1df8b3ae2536d55ba9d4f31f162d4d5ddb5`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:18`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:19`; AST `0d67268bd300c14f31cd018011813e9e284609af1d00652ea2cb1190bc55e310`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::setUp::root.body[10].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:19`; AST `7284f87df770a43bb43b821afc3c980b7c14f951534180b5361ce68c7aef3690`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::tearDown::root.body[10].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_runtime_scope.py:21`; AST `13fc628cded8f8def9f296b061b0d1b4f129ada0770d009511b176b914c63004`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::tearDown::root.body[10].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:22`; AST `03b3f025b568ce93e3252b0f1f4a5ce0348dbf2ecebaae9a0913927af51d7b24`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::tearDown::root.body[10].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:22`; AST `467d2c9d775dc88f51613c917ddb5ec5487d5c87293666d9c9c5f9a88375b66b`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_runtime_scope.py:24`; AST `8c5b6ced29863cffdb502890b994964258e74becc8d8a543748fea04fe482a5e`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, ContractError, a, new, old, restarted, self, sum. Outputs/bindings: a, new, old, restarted.
Calls/effect boundaries: BudgetLedger, restarted.read, restarted.reserve, self.assertEqual, self.assertRaisesRegex, self.ledger.close, self.ledger.reserve, sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:25`; AST `aa906cd7b2033042269d853baa849b00c55eceac0d336a290f2da96ce8cf16ff`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: old.
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:25`; AST `d4bd80a495b7b1d566e1dc1119108f5061512110dd426c57f4a6e368d7b237f0`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:26`; AST `f7aef6b05d8834071e2b56cc22c7719b00d0785c87193740bf3be670ab80bdac`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:26`; AST `4cf5d0d026d175dfb6c803228aa6904457256223c9442b4c70070c65608d13c2`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[2]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:27`; AST `e734da4e3bf644fe33dd634c6302ac66e9df93fec7274d97019e09ddd6d98fe9`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: new.
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:27`; AST `fed9744e25c6cdcac4e4599b4b475d889be7fe63d875f6b5a2055e782a690ce8`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:29`; AST `08cb1fcd849bc66bba95c0be846c043dd914688b3dee2cdbff1206be9408b5b8`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: new, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:29`; AST `3cdf460f311936b45e896f84e61c73f726bae4aa043723feca72ccced5013897`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: new, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[4]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:30`; AST `669c8e00c1182612b074f7435f9292970d4223441730897e556659e62bd1bacd`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, self. Outputs/bindings: restarted.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:30`; AST `7284f87df770a43bb43b821afc3c980b7c14f951534180b5361ce68c7aef3690`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[5]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:31`; AST `f2be207aaddb78a97304b14504c5d8f29b0c0ec9a5395f10c0963e6407a25eaf`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, restarted, self. Outputs/bindings: (none).
Calls/effect boundaries: restarted.reserve, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:31`; AST `3f193d7e6826ba9de1415d7dee5340172610b6552eac915a116e6da04b66326a`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:32`; AST `5bf44bf1b3adf58a27fb4ccfac55731f02482b045788c59de58092e6360b2be6`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: restarted. Outputs/bindings: (none).
Calls/effect boundaries: restarted.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:32`; AST `d908f24cc7e5cd5574e5291118911f53ed5bea4b0bf2b25db8b603a21d4878e1`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: restarted. Outputs/bindings: (none).
Calls/effect boundaries: restarted.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[6]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:33`; AST `602ff503963e488f4d271523cc8128cc86a9cc43ed38e5c06108da67f09d3d16`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, restarted, self, sum. Outputs/bindings: a.
Calls/effect boundaries: restarted.read, self.assertEqual, sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[6].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:33`; AST `a63625e14c81697d996b22d0a36480052b5da1764e0bc5bd86f70d13ef4d89d4`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, restarted, self, sum. Outputs/bindings: a.
Calls/effect boundaries: restarted.read, self.assertEqual, sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:33`; AST `7a397a683e76f4f50e23e83923abf40eab8ea49e31fac9738d105d60fea992a1`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, restarted, sum. Outputs/bindings: a.
Calls/effect boundaries: restarted.read, sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[6].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_runtime_scope.py:33`; AST `342aaf71c06e4a77b3eb03671c44eaa9eb35607c0041aee6350f30c6b141b58e`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, restarted. Outputs/bindings: a.
Calls/effect boundaries: restarted.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[2].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[6].value.args[0].args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:33`; AST `e7e2f0d6a5a66e38a21ca90e12b282a7d335020472a663306b329471c600196e`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: restarted. Outputs/bindings: (none).
Calls/effect boundaries: restarted.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[6].value.args[0].args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[7]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:34`; AST `05d0727ea5bb025060c6ee7ce7e3695976d6a274e80858183e1063ed75b16ad0`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: restarted, self. Outputs/bindings: (none).
Calls/effect boundaries: restarted.read, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[7].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:34`; AST `ef416cf36a44e5c53b11b325e621d07626969acb6f4c818aa5e519580d0f1cea`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: restarted, self. Outputs/bindings: (none).
Calls/effect boundaries: restarted.read, self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases::root.body[10].body[2].body[7].value.args[0].value.value.value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:34`; AST `e7e2f0d6a5a66e38a21ca90e12b282a7d335020472a663306b329471c600196e`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: restarted. Outputs/bindings: (none).
Calls/effect boundaries: restarted.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[7].value.args[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_runtime_scope.py:36`; AST `b3c48f59d342d6c6395c1ff22c0e445fd2262e0756122729a54fd11098de8a61`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, old, self. Outputs/bindings: old.
Calls/effect boundaries: self.assertRaisesRegex, self.ledger.close, self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:37`; AST `a90eece88f26b9ddbca662f0022173c9a9666d1627a191b98d124d3c54d6caec`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: old.
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:37`; AST `5c12949e3f3141b097b09a9c2cfab6a548d57693c67188defaad164864d5a446`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[1]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:38`; AST `92fdc37d28a33ed974099473cff687e463439f39f132a35d03d5b9e7e4901ff9`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:38`; AST `bae23e19cbcae2d9f57577e56bfb78fe4461e33120c6df98c923494182b33ff1`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:39`; AST `e987fc9a426a836da217d1a1e9587281eceb751fde55b7f9a203b265cc201aec`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:39`; AST `dc50420ca2afaee3d09b4cf588f016ff99bc4b369c914b6992c7988ccbaf96ed`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:40`; AST `68e74063e29c24cbbd924d8a3c93292272863ad911432bf2fd5f605305480a03`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:40`; AST `d020869f202bef8b7daabb6a52bc3d9007ee94728b7f7813fa42a1042796d34c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[3]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:41`; AST `df0d7e5e05a4507a041bc2826f56f3bae3b1b4369813838ea39d9806d3134abb`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:41`; AST `1519638af8156a07f9390f0937549143a22f1054e875188be758ca77d8e77d4c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:42`; AST `f424a08d48be65520822870443a80e11e57e4a967dc5eb92973e2f6b98b75796`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_inherited_success_and_unresolved_work_cannot_be_dispatched_again::root.body[10].body[3].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:42`; AST `6f14dcc32343df7dd4d18acdb87df4e6c5c06274cefe2d3543f1a560db710e0c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_runtime_scope.py:44`; AST `31d13a2d5b5dd85c6dd2e767f7942e998f81c6d9da36195ff382eed5b4330eea`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, old, self. Outputs/bindings: old.
Calls/effect boundaries: self.assertRaisesRegex, self.ledger.close, self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[0]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:45`; AST `4f4f9b03d94f856a7b34e601d2a274b55d3c719c94bae2d58b5c67c56cecfa47`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:45`; AST `52b968ab403114afb968212d11a9ed51e1e02a9ef8db34763125471f94762868`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:46`; AST `282d6af6246b2d3d4b98d2e4540a2c1b7b6201f7bc83afd177814eee608c948c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:46`; AST `cb7876eff6c949782dfb8a232e3ae4095f2036506600673117b3e31e2c157dcc`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:47`; AST `a90eece88f26b9ddbca662f0022173c9a9666d1627a191b98d124d3c54d6caec`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: old.
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:47`; AST `5c12949e3f3141b097b09a9c2cfab6a548d57693c67188defaad164864d5a446`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:48`; AST `f9df1c9afbc6118c054a00a802fac5118bcbd1d25f4bd41a27f1af59e2dd3efa`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:48`; AST `859e438e672a14d08f49052b72a73bc1d53712ae5c06613c06084b6f965795b9`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[3]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:49`; AST `35c9bc31eb2c141ec472897701ab53389143bf11b06411e43317781a2c005678`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:49`; AST `940e78b24e00f064d028b8522929e76a19de94f0fd338e49baae8b59b7a7d6f3`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:50`; AST `093176ed99e3e52efbff1031a7714d8747022d3f44900c8be07f709f1b93c7e9`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected::root.body[10].body[4].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:50`; AST `5a1e467b8227f6ed8d7be2e0867fe3691a9f320a3585f2df4c739a6e2b0b30e9`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_runtime_scope.py:53`; AST `46bbee7fc3426f65205009981624eb2b1208039c3c88eeb632cf4177e9de3c9e`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, WorkspaceLease, ancestors, atomic_write_json, before, compiled, current, digest, lease, legacy, owner, path, recipe_scope, record, self, state, str, work. Outputs/bindings: ancestors, before, compiled, current, lease, legacy, owner, path, record, state, work.
Calls/effect boundaries: WorkspaceLease, atomic_write_json, digest, lease.acquire, lease.release, recipe_scope, self.assertEqual, self.assertNotEqual, self.assertRaisesRegex, self.ledger.close, self.ledger.read, self.ledger.reserve, self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:54`; AST `c453ca2215bac7e1ef85e04c01b7387d09a95f784c62a79e80b78a11c1038df0`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self, str. Outputs/bindings: legacy.
Calls/effect boundaries: digest, self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:54`; AST `eff4c725c73c240e5230f9f70d6ccaf0ddc757c2e42761540e6352190ea8918f`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[0].value.args[0].values[1]::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:54`; AST `4ee36b166806517fbd2f36d9a8e9f3e30ee06e71f9dfd7f45fa62881238aa607`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.root.resolve, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[0].value.args[0].values[1].args[0]::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:54`; AST `c98bd2b06965f3c2bd46549c755a912bb5b25cd543d9c96bf693954ed94eb929`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.root.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[1]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:55`; AST `450aa839bb091a4d1c5fa47987374af7ddd35128601c1cb97b576dadfa3955d7`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: legacy, self. Outputs/bindings: before.
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:55`; AST `97da111cd09f433d55651451fac9927aea8b61da263d76e38a173b24a02fb939`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: legacy, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:56`; AST `09e7cbff2b380da75a7aa8247c566c14365d1b11001a21c8ccb4cc15fb4376d9`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:56`; AST `1f9b0e7d988191bf1e95841cecb5bb4f94c1000d6b3e7f8606708230a41a770c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[3]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:58`; AST `4d0a8429d253b313c12841e9977d6fdbaca313c2d2184b68ee9648a6ae2a2f38`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: state.
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:58`; AST `c6af2442a0b071aa928cdefcc4844536c71f08d8b2b793d626686c0669653f01`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[4]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:59`; AST `e4bcf9f4c808c8dbb9fa48e32fd1d5c31023cc05e0639b299ed6d3fa11b7ff01`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[5]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:60`; AST `0895b9169da445a29c83ba13d625f439db62f562cc938ff1445f1e60ab3f4546`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, self, state. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[5].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:60`; AST `130e0f6311304de78ac8d2113b39953694667488b8f546232bb15d4914198129`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, self, state. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[6]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:61`; AST `9102184d42bee34227c2dc6b52b131570a52a53d51e95417c85a55906e75fdd2`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: legacy, self. Outputs/bindings: current.
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[6].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:61`; AST `7b5473652e880364785a97c4d2c7f55c0c052987c0d0b6af2a6466f565cee909`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: legacy, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.reserve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[7]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:62`; AST `81b8b6b5a0dd060f05d7dbb77613aaff8068d98bca78b7fce7822ef14ecd1ced`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[7].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:62`; AST `7e7c261cf12e68e1bdbcabac9b3ad1883484f5e58c4746d5d3cd2711a99ef604`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.close.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[8]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:63`; AST `412626dbce372a362795421fe3888ef6116ecd170c9caccf92a1ff296520a3bf`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, self. Outputs/bindings: lease.
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[8].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:63`; AST `408829ac552086ff1aa49ed525f89889a9374a77ff0f5e75e1759a09776c7b06`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[9]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:64`; AST `7475ad6025ddae36f9e1ee723fe3c5f88c61ed3ce3042b323b84dafe2623156c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: owner.
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[9].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:64`; AST `846f5213a3f0c957ce45d4b1c8102325f69cae8a0612cf942b2a4bdfadcfb1b2`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[10]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:65`; AST `7fb42dd8424742789e57d694e94d0f4f1e4af245f40257d2745bc245f0936e2d`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner. Outputs/bindings: record.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[11]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:70`; AST `21b2a0755d4d416aa5f58d075d8fb3eed7b04c9edfe92ef106097bf655d22490`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[12]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:71`; AST `097c0f4989d8e1aeceac90ed3f4f7f1255f9e8ff289661dc37dec1a4cf8a301c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[12].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:71`; AST `1ddcb0a9ef95a0c4f06d0e699f9580f20833f4aa36707a4809881c574730b94f`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[13]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:72`; AST `7c887608aabf2bf406872ee018371eeb4832f358490b04e08a02847399c76076`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: compiled.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[14]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:74`; AST `4257ac6e6ea454b102018875985933932db3ab8d1fc40aa382f32fd2085e6d67`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, recipe_scope, self. Outputs/bindings: ancestors, work.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[14].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:74`; AST `6ad4882e60bc5412c4611734ad7098a8ed7af2152a31e106e3267f79b0462d3b`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[15]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:75`; AST `53071efa8e7475cb972a8bc519f69fc1b998e72aa70e544b92a1d7355bee91bc`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestors, current, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[15].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:75`; AST `4b509cb02830338ca50e2518b460aea61e7fd6a8f340a4963227a41b274b2fb4`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestors, current, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[16]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:76`; AST `9fd154789a0fd8937cc1408ea7d31eee64815d958009c0ce2d730dabd26b40c6`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: legacy, self, work. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[16].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:76`; AST `167df3d702e495e59bd5172c9ae1913c8df178500bfa2571bba9cc6811a33c1a`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: legacy, self, work. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[17]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:77`; AST `b34dd0278480fd10280d350faf64ba97f27d13e5af3ca92b503cc46f9af284ae`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[5].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[17].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:77`; AST `5596a03fc5b556e883512d9a301d4bc703fe9e32dc9ceae8f7265522f8125686`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[17].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[17].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:78`; AST `5338f3f7d8bd59a959340669c20d4fc713f13a3a36e973e2fd015b88b3c58c12`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[17].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:78`; AST `2400360975241f7b5ef9cea91edb541d78190268dfca81cf9e815a3dbb1becc4`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[18]::Assign

Source: `infra/tests/test_roadmap_runtime_scope.py:79`; AST `862ea2a46d9378da0e10e62020b2097fbd24a046411e6b318791fe6be6667eef`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[19]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:80`; AST `097c0f4989d8e1aeceac90ed3f4f7f1255f9e8ff289661dc37dec1a4cf8a301c`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[19].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:80`; AST `1ddcb0a9ef95a0c4f06d0e699f9580f20833f4aa36707a4809881c574730b94f`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[20]::With

Source: `infra/tests/test_roadmap_runtime_scope.py:81`; AST `cf272520397e697556d22dcd4e05e745bb26d49ec27f9554521af541ba91ca4d`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[10].body[5].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[20].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:81`; AST `6e17b79a9ef19afb1f856bf1b8d232a05888c723f5035f47a2ccbaaece43611b`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[20].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[20].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:82`; AST `7eec9a91edf172c84e25b1d22f5f7dc9f77c3a203b9eb93cf1b19cc3b207338e`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[20].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:82`; AST `6ad4882e60bc5412c4611734ad7098a8ed7af2152a31e106e3267f79b0462d3b`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, recipe_scope, self. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[20].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[21]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:83`; AST `51f27f68f175f168410b03e01a99a5ea1f3fb4fdbaabb5089ed61194e587b993`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease, owner. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::ScopedRecipeTests::test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit::root.body[10].body[5].body[21].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:83`; AST `33f08fcbe408cbac32de9bea021a3da8ca4bcd49c7ffbbd298f75e95301e8e07`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease, owner. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[11]::If

Source: `infra/tests/test_roadmap_runtime_scope.py:86`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[11]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[11].body[0]::Expr

Source: `infra/tests/test_roadmap_runtime_scope.py:87`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_runtime_scope.py::module::root.body[11].body[0].value::Call

Source: `infra/tests/test_roadmap_runtime_scope.py:87`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_runtime_scope`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
