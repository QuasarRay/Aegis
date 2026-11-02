# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 194. Inventory digest: `4a2dbef27cedb5394f3da0ca1b08934b4f10a44f5fa2e79d17577279777a1c66`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_python_catalog.py::module::root::Module

Source: `infra/tests/test_roadmap_python_catalog.py:1`; AST `963dca52f9a755b647fd6ec33c39321d6c779f0ad0cfebb77aed8d0628a347b8`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, __file__, __name__, adapter, after, b, before, closures, compile_roadmaps, compiled, d, dependency, details, fields, first, fixture, fixture_catalog, fixtures, h, iter, key, len, locations, materialize, next, original_occurrences, package, patch, r, record, result, root, runtime_bindings, second, self, set, stale, tempfile, tests, unittest. Outputs/bindings: _, adapter, after, b, before, closures, compiled, d, dependency, details, fields, first, fixture, fixtures, h, key, locations, package, r, record, result, root, second, stale, tests.
Calls/effect boundaries: (package / '__init__.py').write_text, Path, Path(__file__).resolve, compile_roadmaps, first.values, fixture_catalog, fixtures.items, fixtures.values, iter, len, materialize, next, original_occurrences, package.mkdir, patch, result['fixtures'].values, runtime_bindings, second.values, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertRaises, self.catalog, self.helper.read_text, self.helper.read_text().replace, self.helper.write_text, self.test_source.read_text, self.test_source.read_text().replace, self.test_source.write_text, set, tempfile.TemporaryDirectory, tests.mkdir, unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:1`; AST `08da7fcdb2602b59fe4df6263671843a2cc0847b179164f7eb5e0c2386fcadce`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_python_catalog.py:4`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[3]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_python_catalog.py:6`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_python_catalog.py:7`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:8`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[7]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:10`; AST `b1d285d65d46501fd299eba46cb54c457fa080a1c255d9a071836191a103f85a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:11`; AST `c1565ab382ce2dce3702efe43985dcee7a62a1d9fe162b64acbea8ac7cc252c8`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:12`; AST `f03d490df75c7330951b5ce75380b297979b688b88c1f26364ab52e4c8a2c0af`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::root.body[10]::ClassDef

Source: `infra/tests/test_roadmap_python_catalog.py:15`; AST `1a8a3dfd4afb6f2d0a136ea72a0b258ed02c1f9a3bbb4e62ff91a735c81859be`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, __file__, adapter, after, b, before, closures, compile_roadmaps, compiled, d, dependency, details, fields, first, fixture, fixture_catalog, fixtures, h, iter, key, len, locations, materialize, next, original_occurrences, package, patch, r, record, result, root, runtime_bindings, second, self, set, stale, tempfile, tests, unittest. Outputs/bindings: _, adapter, after, b, before, closures, compiled, d, dependency, details, fields, first, fixture, fixtures, h, key, locations, package, r, record, result, root, second, stale, tests.
Calls/effect boundaries: (package / '__init__.py').write_text, Path, Path(__file__).resolve, compile_roadmaps, first.values, fixture_catalog, fixtures.items, fixtures.values, iter, len, materialize, next, original_occurrences, package.mkdir, patch, result['fixtures'].values, runtime_bindings, second.values, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertRaises, self.catalog, self.helper.read_text, self.helper.read_text().replace, self.helper.write_text, self.test_source.read_text, self.test_source.read_text().replace, self.test_source.write_text, set, tempfile.TemporaryDirectory, tests.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:16`; AST `c899ebb7f6fe21740e0dd032b0780eeb6b33a15afcf8ffdb24d465cd3aac6c4e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, package, self, tempfile, tests. Outputs/bindings: package, tests.
Calls/effect boundaries: (package / '__init__.py').write_text, Path, package.mkdir, self.addCleanup, self.helper.write_text, self.test_source.write_text, tempfile.TemporaryDirectory, tests.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:17`; AST `aed684f24ac276f0e7121e6cce3c97723895a3c83e7c086cf3aab5997bac5b9b`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:17`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:18`; AST `be0fdf37b1d8171d3fa8ad7bf50e5c62c9fac9c5be724abd5499be1f56cb798e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:18`; AST `5e2bcaf4be28e656ea35bbf68d353fc84ac3adb02be149a886951ba64dea2378`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:19`; AST `35e4ba0862c162c9d0fed7ea498cab22c824665f26b8232b425d3ac3b4e1407b`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:19`; AST `df6a72f8bc4f533242bba3097d5da8d512f1b7fda6700f75ad71f93e695b95a7`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:20`; AST `d19f212f43546fba6b42d034d8a2cf77eeba6cbd18832e493137623709545904`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: package.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:21`; AST `16c1609a6038ebab05ee904b1e4675bc7b9c8bc619b50c7b59cc4f16617dbf32`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: package. Outputs/bindings: (none).
Calls/effect boundaries: package.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:21`; AST `a21c17d614d31daed05d2370d606feb8e675f36a53ea5ba46be91c6e6d8d82d7`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: package. Outputs/bindings: (none).
Calls/effect boundaries: package.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:22`; AST `3f1c510e8b880c1cbb249ed5bb13b66733b1e3414572a06772d187df59d9fa01`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: package. Outputs/bindings: (none).
Calls/effect boundaries: (package / '__init__.py').write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:22`; AST `7a8c4791deeec57ce1b5139a59ca80fa3acea7cbf6b0a933b135713db8142252`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: package. Outputs/bindings: (none).
Calls/effect boundaries: (package / '__init__.py').write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:23`; AST `d183909e55c1e3ab6e3148789f6ec64ce665a2774af35caee26a8ad3d3ae10b4`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: package, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:24`; AST `6f55cdc25df1db0bdb4bc8b9e26a61bf90a104c0b6cffb6aa6317b6ee78f6532`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.helper.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:24`; AST `9a1be4decfa1fc96184123c761ea12f766ae1fe28893949f8123c0a83a6359e2`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.helper.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[8]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:25`; AST `4322b4b95c1459c006364a8ab662119b8bb12de24450dc01e7e3d8232fe6d308`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tests.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[9]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:26`; AST `f19f41026e2671a53a82f18e64d1997526519ef2044aefe7ca99b30bb553891f`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tests. Outputs/bindings: (none).
Calls/effect boundaries: tests.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:26`; AST `098d9f1ca7c8a5a190ef43abd50d85d06c1733b9c7fc0d37c64f42549218f127`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tests. Outputs/bindings: (none).
Calls/effect boundaries: tests.mkdir.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[10]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:27`; AST `30dc7e12f8a3fcaf40e06ed573264b7badec9fcd6ade403da0a7acf4df6f3e03`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tests. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[11]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:28`; AST `e3e0428aef4da881c709945db45e6324da861587c73bc0a825f303a7d8c4e34d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::setUp::root.body[10].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:28`; AST `f8057d5ad7cec1f2ed08474ad04d69aa5bc2b34c6ec7147a02bb14a22da744ae`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::catalog::root.body[10].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:42`; AST `c66f5dc169b9008c2e1905a5d5c09cf42a7ea2200dd711b78a1c53de659419b6`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: fixture_catalog, original_occurrences, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog, original_occurrences.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::catalog::root.body[10].body[1].body[0]::Return

Source: `infra/tests/test_roadmap_python_catalog.py:43`; AST `4a76ac673d6af25d3d3151b2bb133f2c9ebdc331bedf354b2069b0442e0d21b0`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture_catalog, original_occurrences, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog, original_occurrences.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::catalog::root.body[10].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:43`; AST `9e41706f13511c18e579ead190af7d940a89b724aed66e8936b517b9c871b9e0`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture_catalog, original_occurrences, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog, original_occurrences.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::catalog::root.body[10].body[1].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:43`; AST `e4a5c76f7b2ee78d1778491271717566e7e659d326dfdb86f2c99644d2ece970`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original_occurrences, self. Outputs/bindings: (none).
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:45`; AST `44db42ee8f47ab1278652dd5c80216a3a1a72b7638efe26afec5e51ce922c33d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: b, closures, d, fields, fixtures, h, iter, len, next, record, self. Outputs/bindings: b, closures, d, fields, fixtures, h, record.
Calls/effect boundaries: fixtures.values, iter, len, next, self.assertEqual, self.assertFalse, self.assertIn, self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:46`; AST `2506f25098478eed6ea712ef96235dfaf7eb867c4fb0c0c10cc2386728f9a5af`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: closures, fixtures.
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:46`; AST `b0ff26a2c038a12717c359c23bd8c7e7f3293a8fc8c751bfe4712371cc58fdbd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:47`; AST `0e8be048f8715efa44d765d3b3cfb87703436a73170ce7ad47a7a68764603152`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:47`; AST `1cd5514a1f8ea82fa4eaef0c0baa2f1653783324c538371bca4e93922b6ba33e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:47`; AST `c524d733761ac3122af108d27864d6accf63482320c089c271f3867aa44f58a7`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[2]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:48`; AST `c3fa99883599e6b0ef19a057f6135b39a4647d824dbe5681ca23ad46bb3afb3e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, iter, next. Outputs/bindings: record.
Calls/effect boundaries: fixtures.values, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:48`; AST `98587f8a3cdf2e0f1557ada8ee83a9d688ed025e69ba267b378b7119794fa7c5`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, iter, next. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.values, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:48`; AST `3fcede8226bef16fc4180a83d066488c601303390c1ef80e33eee97ecf7f04c5`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, iter. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.values, iter.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[2].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:48`; AST `caba4d8ec24166e40adbcbd59f98cfbc564f885d67308b690a3ac0ac2d781af9`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:49`; AST `13081e0143fe1fbccb1f27deaab25ae6c77c1a0bb446f092868beb2dfca89621`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: d, record, self. Outputs/bindings: d.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:49`; AST `c8b3a88efdd9ad9bfb94b2f29e02ee86b0c9c9cedd10f252c00be25e4b98145f`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d, record, self. Outputs/bindings: d.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[3].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_python_catalog.py:49`; AST `9000c71eb82ed1be8bbd1ac9f5a6ab41f7f37980d1d2a0f400b04fdfbbb62f4e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: d, record. Outputs/bindings: d.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[10].body[2].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[4]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:50`; AST `dc330b41ca2fb0115d943b81837227cba7bb590256854f66049877371b0eb7cf`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:50`; AST `b6cc2c8bd281715917982d6bd68f010c159e1f08f922edfce5a8e090dfcc1dba`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[5]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:51`; AST `17816ddd331aad2863f3c3686c8e1c654e589e2dd8efdab2a5e77fe3bdfb71e6`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: fields.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[6]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:52`; AST `bffcb177fd6f2e94946b9ca30a319699573d59d044a61e0b010f9f5a4f65c452`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[6].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:52`; AST `dc060ce57ef95b81e02033d067ba6159113a15b28db64d43ae425ade666c5030`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[7]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:53`; AST `c6ab5a0a4bce36a30fab9ac4228d2f8b6c93cb81d191d5d19b66641535f5bad8`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[7].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:53`; AST `b771ea2d0eff660c780d15981309219b5f4a6d1d4081c1368858088a6f32affe`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[8]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:54`; AST `e3c6feb5ceac7fa0ce805293bc71955636a04f159bfdaa4441c8ef3a48676529`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, h, self. Outputs/bindings: h.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[8].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:54`; AST `1c2f17d306e38d6ab5ce3f3951d2b7bd8f8517c00d02e94522a03a04c165e705`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, h, self. Outputs/bindings: h.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[8].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_python_catalog.py:54`; AST `1d49e685658b242929903f88ac8282fa6746fb3ac84ffcdef43a55e62c69f5cd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: fields, h. Outputs/bindings: h.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[10].body[2].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[9]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:55`; AST `273871807d00df1c07dde74e814e87af78a1564e80c31329537202bddb49fbd1`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[9].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:55`; AST `164903c8d7d34903ee62047cced43527ec7fcd4a313cc3ba16838b3b00da7dfe`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[10]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:56`; AST `34b0cc40d56c50b72c7532b7808d7ade81849f203c79d6b1f8ddc453663b6201`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[10].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:56`; AST `025ec2e295a7dad0baaabe3b059fed05549053bad8b04b0d62be353b6ba17637`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[10].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:56`; AST `87b580c65277dac31a657b5b9de2f94fa2fcbb3969f8678f3d5ca421f34825d1`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[11]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:57`; AST `3d513c9e25fc30535bf41913bf3e2c230605cb3ce021f90bc69759411545f02c`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[11].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:57`; AST `9cb7eaa8ae671ac7cf626bf314d6405bd6e605f8c547f88155c72e9e894bcc34`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[11].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:57`; AST `f395285c35c5b212915cd2a07285c75afc39cc7721c66114c16a0c80076557b4`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[12]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:58`; AST `67326a0de2ab3b9c8f43cdd2855a135940dc7597e5b4db12bab6f45d61481735`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[12].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:58`; AST `903ad5141868e8e33ee978a6a8f17b9ac795524e81b923eafbc480734c69e92c`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[12].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:58`; AST `4dc1e61f4b4e0ae81600a3881d827500a1838e1c9822d7f2f3b7723441751a33`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[13]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:59`; AST `adb42c87dd5555c49abfc34df7612ec5d9e413c4a69c772ae3a6bae5f64024a5`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[13].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:59`; AST `36d8a4b1545d13c972c2136d58b6abf58678feec9c3447374d0fb9702e3e2800`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[14]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:60`; AST `68d7fd50bd724caaee089c67076636e04b3f731a9860861497095d00c68a2f02`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, closures, record, self. Outputs/bindings: b.
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[14].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:60`; AST `1a3fe26bd15acde26cb92d1781a8fafa9b27615c461bc971e799c7163afd5e3b`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, closures, record, self. Outputs/bindings: b.
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[14].value.args[1]::SetComp

Source: `infra/tests/test_roadmap_python_catalog.py:60`; AST `faae7cc99b0c1365675c86b1695e1ca3ae5bf742b3545d50609ee2ceddb2c71d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, closures, record. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[10].body[2].body[14].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[15]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:61`; AST `89cf5439dce873be875e4b62e099beff3e03d0d81736c9bf9cf2ed4835c902f4`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound::root.body[10].body[2].body[15].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:61`; AST `c5aea6f34065179005c6ded53612872a0d058dcb9d83980ca588242cc5d09a04`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:63`; AST `f88e5b33749bbee3c30603b6696b9a72a932883bc853df9eaad627af970e598f`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: first, iter, next, second, self, set. Outputs/bindings: _, first, second.
Calls/effect boundaries: first.values, iter, next, second.values, self.assertEqual, self.assertNotEqual, self.catalog, self.helper.read_text, self.helper.read_text().replace, self.helper.write_text, set.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:64`; AST `9c920fd17f8932fce7e47b556d27d6410f2031be225e1c62052eddf62b41eba9`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: _, first.
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:64`; AST `b0ff26a2c038a12717c359c23bd8c7e7f3293a8fc8c751bfe4712371cc58fdbd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:65`; AST `5d60f09f1fd739e8233308833f043e2e347e28bd360186e16a7d220036b6f85e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.helper.read_text, self.helper.read_text().replace, self.helper.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:65`; AST `4269927fb723a728a9ddff6076bc490f395db94dbadaf3aab5c3452ad744d899`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.helper.read_text, self.helper.read_text().replace, self.helper.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:65`; AST `b361f4e7dec74fe8f59e0bbe7093d22fafdc7e9761f93dc99d3c04e501b45f74`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.helper.read_text, self.helper.read_text().replace.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[1].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:65`; AST `7bf790ec7797146c4bc85bb36f59a2e632c7336bd21f7e728f8b32fd9ec4bfee`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.helper.read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[2]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:66`; AST `045f34cfe9ef07b6f46a8d05fefd6bc2e45deb6b7b233e688dc6511f2c9ce6ab`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: _, second.
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:66`; AST `b0ff26a2c038a12717c359c23bd8c7e7f3293a8fc8c751bfe4712371cc58fdbd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[3]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:67`; AST `49e1a1394b3d4edae9118d410d8683e89ccbd9e3be6159848faa08957673e87a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, set.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:67`; AST `22add65e99db4d3a625901e966fb50810ab2fcdac44f2be94fa051dd68a491dd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, set.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:67`; AST `3f2aba6966958aca4a76dbf131b663c05bb5265b6fa1fbc95b85b90f3a2fcc31`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[3].value.args[1]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:67`; AST `549df7abcda6991c532220eac2fa48962535b02ed927b60a48f26ff7ef408427`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `40d41c8e3011c38c0f7a8cd7b9124f0e4abdc6ccdb7f05840acf2ec505f0dae2`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, iter, next, second, self. Outputs/bindings: (none).
Calls/effect boundaries: first.values, iter, next, second.values, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `033cf34890f5b89b9d65105873e8ff5870fbee1227272203c0255e55490a02e4`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, iter, next, second, self. Outputs/bindings: (none).
Calls/effect boundaries: first.values, iter, next, second.values, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `d1fffa2911bbf988f3bb83aebab9d83dcbc408575f741b040d6e8ca2a3090cbc`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, iter, next. Outputs/bindings: (none).
Calls/effect boundaries: first.values, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `0e3ef2ae056714ab32126fd3e48cbf22aca5c508121d77d8bdc2229398741d08`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, iter. Outputs/bindings: (none).
Calls/effect boundaries: first.values, iter.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value.args[0].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `4d752c29e24a1c6468a6ea3383103aec97d329cd5095c37d642e93f6ea2ddc86`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value.args[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value.args[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `ef4cd9900c77a8a5c8b04f77b7d800b91ca62797a8e6710522ae8d71bf7ec2af`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: iter, next, second. Outputs/bindings: (none).
Calls/effect boundaries: iter, next, second.values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value.args[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `c975bb3b7bdf4d7f3ef15d6bb981c47eaf0585208ba39ba3259e33ded8006201`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: iter, second. Outputs/bindings: (none).
Calls/effect boundaries: iter, second.values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value.args[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_unused_imported_helper_change_invalidates_full_fixture_semantics::root.body[10].body[3].body[4].value.args[1].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:68`; AST `114ff61b41bddec9333fa245554313a863c56f351129a753314c8ada16c8289c`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value.args[1].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:70`; AST `84d6ca0b00241699b9610fc7a864f69a8ae37efdc0d786f775c20ffcc73df77f`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: details, fixture, fixtures, iter, key, next, result, runtime_bindings, self, stale. Outputs/bindings: _, details, fixture, fixtures, key, result, stale.
Calls/effect boundaries: fixtures.items, iter, next, runtime_bindings, self.assertEqual, self.assertFalse, self.catalog, self.test_source.read_text, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:71`; AST `62f2ed6d2c87e6951cddd62530aaa271ed6145ba440b5da659643813942d7acd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: _, fixtures.
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:71`; AST `b0ff26a2c038a12717c359c23bd8c7e7f3293a8fc8c751bfe4712371cc58fdbd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:72`; AST `0a2b17c73448209b796a0fd3828ae96ea8f93c7ccd1788e92af8ad875b77f91d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, iter, next. Outputs/bindings: fixture, key.
Calls/effect boundaries: fixtures.items, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:72`; AST `2b6b1dd79a6c785ef5fd977ec678ea40722639180b6f2d6c8e6634e127a22241`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, iter, next. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.items, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:72`; AST `1d31baef58370f80b1023507364de25c3fede822e458975c75db03da404319c5`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, iter. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.items, iter.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[1].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:72`; AST `a99a41db1c567786c4d9b9d14e898919607e646cbed9c0b1a367e921aedb5951`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.items.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[2]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:73`; AST `9329468a101c70bfb00618a2da0cdeea12e3e2a988bf6ce78d5ae69a0aacebfa`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture. Outputs/bindings: details.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[3]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:75`; AST `e70f0780e8950c4263e5213b12a806b7d936d3f57827cf02dfe9423b341c3f0e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: details, fixtures, runtime_bindings, self. Outputs/bindings: result.
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:75`; AST `1303e259e27e95e1553c37155fc6d3d0d0317f797d41c76b58fd05d25092f3f8`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details, fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[4]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:76`; AST `6fda802fc0e0b6fb54de7a76647a34fc09f03b6ab7a3e667f9c2fa98bb23b254`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:76`; AST `b2db281bc75190a2a09c4e3e42c94f47ef93751887b900a6bde18780c43d95bb`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:77`; AST `a5e7006f65a9139f48b77d9bd3faf9eb202692337d3b1a52c54921ab60745221`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:77`; AST `6a7dae88bb28c9b39d59619751df8a2517f137de6f5ac2e6963cbe2c5aeadcf1`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[6]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:78`; AST `4ea2f19e16f798d26a00c45faff9c8027e6ce153aa03b721d9c09ca1be7dda61`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[6].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:78`; AST `c2f5ac952d8d17a87e7886d188428bf21e207673a35e24f97d62d26fe463d46e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[7]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:79`; AST `3eeaf65e90129919401f38945ffddf78974585ef18fce5b7682c8b7744c3226a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[7].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:79`; AST `a1704fae0751b1047fa0bb6a0a44e9dd68dd85e2abe60e39b35b56143241e358`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[7].value.args[0].left::Call

Source: `infra/tests/test_roadmap_python_catalog.py:79`; AST `ce693a811f430d9e8210b315becd3a005203efea5948b5aaa46431a02353e94a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[7].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[8]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:80`; AST `952e01d5c0c23ad448bbb5851db56789c1cbb0bc436a0a2a14ad682de862ad81`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: details, fixtures, runtime_bindings, self. Outputs/bindings: stale.
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[8].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:80`; AST `1303e259e27e95e1553c37155fc6d3d0d0317f797d41c76b58fd05d25092f3f8`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details, fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[9]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:81`; AST `a8484decf7d565f38810533b4cbc1ac722081784eb3070842280427b3fc9cf85`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_runtime_pass_is_only_a_finite_source_matched_observation::root.body[10].body[4].body[9].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:81`; AST `35b73f43b7cd60a81591339811e53c1cb3ae8a37e1e498f97396895c8de48bfc`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, self, stale. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:83`; AST `8b864c32e458ab5eb58491882cb2df28685bbcd146e88a95c9090f68d753834d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: fixture, fixtures, iter, len, next, r, result, runtime_bindings, self. Outputs/bindings: _, fixture, fixtures, r, result.
Calls/effect boundaries: fixtures.values, iter, len, next, result['fixtures'].values, runtime_bindings, self.assertEqual, self.catalog, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:84`; AST `112fedc214b3fc91997c6033e21cd3a8b645196bc4012eb8a9f5bcdee12edfe0`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:84`; AST `42d32aed05cfd34d6cb3159b2a6d966f3b941bd08c6c1b5ca0c4b37db296723f`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[1]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:85`; AST `62f2ed6d2c87e6951cddd62530aaa271ed6145ba440b5da659643813942d7acd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: _, fixtures.
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:85`; AST `b0ff26a2c038a12717c359c23bd8c7e7f3293a8fc8c751bfe4712371cc58fdbd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:86`; AST `4dd4494766cbe6d8be0ba69eff296ad9d616ec28c636247227dec76d680fd91e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:86`; AST `622a70c7ce3ae514f6275248459affe84b0392128de3f9d3471c3eef4673e78c`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:86`; AST `c524d733761ac3122af108d27864d6accf63482320c089c271f3867aa44f58a7`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[3]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:87`; AST `d2f29178f22461fb2d91e85ace1259be427e688258202a923f690b4e0bb62376`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, iter, next. Outputs/bindings: fixture.
Calls/effect boundaries: fixtures.values, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:87`; AST `98587f8a3cdf2e0f1557ada8ee83a9d688ed025e69ba267b378b7119794fa7c5`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, iter, next. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.values, iter, next.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:87`; AST `3fcede8226bef16fc4180a83d066488c601303390c1ef80e33eee97ecf7f04c5`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, iter. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.values, iter.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[3].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:87`; AST `caba4d8ec24166e40adbcbd59f98cfbc564f885d67308b690a3ac0ac2d781af9`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures. Outputs/bindings: (none).
Calls/effect boundaries: fixtures.values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[3].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[4]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:88`; AST `b138736ea9b1ccd20c3ec3f8b7d0e1a351a5abd0be1155a648bbafa1b11fea25`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, fixtures, runtime_bindings, self. Outputs/bindings: result.
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[4].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:88`; AST `18814b06ea392bc334045fbfe047c38c35c32cc58114f7c27cde3bec39e9db65`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[5]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:90`; AST `982fe6a3299d018644c16f06c5f4723c23516f7da2e6e918a6ae8b07c8e1b298`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, result, self. Outputs/bindings: r.
Calls/effect boundaries: result['fixtures'].values, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[5].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:90`; AST `8aa2d63a9d9fc384a12acefb4d4d99a73c5a2be7d2eca2d73fb5d446f73163e3`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, result, self. Outputs/bindings: r.
Calls/effect boundaries: result['fixtures'].values, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[5].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_python_catalog.py:90`; AST `12a226b9f7f32295a5b3e3d57ac05e7af5995dc31e64f4adf8ad655dbea058bf`.

Rust module: `infra::tests::test_roadmap_python_catalog`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, result. Outputs/bindings: r.
Calls/effect boundaries: result['fixtures'].values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[10].body[5].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_shadowed_fixture_name_cannot_collapse_two_source_occurrences::root.body[10].body[5].body[5].value.args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_python_catalog.py:90`; AST `fbbbac8d46bc75a226617f2cefa574e5b96a19584589ae2111c33f4fc793e100`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result['fixtures'].values.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[5].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:92`; AST `7f58379fd82e2a14eb0292f7207dbec20aba477877ccc7c39f85457fe22d86f2`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, fixtures, result, runtime_bindings, self. Outputs/bindings: _, fixtures, result.
Calls/effect boundaries: runtime_bindings, self.assertEqual, self.assertRaises, self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:93`; AST `62f2ed6d2c87e6951cddd62530aaa271ed6145ba440b5da659643813942d7acd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: _, fixtures.
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:93`; AST `b0ff26a2c038a12717c359c23bd8c7e7f3293a8fc8c751bfe4712371cc58fdbd`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[1]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:94`; AST `21d8cc07d92e7a8312e2cd524ec4c1da61a6d32ca92befaf0f25c6a32cc27214`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, runtime_bindings, self. Outputs/bindings: result.
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:94`; AST `47c952d3d8409252422170c0ebc096ba64a547903ece3c4f9669712109d49e69`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:95`; AST `803fe60662c95cdb7bcca10fab1354b7608c75ec5b96e9dca3970e59f8ef65ef`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:95`; AST `64a01a6020cd870019171d91871d3897b5dd1f7cfa315bcb8201fb7182acaaee`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[3]::With

Source: `infra/tests/test_roadmap_python_catalog.py:96`; AST `05440d8258ba7f9ab1bc8045f050fbd0a8dbca81aa24f819f6ada92f68078df2`.

Rust module: `infra::tests::test_roadmap_python_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_catalog.py:96`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:97`; AST `242b2a7887fee6ac9b6969d7436075a7e9896cb4dcf9981ad6bd90d3931bae23`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded::root.body[10].body[6].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:97`; AST `c392d0c33cd3a0bf6d387872e4e950e3b45b1493ad74cc1dee5aba14b64f8a03`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixtures, runtime_bindings, self. Outputs/bindings: (none).
Calls/effect boundaries: runtime_bindings.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:99`; AST `99f5fce5fed53b703f643b90fa762e2d7ff3d2bb74ad89bb5e9fa058e0b5f876`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, fixture_catalog, locations, original_occurrences, self. Outputs/bindings: locations.
Calls/effect boundaries: fixture_catalog, original_occurrences, self.assertRaises, self.test_source.read_text, self.test_source.read_text().replace, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:100`; AST `6345a39227530ca87dada3ec3f7ef88700ec6dc5ee402418e03c17bfb85f2786`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original_occurrences, self. Outputs/bindings: locations.
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:100`; AST `e4a5c76f7b2ee78d1778491271717566e7e659d326dfdb86f2c99644d2ece970`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original_occurrences, self. Outputs/bindings: (none).
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:101`; AST `57ff2deeac2e220955c103d3fed89fd0dab9abb028497854657213aa846ad249`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text, self.test_source.read_text().replace, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:101`; AST `befaf4512ac662541fdc99ac03b14a72aa63d6d056950bcfff0cd7825718b6b6`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text, self.test_source.read_text().replace, self.test_source.write_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_catalog.py:101`; AST `5dbef0c0873b4ce71521cd631ed26d0dd85e28498df34a80422e49db90360550`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text, self.test_source.read_text().replace.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[1].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:101`; AST `ce693a811f430d9e8210b315becd3a005203efea5948b5aaa46431a02353e94a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.test_source.read_text.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[1].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[2]::With

Source: `infra/tests/test_roadmap_python_catalog.py:102`; AST `c9f5c46421238de915001aeaef01666b97373e6903395ba5f3e82590648b406b`.

Rust module: `infra::tests::test_roadmap_python_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, fixture_catalog, locations, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_catalog.py:102`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:103`; AST `1ce0455e2e4e58b1be0020a2422dc12ed44a3bb3bc08a11016bc2da4d7a055c7`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture_catalog, locations, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_changed_original_method_body_cannot_reuse_a_static_location::root.body[10].body[7].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:103`; AST `b38c18c8889767f2c5c22bf5375a5e96e7322f5945a3086a5e1f3141fc7844b1`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture_catalog, locations, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture_catalog.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_python_catalog.py:105`; AST `d1bf56779fb682b9858988f3ce9aefd1ea9c06c0a0bdfd9787f4ce5c8f705645`.

Rust module: `infra::tests::test_roadmap_python_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, __file__, adapter, after, before, compile_roadmaps, compiled, dependency, materialize, patch, root, self. Outputs/bindings: adapter, after, before, compiled, dependency, root.
Calls/effect boundaries: Path, Path(__file__).resolve, compile_roadmaps, materialize, patch, self.assertEqual, self.assertIn, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[0]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:106`; AST `3b1f096af51b088fc8db1bcf6f2df1bf3d578425197b6db1f15386d0b11cf950`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_catalog.py:107`; AST `9522470acdd9432bb8a66c5f3ab64ab27f43c5e9d9cfed23e8413315fafcd375`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[2]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:108`; AST `102a72c5f3942e83b9aacee69bcfb09ce3245f1d4d9767548da37bf9e4c027ac`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: root.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[2].value.value.value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:108`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[2].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[2].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:108`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[2].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[3]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:109`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[3].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:109`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[4]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:110`; AST `d6febbe01de434eb6e32656763baf710b21b8b8d79446e0f87e92607d1f2a278`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dependency.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5]::With

Source: `infra/tests/test_roadmap_python_catalog.py:111`; AST `30b1ddcada5e5f61ac2887446b7725d512545ea0b716ab6afec06e4d6ec6d957`.

Rust module: `infra::tests::test_roadmap_python_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: adapter, compiled, dependency, materialize, patch, root. Outputs/bindings: adapter, after, before.
Calls/effect boundaries: materialize, patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_catalog.py:111`; AST `bbb1b9b6d4f336f0b21a21f67813e261928092532a3073a94ab28f6a3467eb88`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_python_catalog.py:111`; AST `8a1670d5130c1f428bd0fabd5771e6a1faf7e512b9e2e4c74cb0b729c9a7917d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:112`; AST `d29e97dc6b7e31fa281768d897025d5896e7b25765f6fd382387c600d78c99b7`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[1]::With

Source: `infra/tests/test_roadmap_python_catalog.py:113`; AST `ee738b45c95510f73ca50e1cb5610677af605af9316a40216d3117c6b6c7ab72`.

Rust module: `infra::tests::test_roadmap_python_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: compiled, materialize, patch, root. Outputs/bindings: before.
Calls/effect boundaries: materialize, patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[8].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_catalog.py:113`; AST `c3a5571317df0619f5fc1b096548722ecd06ee7b1380fbe4f69b5ed2961856fe`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:114`; AST `012c342466d6fabeecc54a0234545c989d2474d171bd5412494a6d304a48b406`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, materialize, root. Outputs/bindings: before.
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:114`; AST `c8cc254a29092adc8d482f3de3cbf13b41d08c45dac73043ee576a3e0dd532ae`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, materialize, root. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[2]::With

Source: `infra/tests/test_roadmap_python_catalog.py:115`; AST `100ec6e48185e863cfd13d8b034bccd2ee693441257cedd56f1804871ad6c062`.

Rust module: `infra::tests::test_roadmap_python_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: compiled, dependency, materialize, patch, root. Outputs/bindings: after.
Calls/effect boundaries: materialize, patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[8].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_catalog.py:115`; AST `0c254220d4d1d0deb4d26a23055f08e6f4ee29cb21dcc1a0b5f07a1c82f46a7a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python_catalog.py:116`; AST `fee9b65901b7dcbffe47cb39c0401099fd28a220cd73978b3aeab390c88bbf06`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, materialize, root. Outputs/bindings: after.
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:116`; AST `c8cc254a29092adc8d482f3de3cbf13b41d08c45dac73043ee576a3e0dd532ae`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, materialize, root. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[6]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:117`; AST `c9a9f862789180ff4bf1c09c458ba8e4da564ab61a66e4c6f1b3d6713ac79f0a`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[6].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:117`; AST `5a296ab5b62394a4bb03db76d70a9221a6ef73282b9a3c7a40b40c6a0eaafbf2`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[7]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:118`; AST `12d6c11bc79c662f217d25a678ab9b7693c116533822c45c46033e20a1f91f8e`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[7].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:118`; AST `0e0dff0746870b9a939ad36ca46a3d4bd1c9e408702624c4b08fee3ae334a407`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[8]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:119`; AST `202a7b85a78cf8fd3b66a448dde99ae8445568b106d07c3ca44411a83d54317d`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[8].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:119`; AST `c596e85e2095c5f3498a2f7f3c3fc0bf85b220ee5baad7934dc48c21448b568c`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[9]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:120`; AST `651e09599797bf2f6da19d2bcf83fadbd28d2d82756dfebcf9cdcb90556e36b1`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::OriginalFixtureCatalogTests::test_new_runtime_witness_changes_route_spec_without_changing_code_candidate::root.body[10].body[8].body[9].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:120`; AST `89822c0b610ad2a407074c7ba4cd2b88ba3e015db40a7735da3ca4723b03115f`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[11]::If

Source: `infra/tests/test_roadmap_python_catalog.py:123`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_python_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[11]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[11].body[0]::Expr

Source: `infra/tests/test_roadmap_python_catalog.py:124`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_python_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_catalog.py::module::root.body[11].body[0].value::Call

Source: `infra/tests/test_roadmap_python_catalog.py:124`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_python_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap, agentinfra.roadmap_python, agentinfra.roadmap_python_catalog, agentinfra.roadmap_records, agentinfra.roadmap_work, json, pathlib, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
