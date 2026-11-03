# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 168. Inventory digest: `aba4a9c0b9bf38f5376d73d2afaef8f92902fff640f6716cc1550d5f1fbacb9e`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_python_deal.py::module::root::Module

Source: `infra/tests/test_roadmap_python_deal.py:1`; AST `63292b46b18cb23bf2aa866c78758b9503c1facdf7f84cb88499515dbc506d5c`.

Rust module: `infra::tests::test_roadmap_python_deal`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, ROOT, __file__, __name__, assertions, ast, backend_observation_key, calls, classify_deal, dict, directory, isinstance, json, len, n, negative, new, observation, old, original_assertions, path, qualification_backend, result, root, self, targets, tempfile, tree, unittest, update. Outputs/bindings: ROOT, assertions, calls, directory, n, negative, new, observation, old, original_assertions, path, result, root, targets, update.
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_negative.py').read_bytes, (ROOT / 'verification/roadmap/python/policy_deal_positive.py').read_bytes, (ROOT / 'verification/roadmap/python/policy_positive.py').read_bytes, Path, Path(__file__).resolve, ast.dump, ast.parse, ast.walk, backend_observation_key, calls, classify_deal, dict, isinstance, json.dumps, len, path.parent.mkdir, path.write_text, qualification_backend, self.assertEqual, self.assertIn, self.assertIsInstance, self.assertRaises, self.observation, self.run_record, self.subTest, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:1`; AST `eb3676c6dccbc3dcfc0ad1b67e2d5ee7b7f26f3131aebda19ee242fd4eb6cd2b`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_deal.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_python_deal.py:4`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_python_deal.py:5`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_python_deal.py:6`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_roadmap_python_deal.py:7`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_python_deal.py:8`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_python_deal.py:9`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_roadmap_python_deal.py:11`; AST `7bf1f2bf436794fa98b588d2edd8b9edc3d490f3c1f1b01a911f950d1cce76d6`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_python_deal.py:12`; AST `f03d490df75c7330951b5ce75380b297979b688b88c1f26364ab52e4c8a2c0af`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[10]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:15`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[10].value.value.value::Call

Source: `infra/tests/test_roadmap_python_deal.py:15`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[10].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python_deal.py:15`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[10].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::root.body[11]::ClassDef

Source: `infra/tests/test_roadmap_python_deal.py:18`; AST `6bcf440339a2c5157fa9d97cd5811b608ae76e6a2b851f9fed2d085e00880930`.

Rust module: `infra::tests::test_roadmap_python_deal`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, ROOT, assertions, ast, backend_observation_key, calls, classify_deal, dict, directory, isinstance, json, len, n, negative, new, observation, old, original_assertions, path, qualification_backend, result, root, self, targets, tempfile, tree, unittest, update. Outputs/bindings: assertions, calls, directory, n, negative, new, observation, old, original_assertions, path, result, root, targets, update.
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_negative.py').read_bytes, (ROOT / 'verification/roadmap/python/policy_deal_positive.py').read_bytes, (ROOT / 'verification/roadmap/python/policy_positive.py').read_bytes, Path, ast.dump, ast.parse, ast.walk, backend_observation_key, calls, classify_deal, dict, isinstance, json.dumps, len, path.parent.mkdir, path.write_text, qualification_backend, self.assertEqual, self.assertIn, self.assertIsInstance, self.assertRaises, self.observation, self.run_record, self.subTest, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::run_record::root.body[11].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:19`; AST `0904f69d989877618de53518ca3ad5a4ae9e9e558263b7c32a4b41b152ec956c`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::run_record::root.body[11].body[0].body[0]::Return

Source: `infra/tests/test_roadmap_python_deal.py:20`; AST `6571a0fcec510841531ddd93a41c760521fcdcd2f151d12f79b6460159cdc40b`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Return evaluation at root.body[11].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::observation::root.body[11].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:22`; AST `e81b7d4574e153ecd483806708090e803b74c29feffe40e75d90439d7372a01e`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::observation::root.body[11].body[1].body[0]::Return

Source: `infra/tests/test_roadmap_python_deal.py:23`; AST `fed99c227fd81cf739a9a54c3322aec679b9bc185964007ce4d839b88aa5ae57`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Return evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:26`; AST `da5dac86f949e0ceb67644fa1f19ffed369a997bc50a63a398eba93c352babff`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_deal, dict, observation, self, update. Outputs/bindings: observation, update.
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record, self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0]::For

Source: `infra/tests/test_roadmap_python_deal.py:27`; AST `4ad4ae89757a8bc47472909f43a2f04382e25fcb590d7fecc6f58ba28ba20c64`.

Rust module: `infra::tests::test_roadmap_python_deal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: classify_deal, dict, observation, self, update. Outputs/bindings: observation, update.
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record, self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted. Iteration: update in ({'solver_results': []}, {'proof': {'conclusion': 'OK', 'description': 'nothing to prove'}}, {'proof': {'conclusion': 'PARTIAL', 'description': 'assertion'}}, {'proof': {'conclusion': 'SKIP', 'description': 'unsupported'}}, {'skips': ['unsupported production operation']})
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:31`; AST `de23d460da59fe4b8cadb8c17a71fb22e3055a968f4bb8be2d1f280126c00c5f`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self, update. Outputs/bindings: observation.
Calls/effect boundaries: dict, self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:31`; AST `40bcbb3d50e608135a10759616e897f905bd46acacc37fd8f5c0ab3b17618f7e`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self, update. Outputs/bindings: (none).
Calls/effect boundaries: dict, self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:31`; AST `bde40dad4654296874cfa317e16e8638421ef7251b4012dcb8f9a2e3cade376d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[1]::With

Source: `infra/tests/test_roadmap_python_deal.py:32`; AST `a9f1529a076fe0d4915b390b5284c5f1e36f56c725c8641394223d2ea90931bc`.

Rust module: `infra::tests::test_roadmap_python_deal`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: classify_deal, observation, self, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.assertEqual, self.run_record, self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[11].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_deal.py:32`; AST `89799ee3b9235393b3b4cb9a263a1f1550412f66a0ad747fbd4e0c88d7fd6569`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, update. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:33`; AST `74d92995b8a3292055579ece4d804fb77ffbb5926d9180fc36203b076b975778`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.assertEqual, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:33`; AST `c3de82f2f2dd28ac9a6a6f229c601f6a06c5773c7c380e8ad6b270d17b3a82f2`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.assertEqual, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[1].body[0].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:33`; AST `6fe01df7cbd051a76115a65329a380dd621a1f2315ef12ec151231a578881a3d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].body[1].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit::root.body[11].body[2].body[0].body[1].body[0].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:33`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].body[1].body[0].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:35`; AST `75b7e6c0a6fe822b63758813d8a5ea81cd56fcf6cb5459782ed41a7ea594fc06`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_deal, dict, self, update. Outputs/bindings: update.
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0]::For

Source: `infra/tests/test_roadmap_python_deal.py:36`; AST `43de942c85133596adf6594cbbf832b754331990c13994bb5d2c27e9f13b64c5`.

Rust module: `infra::tests::test_roadmap_python_deal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: classify_deal, dict, self, update. Outputs/bindings: update.
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted. Iteration: update in ({'timed_out': True}, {'stdout_truncated': True}, {'stderr_truncated': True})
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:37`; AST `674e8c3f1d6ed99fff580bc550626f3647cf4c1de0959e04cfbe046c49089f56`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, dict, self, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:37`; AST `3eba04a73c00bb7f0f75f124dfc6e7276a712cf3ad6caa45b75824216e8af845`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, dict, self, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0].body[0].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:37`; AST `2565e2d5bd2228f302d984d0adc2ac6c48225f3736c39315c3bf253ab5736478`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, dict, self, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0].body[0].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:37`; AST `5bb32f85ed90054bd57313550c01da7ff1f4512281dd902cf95000214c826c86`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self, update. Outputs/bindings: (none).
Calls/effect boundaries: dict, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].body[0].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0].body[0].value.args[0].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:37`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].body[0].value.args[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[0].body[0].value.args[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:37`; AST `bde40dad4654296874cfa317e16e8638421ef7251b4012dcb8f9a2e3cade376d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].body[0].value.args[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:38`; AST `56ad30da3f47718a45a51ec4b8694addbd873d855caff8cefdd371ef86d7e640`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:38`; AST `1a30a5ab5d6925fe9b5b09bfa112f840bad1a9fdaf54a63bdb48487657a0b0b3`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:38`; AST `703bd9151d0e9d62c345bda4d91e0012448ed771389adb0f0ca1891bfa9301cd`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[1].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:38`; AST `290bedee5fd08fb6b7864ae9e6a34e34eebfe7d5389fa56c67cf766f7aa9a1f5`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[1].value.args[0].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:38`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value.args[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[1].value.args[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:38`; AST `bde40dad4654296874cfa317e16e8638421ef7251b4012dcb8f9a2e3cade376d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value.args[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:39`; AST `d41f4e7f12e6199cf65903658a72823976a1e4b851fc1aa568ac6b3a22b4d9ec`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:39`; AST `aeea661c1778ad891affc1e629e33875c74b61d9966cd72f33d4a30d0b059942`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.assertEqual, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[2].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:39`; AST `6631f5c0a6a8a455678790c9d40e6a198cc1ec42a3f6261a13afef440a8910d1`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, dict, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[2].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:39`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[2].value.args[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:39`; AST `f71f61d7cbdc3cb5854048f0294dbf9767d67200462f99885992d2a3e330dbc3`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict, self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value.args[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection::root.body[11].body[3].body[2].value.args[0].value.args[1].args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:39`; AST `bde40dad4654296874cfa317e16e8638421ef7251b4012dcb8f9a2e3cade376d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value.args[0].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:41`; AST `cbb79b6f677342ebed761cca743630a1b3eb3a080cc1a5f2db0901b96c295078`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_deal, result, self. Outputs/bindings: result.
Calls/effect boundaries: classify_deal, self.assertEqual, self.assertIn, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:42`; AST `59b7f1897714c7d41f26beb5a6d8c7f5f53ee25aa50dd094c0d6d8a5ff99637d`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, self. Outputs/bindings: result.
Calls/effect boundaries: classify_deal, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:42`; AST `22cdb5ad0b24f38ed20f0aa04ddc0527202a28b65e1b5205c71f54ba89e82d03`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:42`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:42`; AST `bde40dad4654296874cfa317e16e8638421ef7251b4012dcb8f9a2e3cade376d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[1]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:43`; AST `34ffcdc215d785b2fc8a306102df6247896f926a79529d94232dcf1a7a66acba`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:43`; AST `970ac04a74ffc4a8f92d459532d165c75b31113c55b0ad56e1b8b6098052f361`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:44`; AST `fa600f28143396e35dfd76761a2d65824163db89a978fde10784b8884431560f`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_solver_ok_remains_semantically_unqualified::root.body[11].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:44`; AST `ca43d325c729f80a8591afe8d67b7123578d71df66f4de618de7bec02c25a8ab`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:46`; AST `63acd1f22506a024efda2c0928dc2f02af3509e7a63b01a67d84378163a64fed`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_deal, observation, result, self. Outputs/bindings: observation, result.
Calls/effect boundaries: classify_deal, self.assertEqual, self.assertIn, self.observation, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:47`; AST `71d44f29a350d1e2e9b169795e8e29b78a7563d0b4fa1774f001efb92071146b`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: observation.
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:47`; AST `bde40dad4654296874cfa317e16e8638421ef7251b4012dcb8f9a2e3cade376d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observation.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[1]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:48`; AST `5a083b8c774fc096845ecb1bedf2160b203e94d824d847521619e5a07cf438e1`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[2]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:49`; AST `905b03a47deda5bc4fdf980d0b993f8e979660634ea396897142f693544aa79a`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[3]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:50`; AST `74d92995b8a3292055579ece4d804fb77ffbb5926d9180fc36203b076b975778`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.assertEqual, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:50`; AST `c3de82f2f2dd28ac9a6a6f229c601f6a06c5773c7c380e8ad6b270d17b3a82f2`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.assertEqual, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[3].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:50`; AST `6fe01df7cbd051a76115a65329a380dd621a1f2315ef12ec151231a578881a3d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[3].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:50`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[3].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[4]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:51`; AST `f011c0836fc5eb34c835b149cd8b3e6ed13e67d583b53604a85aea82ed30a4a3`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[5]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:52`; AST `d75663b9d1f47c8a3293f903ba926a2685a87692d8808d6d3dfa91c98cf73ff0`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_deal, observation, self. Outputs/bindings: result.
Calls/effect boundaries: classify_deal, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[5].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:52`; AST `6fe01df7cbd051a76115a65329a380dd621a1f2315ef12ec151231a578881a3d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_deal, observation, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_deal, self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:52`; AST `0d290542a1b8429ec8eca8bcb4e3c9bad1b37e8478930e74205a6369c555e317`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.run_record.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[6]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:53`; AST `5bddab33ad606eeaf66880144c3a52bac7950b3e9de6ba48405b3442a2b09787`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[6].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:53`; AST `30bed06a3d0a5f958796aba462eee71e1eb8b9a85c9669d00a3910278153ad79`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[7]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:54`; AST `9f56674975e8945f4570a9dcd35acc406a5f4656c99f80f0dfaa0971352cc665`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion::root.body[11].body[5].body[7].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:54`; AST `093622cb05681400d6df558e75f36b191dcbd591b176d01813cd563d10d31351`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:56`; AST `4db6ca4fc529e7e2b52a324ba381371d403454bbb7901faa75ea95e12f6a1c94`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, assertions, ast, calls, isinstance, len, n, negative, new, old, original_assertions, self, targets, tree. Outputs/bindings: assertions, calls, n, negative, new, old, original_assertions, targets.
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_negative.py').read_bytes, (ROOT / 'verification/roadmap/python/policy_deal_positive.py').read_bytes, (ROOT / 'verification/roadmap/python/policy_positive.py').read_bytes, ast.dump, ast.parse, ast.walk, calls, isinstance, len, self.assertEqual, self.assertIsInstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:57`; AST `7f2743ab53a329a1579b79d0472962e73ec3d82cbb3256767e6e16afe3264598`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, ast. Outputs/bindings: old.
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_positive.py').read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:57`; AST `0da3af028ce1f6d92406efc42fbfc874142af68ffbe02781c0f003c1d9f4ea04`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, ast. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_positive.py').read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:57`; AST `ec0f1503cfdcce0af96cbf8afe80469b4f6055d58bab72d2603de4b5424e14ed`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_positive.py').read_bytes.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[1]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:58`; AST `236d8b266be19d96d1ff93b760b4c0ef868ba695ab6c60993daeacac41d4bf5e`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, ast. Outputs/bindings: new.
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_positive.py').read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:58`; AST `f7bc94c7a921b8c67ad0c5e797c3d5f70b108d86923d6fc838163ee3a73b596d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, ast. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_positive.py').read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:58`; AST `ec0e0745cc6186e9435b2cde5a45f3f7c9960b68b4b5796b21b32a0634fd822f`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_positive.py').read_bytes.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[2]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:59`; AST `c9aadf05b4f145fd09d3eab19ab358e82ca839f444e9a1ef266379a9ced6fb61`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: targets.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:60`; AST `5ee60905f6c52c185c590b56d305164e1bf2620a200e32cce38ab40f6140ecc8`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, targets, tree. Outputs/bindings: calls, n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3].value::Lambda

Source: `infra/tests/test_roadmap_python_deal.py:60`; AST `27ceb3df42beaf777149228201500abc50939d65e0e461e9e5d6912db3ddfd50`.

Rust module: `infra::tests::test_roadmap_python_deal`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: ast, isinstance, n, targets, tree. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[11].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3].value.body::ListComp

Source: `infra/tests/test_roadmap_python_deal.py:60`; AST `7ace8433dee14602a710ae1f7cfc90617dc41fa8d612b7a526224b4fad01b8d1`.

Rust module: `infra::tests::test_roadmap_python_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, targets, tree. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[6].body[3].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3].value.body.elt::Call

Source: `infra/tests/test_roadmap_python_deal.py:60`; AST `a8894dcbc048f57508ef0b204d52c09827f7d3518c19439cca92c87fcdaa7146`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].value.body.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3].value.body.generators[0].iter::Call

Source: `infra/tests/test_roadmap_python_deal.py:60`; AST `19592678e84fe9470658558ce2f8969cde685bcf0acebf08ba251a95a79335f2`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].value.body.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3].value.body.generators[0].ifs[0].values[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:60`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].value.body.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[3].value.body.generators[0].ifs[0].values[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:61`; AST `9ce24aafa5e3ed7e693706a6715fd0404a2b6319de627d2f2e69ce8c15babbe7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].value.body.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[4]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:62`; AST `9cf21f4057b2c3cc12e7ba229a0d2d588e7d180f87176baf058f684bc3e22ca8`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: calls, new, old, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[4].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:62`; AST `baf49c2d7a1dca693aa51444ed087bf3959dbf1d0cf95e4f1646153ec253ec83`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, new, old, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:62`; AST `0dd0541a676bf30e2454ccb3e69dd38c4ec06bb1ef8e1dfed34c7a6a6c14847e`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, old. Outputs/bindings: (none).
Calls/effect boundaries: calls.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[4].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:62`; AST `8cece3018ca2959b11c71efb3a2e0ad796a32076680428dcfd7bc3f496e084e7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, new. Outputs/bindings: (none).
Calls/effect boundaries: calls.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:63`; AST `16fd5f6e024e8d1b91932b68e46f9f261ad5b7f22306cb71cfb883569aece43a`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: calls, len, new, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:63`; AST `40f468144049544b3097d956d7cb7a81ee72208f6c9263ea6d34b2906e48d4a7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, len, new, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:63`; AST `907550bb22451c448ae379054ee7f55478a91118da646a92f28c3c7896276e32`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, len, new. Outputs/bindings: (none).
Calls/effect boundaries: calls, len.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[5].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:63`; AST `8cece3018ca2959b11c71efb3a2e0ad796a32076680428dcfd7bc3f496e084e7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, new. Outputs/bindings: (none).
Calls/effect boundaries: calls.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[5].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[6]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:64`; AST `7b18486aa000bf2a1834d2cd9cf15504576987ad809a64f31a9c3462ced48e3e`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, old. Outputs/bindings: n, original_assertions.
Calls/effect boundaries: ast.dump, ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[6].value::ListComp

Source: `infra/tests/test_roadmap_python_deal.py:64`; AST `c0bddb1cd42dbfc33b36bb61db063d4a618ec382431f3a90ef680be0fde27cad`.

Rust module: `infra::tests::test_roadmap_python_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, old. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[6].value.elt::Call

Source: `infra/tests/test_roadmap_python_deal.py:64`; AST `7e0c2f2459e1235c0b6b11b2a1def7dbc9f83c2d9878cea09410f52cc50de0cf`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[6].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_python_deal.py:64`; AST `e32ac360b9f0fd55998c3e58f5f17ed31af3b7ad8c145ee32b25366bc962a392`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, old. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[6].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[6].value.generators[0].ifs[0].values[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:65`; AST `23e18c3c39ade2f3d2432c60fe81aa102408a21a7fb08bfc38a5c11908cdae5c`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[6].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[6].value.generators[0].ifs[0].values[1]::Call

Source: `infra/tests/test_roadmap_python_deal.py:65`; AST `9ce24aafa5e3ed7e693706a6715fd0404a2b6319de627d2f2e69ce8c15babbe7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[6].value.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[7]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:66`; AST `0e3e992fdb9db9160de28ef14e7d5d08682dc571c9cac8bcaffffac81f37f391`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, new, original_assertions, self. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[7].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:66`; AST `fd553b7d3133b78d0641fe1d3f9619b4dce13220c7ebab16143f958dc6981ad3`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, new, original_assertions, self. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[7].value.args[1]::ListComp

Source: `infra/tests/test_roadmap_python_deal.py:66`; AST `bb5bc68e8f6c97b3ec3353ff745e90d56e903a1c852eb635cc64ef60ef6f6f48`.

Rust module: `infra::tests::test_roadmap_python_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, new. Outputs/bindings: n.
Calls/effect boundaries: ast.dump, ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[6].body[7].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[7].value.args[1].elt::Call

Source: `infra/tests/test_roadmap_python_deal.py:66`; AST `f7e7351e55e236c9d04c513a26163c268040eb9bb56c626484882e95e30ebc49`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, n. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[7].value.args[1].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[7].value.args[1].generators[0].iter::Call

Source: `infra/tests/test_roadmap_python_deal.py:66`; AST `93e09d689ba3dc280792f8a83e3514509b91b120d708dcfde66c4f75560b4451`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, new. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[7].value.args[1].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[7].value.args[1].generators[0].ifs[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:66`; AST `ec459fe7660e2311b9d6374445e99c314277891140df6f9795bcc3affd02ce37`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[7].value.args[1].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[8]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:67`; AST `47b385b80cdd6f101b3d920e4a26e75f03002bf74ff1783b930e9afdb4189b51`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, ast. Outputs/bindings: negative.
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_negative.py').read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[8].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:67`; AST `fdbd831e54baee45881233acefab32130cea4af881e64c7a788ed050b46bb5b8`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, ast. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_negative.py').read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:67`; AST `ce7a2ecb2804a76f62b302e7a2c79eaec4353679976515a5b95aed932164c541`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'verification/roadmap/python/policy_deal_negative.py').read_bytes.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[9]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:68`; AST `2a222314a16afb995cf05db2293f5d85a8f4018cba3a67755941ef8b649d95e7`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: calls, len, negative, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[9].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:68`; AST `675f962578d08e8f5a29dffb9453e5e1d3358df64882e71aaae2bcbc75e440b5`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, len, negative, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[9].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:68`; AST `3277c7b5a75d3945da8fddc2763eed55e65bf110c1d37e5ea6f27ba8a0a6133b`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, len, negative. Outputs/bindings: (none).
Calls/effect boundaries: calls, len.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[9].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:68`; AST `bcd830089eaab127833aaa47eb2401bd5742f3093ef11795a1097f956076568d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, negative. Outputs/bindings: (none).
Calls/effect boundaries: calls.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[9].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[10]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:69`; AST `26291e7203e8849cf893ccd1adc49943321483f472009aee70774a3d6e348a38`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: calls, negative, new, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[10].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:69`; AST `68938cce1326822279423e35ff1547c4c0886634879862d608ac6349bb3b5201`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, negative, new, self. Outputs/bindings: (none).
Calls/effect boundaries: calls, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[10].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:69`; AST `bcd830089eaab127833aaa47eb2401bd5742f3093ef11795a1097f956076568d`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, negative. Outputs/bindings: (none).
Calls/effect boundaries: calls.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[10].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[10].value.args[1].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:69`; AST `8cece3018ca2959b11c71efb3a2e0ad796a32076680428dcfd7bc3f496e084e7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, new. Outputs/bindings: (none).
Calls/effect boundaries: calls.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[10].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[11]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:70`; AST `3227673d4587333aced22fe80aec5b6eac7de6f5170d1bced30f97f93e84777d`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, negative. Outputs/bindings: assertions, n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[11].value::ListComp

Source: `infra/tests/test_roadmap_python_deal.py:70`; AST `35a6ac7c21ffb248e87821ebb04742a42f1c9b8769b9ffebb6b2db7c782cb737`.

Rust module: `infra::tests::test_roadmap_python_deal`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ast, isinstance, n, negative. Outputs/bindings: n.
Calls/effect boundaries: ast.walk, isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[6].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[11].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_python_deal.py:70`; AST `f8fc5fad29a1f36b30ece969316c1720f35e08e7938ae95eab2edffc8a19c068`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, negative. Outputs/bindings: (none).
Calls/effect boundaries: ast.walk.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[11].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[11].value.generators[0].ifs[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:70`; AST `ec459fe7660e2311b9d6374445e99c314277891140df6f9795bcc3affd02ce37`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[11].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[12]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:71`; AST `b849841ba5d3598c767330fdd7d4633133ad7f425b08e2dc37e4a94c8332ead0`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertions, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[12].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:71`; AST `22abb17b278929057f4606365e303090f67d0cb67f9c47cc8bf808cc41ba168f`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertions, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[12].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:71`; AST `05b0073b364f4e014bf089ac6703473d70882b117e2b081fd0083b56418947ae`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertions, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[13]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:72`; AST `50d2750962a55650daf7a16efb1febb2d6af36c1a628783485576c9326b1cd97`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertions, ast, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsInstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[13].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:72`; AST `59cf95ac26e201059e2296cd058c2dd91ca6a769d0debe828188822b9cd96f8a`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertions, ast, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsInstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[14]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:73`; AST `81edd31d6b43c82f5d8b048e988d1898f4423841d4157b99df9bd1d1b49aeaa2`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertions, ast, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsInstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_controls_keep_all_original_calls_bool_case_and_assertion_expressions::root.body[11].body[6].body[14].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:73`; AST `d883a75163c9b8de65ef181ba406be9fc3939699796c7c3690c9547da0bcd283`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertions, ast, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsInstance.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_python_deal.py:75`; AST `4e0e8bbc9cc03dca2a98aa0687a5ebb75f06f3ab47e0fc891f5d5727e23dcc18`.

Rust module: `infra::tests::test_roadmap_python_deal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, Path, backend_observation_key, directory, json, path, qualification_backend, root, self, tempfile. Outputs/bindings: directory, path, root.
Calls/effect boundaries: Path, backend_observation_key, json.dumps, path.parent.mkdir, path.write_text, qualification_backend, self.assertEqual, self.assertRaises, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:76`; AST `1aae77bf376dbb897a065304b71ed6655f89aa37ba1b5717e7c8b36a09213f62`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:76`; AST `96a17c30ac1de7b5996895fd7cdf4816056133c7e1742e98c35ea858b41d05ae`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:76`; AST `ff940ab2b94573ce861e6180cc418aa06da4ab4084cdb590f030bdc380736413`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:77`; AST `366b8d86f9068f8046a97514cf35c8290d6b8e8a7e36b652341f571e8329fc17`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:77`; AST `3a8191a332fb65efdc6f9613dd9745b87ec5a6f18cd4d046354dbaa079eb5451`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:77`; AST `65f470dc6792151a8eb92bf95e7410e40cd17cdba54a6de6e189c349f683f27a`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[2]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:78`; AST `51c0cea1089849061c758c3f533389d3e2e03b6f8152f73491fbe9152b9b0369`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:78`; AST `f7c68343a813729f1da77e810906366befbebc9bf5329bcc09178f170719c6e4`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:78`; AST `9bda55d6b962dec8536101d56ba7e8a38db85cf46ddcc04deee23904b7306b2e`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[3]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:79`; AST `d11707624c961c727569f56ff9e2bcbd7d5d9dbbf2bb7fdb84f19f44de736b20`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[3].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:79`; AST `52989f41b783b4db633b3c0eb78a850b86373cafaf8e082dcdaf49b8fee643b9`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key, self. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:79`; AST `36655f81da593bb8eacc454e72fe0325649d3af555e537faf798db387fa6290c`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend_observation_key. Outputs/bindings: (none).
Calls/effect boundaries: backend_observation_key.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4]::With

Source: `infra/tests/test_roadmap_python_deal.py:80`; AST `bb55d588a0e4bfed427e85fc640ad3ba19ece6c5bb4e22ce6dfcecc64626161c`.

Rust module: `infra::tests::test_roadmap_python_deal`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, Path, directory, json, path, qualification_backend, root, self, tempfile. Outputs/bindings: directory, path, root.
Calls/effect boundaries: Path, json.dumps, path.parent.mkdir, path.write_text, qualification_backend, self.assertEqual, self.assertRaises, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[11].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_deal.py:80`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:81`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:81`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_python_deal.py:82`; AST `447bbe084c0fd03f3cf707b1cba1d1c592a278e2f437ad76c6e50c3f251c0603`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:83`; AST `4a02dacfcdc4bdb0f5e882cce3190753b897fe61bcc8e2b13d0ac08a1dbc7824`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:83`; AST `994840cf9a86a7ba49bb09b92b22661abceaeff09aca1fbcfc473e1e6303e386`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:84`; AST `673d53127b2462829449f4416df94035099af20a88a961b9a4e69f414abc7968`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:84`; AST `f0bacd154dbfd06d97a3e5c8c15e10a418b7dd20eded67eca56d252f49e1adb7`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:84`; AST `054f48b30c11ad3f428544f696ede51d225ffc36143d3fb4003f80f6428d55dd`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[4]::With

Source: `infra/tests/test_roadmap_python_deal.py:85`; AST `d3ad325911eab83a580989ebd410968fdc0df657f3e81d99fee0f32f0c6b8143`.

Rust module: `infra::tests::test_roadmap_python_deal`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, qualification_backend, root, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_backend, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[11].body[7].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_deal.py:85`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:86`; AST `511d6948b642d5a60d0b0400bd49934c214263c8bff938ac3155854cb30c0b9a`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualification_backend, root. Outputs/bindings: (none).
Calls/effect boundaries: qualification_backend.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:86`; AST `7ed80140789c6ea5e2bbc019c886c83b3f203e073a4356b336214c7d39d926ff`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_backend, root. Outputs/bindings: (none).
Calls/effect boundaries: qualification_backend.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:87`; AST `e9bb8946dc088cff0015a408805035ea4b81fabc43fc3aff8f1363d9fce4566e`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:87`; AST `9ff52ccc6a31c58b6b0e6b98056c595376e878c4932d8572e463da02cec178fd`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[6]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:88`; AST `3d0cd4e6599fab639ea8135f7f0227e66348c539c69f6b8391c96c708490ba16`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualification_backend, root, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_backend, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[6].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:88`; AST `b6dfb00edbde7955dd365082ddf00ca260915ce9306648b1338fca6b9794e8b6`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_backend, root, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_backend, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::DealQualificationTests::test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend::root.body[11].body[7].body[4].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_deal.py:88`; AST `7ed80140789c6ea5e2bbc019c886c83b3f203e073a4356b336214c7d39d926ff`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_backend, root. Outputs/bindings: (none).
Calls/effect boundaries: qualification_backend.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[12]::If

Source: `infra/tests/test_roadmap_python_deal.py:91`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_python_deal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[12]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[12].body[0]::Expr

Source: `infra/tests/test_roadmap_python_deal.py:92`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_python_deal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_deal.py::module::root.body[12].body[0].value::Call

Source: `infra/tests/test_roadmap_python_deal.py:92`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_python_deal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, copy, json, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
