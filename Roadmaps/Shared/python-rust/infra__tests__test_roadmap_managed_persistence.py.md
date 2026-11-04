# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 221. Inventory digest: `c422e59ac2442d7bdfcaf497f3eab2588c2c6e5414c5aed03d28a4b6cd8fee2d`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_managed_persistence.py::module::root::Module

Source: `infra/tests/test_roadmap_managed_persistence.py:1`; AST `c56c4146c6d6c876318a91678b69362b1f937952da1377da076eb8118984df25`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, ContractError, ManagedTurnTests, POLICY_PATH, Path, ROOT, _TurnClient, __file__, a, all, any, catalog, client, cursors, failed, file_binding, int, json, k, len, list, method, number, original, original_call, page, params, patch, plan, range, requests, result, rows, self, shutil, spec, str, sum, time, unit, unittest, x. Outputs/bindings: ROOT, a, cursors, failed, k, number, original, original_call, page, plan, requests, result, rows, spec, unit, x.
Calls/effect boundaries: (self.root / 'readiness-observation.json').write_text, (self.root / 'recovery.json').write_text, BudgetLedger, ManagedTurnTests, Path, Path(__file__).resolve, all, any, cursors.append, file_binding, int, json.dumps, len, list, original_call, params.get, patch.object, plan.update, range, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIsNone, self.assertIsNotNone, self.assertRaisesRegex, self.assertTrue, self.fixture.adapter.read, self.fixture.compiled['milestones']['A04']['budget_policy'].update, self.fixture.configure, self.fixture.fixture, self.fixture.observe, self.fixture.runner._consume, self.fixture.runner.interrupt, self.fixture.runner.poll, self.fixture.runner.prepare, self.fixture.runner.start, self.fixture.setUp, self.fixture.start, self.fixture.state, self.ledger.read, shutil.copyfile, str, sum, time.monotonic.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:1`; AST `9b9be13a2c0ba37e90aa0e54ecd1cf32a9f3c7beffca763328495a9cd512c521`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_managed_persistence.py:4`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[3]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_managed_persistence.py:6`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_managed_persistence.py:7`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_managed_persistence.py:8`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[7]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:9`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:11`; AST `a6292a2050119772b35445e26eac2ee96e486d36a5c1f256821e2e60823bd95f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:12`; AST `8bdac217cfbedd0b5f9a60ad6a666d4afdf795f9b90e37d092260fbfb7a8f741`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:13`; AST `bc6cc52480242f27d380aa62c3f475220a93d53f7114d00dc484119da07516a1`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[11]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:16`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[11].value.value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:16`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::root.body[11].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:16`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::root.body[12]::ClassDef

Source: `infra/tests/test_roadmap_managed_persistence.py:19`; AST `5187d5411960d7e94a820f49908c7f3db243bc5886fabc332f69c1dd1c7b62cf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: BudgetLedger, ContractError, ManagedTurnTests, POLICY_PATH, ROOT, _TurnClient, a, all, any, catalog, client, cursors, failed, file_binding, int, json, k, len, list, method, number, original, original_call, page, params, patch, plan, range, requests, result, rows, self, shutil, spec, str, sum, time, unit, unittest, x. Outputs/bindings: a, cursors, failed, k, number, original, original_call, page, plan, requests, result, rows, spec, unit, x.
Calls/effect boundaries: (self.root / 'readiness-observation.json').write_text, (self.root / 'recovery.json').write_text, BudgetLedger, ManagedTurnTests, all, any, cursors.append, file_binding, int, json.dumps, len, list, original_call, params.get, patch.object, plan.update, range, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIsNone, self.assertIsNotNone, self.assertRaisesRegex, self.assertTrue, self.fixture.adapter.read, self.fixture.compiled['milestones']['A04']['budget_policy'].update, self.fixture.configure, self.fixture.fixture, self.fixture.observe, self.fixture.runner._consume, self.fixture.runner.interrupt, self.fixture.runner.poll, self.fixture.runner.prepare, self.fixture.runner.start, self.fixture.setUp, self.fixture.start, self.fixture.state, self.ledger.read, shutil.copyfile, str, sum, time.monotonic.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:20`; AST `f64a70b8b6b97d6fd4a44631f2dd98893af0cbb5bf6b6e4545a3bd45330ffd68`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, ManagedTurnTests, POLICY_PATH, ROOT, self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger, ManagedTurnTests, self.addCleanup, self.fixture.compiled['milestones']['A04']['budget_policy'].update, self.fixture.setUp, shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[0]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:21`; AST `ce8577330257b7d5070e39807b5e715efb56e20397c54a2c72f428c041b01735`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:22`; AST `412fe2b06a6c8d48018ffbc15be73179ee03d8c56c1146e302a44df421f7d3d3`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ManagedTurnTests, self. Outputs/bindings: (none).
Calls/effect boundaries: ManagedTurnTests.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:22`; AST `e585f730e9371607c807c897d6f2c860119befcba6ce8cc576654a1d5ef4185f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ManagedTurnTests. Outputs/bindings: (none).
Calls/effect boundaries: ManagedTurnTests.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:23`; AST `b4195e7a806d59e33ddad497d89ed91aad1ad58098dbab110d42413c50b08654`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:23`; AST `50cff38fab903a202c80c0638fc0d6a67d5df57c13482f23bcdfcc3ebd759abf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:24`; AST `f82bef1d0d00e396deb20513c185f4f4caa53d75882923b02b120565a19d5187`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:24`; AST `d814e7f39f0a46438b2ad83abc5670ae18d4e49faa13df207d2c86e7d0defa1a`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:25`; AST `ce377bcf217cfba8c9936dfd53277dad159f317f89aa0d9490b2b0d98b83aa46`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:26`; AST `e181c2a386a091ee3af398825fc50db65c9ab6ecc05d92fa3853729f3556f121`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, ROOT, self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:26`; AST `bfba2b5b2ece2113806f571d1abde52516afa040d01d792333dade0e15decad1`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, ROOT, self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:27`; AST `a4b5ce4a174cdbd8c97c6099d613a4bc8a7067e6fd928b42fb8dc4688180f88e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:28`; AST `eaab1d8e4fc37d6d18f7c8931af7ba5b496b68d9ee47547b2cb2beab845636fe`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.compiled['milestones']['A04']['budget_policy'].update.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:28`; AST `c210fde791bc4cf8b3e7389147b442847c16face5b0399f5ecdf52ddac480573`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.compiled['milestones']['A04']['budget_policy'].update.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[8]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:29`; AST `0d67268bd300c14f31cd018011813e9e284609af1d00652ea2cb1190bc55e310`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::setUp::root.body[12].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:29`; AST `7284f87df770a43bb43b821afc3c980b7c14f951534180b5361ce68c7aef3690`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:31`; AST `42bc569702f83b390524c02e3e265490397bf6b336c408f6b4dd3094a827ff5e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, POLICY_PATH, k, self, spec. Outputs/bindings: k, spec.
Calls/effect boundaries: self.assertEqual, self.assertRaisesRegex, self.fixture.fixture, self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:32`; AST `10b782817c78f0921f7b04b4f088f268f0c0478a5fbeff5f834e2daa665de277`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, POLICY_PATH, k, self, spec. Outputs/bindings: k, spec.
Calls/effect boundaries: self.assertEqual, self.assertRaisesRegex, self.fixture.fixture, self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:32`; AST `43fe43817441ad276a441adc49ca488dc2c7bb3f0b388a18604a78266e5b56c5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.fixture.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:33`; AST `50761bb7fff553c90b707f34d784bf526f08e7c0953670106bbb965478e24783`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: spec.
Calls/effect boundaries: self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:33`; AST `ad5b3f90b1ba06f26985dbc3f1716710389903f72bd7ab3efe7669e1b80008e7`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:34`; AST `ebad0f39cef6b235489c79c1b59e5566d53338a864b87d0afba1f84e49cd77c7`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:34`; AST `1aa32b360369b010fefca16559ace0b837a12ac2ef3e4b86a6f32cbc2a91ca44`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:35`; AST `d01b95197e0756e9254a05fb46f32eda73fe23f2098db0cb095e99b2c49abc8f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: k, self, spec. Outputs/bindings: k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:35`; AST `1570dbd65c40cf26da0d6adee43f259b790c9f70dc7b70361ea40860e7f38360`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, self, spec. Outputs/bindings: k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[2].value.args[0]::ListComp

Source: `infra/tests/test_roadmap_managed_persistence.py:35`; AST `94f5653ef37837385440f8feba0f639ce66c419d87ef70043c4f787110188afb`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: k, spec. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[1].body[0].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:36`; AST `f03ef6b248510de12e1a9a5622b055d74ba6346969458786f8c5ab2060b73c2d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:36`; AST `26abad9447a1e8490cc229b154409a3ebe7b11a8048ceeb98a89af5beae7e9a4`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[4]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:37`; AST `cc3723603f72dacc74a7c11a222a73ccbd1f0674f60d96d4a222dca2e3c58de6`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:37`; AST `58450c100256b48dd09c1dc1bd773f0fc68a39ea3844140d679f513e753c3392`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:38`; AST `c14c60d161d0109acc13ebbca2c29117950b1acfb39ca9ca9c9b46defe652665`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps::root.body[12].body[1].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:38`; AST `589302d59c3361db97864049a8a83148f7e0b66614efee6c48b38c9a9c907489`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:40`; AST `789f9b499e96574612791c29b14026145a14b0f8180b92415bc912565a49e7a0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, result, self, time, x. Outputs/bindings: result, x.
Calls/effect boundaries: any, self.assertEqual, self.assertFalse, self.assertIsNone, self.fixture.fixture, self.fixture.observe, self.fixture.runner.interrupt, self.fixture.runner.poll, self.fixture.start, self.fixture.state, self.ledger.read, time.monotonic.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:41`; AST `eff30cf661bc93f4886edbf28a2c45c6caa4b5b3a98d64005969172b28c978dd`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: any, result, self, time, x. Outputs/bindings: result, x.
Calls/effect boundaries: any, self.assertEqual, self.assertFalse, self.assertIsNone, self.fixture.fixture, self.fixture.observe, self.fixture.runner.interrupt, self.fixture.runner.poll, self.fixture.start, self.fixture.state, self.ledger.read, time.monotonic.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:41`; AST `43fe43817441ad276a441adc49ca488dc2c7bb3f0b388a18604a78266e5b56c5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.fixture.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:42`; AST `1d8364173c1202d14e56b35c869ccf26aeddbcbdc8e9a967e8e8ae50612c0a50`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:42`; AST `9be278f5f32607cc2137ea5eb14604241e54b1a6b20c0c3cbe287be0d0e2e58c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:43`; AST `c023c11de145a9b0d47fc97bb58f31ef1d3d398f90df07a8aeb31e14f4d8d215`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[1].value.left::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:43`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:44`; AST `dc43ee83a248de24cfd6bbf51ef64de04eb4c93336f5819e69ff8f158a3d88ae`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:44`; AST `8d2fc40195a5b6f3cf931929e2008523673537b35ebc226468b04cebb56afccf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:45`; AST `5705c9d1eefa3077531b136fb770c2d2b996f073c4e9afa7c427a0788ce585a4`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:45`; AST `105316d217d5aefe6b56befe7ae22a9a13bdb4ee472c5f8892078cf4a06b1222`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:46`; AST `0bddd39fa88615b344ea946bbebcc06636e1af28026f6c6694f6060707c1584a`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:46`; AST `51db7bd541df51ddab8b728ab43e1e03b2ac6c0ec1c6ef114ad442dcd62001e5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[4].value.args[0].value.value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:46`; AST `c6af2442a0b071aa928cdefcc4844536c71f08d8b2b793d626686c0669653f01`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[4].value.args[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:47`; AST `581a2ed979a0fe0932a3e01bece128e19764afb7a512e3c68a3726d8ace44f77`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNone, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:47`; AST `3d14371b002d93e508aad4d5e141c0532f06fb1bb15c2cd6849ec097259b1846`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNone, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[5].value.args[0].value.value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:47`; AST `c6af2442a0b071aa928cdefcc4844536c71f08d8b2b793d626686c0669653f01`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[5].value.args[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:48`; AST `8abb38ba64317da58266fd98ca75a7f14972855b970656efefc41f01c3944170`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertFalse, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:48`; AST `de56cc407ca9ed3f27afc9cf98fa9ad30782232f0b845653b6e506b64e08a364`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertFalse, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:48`; AST `59af2ac9fbe58b51282b27888dd59c55d5140fc30edf6ae468b7c85392eb4264`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[6].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_managed_persistence.py:48`; AST `5833bff16caf620bf5fe21280a261bd3a07d5fef72d28f959a79d85c321ef328`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: self, x. Outputs/bindings: x.
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[2].body[0].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[6].value.args[0].args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:48`; AST `546029a5cf3aa35cb694d13fbeb3cc2a415b6280053b299b51b3bdd582cf1e9d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[6].value.args[0].args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:49`; AST `dc5825e2a0a3b0c7e21f6846167eb38e6099db10deb90a2c7ad84e0703edc98e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.interrupt.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:49`; AST `b5d236e31bfc312a6c7297b49405231ecc7785a6e4ccb435800b1787800c5d1b`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.interrupt.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:50`; AST `ea021576b7b2975cc329db94bbd3ae4e0e35e79b10a2a8a69fefb6063610a200`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.fixture.observe, self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:50`; AST `111d49664dad0800ff0ca1d807d12068966e7cde6878b256b82f7e7c22a89ff0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.fixture.observe, self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[8].value.args[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:50`; AST `7241fae2d70ebe1ea29b11e600e2e244cdc8d4257d6a61b72c3d2a0e24ad9983`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.observe, self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[8].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle::root.body[12].body[2].body[0].body[8].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:50`; AST `8d2fc40195a5b6f3cf931929e2008523673537b35ebc226468b04cebb56afccf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[8].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:52`; AST `5e6acd94e79b4ec54f53f61b4682a1b17d4f92155b33db4033d3f0bf00e3f6aa`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, a, all, failed, file_binding, json, len, original, plan, result, rows, self, spec, sum, unit, x. Outputs/bindings: a, failed, original, plan, result, rows, spec, unit, x.
Calls/effect boundaries: (self.root / 'readiness-observation.json').write_text, (self.root / 'recovery.json').write_text, all, file_binding, json.dumps, len, plan.update, self.assertEqual, self.assertRaisesRegex, self.assertTrue, self.fixture.adapter.read, self.fixture.configure, self.fixture.fixture, self.fixture.observe, self.fixture.runner.prepare, self.fixture.runner.start, self.fixture.state, self.ledger.read, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:53`; AST `14996499eaf0878197c1f17c6aabb558552b18858cbdc8ca1cbddf73c0ef983f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.configure.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:53`; AST `10c7f93873d9e1586229bf78bde8a02f9e9f292a508a89f85f5232cb10a11741`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.configure.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:54`; AST `e978c9ffe19a10b35903e02343df4222afa500d271baa5f238b2e9151dd3052e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, a, all, failed, file_binding, json, len, original, plan, result, rows, self, spec, sum, unit, x. Outputs/bindings: a, failed, original, plan, result, rows, spec, unit, x.
Calls/effect boundaries: (self.root / 'readiness-observation.json').write_text, (self.root / 'recovery.json').write_text, all, file_binding, json.dumps, len, plan.update, self.assertEqual, self.assertRaisesRegex, self.assertTrue, self.fixture.adapter.read, self.fixture.configure, self.fixture.fixture, self.fixture.observe, self.fixture.runner.prepare, self.fixture.runner.start, self.fixture.state, self.ledger.read, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:54`; AST `43fe43817441ad276a441adc49ca488dc2c7bb3f0b388a18604a78266e5b56c5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.fixture.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:55`; AST `50761bb7fff553c90b707f34d784bf526f08e7c0953670106bbb965478e24783`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: spec.
Calls/effect boundaries: self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:55`; AST `ad5b3f90b1ba06f26985dbc3f1716710389903f72bd7ab3efe7669e1b80008e7`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.prepare.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:56`; AST `b3076841f8c8a8d37c23027ffc4d91a53072b22348378f8b82b425b1d4ea8b86`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, spec. Outputs/bindings: failed.
Calls/effect boundaries: self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:56`; AST `8b6ddd8b8c9e1c71c47966fa6ee8fd32f76d5527193c64a575d0eb90ca6f6ad3`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[2]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:57`; AST `28bb102fffa50d2a7d211dde20407b5adfab1b509f2e9cc60cf1cb274a68723e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[2].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:57`; AST `7ccd9da2726325f513b9376e48ba423787900240b04743cca67ff7e27b6b9eef`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[3]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:58`; AST `894286abc3aa9fefecf1ffa09df8947111cabee4f3891dacce7e5613d2620a37`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: original.
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[3].value.value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:58`; AST `c6af2442a0b071aa928cdefcc4844536c71f08d8b2b793d626686c0669653f01`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[3].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[4]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:59`; AST `01539865febd335ad0cd8a13280cad9c91131c7f680f7fbabd4ae0b79807fd3b`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:59`; AST `f0ea87584d5357620a82d5a0a34324c2326b8e5fadf5a10172c8d1b014680e46`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:60`; AST `090a8153584b8eb03f1d0bfb40f8d7574107ce54852dda0d342e33e2ce4adcec`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:60`; AST `8b6ddd8b8c9e1c71c47966fa6ee8fd32f76d5527193c64a575d0eb90ca6f6ad3`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, spec. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[5]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:61`; AST `72c643311a3aba9b0a821c32a95a05a54f2e0807552c572370e9983144d03201`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.configure.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[5].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:61`; AST `7e07d06e3384b2cba5baf2548d46eca4d5686a34779527f2861106eac2b79ba6`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.configure.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[6]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:64`; AST `2f2dbfd6b35b4f48110a1494080283b752da29c643f28a0f48f704e0ab3af72d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'readiness-observation.json').write_text, json.dumps, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[6].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:64`; AST `628f61ae8a6bb2c3f0144130144c85704332e723823714aff4d500c122f7da3d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'readiness-observation.json').write_text, json.dumps, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:64`; AST `0f24ee81673d03a6871a1b568539fb069eccd0a584a8fe972f4cc0db760f46ed`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[6].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:64`; AST `546029a5cf3aa35cb694d13fbeb3cc2a415b6280053b299b51b3bdd582cf1e9d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[7]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:65`; AST `1233a7b2502b88a55ac3aaefafa56df6c5fb68ab470cdf42235ec6bc45c7a8b3`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: failed. Outputs/bindings: plan.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[8]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:66`; AST `bc1433540d43b40b7e6bd0a65ad0ae6b1aea1b5fc34159074d0be977349d7621`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, plan, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, plan.update.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[8].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:66`; AST `ad4dd29ab9bee5447de8de374d1f558a1f9a31133ca0e38ee318624308331350`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, plan, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, plan.update.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[8].value.keywords[5].value.elts[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:70`; AST `e068e2d26440ef1d966a2b5e6701073a114dcd0cb9e9bfb37ad07206058a4afe`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[8].value.keywords[5].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[9]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:71`; AST `d70dd0095a513586b47171395a0fcd1b9ad9ccc705293ab5003245c179f067c0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, plan, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'recovery.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[9].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:71`; AST `93fa2309fdbf28019599fb9f02947a8c706e9ecf8a76fe49b5d22d03c6c2e36c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, plan, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'recovery.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[9].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:71`; AST `706470dfeecf3d0b4a66a5bc8a62d41895e55b30ce07e73ddffcc2d0a0a280c8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, plan. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[10]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:72`; AST `dbf67a6307155ba8715d46f1e757edc63a29b80ca6a1804d00bbf7f2e05b0cdf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, self, spec. Outputs/bindings: result.
Calls/effect boundaries: file_binding, self.fixture.observe, self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[10].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:72`; AST `b8a683ad5c571614a7314d8ff45b8e04128876257b9bdb002cfa9ce21451b38a`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, self.fixture.observe, self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[10].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:72`; AST `ca1e96ca6710ca00347122436664af0f5417097ad1b3bf0c49148380e69394cb`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, self.fixture.runner.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[10].value.args[0].keywords[1].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:73`; AST `ca0f83c521fe719cf83ac6bfba054cc0abd2a825954ac3a1f6279d1ffce70ed8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[10].value.args[0].keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[11]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:74`; AST `392100866da8378cdb3b5baff2d2ce1fcaf529d49ee9b93c3add1dcc32692814`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[11].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:74`; AST `19ab862b48ed111be6634ca0047c32616f8a1da514ff9aa1f307d433693d4a31`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[12]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:75`; AST `48d48afd8869907dd7e9c5be9048b6b14d27eea5e8748b02788cd82be4958bb5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: rows.
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[12].value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:75`; AST `c6af2442a0b071aa928cdefcc4844536c71f08d8b2b793d626686c0669653f01`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[12].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[13]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:76`; AST `4a1744ae335d1452b7ab921c6ed6bff610241a92d2359d4c62f51dddb7bd59af`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, rows, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[13].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:76`; AST `14b76712639b7ed711dd9e7027b6db41cdcd52d2e2649e930dd7fd20cb713009`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, rows, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[13].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:76`; AST `0ea89ccf64714bf68d73a0787f966d27dbc61ef098aa73a74b057b16edd97566`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, rows. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[13].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[14]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:77`; AST `92bbfcfe58d35d595500d54579d9f86ffefaa7be652617a96590ba88c9d9c449`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, rows, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[14].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:77`; AST `139175ab04b54de0576d1576403a197f18f29bf792dbb76330587ac0bd8446a0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, rows, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[15]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:78`; AST `aac3be7fc188501de79aa54ffb6f2ed1af327a2b77a8bf9009a9dd42b525d47f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, all, rows, self. Outputs/bindings: a.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[15].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:78`; AST `50228826c2a5049506b19b200181f7f2bf8c210835bbc086ff6c1a885f20e094`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, rows, self. Outputs/bindings: a.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[15].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:78`; AST `294868e1d88dde9cc9c5f53786031ba3cdae49123ef12e1689c8a8358b00561a`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, rows. Outputs/bindings: a.
Calls/effect boundaries: all.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[15].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[15].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_managed_persistence.py:78`; AST `ef3e9b149f8ecc165cbdaafd121e7fe3438b136d52dd3329ab299a465cda6faa`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, rows. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[3].body[1].body[15].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[16]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:79`; AST `9d46f1105394c72e43e7dd19be411b54fc5eaa62a2e48a7011133cc116012746`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, spec. Outputs/bindings: unit.
Calls/effect boundaries: self.fixture.adapter.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[16].value.value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:79`; AST `35ca889373c3486dabb74e07334773c7d98da3bd8b85cd330e5e278947be5fe2`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.adapter.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[16].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[17]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:80`; AST `ad67f4a5e724841afc1fa41bb2fe92d0392c6557b7573455b72c684efc424eaa`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, self, unit. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[17].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:80`; AST `92f490e6cb30ba9b9ddbc82fec33e978ca9a4b9612a9c54e5781e699d61cdfa7`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, self, unit. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[18]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:81`; AST `e40783d6bacf78b7089e586bade8714efbd770f1a57fb15f214d40bed54b460f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, sum, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertEqual, self.fixture.state, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[18].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:81`; AST `d364278438a9be74fa841169963cd663353f857a3b32cb12378ffbe5b9c71c7f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, sum, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertEqual, self.fixture.state, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[18].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:81`; AST `2a1470f5f8d2cf2718b014ffdbcdca637e6a895090d99075932063e64077ddb8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, sum, x. Outputs/bindings: x.
Calls/effect boundaries: self.fixture.state, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[18].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[18].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_managed_persistence.py:81`; AST `60972606a595600b98e4d91cd01ee33c5ddfe88e6baae7a4510c514a30524085`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: self, x. Outputs/bindings: x.
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[3].body[1].body[18].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history::root.body[12].body[3].body[1].body[18].value.args[0].args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:81`; AST `546029a5cf3aa35cb694d13fbeb3cc2a415b6280053b299b51b3bdd582cf1e9d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[18].value.args[0].args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:83`; AST `ac89db3d6deadd891c43bf8e2918404ebbea6f30d111838ef7b2471df4782278`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, len, number, range, requests, self, str, x. Outputs/bindings: number, requests, x.
Calls/effect boundaries: any, len, range, self.assertEqual, self.assertFalse, self.fixture.fixture, self.fixture.observe, self.fixture.runner._consume, self.fixture.runner.interrupt, self.fixture.runner.poll, self.fixture.start, str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:84`; AST `4501cba4ea11efc6a95487917a2aeda679ee03546f1af4236677d45141648b0d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: any, len, number, range, requests, self, str, x. Outputs/bindings: number, requests, x.
Calls/effect boundaries: any, len, range, self.assertEqual, self.assertFalse, self.fixture.fixture, self.fixture.observe, self.fixture.runner._consume, self.fixture.runner.interrupt, self.fixture.runner.poll, self.fixture.start, str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:84`; AST `43fe43817441ad276a441adc49ca488dc2c7bb3f0b388a18604a78266e5b56c5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.fixture.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:85`; AST `6354230c904985770140ff5601bd0bf1db63f2a277dd31ffee721924632a56b6`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:85`; AST `9be278f5f32607cc2137ea5eb14604241e54b1a6b20c0c3cbe287be0d0e2e58c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[1]::For

Source: `infra/tests/test_roadmap_managed_persistence.py:86`; AST `bd28284506848bd43dd1b713e52c61e0b9713723e4ad626f64307cd3b242a9ea`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: number, range, self, str. Outputs/bindings: number.
Calls/effect boundaries: range, self.fixture.runner._consume, str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[4].body[0].body[1]; no call, error or mutation may be omitted. Iteration: number in range(250)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[1].iter::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:86`; AST `fb7aba01177138dc7a6be0ff1d71c2d78021e5551b18e3a0eba93eeb4f1f32e9`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:87`; AST `138cd37509951a81170256564d71e74614f1289e43d415fb6b4ad8584a6af97c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: number, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner._consume, str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:87`; AST `3149760130ac985aa60d573241f7c54f76aabab2967381a20e9bcc9d7c9c6ab0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: number, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner._consume, str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[1].body[0].value.args[0].values[0].right::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:87`; AST `d20a7b35ad9dd3f53a7abadb9e71c9644d7025c6a5ae7bb534174c6601c538b3`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: number, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[1].body[0].value.args[0].values[0].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:89`; AST `69f1d7630579ece462d211c72f92baef1990db1b48598f4339cf2896d61128a0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: requests.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:90`; AST `67403f3a6f4f60b63fda16eecc81a42ce3ccf9e7ce601b5d10e6199f8399462e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, requests, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:90`; AST `5ef76a21e6f39ac1ecb04d1ad2f46a171ad0416d36d313f81f809a3ae1a1e405`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requests, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:90`; AST `8b6d52797c4d769c21437f81a865bcba1664a236275db58bb5b6aaf8943bd1d8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requests. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:91`; AST `1570beba499685ae50ea0bb786e11a4e0f99df842cbf9af1c76913a1d788b57f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, requests, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:91`; AST `3fcea7177c4f687dd84d7b87c8c3ce4fdd45b128a2269ccb7c9af6ae4f1a3b4a`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, requests, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:91`; AST `5bf382df1409dcc989f8c96c700f904da02f9353cb72028a4595e02bb9da4a37`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, requests, x. Outputs/bindings: x.
Calls/effect boundaries: any.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[4].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_managed_persistence.py:91`; AST `5b0ebe6b6a692f65553eca092558ff1cda8d0b140214e352edfcc4fb7b50a5f0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: requests, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[4].body[0].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:92`; AST `dc5825e2a0a3b0c7e21f6846167eb38e6099db10deb90a2c7ad84e0703edc98e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.interrupt.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:92`; AST `b5d236e31bfc312a6c7297b49405231ecc7785a6e4ccb435800b1787800c5d1b`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.interrupt.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:93`; AST `ea021576b7b2975cc329db94bbd3ae4e0e35e79b10a2a8a69fefb6063610a200`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.fixture.observe, self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:93`; AST `111d49664dad0800ff0ca1d807d12068966e7cde6878b256b82f7e7c22a89ff0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.fixture.observe, self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[6].value.args[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:93`; AST `7241fae2d70ebe1ea29b11e600e2e244cdc8d4257d6a61b72c3d2a0e24ad9983`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.observe, self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[6].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_many_external_action_requests_are_retained_without_an_internal_count_stop::root.body[12].body[4].body[0].body[6].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:93`; AST `8d2fc40195a5b6f3cf931929e2008523673537b35ebc226468b04cebb56afccf`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.runner.poll.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[6].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:95`; AST `8f1a3a7712be06b588a0d35b608606f4d0a579d8078ba2d6836e1d7ff3745648`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _TurnClient, catalog, client, cursors, int, list, method, original_call, page, params, patch, range, result, self, str, sum, x. Outputs/bindings: cursors, original_call, page, result, x.
Calls/effect boundaries: cursors.append, int, list, original_call, params.get, patch.object, range, self.assertEqual, self.fixture.configure, self.fixture.fixture, self.fixture.observe, self.fixture.start, self.fixture.state, str, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[0]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:96`; AST `d0022c61b0725ecc608d9597bf37700a42407c8758fd6c220d8771ada7421dbe`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[1]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:97`; AST `7f1c81867714cb6463ab44d44f15b870c3ae44cc0a7ef0893f94f140a8946b14`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _TurnClient. Outputs/bindings: original_call.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[2]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:98`; AST `8d61e5565ab150d17661e7ee5ae6c56f25905ed14c4a6578227424a948dff879`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: cursors.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:100`; AST `a4116dbbff8a49e456fa1f32e3bc79db8aeb34805fbb62e3778d9d3fefddaec4`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: client, cursors, int, method, original_call, page, params, str. Outputs/bindings: page.
Calls/effect boundaries: cursors.append, int, original_call, params.get, str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[0]::If

Source: `infra/tests/test_roadmap_managed_persistence.py:101`; AST `734b49eb7f46d0e315fcdd0c7c5c9a9d194b7a240f38893278e7effaba67e28b`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: client, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: original_call.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[12].body[5].body[3].body[0]; no call, error or mutation may be omitted. Condition: method != 'model/list'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[0].body[0]::Return

Source: `infra/tests/test_roadmap_managed_persistence.py:102`; AST `3a4457bc7bcd51ffef35e49e0943717c31d48972a051c893fc6ca14abcbdf21f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: original_call.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[5].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:102`; AST `232c6b51ce9283a722b6acbc97931f5f13e909c2f0a304a82615f83ae9034335`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: original_call.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[1]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:103`; AST `c72d24786f37266125b4ca2e611158ef500c80691598555db7bf49ec7776db8e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, params. Outputs/bindings: page.
Calls/effect boundaries: int, params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:103`; AST `f261f7bbad8c8cf2f1fe938d77657ab3a3dd19e26a7055d87b60527e74086a22`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, params. Outputs/bindings: (none).
Calls/effect boundaries: int, params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:103`; AST `e6a8eac14eb79cb71fddd5da3ef3b30fe79b68554f42ee86d2f899a30a397060`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: params. Outputs/bindings: (none).
Calls/effect boundaries: params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:104`; AST `0a9b243fdb0a1456a4a1c0b4364e51cdfa561334590da100414cc120388b5f5d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cursors, page. Outputs/bindings: (none).
Calls/effect boundaries: cursors.append.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:104`; AST `05cf2d3e961175d9200d429468544b0cb5d668c8f1e1e8c02a227a54dda81f55`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cursors, page. Outputs/bindings: (none).
Calls/effect boundaries: cursors.append.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[3]::Return

Source: `infra/tests/test_roadmap_managed_persistence.py:105`; AST `39a468b170757010a88393891769c2b2790eab92c5cbb71c2861077e63acaf64`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: page, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[5].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::catalog::root.body[12].body[5].body[3].body[3].value.values[1].body::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:106`; AST `2345802c08096b86eb5c3aa2a6a82bf212a14adcfd48c34500fb43a041e23b16`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: page, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].body[3].value.values[1].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[4]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:108`; AST `e76f4c3995dcc552ce4bc86bf9be16854d69cff3271c864e494af13161845768`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.configure.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[4].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:108`; AST `eb48d58e23a195125e064487936af9e13e6b2c1057c3ed6969fde7000cbe6ab3`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.configure.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[5]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:109`; AST `d2feca255de6a6f01e3a1a4044b23f2ead59b1ff645b698807436dc68cfc7233`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: _TurnClient, catalog, patch, self. Outputs/bindings: result.
Calls/effect boundaries: patch.object, self.fixture.fixture, self.fixture.observe, self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:109`; AST `43fe43817441ad276a441adc49ca488dc2c7bb3f0b388a18604a78266e5b56c5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.fixture.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[5].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:109`; AST `d385ad27065b47ba91c414920fcbfc67372a4dd02d89f4a94cee3465d4705ff6`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _TurnClient, catalog, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:110`; AST `bc2d055a5edb3ad5180042f4e8741848dd480bdaffffd813ce38c4880661c0d8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.fixture.observe, self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:110`; AST `0a38bbcd829c34f7ec553bdb3f61808947c8e21dcbe85ef2c69f8646fb1382f2`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.observe, self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[5].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:110`; AST `9be278f5f32607cc2137ea5eb14604241e54b1a6b20c0c3cbe287be0d0e2e58c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[6]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:111`; AST `392100866da8378cdb3b5baff2d2ce1fcaf529d49ee9b93c3add1dcc32692814`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[6].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:111`; AST `19ab862b48ed111be6634ca0047c32616f8a1da514ff9aa1f307d433693d4a31`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[7]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:112`; AST `a880402947c162f8836cdc7478838ab4a5617ae1d863e6cc2311a8a1d963f150`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cursors, list, range, self. Outputs/bindings: (none).
Calls/effect boundaries: list, range, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[7].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:112`; AST `3e924c04f6a0f808cba6211f4feed898c81f40d3aff667a8a82f315213c6c484`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cursors, list, range, self. Outputs/bindings: (none).
Calls/effect boundaries: list, range, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[7].value.args[1]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:112`; AST `4af52cd6aa003ca4c69b191706a2b55e45f7df15b32db46b6ee4657e510d6a7d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, range. Outputs/bindings: (none).
Calls/effect boundaries: list, range.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[7].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[7].value.args[1].args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:112`; AST `6075a479794a547d6d7514d8ccddee64a168fbff7352b7ddcef73c59475ae214`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[7].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[8]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:113`; AST `4f3db9c32a52f5e04b48439fa70fccc9e6e741301f9510bdbeec0fc8249d97bd`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, sum, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertEqual, self.fixture.state, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[8].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:113`; AST `fc0659875cbd88faf345f5280ff049895a7443486c741ec81fa10bb8116ac48d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, sum, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertEqual, self.fixture.state, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:113`; AST `2a1470f5f8d2cf2718b014ffdbcdca637e6a895090d99075932063e64077ddb8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, sum, x. Outputs/bindings: x.
Calls/effect boundaries: self.fixture.state, sum.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[8].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_managed_persistence.py:113`; AST `60972606a595600b98e4d91cd01ee33c5ddfe88e6baae7a4510c514a30524085`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: self, x. Outputs/bindings: x.
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[5].body[8].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn::root.body[12].body[5].body[8].value.args[0].args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:113`; AST `546029a5cf3aa35cb694d13fbeb3cc2a415b6280053b299b51b3bdd582cf1e9d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[8].value.args[0].args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:115`; AST `baf00766d157a81552eb7d2824c984db0fd0a063271ea904c76259ede16d5b14`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _TurnClient, any, catalog, client, cursors, method, original_call, params, patch, result, self, x. Outputs/bindings: cursors, original_call, result, x.
Calls/effect boundaries: any, cursors.append, original_call, params.get, patch.object, self.assertEqual, self.assertFalse, self.assertIsNotNone, self.fixture.fixture, self.fixture.start, self.fixture.state, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[0]::ImportFrom

Source: `infra/tests/test_roadmap_managed_persistence.py:116`; AST `d0022c61b0725ecc608d9597bf37700a42407c8758fd6c220d8771ada7421dbe`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[1]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:117`; AST `7f1c81867714cb6463ab44d44f15b870c3ae44cc0a7ef0893f94f140a8946b14`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _TurnClient. Outputs/bindings: original_call.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[2]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:118`; AST `8d61e5565ab150d17661e7ee5ae6c56f25905ed14c4a6578227424a948dff879`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: cursors.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_managed_persistence.py:120`; AST `7dd7b28bb5e5d0d51b38afec466087eacf1cfc6147f0e74fce02baa7bf10f33e`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: client, cursors, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: cursors.append, original_call, params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[0]::If

Source: `infra/tests/test_roadmap_managed_persistence.py:121`; AST `734b49eb7f46d0e315fcdd0c7c5c9a9d194b7a240f38893278e7effaba67e28b`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: client, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: original_call.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[12].body[6].body[3].body[0]; no call, error or mutation may be omitted. Condition: method != 'model/list'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[0].body[0]::Return

Source: `infra/tests/test_roadmap_managed_persistence.py:122`; AST `3a4457bc7bcd51ffef35e49e0943717c31d48972a051c893fc6ca14abcbdf21f`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: original_call.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[6].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:122`; AST `232c6b51ce9283a722b6acbc97931f5f13e909c2f0a304a82615f83ae9034335`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, method, original_call, params. Outputs/bindings: (none).
Calls/effect boundaries: original_call.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:123`; AST `82dfcc8c3f1f6ff68920da8d9bbbdc92e4a842207099a32258e81f1441a65445`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cursors, params. Outputs/bindings: (none).
Calls/effect boundaries: cursors.append, params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:123`; AST `9ba1d5d50b05fa7120d9a96e6d159d3b43913635343f1db90ed76ecf6c1aea02`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cursors, params. Outputs/bindings: (none).
Calls/effect boundaries: cursors.append, params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:123`; AST `0c3148b0ea73a2ba7569b6033c40cb377a1f9ae684256f096efb79d79127cf95`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: params. Outputs/bindings: (none).
Calls/effect boundaries: params.get.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::catalog::root.body[12].body[6].body[3].body[2]::Return

Source: `infra/tests/test_roadmap_managed_persistence.py:124`; AST `f60f68507537580643c3bfbeeffd91c97484ab7d18c6cc52de9839cda2a43eb8`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[6].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[4]::With

Source: `infra/tests/test_roadmap_managed_persistence.py:126`; AST `e50bf45705567c25458f73cc70d57a6a0a9ffa85d979e2bb597d83b79cc5dc34`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: _TurnClient, catalog, patch, self. Outputs/bindings: result.
Calls/effect boundaries: patch.object, self.fixture.fixture, self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:126`; AST `43fe43817441ad276a441adc49ca488dc2c7bb3f0b388a18604a78266e5b56c5`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.fixture.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[4].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:126`; AST `d385ad27065b47ba91c414920fcbfc67372a4dd02d89f4a94cee3465d4705ff6`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _TurnClient, catalog, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_managed_persistence.py:127`; AST `1d8364173c1202d14e56b35c869ccf26aeddbcbdc8e9a967e8e8ae50612c0a50`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:127`; AST `9be278f5f32607cc2137ea5eb14604241e54b1a6b20c0c3cbe287be0d0e2e58c`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.start.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:128`; AST `c20a17c09bcd0ed10273fea4a43a344b9f968b4abbabbd4f7115ebd9ea1fca12`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:128`; AST `e4abcf31afb609d17186f9d9c3b63d803310bbc22a2e4e3f2f457675bc033def`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[6]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:129`; AST `cdfcfaf8a17293946f8c1b00a4b170305b4ec9655d393c7d8fa6447919c295c0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cursors, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[6].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:129`; AST `70c6f69d4ac4c3eba5fec9d76f2815e033993c3dbff2efe9a3731e994ef0e9b0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cursors, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[7]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:130`; AST `cc5b4a5d46333d173e31966505e9868f97cd2a034ad5c6007de229333ec7e4ed`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertFalse, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[7].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:130`; AST `8e7089f49badffa7fbdb5f13f9b803dd5db33da17b7e9b83afcadd97faeb6ef7`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertFalse, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[7].value.args[0]::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:130`; AST `e0aef242e45df35214392f3c1f1f39202d335eddff2790c32df25b9a5f6a4926`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[7].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_managed_persistence.py:130`; AST `60972606a595600b98e4d91cd01ee33c5ddfe88e6baae7a4510c514a30524085`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: self, x. Outputs/bindings: x.
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[6].body[7].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[7].value.args[0].args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:130`; AST `546029a5cf3aa35cb694d13fbeb3cc2a415b6280053b299b51b3bdd582cf1e9d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.state.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value.args[0].args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[8]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:131`; AST `a2e162fd55ec854f47156884782bafe043c407fad284aee0d687427667a36eb0`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[8].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:131`; AST `31b2b64ee971efe9c535cf36099c4fcb378ce23ce21a6ea905de02f07f0bc55d`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[8].value.args[0].value.value.value.value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:131`; AST `c6af2442a0b071aa928cdefcc4844536c71f08d8b2b793d626686c0669653f01`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.ledger.read.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[8].value.args[0].value.value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[9]::Expr

Source: `infra/tests/test_roadmap_managed_persistence.py:132`; AST `958e1690d972fbe230c26ec84d4d5a1b5191c7bcf05c3085ae8daec5f248e333`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNotNone.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_managed_persistence.py::module::ManagedPersistenceTests::test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model::root.body[12].body[6].body[9].value::Call

Source: `infra/tests/test_roadmap_managed_persistence.py:132`; AST `e9306f19caa3b51e38ccbfa48e1b6c4fda6348d14688cb6aea260f642093fc96`.

Rust module: `infra::tests::test_roadmap_managed_persistence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNotNone.
Dependencies: __future__, agentinfra.roadmap_managed, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_runtime, json, pathlib, shutil, test_roadmap_managed_turn, time, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
