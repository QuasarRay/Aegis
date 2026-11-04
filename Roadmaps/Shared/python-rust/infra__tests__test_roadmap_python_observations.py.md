# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 304. Inventory digest: `1a2c03b825cf9371307cf3af719a4e2b886931ed9c5a2cf9d310570faa6fbbaa`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_python_observations.py::module::root::Module

Source: `infra/tests/test_roadmap_python_observations.py:1`; AST `014916ecce10904a063379e1b99656b95246a3db2ea99da094eb69a0b1bb369a`.

Rust module: `infra::tests::test_roadmap_python_observations`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, ROOT, __file__, __name__, adapter, after, any, ast, b, before, binding, candidate, compile_roadmaps, compiled, content, copy, dependency, dependency_before, diagnostic, digest, directory, file_binding, fixture, intent, isinstance, json, ledger, len, materialize, n, name, next, node, observation, original, packet, patch, path, policy, qualification_receipt_dependencies, qualification_reports, r, raw, receipt, relative, replacement, report, result, result_path, self, shutil, source_closure, str, sys, tempfile, tool_binding, unittest, value, x. Outputs/bindings: ROOT, adapter, after, b, before, binding, compiled, dependency, dependency_before, diagnostic, directory, fixture, intent, ledger, n, name, node, observation, original, packet, path, policy, r, raw, receipt, replacement, report, result, result_path, tool_binding, x.
Calls/effect boundaries: (self.root / '.aegis/roadmaps/reservations.json').read_text, (self.root / '.aegis/test-tool-binary').unlink, (self.root / 'infra/agentinfra/roadmap_policy.py').read_text, (self.root / policy['path']).read_bytes, (self.root / result['path']).read_text, Path, Path(__file__).resolve, Path(sys.executable).resolve, any, ast.parse, compile_roadmaps, copy.deepcopy, digest, file_binding, isinstance, json.dumps, json.loads, len, materialize, next, patch, path.parent.mkdir, path.write_text, qualification_receipt_dependencies, qualification_reports, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.bind, self.details['artifacts'].extend, self.details['runs'].append, self.persist, self.reports, self.save, self.write, shutil.copyfile, source_closure, str, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:1`; AST `e31b272a05bdd8a06aedca8325d390272e142afde3dfcca6977332679764f68b`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_python_observations.py:8`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_python_observations.py:9`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_python_observations.py:10`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_python_observations.py:12`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_python_observations.py:13`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[8]::Import

Source: `infra/tests/test_roadmap_python_observations.py:14`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[9]::Import

Source: `infra/tests/test_roadmap_python_observations.py:15`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:16`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:18`; AST `6ec1f57b05a0868100633c99a7da2f6640381f55496fafdd70cc006ccbd23c65`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[12]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:19`; AST `4e8a6be0cf971ee8054ec9103737dd9ef387f3567e3c7d96f8f1a67304d45a6b`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:20`; AST `7903500660d6419532fb05d53920d5290554e3194c5894134211635fe8ad7cbf`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[14]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:23`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[14].value.value.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:23`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[14].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:23`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::root.body[15]::ClassDef

Source: `infra/tests/test_roadmap_python_observations.py:26`; AST `a0f1f74498dbaf9dc82fe12ff3fc23e88d41306ec273d44569f11833342fd01c`.

Rust module: `infra::tests::test_roadmap_python_observations`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, ROOT, adapter, after, any, ast, b, before, binding, candidate, compile_roadmaps, compiled, content, copy, dependency, dependency_before, diagnostic, digest, directory, file_binding, fixture, intent, isinstance, json, ledger, len, materialize, n, name, next, node, observation, original, packet, patch, path, policy, qualification_receipt_dependencies, qualification_reports, r, raw, receipt, relative, replacement, report, result, result_path, self, shutil, source_closure, str, sys, tempfile, tool_binding, unittest, value, x. Outputs/bindings: adapter, after, b, before, binding, compiled, dependency, dependency_before, diagnostic, directory, fixture, intent, ledger, n, name, node, observation, original, packet, path, policy, r, raw, receipt, replacement, report, result, result_path, tool_binding, x.
Calls/effect boundaries: (self.root / '.aegis/roadmaps/reservations.json').read_text, (self.root / '.aegis/test-tool-binary').unlink, (self.root / 'infra/agentinfra/roadmap_policy.py').read_text, (self.root / policy['path']).read_bytes, (self.root / result['path']).read_text, Path, Path(sys.executable).resolve, any, ast.parse, compile_roadmaps, copy.deepcopy, digest, file_binding, isinstance, json.dumps, json.loads, len, materialize, next, patch, path.parent.mkdir, path.write_text, qualification_receipt_dependencies, qualification_reports, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.bind, self.details['artifacts'].extend, self.details['runs'].append, self.persist, self.reports, self.save, self.write, shutil.copyfile, source_closure, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:27`; AST `9b1196c3b24444219a5cb71531c6ea4caa05135a4728d99fccfc37bbd148699d`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, ast, digest, directory, fixture, intent, isinstance, n, name, next, node, path, policy, raw, result, result_path, self, shutil, source_closure, str, sys, tempfile, tool_binding. Outputs/bindings: directory, fixture, intent, n, name, node, path, policy, raw, result, result_path, tool_binding.
Calls/effect boundaries: (self.root / policy['path']).read_bytes, Path, Path(sys.executable).resolve, ast.parse, digest, isinstance, next, path.parent.mkdir, self.addCleanup, self.bind, self.details['artifacts'].extend, self.details['runs'].append, self.persist, self.save, self.write, shutil.copyfile, source_closure, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:28`; AST `5a297ee9d55f4a5ad5db69390f11e5ff6b29b0e60014cfe9e10a20b6e9789438`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:28`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:29`; AST `a12d3f2c575f32263e699cd5731a2f11f4bc92700e9417bd96671b447f58f305`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:29`; AST `5a2c45b19a614ce704c6b848fb6284c67bd01e2dc59f0560df9787494a37d110`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:30`; AST `771e6485628d563393a4148f597a406433d53eb73a03e4ac91444a38b131ab10`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:30`; AST `b130fb7f3f48af704e9fdced25074dd867fc0b17d3e9dae24a1bfcce79dfe708`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[3]::For

Source: `infra/tests/test_roadmap_python_observations.py:31`; AST `1951d3ce4d28427658aaf5668efc318ed1b9ff481c3f5a3b73a9db6a7261ebae`.

Rust module: `infra::tests::test_roadmap_python_observations`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ROOT, name, path, self, shutil. Outputs/bindings: name, path.
Calls/effect boundaries: path.parent.mkdir, shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[15].body[0].body[3]; no call, error or mutation may be omitted. Iteration: name in ('Roadmaps/Shared/registry.json', 'Roadmaps/Shared/records.schema.json', 'infra/agentinfra/__init__.py', 'infra/agentinfra/roadmap_policy.py', 'infra/agentinfra/roadmap_records.py', 'infra/agentinfra/security.py', 'verification/roadmap/python/policy_positive.py', 'verification/roadmap/python/policy_negative.py')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:35`; AST `16c8e9194cc4e905a83d3c71092388e0be89d88461647b1e485eaa9b22d71c6b`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:36`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:36`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:37`; AST `6205c85f75614c4232f9b309c97af8da87edf511b8d0f9577c2d040f86244710`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, name, path, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:37`; AST `15b91187c11f42f30998a2c204cce4486bd8ff999a567d35855f15fd6b08c82b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, name, path, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:38`; AST `c6febd833343bfe8bbd80e5b48105e8b23e32066750edac442d4e3a9a1f64596`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:38`; AST `661dd2747da097b38cf51de1a915b3b1eb50d12711308907e95d4f51cf021837`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:39`; AST `a4da2ce6a515d850aad4f138f7fc8e8a211bd909947b89e94418268109759a8c`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:39`; AST `81fc96d479f86208e9cc61a2ea48c80be6d7ce612f95482db35c60e5e6b2570c`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:40`; AST `c6baf72a03b1c9d1a3baf6c228c15d6797d42d065ffaa9bc64a824aa72491360`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:40`; AST `ce722cb7de33981ce783c7e6ae71b39d54d5d94040b206bedbc8d3239129a9bd`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[7]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:41`; AST `792f078214f572a57316c78b709be4f5718334209baada9be0eba410257ee18d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:41`; AST `63cdadbc9239213e991e0c197cd68a293c5e1cebcb14723605e180f6edaeb7e3`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[8]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:42`; AST `6e4e59a4df5fe8dff24c580bd357873d3af43dff2d72685e227a797e488e51af`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[8].value.values[3].elts[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:43`; AST `67c79a01b164fe1b4fd82544b069456d6518dae6ef7335200685cdb80120990f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[8].value.values[3].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[9]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:44`; AST `929b8b8e94af42009083a0e5ee5e5a5510dd22f7afee99a12d0d6b961b020a4d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:44`; AST `38e2aa1c0fe67c04bd64601299ae88b7ef708e4145862028c429f22162aaf598`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[10]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:45`; AST `4135d1686b282eace68fadadb20cc7f1a66f83dd687bca38af6cf8c1c33cd998`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool_binding.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[10].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:45`; AST `7f5f1c76560d6604412631b74ec0d2df1ca5227cbadd06fa106498fe91198494`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[11]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:46`; AST `8e690d38c5df7bcae5e5597d2cfa9fd86ba1f6cde03ed1332fb7793ad1c6af0d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:46`; AST `d63dd6731a7c44379e6d04b7275109a8ef25fef93f5621c6082e5959f78eddee`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[12]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:47`; AST `3bbfa9dbf1e3c8248b6a50da4304a20118b8fe62a1f37cae4f61f692f512df28`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self, str, sys, tool_binding. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).resolve, self.bind, str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[12].value.values[5].values[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:49`; AST `5f4301ece7418d11bc319c98233bc3212d0be4800c3f5f269ff7cbb3822bd4a4`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).resolve, str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[12].value.values[5].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[12].value.values[5].values[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:49`; AST `ffc3d1229ffb96e896c21a46d0a14c6093fceaf85290bc162305ed6355a20a10`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).resolve.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[12].value.values[5].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[12].value.values[5].values[0].args[0].func.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:49`; AST `0dfff54cbeeb64407db17d4e6b154f3aff810a988368a772f2aaa5d71265f9f3`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[12].value.values[5].values[0].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[12].value.values[6].elts[2]::Call

Source: `infra/tests/test_roadmap_python_observations.py:50`; AST `1128bb31344076b6092b0ef6b5c9147c7c923ac928785ac3444d669cd4896b38`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[12].value.values[6].elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[13]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:52`; AST `fc0049028fd50ef3f27bbc85c42411c59bde7db3de453d18ac37b103199ca7c4`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, sys, tool_binding. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[14]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:55`; AST `2475dceb6512c14a58cd9bbaf2051457b39b694bdff508642c502248c4b1f5cc`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[14].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:55`; AST `7d1613b5e617c70fe4c4aa38751af0f65f1a5ed0859dfd7bb1e05529d4fc8010`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[15]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:56`; AST `535ffcceb183fa4420e23d73952e544ff2999db6f365b43845aad5c0dd725b27`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: directory.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[16]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:57`; AST `c9b0fe17e10b0c2365b9d3f12b33e4198212582c11d06499ab9547da660e7a9f`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[17]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:58`; AST `d307caf9256f180e752110de11d68055fee5100c9c90e3d374e4800eb478782b`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[18]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:59`; AST `aa18a95381fb9072495e5ac3c4db0d12af58231699dd3c402882e44cbe8ed09e`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[18].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:59`; AST `37c53b9f591eb6686816bf21413731d00f43aa421fe8fa00a3db0cd4892c2bda`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[19]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:60`; AST `06a868de87bd2e9b25e7f2d8ae6de5037da585de9a6a37110b8056526c9e3388`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool_binding. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20]::For

Source: `infra/tests/test_roadmap_python_observations.py:63`; AST `9854211159df04291f355d20afced8e32baa76cc7e2ff7b3ac207365454f80c1`.

Rust module: `infra::tests::test_roadmap_python_observations`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: directory, fixture, intent, name, raw, result, result_path, self, str. Outputs/bindings: fixture, intent, name, raw, result, result_path.
Calls/effect boundaries: self.bind, self.details['artifacts'].extend, self.details['runs'].append, self.save, str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[15].body[0].body[20]; no call, error or mutation may be omitted. Iteration: (name, intent) in (('policy_positive.py', 'positive'), ('policy_negative.py', 'deliberately_wrong_assertion'))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:64`; AST `eb93169b5e9694e17cf4cac633713b6d75a2fc508a8dd37058f58545297fa099`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: fixture.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:64`; AST `c7eef567c481ad8651ceda308a79e39f7a6a084ce3b4f436d8281cac9d6c53a1`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[1]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:65`; AST `b47efeff972b033b3b177ed17e3ded6f0e3e9400837662bd46c4133d5c6b5daf`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, self, str. Outputs/bindings: raw.
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[1].value.values[0].elts[4]::Call

Source: `infra/tests/test_roadmap_python_observations.py:65`; AST `270cf1725930651482e1813157b30cf0ec221d4019e7efc4369bdb8f0cdf6bc0`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[1].value.values[0].elts[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[1].value.values[0].elts[5]::Call

Source: `infra/tests/test_roadmap_python_observations.py:65`; AST `81c10a0b3a3c064213395c486db923755af1831fc785680f6889b890f356f801`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[1].value.values[0].elts[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[1].value.values[1]::Call

Source: `infra/tests/test_roadmap_python_observations.py:66`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[1].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[2]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:68`; AST `03716d25732fbc70d6a273cfa6ab0ba714e3401a8cfd68f9338704f967a4c9b2`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, name. Outputs/bindings: result_path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[3]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:69`; AST `e33d891c9fa5292a78828215a299839f43d3a536670ca8e3ae1429ca9523926d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, result_path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:69`; AST `4d29600cd574b7ee005c033afbbc6636a066217506fc3051bb33a3adab6a255e`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, result_path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[4]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:70`; AST `c86aaba3c8f31d85a7096713c13a4ab7aa3a9ae50f01c2d34f0cdef8824481e6`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result_path, self. Outputs/bindings: result.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:70`; AST `05266139b09ad3c61fc9f86ef31f1b389ec3ceb5b6d9be28ebe8c43eb11d2945`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result_path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:71`; AST `f4df62b9cad46a6d05ad05ed9a3777c415791416e59a0b2e615f7558990a95ef`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, intent, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.details['runs'].append.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:71`; AST `bbcff1314d5b2950cd8ac47e60fe66cbf57e7da8b5ce28783d1320c9e249b9a3`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, intent, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.details['runs'].append.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[6]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:73`; AST `f65417cac895bbd2b15af4ab798fd7b1dd9cfdedc56ab90dc1800de815fd8e4a`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.details['artifacts'].extend.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[20].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[20].body[6].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:73`; AST `7bcae99ff6dd5725cb36687eeb47eff6bed2f7ad87b4b97ffbf9d2872b32258a`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.details['artifacts'].extend.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[20].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[21]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:74`; AST `3ab51c59c63f69a2992021c4e81bcaa7d65e683869d9ef917d15830ce91df5b9`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[22]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:75`; AST `92fb10109e7893e1448355f023613a1df3eaf2a9a585f852eb5b2e62b9d3a9ad`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[22].value.values[1]::Call

Source: `infra/tests/test_roadmap_python_observations.py:75`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[22].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[23]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:78`; AST `441c48d67f70d507e569a49ee4e80f84b9a0acc8c47a70bd06ef614a10c81032`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[23].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:78`; AST `a97a6619549ac1d07ebfd44239ae5a653686f08dc960c3990549cca150257c59`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[24]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:79`; AST `b59f53d2bf8608391362d8a00a65dbb548905da27b4e7869b7a43e4763644d50`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[24].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:79`; AST `b0962e0c3abeb032d8659a565b52b69a92af2e063821ca5584ed414c6b34a3da`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[25]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:80`; AST `38fc969bec0d2416f54aaa32137fd78beb71775c50587de775de448620a9504d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: policy.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[25].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:80`; AST `4d8e5bcbcb7d5f54ba4371bd120bdd467c0184eafaece71ae26bfff2064cbc31`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[26]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:81`; AST `33b83b72ca098ffd87aa00ef1fa2464123322376d50099f070d2a87a1151e1ae`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, isinstance, n, next, policy, self. Outputs/bindings: n, node.
Calls/effect boundaries: (self.root / policy['path']).read_bytes, ast.parse, isinstance, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[26]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[26].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:81`; AST `644b7dbad0185cac0ad954612856667efd386be54c4120a79e86aba00e6951cf`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n, next, policy, self. Outputs/bindings: n.
Calls/effect boundaries: (self.root / policy['path']).read_bytes, ast.parse, isinstance, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[26].value.args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_python_observations.py:81`; AST `d7a5cc4eeee41a52deee264f80a9c5c96043cb254fc8499f7155d3a447f37246`.

Rust module: `infra::tests::test_roadmap_python_observations`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: ast, isinstance, n, policy, self. Outputs/bindings: n.
Calls/effect boundaries: (self.root / policy['path']).read_bytes, ast.parse, isinstance.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[0].body[26].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[26].value.args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:81`; AST `46a36a3be10848082612a166f13af5a278e63e2880473509537fe03c3030eeea`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, policy, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / policy['path']).read_bytes, ast.parse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[26].value.args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[26].value.args[0].generators[0].iter.value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:81`; AST `7a706c968913f16183993b75b80810e19ffded112d0a0b72e1499699fedafef9`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / policy['path']).read_bytes.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[26].value.args[0].generators[0].iter.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[26].value.args[0].generators[0].ifs[0].values[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:81`; AST `6be47f9e1551f535bf2aed1cf83932df0390bf06e04c27a299cb9ed3d358cabb`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, n. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[26].value.args[0].generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::setUp::root.body[15].body[0].body[27]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:82`; AST `ac1380b1fd78745bfe4b44cca910e14c45134e69a796aa93cbdcc129f935a889`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, policy, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[27]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::write::root.body[15].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:90`; AST `920a1bfd18604899c9aa9684a777f1aeb518b68877910b88f98260a3d424584b`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: content, path, relative, self. Outputs/bindings: path.
Calls/effect boundaries: path.parent.mkdir, path.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::write::root.body[15].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:91`; AST `612dd2adce6a63dd3e2fad8942c57edbe760aab2f5efec5eca54b7d564d39a09`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::write::root.body[15].body[1].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:92`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::write::root.body[15].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:92`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::write::root.body[15].body[1].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:93`; AST `e7d86295d64179d2b028cb2ce422f18f3556fa2e2a9c6af0c721dfc49b2f7acb`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: content, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::write::root.body[15].body[1].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:93`; AST `2fbf8b8c80013d8ffd9731649468260004960f701b5582e50e9b79d98bbcbd74`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::save::root.body[15].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:95`; AST `caad8af4e6b75201d728ebff583e1fde2e01f0ad330300d11da21cd1aa1a0b31`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: json, relative, self, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::save::root.body[15].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:96`; AST `36adc4c600f319ea9f6601faeb42ff2ae6063eddce32f21f7813842347c15169`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, relative, self, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::save::root.body[15].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:96`; AST `331966d62f4925eed29e682349194259875f3a945effb7f98a8da6c5c9da0d21`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, relative, self, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::save::root.body[15].body[2].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_observations.py:96`; AST `ccf75a3fee685fba92dbd87286589aeb7a31a140dc5ab06ed02ae7cde17c019e`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::bind::root.body[15].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:98`; AST `06d9f9dfa00f276262bde5104590d900ceda74a9ed1d3bcb2d17e533b833c64f`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: file_binding, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::bind::root.body[15].body[3].body[0]::Return

Source: `infra/tests/test_roadmap_python_observations.py:99`; AST `db7a60d6b0f8e3ea84a494129d986f896401f5f7217ddf33c159624f14b83fbf`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::bind::root.body[15].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:99`; AST `0141101de894968acf540353740c530e21d41ce6beee8c589e9d8fe752d74698`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:101`; AST `64440b2700a7de5b89db5dec8e42bdc99098d824095a84b0c7a034266b36114f`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: binding, receipt, self. Outputs/bindings: binding, receipt.
Calls/effect boundaries: self.bind, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:102`; AST `9d2b1a81e52cbe2ddc1962fc00cf761b93d1742085b241568d4c4868b4e87395`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:102`; AST `310ac51067324c4bdfe468aba7a5a111cc576d82dfd6123a65dacfbefa60982b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:103`; AST `2567046b27557fed63393ba6bfb1c0a2b03c515f99f7a5faf4e565ea622b5337`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: binding.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:103`; AST `cd6bc04bebe7c61f84592d0ada361b540ca7d8586542e4562d159ba53ae22e44`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[2]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:104`; AST `1820af82df7f9a3bb05c7a9d462d6d847e72a505063f17cf55b66b868a26a882`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: receipt.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[2].value.values[13].elts[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:108`; AST `157a6b52e54df632e200f7dcbd84146412596720c2004da490195c2b0c3c5ebd`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[2].value.values[13].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[2].value.values[13].elts[1]::Call

Source: `infra/tests/test_roadmap_python_observations.py:108`; AST `763a7b95347c03303460314cac69c881283f35a6fb2e717ce509b01a6cbfce3b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[2].value.values[13].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[3]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:109`; AST `737bfd75c6280d2d08e4d375bf16cbb6d507666b202a152d29918aade8ba699c`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[3].value.values[4].values[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:110`; AST `157a6b52e54df632e200f7dcbd84146412596720c2004da490195c2b0c3c5ebd`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[3].value.values[4].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[4]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:111`; AST `fee18fd1f96eec0c70a31e4ad10b8d5fa82b7b52d11b307cdae1d29b4ebc2d32`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:111`; AST `d1faaf77ec465d7abdfc2a8af4210c9a053fed2153a14cf49b1bf056b22234cb`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:112`; AST `38d135c307fabe6278854c3d837d39497adf3e318e1afdfffbbdc1a598eb093f`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::persist::root.body[15].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:112`; AST `2ff36c52de537b37390448651a48a12fd51c7ac70ef390cca6ea308b057ece2a`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::reports::root.body[15].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:114`; AST `a2e67788f7b4fb160b20167e7bea396aa115a411975fb20ad83a448f64e2b88c`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: candidate, qualification_reports, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::reports::root.body[15].body[5].body[0]::Return

Source: `infra/tests/test_roadmap_python_observations.py:115`; AST `72d00f1962fb4c8861c8baae05b4fb4ae96df2468c38168df16d219ea5e15f62`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, qualification_reports, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[15].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::reports::root.body[15].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:115`; AST `13a7d28fc836673f74f8d4ed2cff9f1388f5fb229217b0a933ad86518383a8db`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, qualification_reports, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:117`; AST `6e5ed2d85fffc4952ba4adf818a9e3e7b9a7bc70e89fc3a0ad5f4ad3a2a0924d`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: len, observation, packet, r, report, self. Outputs/bindings: observation, packet, r, report.
Calls/effect boundaries: len, self.assertEqual, self.assertFalse, self.assertTrue, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:118`; AST `343e6ea4b1f1b2f6495ad3bef99e1fb97b6098cf7e847a00b81c0fccb140d9ba`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: report.
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:118`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[1]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:119`; AST `8898a035ed40cc57608fd94ae18a21bf82abbfeeed5470a0ddf6610e9fdd92b5`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: report. Outputs/bindings: observation.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:120`; AST `bbae6b839f071b83f72d6bc87aa577e25e38b200decd329ca6bcacb0198e8c17`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:120`; AST `7a43be1b52d9165eb80f21d82a91d7da12d3afae4570f6c2d658965326f72e24`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[3]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:121`; AST `bc4b05e89858efe2f72ead7276c7e501d8125a0779a003bb6e29a860724af94d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:121`; AST `4b70a2cc7aecdfb4b4aa74f2df7f811376b7c93ca9a89d373849b41a619c36f6`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[4]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:122`; AST `41c7e761ec2e9dd7ba4b6dfe725c228907baf72248726d70bb532e8778d59a64`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, report, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:122`; AST `3c4abeb1a7e02a1c78c0110f42686543d379956c1e4c73c869f8c0515bc586a0`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, report, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:122`; AST `f1662388608f086dcd54fa25c18ee6c6da3ecb4344dbd53b781f7b5fc4cf03e1`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, report. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:123`; AST `81cc13e621a2500f3b1ebf9e668b81fc282305f83131a09e06e340c37e2caa93`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, observation, r, self. Outputs/bindings: r.
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:123`; AST `78e76fd528737a60e62903cdb0a2f5b3179829b8c8d298b751355a682a3b557e`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, observation, r, self. Outputs/bindings: r.
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[5].value.args[0]::ListComp

Source: `infra/tests/test_roadmap_python_observations.py:123`; AST `4d6338ea1865c90c984ebd54c4adcb1adbbca2a5e31926923bd1b91436478188`.

Rust module: `infra::tests::test_roadmap_python_observations`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: len, observation, r. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[6].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[5].value.args[0].elt::Call

Source: `infra/tests/test_roadmap_python_observations.py:123`; AST `746d3789a73b59da0f71833f4ba05ac40fc1dfc06044bc025ced1d692d8854ee`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, r. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6]::For

Source: `infra/tests/test_roadmap_python_observations.py:124`; AST `d0097c7a317d1b56e1a46484a028345d796e4c7be3d72680d34b0c00d7d87937`.

Rust module: `infra::tests::test_roadmap_python_observations`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: packet, report, self. Outputs/bindings: packet.
Calls/effect boundaries: self.assertEqual, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[15].body[6].body[6]; no call, error or mutation may be omitted. Iteration: packet in report['qualification_interventions']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:125`; AST `cd0a6242929527fc683391af051a440af299df8cb0d93057276f68405f1c85d8`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:125`; AST `c5316ce402cad1c351301d2179296d9a001de6d6ecc635ec4a7af977abf95121`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:126`; AST `06768d838d1c677a4e82a3db7c626c1db6edf04f4ffc0557d9232b6b7e618af5`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:126`; AST `e378c25145a53db93f46072f9a9b88d30299ec46ec3309f53409c5741e82709f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:127`; AST `35ee1e6f67eb864e3b5e2e4556d723a809188fdd86acadf8ff3424e9c40be780`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:127`; AST `55c4ca938f2431acf1dd5186e133fa54752e7ed583c98815570fcdfd47d14b9b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[3]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:128`; AST `0be69c915fcea2756955a9799e0dfee4cfef2351ac17028d77e2b240f83c2f53`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:128`; AST `1aa3869866b77ffe46f0abffa3d72121236fb0be6aac1bc9803c8aa8c51bc100`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[4]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:129`; AST `337aa19ece8536e6e5567c4689a898b720bef851933ccd701576440560af40b7`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:129`; AST `30dc34e5384f0cfb884fe5989a91919c4963ef34a990c574a48aaa4b13fedc44`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:130`; AST `50ab983b9e174a079cdbd61d11d0ec2a371709964b75427ab89c2b15954c8a21`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_actual_unsupported_controls_join_originals_and_exact_production_location::root.body[15].body[6].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:130`; AST `91ad0b196fdf7e8137a7f8ba86e74cf62b1d9af7e9c1b6cdead3ee3c281d869b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:132`; AST `d7c7d789752ee5b724453161b4358648f215252d8347e0b811dd3812553281e7`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: qualification_receipt_dependencies, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_receipt_dependencies, self.assertEqual, self.reports, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:133`; AST `012b5e64eb3f210609a540f510ef1bbca42a63b1bbb7f7c6932e664b9fa57f65`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:133`; AST `7b5363944a6fcb48d76360e51bbcc8b47078febe3208465887eecb48f5999b60`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:134`; AST `ebc57152aa000cb21afdb79b9738b926d981678af9e4eb5a7b8a3d2312f1f3b8`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualification_receipt_dependencies, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_receipt_dependencies, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:134`; AST `2c5e175534bddb949702caa38183a193f023af8705c5a921655dd5a246f6858b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_receipt_dependencies, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_receipt_dependencies, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:134`; AST `5fcaa050ef9889728c483f9e60bbf3154d4d13f573a177718b9de0db90dea574`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_receipt_dependencies, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_receipt_dependencies.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:135`; AST `90547d493e9781f13fff8c3e5cd074b48b71b6c53af29ebac9b46498bab28be6`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:135`; AST `771fb007db93b00ddacac9daf8f9d8b05c6a7f2619b662c922a7722917c10979`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_observation_remains_not_attempted::root.body[15].body[7].body[2].value.args[0].value.value.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:135`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].value.args[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:137`; AST `6b8310a760492ecdabd7250137c3adcab9425c35fa7f9410d092e9f19b90269f`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy, self.assertRaisesRegex, self.reports, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:138`; AST `6dd4b98537667d49a4ce5b6738f857f918554ba3cfa526b11ea43f430da82a81`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:138`; AST `949f8d4c25c267cda91817e49421925df9818fb8aa3dfb975472704d6c834c00`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[1]::With

Source: `infra/tests/test_roadmap_python_observations.py:139`; AST `1b43a17e4633d68edc699e62e2c1ca2ed2e3cc9f9be8c38be0dfb72c5f581578`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:139`; AST `ad3cfd68e6e0f9a7eca5b60c2bb210b131fb6caf50e4de62a842642a358edfb3`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:140`; AST `dc8293c98c71e543185527516db4c947b5e52b548e27587f960b95943685e718`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:140`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:141`; AST `d30956b299269e58acb05cadff0532bf2ae7f5b9e065fe06a4b472d0a1aafd88`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:141`; AST `0326d43858ec50971403a45594117332a3aac570035fedec7e34a4c9cd3bcb94`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[2].value.args[1].values[1].elts[1]::Call

Source: `infra/tests/test_roadmap_python_observations.py:141`; AST `d554a41c6fecba834b80b389fde943401d9326490bc29b35048dae657a0af0e7`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[2].value.args[1].values[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[3]::With

Source: `infra/tests/test_roadmap_python_observations.py:142`; AST `1b43a17e4633d68edc699e62e2c1ca2ed2e3cc9f9be8c38be0dfb72c5f581578`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:142`; AST `ad3cfd68e6e0f9a7eca5b60c2bb210b131fb6caf50e4de62a842642a358edfb3`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:143`; AST `dc8293c98c71e543185527516db4c947b5e52b548e27587f960b95943685e718`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_convenient_json_and_duplicate_producers_are_rejected::root.body[15].body[8].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:143`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:145`; AST `e3b98ad8bc02db4ea79bbb337b8829d257060a34c63cb848798bfe7dba6b6440`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, json, ledger, self. Outputs/bindings: ledger.
Calls/effect boundaries: (self.root / '.aegis/roadmaps/reservations.json').read_text, json.loads, self.assertRaisesRegex, self.persist, self.reports, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:146`; AST `126d37faadca3631350b2d07bd9e76d2c38bfd3d78e79b8e105d0f75ce78125b`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:147`; AST `441c48d67f70d507e569a49ee4e80f84b9a0acc8c47a70bd06ef614a10c81032`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:147`; AST `a97a6619549ac1d07ebfd44239ae5a653686f08dc960c3990549cca150257c59`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:148`; AST `b59f53d2bf8608391362d8a00a65dbb548905da27b4e7869b7a43e4763644d50`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:148`; AST `b0962e0c3abeb032d8659a565b52b69a92af2e063821ca5584ed414c6b34a3da`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[3]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:149`; AST `cd1f16ebb8e484c3f45423c995cd350f5a6762bc675b0624d09fc1ce83d9644e`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: ledger.
Calls/effect boundaries: (self.root / '.aegis/roadmaps/reservations.json').read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:149`; AST `997eb1f368af3a80c453a387b14f7600a198c94b1d48a8267e84eebadd1aeeff`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/roadmaps/reservations.json').read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:149`; AST `c1d484177718d8b20104f626122ec862c684281e192b96faa6f1737f7a9e8ad5`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/roadmaps/reservations.json').read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[4]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:150`; AST `09dfad327ee3377e51317f9f0b11645c2a5bd8073388bc15f926041b595acbeb`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:151`; AST `fd63600d8b27cf8f162c6e9bbbfd4bf6e1761b6a38b66e51231c7ffebde26ac7`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ledger, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:151`; AST `cee840c7832a655ea1f4b8c0d1c48fca5e09928a96bc9e8d76a485e690076495`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[6]::With

Source: `infra/tests/test_roadmap_python_observations.py:152`; AST `ba64a7c785847c543ae7ac360dc2d4fa7af2435d75a248a90c394481ba1e5026`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[6].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:152`; AST `caba630c34f76c1e59b57cc071a32d8e40afd025d7fe2da3bfdc81a904a28fd1`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:153`; AST `dc8293c98c71e543185527516db4c947b5e52b548e27587f960b95943685e718`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash::root.body[15].body[9].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:153`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:155`; AST `f41847a11f18be1805da550ad7ab51ed76e294f54c7746fa50930c9b6583be3c`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, dependency_before, qualification_receipt_dependencies, report, self, x. Outputs/bindings: dependency_before, report, x.
Calls/effect boundaries: (self.root / '.aegis/test-tool-binary').unlink, (self.root / 'infra/agentinfra/roadmap_policy.py').read_text, any, qualification_receipt_dependencies, self.assertEqual, self.assertNotEqual, self.assertTrue, self.reports, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:156`; AST `264d3bad2c2c8ec43205be36880f57636db611024c5a33fbff0e079f6589cad3`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualification_receipt_dependencies, self. Outputs/bindings: dependency_before.
Calls/effect boundaries: qualification_receipt_dependencies.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:156`; AST `5fcaa050ef9889728c483f9e60bbf3154d4d13f573a177718b9de0db90dea574`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_receipt_dependencies, self. Outputs/bindings: (none).
Calls/effect boundaries: qualification_receipt_dependencies.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[1]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:157`; AST `7b4cafd6e0a8260f99f44095790774340108d5f8682a49eb8d9ce2db69c0baa5`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/agentinfra/roadmap_policy.py').read_text, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:157`; AST `f2b25305383e53f37dc427046a1b18de7f3f323d5b8e545d10cd9d16354eac85`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/agentinfra/roadmap_policy.py').read_text, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[1].value.args[1].left::Call

Source: `infra/tests/test_roadmap_python_observations.py:157`; AST `785c018196ac33499adcd002522e25c2caf6bdd45ed00e98c53cb788efcd400a`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/agentinfra/roadmap_policy.py').read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[1].value.args[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[2]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:158`; AST `343e6ea4b1f1b2f6495ad3bef99e1fb97b6098cf7e847a00b81c0fccb140d9ba`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: report.
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:158`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[3]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:159`; AST `9b5a4e467d5f5fb63ad999791d58883cc2bfd232a07909cef07c46a3e76ca2dd`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency_before, report, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:159`; AST `d308beec04aa4dbc84085ada0edd554eb021e5404e281e72aa6c06ddeba33f5c`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency_before, report, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[4]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:160`; AST `4c3d1f342ecde15517276bc698b9ec35f3123bf65c1fc57fe01d086f05ebff8e`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: report, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:160`; AST `d62cc7e02d9da82747556d34312e859699e871c7c3a67bceb32948b5210ebd24`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: report, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:161`; AST `ef241e8fa3c15e8dcf6d3d7fe36f32edbce49f42462480a7afd7c7c1293c398d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: report, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:161`; AST `52c2e6b3005d1c260ed1e061fb8b3bf24533347ad4af95c93045c8ea5dff9fec`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: report, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[6]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:162`; AST `27cceb12aa61db3788115728cd51e171e30a0ef3e89cd04bee8e1b3505e322cc`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/test-tool-binary').unlink.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[6].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:162`; AST `b592ba7cbb2587b78e304bd8ea1dd4ffeb6885f66164d5cb39876f242951aefc`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/test-tool-binary').unlink.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[7]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:163`; AST `343e6ea4b1f1b2f6495ad3bef99e1fb97b6098cf7e847a00b81c0fccb140d9ba`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: report.
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[7].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:163`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[8]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:164`; AST `1eb57aa21c58ae4e32c52cb4b29f3af7c4f9404058d9b164d5c1a85e3cc47fe9`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, report, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[8].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:164`; AST `bb0cb726770430f350bd4259a490c41bd41aa447699ba81da139e502b3b32361`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, report, self, x. Outputs/bindings: x.
Calls/effect boundaries: any, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:164`; AST `7cadadb1751a1fbe5829500086fed103809789464c27287ba7954e3d173b871f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, report, x. Outputs/bindings: x.
Calls/effect boundaries: any.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit::root.body[15].body[10].body[8].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_python_observations.py:164`; AST `41f30d1772938d82c53bd1c956cad88add6efbc8a959acacef4e113117aa9ad2`.

Rust module: `infra::tests::test_roadmap_python_observations`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: report, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[10].body[8].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:166`; AST `bc5dbf0fcfe20a1a9e17d92a8363ee028915329fd8ac0660f0a06007add8b9e4`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: observation, self. Outputs/bindings: observation.
Calls/effect boundaries: self.assertFalse, self.assertTrue, self.reports, self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:167`; AST `2fa5200918b73b2eda494b9f1983eadc2e8815bb2437d791dfeb00ef67672962`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:167`; AST `6667bb7f538b9a2a95b0c01a2bc3f3ab0d35a7fb4da9bb4d5abc3dfd5ffe7db9`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[1]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:168`; AST `803bfcb91969016b665cac022b2fcaf9b25e68c8608cc92e6f7dda977f562048`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: observation.
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[1].value.value.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:168`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[11].body[1].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:169`; AST `ae7e6592dd79290d1d8e9af54d93be3eb8be48fde10e783047b8a680f1a0e9c7`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:169`; AST `ffacc34fa18ba8b000c15961aba496e65173251d94bf5a2668100eecdba762fe`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[3]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:170`; AST `bbae6b839f071b83f72d6bc87aa577e25e38b200decd329ca6bcacb0198e8c17`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:170`; AST `7a43be1b52d9165eb80f21d82a91d7da12d3afae4570f6c2d658965326f72e24`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[4]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:171`; AST `b3a4ae1b8ab59c1da9c7f59d0f8ff1a2471733ed33387c3843a8deff37962c58`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification::root.body[15].body[11].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:171`; AST `fb61f32786c31fa97abd8ef3fb7ac3a38a3994a4cf5b20cf08f55717961044bc`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[11].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:173`; AST `cfdce95f4fbd454cf190ebd1ea2f4fde1b3ff44ce6529a3fdcc23691d74acd35`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, b, copy, json, original, raw, replacement, result, self. Outputs/bindings: b, original, raw, replacement, result.
Calls/effect boundaries: (self.root / result['path']).read_text, copy.deepcopy, json.loads, self.assertRaisesRegex, self.bind, self.persist, self.reports, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:174`; AST `9b4be5ff9b3f19a29dd9d0b3b3b46e6b5d4eee490a109e936396a9d3ca3164ad`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: original.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:174`; AST `bab7c8830bdae1298fd17bd14001856280d26833919c6db9ac93240f36dd13f1`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[1]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:175`; AST `efa5249f44a07ca4bc8946e61791f3e427b1610ecaa2748314927dc5c3c74384`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[2]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:176`; AST `b59f53d2bf8608391362d8a00a65dbb548905da27b4e7869b7a43e4763644d50`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:176`; AST `b0962e0c3abeb032d8659a565b52b69a92af2e063821ca5584ed414c6b34a3da`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[3]::With

Source: `infra/tests/test_roadmap_python_observations.py:177`; AST `201c16cdd12131d3187c53a9e1e9d96fec2b1390a82bc291f5e94799fdd84422`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:177`; AST `c05dd7dcf257550db25401d47c689d438437d665d1b0a2eed2e89b6c0d94b523`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:178`; AST `dc8293c98c71e543185527516db4c947b5e52b548e27587f960b95943685e718`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:178`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[4]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:179`; AST `c7d39c8e5847d3e6ebddaf7c029a7442c7e9f2d84cff18596f690b92984470fb`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[5]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:180`; AST `a86e7bad96d4eefcd002fb2c1067d231ffda00116a87862fcd7ab32c5da44e82`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[6]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:181`; AST `0c94776934f74480422fb68ed0edfbf1bc1f79de3d55ed5237f5217f39d56487`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, result, self. Outputs/bindings: raw.
Calls/effect boundaries: (self.root / result['path']).read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[6].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:181`; AST `94baf44ea5553b4702a963c37029315bf4a07f80702c6cd28c45b652712590f7`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / result['path']).read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:181`; AST `5314e24053de2d5f38b19816681b159bd2b63197c274a4e52ab4d80b6ad34c22`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / result['path']).read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[7]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:182`; AST `7900b0a35d0a5804a012b92609dd2dc47a073b52cf9f004249923466b6285017`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[8]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:183`; AST `1bd73dcfcc217b788a7aa708966601bff62ce592b9607a251abe59402f473e83`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[8].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:183`; AST `b23dd929b98e5d6e80f750acb6316894b673f46fd55cf6971cff127064263dbe`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[9]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:184`; AST `d47d178b2850d1b6064fcf79cc5a7d72ce28c3462ca1364df4360ca0fe54c4bf`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: replacement.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[9].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:184`; AST `d6faceda91080fb7c074d74c258430cd00175eec9fb02a920627e0ea5a243616`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[10]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:185`; AST `73b71b68b74f163494e2477a288e30b51fa2ba12fbebcfffcb0b104b1408a683`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: replacement, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[11]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:186`; AST `6fb20970009419c036b1e51495c15a52053cf88502aee115ed68c5fd27fdf598`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, replacement, result, self. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[11].value::ListComp

Source: `infra/tests/test_roadmap_python_observations.py:186`; AST `7681bbdcb441178b714eaec28732b92338c4cef14916e04419111740a2ae29a2`.

Rust module: `infra::tests::test_roadmap_python_observations`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, replacement, result, self. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[12]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:187`; AST `b59f53d2bf8608391362d8a00a65dbb548905da27b4e7869b7a43e4763644d50`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[12].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:187`; AST `b0962e0c3abeb032d8659a565b52b69a92af2e063821ca5584ed414c6b34a3da`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[13]::With

Source: `infra/tests/test_roadmap_python_observations.py:188`; AST `3720f7c5ea982c6a15b74c2d00a574e5fe3d5882f91033caa6f9b8a69a78a444`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[12].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[13].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:188`; AST `64e594be5298690d7d04b053f4f3171a09b740eef29c2fe22656f4f46641260b`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[13].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[13].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:189`; AST `dc8293c98c71e543185527516db4c947b5e52b548e27587f960b95943685e718`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[12].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_missing_negative_control_and_forged_console_arguments_are_rejected::root.body[15].body[12].body[13].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:189`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[12].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:191`; AST `961bbba225aa77b807b553cee9e5df8be06caa38ff6ecff30909560c77012e1d`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: b, diagnostic, json, raw, replacement, result, self. Outputs/bindings: b, diagnostic, raw, replacement, result.
Calls/effect boundaries: (self.root / result['path']).read_text, json.loads, self.assertEqual, self.bind, self.persist, self.reports, self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:192`; AST `a86e7bad96d4eefcd002fb2c1067d231ffda00116a87862fcd7ab32c5da44e82`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[1]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:193`; AST `0c94776934f74480422fb68ed0edfbf1bc1f79de3d55ed5237f5217f39d56487`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, result, self. Outputs/bindings: raw.
Calls/effect boundaries: (self.root / result['path']).read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[1].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:193`; AST `94baf44ea5553b4702a963c37029315bf4a07f80702c6cd28c45b652712590f7`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / result['path']).read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_observations.py:193`; AST `5314e24053de2d5f38b19816681b159bd2b63197c274a4e52ab4d80b6ad34c22`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / result['path']).read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[2]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:194`; AST `84efb769e5cfa76c828d24ba92d717113acc327a26bed26b205daf2704a0bc2e`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[3]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:195`; AST `1bd73dcfcc217b788a7aa708966601bff62ce592b9607a251abe59402f473e83`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[3].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:195`; AST `b23dd929b98e5d6e80f750acb6316894b673f46fd55cf6971cff127064263dbe`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[4]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:196`; AST `d47d178b2850d1b6064fcf79cc5a7d72ce28c3462ca1364df4360ca0fe54c4bf`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: replacement.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[4].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:196`; AST `d6faceda91080fb7c074d74c258430cd00175eec9fb02a920627e0ea5a243616`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[5]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:197`; AST `73b71b68b74f163494e2477a288e30b51fa2ba12fbebcfffcb0b104b1408a683`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: replacement, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[6]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:198`; AST `6fb20970009419c036b1e51495c15a52053cf88502aee115ed68c5fd27fdf598`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, replacement, result, self. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[6].value::ListComp

Source: `infra/tests/test_roadmap_python_observations.py:198`; AST `7681bbdcb441178b714eaec28732b92338c4cef14916e04419111740a2ae29a2`.

Rust module: `infra::tests::test_roadmap_python_observations`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: b, replacement, result, self. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[7]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:199`; AST `b59f53d2bf8608391362d8a00a65dbb548905da27b4e7869b7a43e4763644d50`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[7].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:199`; AST `b0962e0c3abeb032d8659a565b52b69a92af2e063821ca5584ed414c6b34a3da`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.persist.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[8]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:200`; AST `d7cd11d1d57fa702a189e07bdb0dc17a37f3357d45f24ae2712381576a636b83`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: diagnostic.
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[8].value.value.value.value.value::Call

Source: `infra/tests/test_roadmap_python_observations.py:200`; AST `d085a723d7472af6de592b5efe03c8690757c40347ea3593f23569c1b2af080f`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.reports.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[8].value.value.value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[9]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:201`; AST `d6f7bd038c88f85c1cd3a6d31f1f99c8b5b8c1e7ad1021206c4490ff9798f483`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnostic, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[9].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:201`; AST `fb7c095359103e745dcf72b3a091201dd5bc4f05cd1c03c92ce4e35487daf5c5`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnostic, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[10]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:202`; AST `e462263daddca214e9005adcd3561dd59a790e62593260bde13de0b711a6694e`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnostic, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_diagnostic_outside_the_bound_closure_remains_unresolved::root.body[15].body[13].body[10].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:202`; AST `127c7dc25719ffcc2e554e3875172216c2d6b2dd30b60548e225ae7013494b8d`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnostic, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[13].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14]::FunctionDef

Source: `infra/tests/test_roadmap_python_observations.py:204`; AST `81d0e1a1a82487a2af0f7da309bb30b08cd81de0e49ce90e342886413379d255`.

Rust module: `infra::tests::test_roadmap_python_observations`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, adapter, after, before, compile_roadmaps, compiled, dependency, materialize, patch, self. Outputs/bindings: adapter, after, before, compiled, dependency.
Calls/effect boundaries: compile_roadmaps, materialize, patch, self.assertEqual, self.assertIn, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[0]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:205`; AST `3b1f096af51b088fc8db1bcf6f2df1bf3d578425197b6db1f15386d0b11cf950`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_observations.py:206`; AST `9522470acdd9432bb8a66c5f3ab64ab27f43c5e9d9cfed23e8413315fafcd375`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[2]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:207`; AST `3c07c0402fa43263ec82c91b4762405ec0038e65db08c76c82a45398d7e61ed1`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, compile_roadmaps. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[2].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:207`; AST `d1af4336e7af420cac99b4dd6cdf27c0ceea85cd6a7b14065da627f3fa88a4d7`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compile_roadmaps. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[3]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:208`; AST `152d76f4764c25e7d6347f68dda4e4f9d661376708c6280ec2438a28cad6bae5`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dependency.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4]::With

Source: `infra/tests/test_roadmap_python_observations.py:209`; AST `3a54799dc9448f1e034a20ccfc4741c781a50768f42310fcdf92b885cb783376`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ROOT, adapter, compiled, dependency, materialize, patch. Outputs/bindings: adapter, after, before.
Calls/effect boundaries: materialize, patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:209`; AST `bbb1b9b6d4f336f0b21a21f67813e261928092532a3073a94ab28f6a3467eb88`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:210`; AST `8a1670d5130c1f428bd0fabd5771e6a1faf7e512b9e2e4c74cb0b729c9a7917d`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:211`; AST `c3a5571317df0619f5fc1b096548722ecd06ee7b1380fbe4f69b5ed2961856fe`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:212`; AST `b257a05bb6a518286e1e04e095de68e76139f200f6f09dbbfed908fccdb7adba`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[14].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[1]::With

Source: `infra/tests/test_roadmap_python_observations.py:213`; AST `7feedf0d3802c95919e698c3fb2bf552ec4b3fb1afcfd5585433cc6a7cb83495`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ROOT, compiled, materialize, patch. Outputs/bindings: before.
Calls/effect boundaries: materialize, patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[14].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:213`; AST `db9b5ae47aa6af3348dab74806ca6c58e205b70face592b92208d6c153f540ba`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:214`; AST `2d96603b557c77b8be365023d423aaf0d8b87ac31339538eb1f200ceea426316`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, compiled, materialize. Outputs/bindings: before.
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[14].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:214`; AST `42b00045c2002d3615a5e976b25ff73f8378ea72a0840864e8abce8b36f5d031`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compiled, materialize. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[2]::With

Source: `infra/tests/test_roadmap_python_observations.py:215`; AST `fbb8e237d1b4d4dfadb26ee81ed586d9f971ad13858a61759b3eeffad428894c`.

Rust module: `infra::tests::test_roadmap_python_observations`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ROOT, compiled, dependency, materialize, patch. Outputs/bindings: after.
Calls/effect boundaries: materialize, patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[14].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_observations.py:215`; AST `4de78e38fb192150deb39f0d9cf8cc1f2d8b4abb6a363a40d11538e382ee0d80`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python_observations.py:216`; AST `37d105e907218fbdd000fbef43254e38ba1a1174aab2d1e0164889de3541d2c0`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, compiled, materialize. Outputs/bindings: after.
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[14].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[4].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:216`; AST `42b00045c2002d3615a5e976b25ff73f8378ea72a0840864e8abce8b36f5d031`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compiled, materialize. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[5]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:217`; AST `c9a9f862789180ff4bf1c09c458ba8e4da564ab61a66e4c6f1b3d6713ac79f0a`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[5].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:217`; AST `5a296ab5b62394a4bb03db76d70a9221a6ef73282b9a3c7a40b40c6a0eaafbf2`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[6]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:218`; AST `12d6c11bc79c662f217d25a678ab9b7693c116533822c45c46033e20a1f91f8e`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[6].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:218`; AST `0e0dff0746870b9a939ad36ca46a3d4bd1c9e408702624c4b08fee3ae334a407`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[7]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:219`; AST `73f2715c41192a36482e3b329d1b769a9c21eaa6ef7474a42c0943edf570edfa`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[7].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:219`; AST `1746a0b8eeee9d0a04eae529815d21683771d0d03e4300b00460bb5092d46301`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[8]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:220`; AST `202a7b85a78cf8fd3b66a448dde99ae8445568b106d07c3ca44411a83d54317d`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::QualificationObservationTests::test_new_backend_witness_changes_route_spec_without_changing_code_candidate::root.body[15].body[14].body[8].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:220`; AST `c596e85e2095c5f3498a2f7f3c3fc0bf85b220ee5baad7934dc48c21448b568c`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[14].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[16]::If

Source: `infra/tests/test_roadmap_python_observations.py:223`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_python_observations`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[16]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[16].body[0]::Expr

Source: `infra/tests/test_roadmap_python_observations.py:224`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_python_observations`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_observations.py::module::root.body[16].body[0].value::Call

Source: `infra/tests/test_roadmap_python_observations.py:224`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_python_observations`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, ast, copy, json, pathlib, shutil, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
