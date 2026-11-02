# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 137. Inventory digest: `30e8920424afdaf92c42478b8e2c1c75d6bab79c69dc1d0782597c4349f3d533`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_catalog.py::module::root::Module

Source: `infra/tests/test_catalog.py:1`; AST `c94796eb627df88682d0142e33a8fb818cb81a72fd173f0256f383cd804bc159`.

Rust module: `infra::tests::test_catalog`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, ValueError, __file__, __name__, actual, ambiguous, candidates_for, cpp_case, done, expected, first, inventory, len, marked, path, python_case, qualify, r, read, required, root, row, rows, s, second, self, sources, str, sys, temp, tempfile, text, unittest, value. Outputs/bindings: actual, ambiguous, done, expected, first, marked, path, r, read, required, root, row, rows, s, second, sources, temp, text, value.
Calls/effect boundaries: '\n'.join, Path, Path(__file__).resolve, candidates_for, cpp_case, inventory, len, path.parent.mkdir, path.write_text, python_case, qualify, self.assertEqual, self.assertIn, self.assertNotIn, self.assertRaisesRegex, str, sys.path.insert, tempfile.TemporaryDirectory, unittest.main.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[0]::Expr

Source: `infra/tests/test_catalog.py:1`; AST `8dffe37954b77777afbef6e4d3d9f1ca4c49dc7320a37540f6045d91d7786f64`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_catalog.py:2`; AST `b7d6bcdca8b664f6f9b11b53c3698446d9319e67139aff16db27b97fbdc0b6da`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_catalog.py:3`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[3]::Import

Source: `infra/tests/test_catalog.py:4`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[4]::Import

Source: `infra/tests/test_catalog.py:5`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[5]::Import

Source: `infra/tests/test_catalog.py:6`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[6]::Expr

Source: `infra/tests/test_catalog.py:8`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[6].value::Call

Source: `infra/tests/test_catalog.py:8`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[6].value.args[1]::Call

Source: `infra/tests/test_catalog.py:8`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[6].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_catalog.py:8`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[6].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_catalog.py:8`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[7]::ImportFrom

Source: `infra/tests/test_catalog.py:9`; AST `807629fc938e6cfa82011fbfd4ffe64406151ad0ee2485149159868dd87d72cc`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::root.body[8]::ClassDef

Source: `infra/tests/test_catalog.py:12`; AST `8d0d6cd49e8620a89408f7f1c4abb920b55371837a3b894d6e534065ee5a359b`.

Rust module: `infra::tests::test_catalog`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, ValueError, actual, ambiguous, candidates_for, cpp_case, done, expected, first, inventory, len, marked, path, python_case, qualify, r, read, required, root, row, rows, s, second, self, sources, temp, tempfile, text, unittest, value. Outputs/bindings: actual, ambiguous, done, expected, first, marked, path, r, read, required, root, row, rows, s, second, sources, temp, text, value.
Calls/effect boundaries: '\n'.join, Path, candidates_for, cpp_case, inventory, len, path.parent.mkdir, path.write_text, python_case, qualify, self.assertEqual, self.assertIn, self.assertNotIn, self.assertRaisesRegex, tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0]::FunctionDef

Source: `infra/tests/test_catalog.py:13`; AST `27b323e8da192234578d483dd7bbff98345c1d27d35917c5c16fbe23b8ef9b3e`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: python_case, required, row, s, self, sources, text, value. Outputs/bindings: required, row, s, sources, text, value.
Calls/effect boundaries: '\n'.join, python_case, self.assertEqual, self.assertIn, self.assertNotIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[0]::Assign

Source: `infra/tests/test_catalog.py:14`; AST `0665485deb897d2b5bde1225b3457f50b9400e3832b75357620cc65cc678ba02`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: sources.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[1]::Assign

Source: `infra/tests/test_catalog.py:16`; AST `9333233598dd36392ad374009ed901ae1d47503e974ffb9db2f759856f2f85bf`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: python_case, sources. Outputs/bindings: value.
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[1].value::Call

Source: `infra/tests/test_catalog.py:16`; AST `437d69e311023b7772079d2abc4a766c9bf3ff97cb79a1b42481cde8f81ea395`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python_case, sources. Outputs/bindings: (none).
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[2]::Assign

Source: `infra/tests/test_catalog.py:17`; AST `a9dcaeb423871e6847464b6fa51cccc2026cb863095c49942316371d5b0b584f`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: s, value. Outputs/bindings: s, text.
Calls/effect boundaries: '\n'.join.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[2].value::Call

Source: `infra/tests/test_catalog.py:17`; AST `d395d59ded764667a3ad2732d9bdb4d4b5992325d221202535273e5072c7f2d8`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s, value. Outputs/bindings: s.
Calls/effect boundaries: '\n'.join.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[2].value.args[0]::GeneratorExp

Source: `infra/tests/test_catalog.py:17`; AST `d6223d8a6d0915cbf82f20917708bb9d108918f7ad0f01d0436437ca18d92d69`.

Rust module: `infra::tests::test_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: s, value. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[0].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[3]::Expr

Source: `infra/tests/test_catalog.py:18`; AST `5eca612967c871b2b47968d1605e1dddc02a4ec8eadd7dee27c003e98a3a5c27`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[3].value::Call

Source: `infra/tests/test_catalog.py:18`; AST `6741ae00c3ec9d1ec88e4a735b972eac4cc5981f0723574aca343a40ddf6bedb`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[4]::For

Source: `infra/tests/test_catalog.py:19`; AST `8cc4906dff39e7636acc7f4c04f3422051eece08ea985f73dd9ec5116c22c610`.

Rust module: `infra::tests::test_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: required, self, text. Outputs/bindings: required.
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[8].body[0].body[4]; no call, error or mutation may be omitted. Iteration: required in ('super(Selected,self).setUp()', 'self.park=7', 'def check_setup', 'def tearDown', 'self.assertEqual(self.park,7)')
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[4].body[0]::Expr

Source: `infra/tests/test_catalog.py:20`; AST `3b9c61dba765bf01819204ee1252e0218e5f361a59da5141915682138feb5fde`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: required, self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_catalog.py:20`; AST `897185c4a2a95e43f9b7a2263b3f4b6e62e0ee3709bdd051e91a49fa4cebdf26`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: required, self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[5]::Expr

Source: `infra/tests/test_catalog.py:21`; AST `bec5a58922521c77f65cdd4b01f4e41017598953fcc982110fe635e88c2cd51e`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[5].value::Call

Source: `infra/tests/test_catalog.py:21`; AST `bb29cb036d41d9c00ef62cc4a92923ba34b9eeddff410227d66e1cee1e07e70e`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[6]::Expr

Source: `infra/tests/test_catalog.py:22`; AST `b856a57f93e227d0f5433e6cfc3df16b7f7e76fc57ce8ac4ac07e6d5e46ea4e3`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, self, value. Outputs/bindings: row.
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[6].value::Call

Source: `infra/tests/test_catalog.py:22`; AST `eb9bb18ee2164b0fe7d5b0312f13031cca47dbf41ede16a07694bc97ac826676`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row, self, value. Outputs/bindings: row.
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_super_fixture_reference_does_not_copy_unrelated_cases::root.body[8].body[0].body[6].value.args[0]::ListComp

Source: `infra/tests/test_catalog.py:22`; AST `d05087bf26a1cb3de261dcb7cff8826a941d2a0d5b683bafd9893133359822a6`.

Rust module: `infra::tests::test_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: row, value. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[8].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1]::FunctionDef

Source: `infra/tests/test_catalog.py:24`; AST `47dae3d47df2730fab744407429e01bc27c52bfa3f6ef907be7ac7e5ff20ec47`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: expected, python_case, r, s, self, sources, text, value. Outputs/bindings: expected, r, s, sources, text, value.
Calls/effect boundaries: '\n'.join, python_case, self.assertEqual, self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[0]::Assign

Source: `infra/tests/test_catalog.py:25`; AST `07215570a8a327f869b4ffe252ceb6d166a029b78bc11fbb82439cfae42a655e`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: sources.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[1]::Assign

Source: `infra/tests/test_catalog.py:29`; AST `6ec732cf338baad0238389685f3530de8fb0e1511b132a579d1682d855d64fdf`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: python_case, sources. Outputs/bindings: value.
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[1].value::Call

Source: `infra/tests/test_catalog.py:29`; AST `6041750ceaeb94937e6fa15bb2662c2f96f71c5f1d20be31a153c1d25d21267d`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python_case, sources. Outputs/bindings: (none).
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[2]::Expr

Source: `infra/tests/test_catalog.py:30`; AST `76a898377b24a8fa276483d8203974859550bf9c32e25745816c1187c16a1cea`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[2].value::Call

Source: `infra/tests/test_catalog.py:30`; AST `e3deac4be6a0ce63f05c0dd1f9cda261b1f7aa71e448613a610205410abde2f9`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[3]::Assign

Source: `infra/tests/test_catalog.py:31`; AST `a9dcaeb423871e6847464b6fa51cccc2026cb863095c49942316371d5b0b584f`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: s, value. Outputs/bindings: s, text.
Calls/effect boundaries: '\n'.join.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[3].value::Call

Source: `infra/tests/test_catalog.py:31`; AST `d395d59ded764667a3ad2732d9bdb4d4b5992325d221202535273e5072c7f2d8`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s, value. Outputs/bindings: s.
Calls/effect boundaries: '\n'.join.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[3].value.args[0]::GeneratorExp

Source: `infra/tests/test_catalog.py:31`; AST `d6223d8a6d0915cbf82f20917708bb9d108918f7ad0f01d0436437ca18d92d69`.

Rust module: `infra::tests::test_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: s, value. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[1].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[4]::For

Source: `infra/tests/test_catalog.py:32`; AST `6c988435e7d04b9501896c3a2d166c23eb9402e4738f64e17fd01dff6ab4bf49`.

Rust module: `infra::tests::test_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: expected, self, text. Outputs/bindings: expected.
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[8].body[1].body[4]; no call, error or mutation may be omitted. Iteration: expected in ('def setUp', 'def tearDown', 'DEFAULT = 7', 'SLOT = 2', 'def make', 'self.assertEqual')
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[4].body[0]::Expr

Source: `infra/tests/test_catalog.py:33`; AST `fe3f405dd424c338db0141ac12da6c84771647c752336d3ab865c24d10b7f3a6`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[4].body[0].value::Call

Source: `infra/tests/test_catalog.py:33`; AST `4d8b20e9e181e2f7783f2f4b2942e203378a86e7b8f22fe62fcc9b7643027182`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[5]::Expr

Source: `infra/tests/test_catalog.py:34`; AST `f1703bc7f83fa2ec595462eca5277f6ff3bc7bc5e689d2a97a5a37f2a261bbc4`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, self, value. Outputs/bindings: r.
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[5].value::Call

Source: `infra/tests/test_catalog.py:34`; AST `2d3f9a340dca31f91f397a8db6d0e45063e34be75e95ea1fb4b2018bb21cc474`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, self, value. Outputs/bindings: r.
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[5].value.args[0]::ListComp

Source: `infra/tests/test_catalog.py:34`; AST `36256287ae1d226fbf6e2ba3875ed25d2cb4d2d0c1b985d785f864eed72b88f8`.

Rust module: `infra::tests::test_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, value. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[8].body[1].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[6]::Expr

Source: `infra/tests/test_catalog.py:35`; AST `14329c42329d3620dc1c3012b0688cbeb7c9dcb8a4186d1c680110db65a167d5`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_fixture_and_transitive_setup_are_extracted_from_source::root.body[8].body[1].body[6].value::Call

Source: `infra/tests/test_catalog.py:35`; AST `0b40a8edfff25ba744b3395984a7e27cb65ff22420c406152ef7ccf8481b37d7`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2]::FunctionDef

Source: `infra/tests/test_catalog.py:37`; AST `8412c873692f455b07ee8440b34344941f5fc5ca8361cbf2603a44b52cc298d7`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: done, first, python_case, read, second, self, text. Outputs/bindings: done, first, read, second, text.
Calls/effect boundaries: python_case, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[0]::Assign

Source: `infra/tests/test_catalog.py:38`; AST `f9a0128ef367101c0d22a0c0f645e97be67c9ac0aad4e1730b827148bd757b10`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: text.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[1]::Assign

Source: `infra/tests/test_catalog.py:39`; AST `a10d6a6d30049d8731cf887ac38758304be3a44c454df26993113296e1140963`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: text. Outputs/bindings: read.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[1].value::Lambda

Source: `infra/tests/test_catalog.py:39`; AST `39dfe9cacf4bffc0abfe597ce9710f9451753edf089bb6a30a4efb127a5e0eb8`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[2]::Assign

Source: `infra/tests/test_catalog.py:40`; AST `d286f692713adfe976a1233848101e4271b35004b8c65c8ef8d7164c6cc38ba3`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: python_case, read. Outputs/bindings: first.
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[2].value::Call

Source: `infra/tests/test_catalog.py:40`; AST `0eecd00abba3db2413c108b36634b2807e790c6af6d8bf157abb5f213281594f`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python_case, read. Outputs/bindings: (none).
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[3]::Assign

Source: `infra/tests/test_catalog.py:41`; AST `6c2e4b0dc731b412c4211e365790721ef666164d12f0478c0c2ba8b4e750a644`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: python_case, read. Outputs/bindings: second.
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[3].value::Call

Source: `infra/tests/test_catalog.py:41`; AST `6bd767f303772f5e821b6ca33538894b9d5d53c5f1b8481212c04373f6821bb2`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python_case, read. Outputs/bindings: (none).
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[4]::Expr

Source: `infra/tests/test_catalog.py:42`; AST `38462d33ab46369d10b2f695352f777fd69dcdb024fb811ff58f4b583371628b`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[4].value::Call

Source: `infra/tests/test_catalog.py:42`; AST `6f37fc3ba06b1c9a91daba29019540fe739738a27e654047238f4a613739efc2`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[5]::Expr

Source: `infra/tests/test_catalog.py:43`; AST `d36c8a0368062bfbc1e8e244d18b7e53c3741e01ce7284657acd82c7817ec90d`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[5].value::Call

Source: `infra/tests/test_catalog.py:43`; AST `c500bbfa99b4b8c5b882eb5461ebc27fab92aed99070b165c826ceb967536204`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[6]::Assign

Source: `infra/tests/test_catalog.py:44`; AST `d1eb568daa168d9a6c0e77ddd3d1698a464bc01d760553286c5c806330b952a5`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: python_case, read. Outputs/bindings: done.
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[6].value::Call

Source: `infra/tests/test_catalog.py:44`; AST `75e3d32158cb47edbefc8f3e3bc8b71fab9565e0d3490a918bde9f3662731a85`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python_case, read. Outputs/bindings: (none).
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[7]::Expr

Source: `infra/tests/test_catalog.py:45`; AST `443790b4e99dc68486d823869ec4b421ac25fdc56fa3aa56790c1f469f89f32d`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: done, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_duplicate_names_select_each_original_fixture_automatically::root.body[8].body[2].body[7].value::Call

Source: `infra/tests/test_catalog.py:45`; AST `af29c7457d8c3b2d2d20fc78cb833b6fc9c596080a04dc96f25721fbef8af58d`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: done, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3]::FunctionDef

Source: `infra/tests/test_catalog.py:47`; AST `a8601834edaa1d70c55fa8a518793a56f688992196332730e8c65ca840af1174`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ValueError, actual, ambiguous, candidates_for, inventory, len, marked, path, qualify, r, root, row, rows, self, temp, tempfile. Outputs/bindings: actual, ambiguous, marked, path, r, root, row, rows, temp.
Calls/effect boundaries: Path, candidates_for, inventory, len, path.parent.mkdir, path.write_text, qualify, self.assertEqual, self.assertRaisesRegex, tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0]::With

Source: `infra/tests/test_catalog.py:48`; AST `cd37aa0e84f7a84590d4e0308b21e54d64369cccd0a1c7d8e5303390b6d5fde3`.

Rust module: `infra::tests::test_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, ValueError, actual, ambiguous, candidates_for, inventory, len, marked, path, qualify, r, root, row, rows, self, temp, tempfile. Outputs/bindings: actual, ambiguous, marked, path, r, root, row, rows, temp.
Calls/effect boundaries: Path, candidates_for, inventory, len, path.parent.mkdir, path.write_text, qualify, self.assertEqual, self.assertRaisesRegex, tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[8].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_catalog.py:48`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[0]::Assign

Source: `infra/tests/test_catalog.py:49`; AST `1861de60e4ce9c8751686215af7f71a552c7711618c9ec883a80fb2a7735b59d`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, temp. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_catalog.py:49`; AST `4cfcc954aba7bc6bf35683d91e1dda5030b914a56a74caadfdfab2fe3bef9272`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, temp. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[1]::Assign

Source: `infra/tests/test_catalog.py:50`; AST `dce4899630f8a9a7bd0af16a69131e39afe092c803531354385bfa474be3dc21`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[2]::Expr

Source: `infra/tests/test_catalog.py:51`; AST `4a02dacfcdc4bdb0f5e882cce3190753b897fe61bcc8e2b13d0ac08a1dbc7824`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[2].value::Call

Source: `infra/tests/test_catalog.py:51`; AST `994840cf9a86a7ba49bb09b92b22661abceaeff09aca1fbcfc473e1e6303e386`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[3]::Expr

Source: `infra/tests/test_catalog.py:52`; AST `7c0a7c97d9f1ec6fae1c5af992a6e9b333fea46745a664321ea32fb4bb6bc748`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[3].value::Call

Source: `infra/tests/test_catalog.py:52`; AST `eb94607aa26b92de91f647f9846ebf3d232a7347b4d5c7a80f77515d84181227`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[4]::Expr

Source: `infra/tests/test_catalog.py:53`; AST `4405e16cd703b1ff47f9b84c6cf719390ecc00ebbe378197b621d79852345c7e`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, root, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[4].value::Call

Source: `infra/tests/test_catalog.py:53`; AST `a4518145a130002cd9ae4448b1fa529ec685b7cdf421ed1fa62c5e3ffd478d76`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[4].value.args[0].value::Call

Source: `infra/tests/test_catalog.py:53`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[5]::Assign

Source: `infra/tests/test_catalog.py:54`; AST `8c1b076c907b2f5ff857ed451429f199343847a7def5126319496f9250ca1c6d`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, qualify, root. Outputs/bindings: rows.
Calls/effect boundaries: inventory, qualify.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[5].value::Call

Source: `infra/tests/test_catalog.py:54`; AST `dc28ea77d46bef8cc81eb7925673eaf82457e244f0226ed030cd18698d4d001c`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, qualify, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory, qualify.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[5].value.args[0]::Call

Source: `infra/tests/test_catalog.py:54`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[5].value.args[1]::Lambda

Source: `infra/tests/test_catalog.py:54`; AST `9e48dc809257a36e54b235ec401af314c49052cb1b263b33657bdd55c3beb748`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[3].body[0].body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[6]::Expr

Source: `infra/tests/test_catalog.py:55`; AST `57ed242163fd5a36e06036aebc816bfd338fbb6857f448ede75bc9d6087364bf`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, rows, self. Outputs/bindings: r.
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[6].value::Call

Source: `infra/tests/test_catalog.py:55`; AST `35c72fa8f6678afeb195ee29b5e63472ddf3b5bb7b66c81199a0787437c1a01c`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, rows, self. Outputs/bindings: r.
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[6].value.args[0]::ListComp

Source: `infra/tests/test_catalog.py:55`; AST `355ca8328c0c25b9c6911d64ade5bdfb188379bf88e2f3747374fbbc60088e58`.

Rust module: `infra::tests::test_catalog`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[8].body[3].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[7]::Assign

Source: `infra/tests/test_catalog.py:56`; AST `fe1a3a98eaa08e7078c64b6c1bc9272907fc28e6da6684bace4292662e1be9b4`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: marked.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8]::For

Source: `infra/tests/test_catalog.py:57`; AST `e477cef8ae7c5cf2b6f3e3c4c62f643f1ee3676ac1e1d4b4f24183ce88e57151`.

Rust module: `infra::tests::test_catalog`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: actual, ambiguous, candidates_for, len, marked, row, rows, self. Outputs/bindings: actual, ambiguous, row.
Calls/effect boundaries: candidates_for, len, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[8].body[3].body[0].body[8]; no call, error or mutation may be omitted. Iteration: row in rows
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[0]::Assign

Source: `infra/tests/test_catalog.py:58`; AST `8381ed8378421276334c4ec101af7354e4e561266c5888fcc511a1e6c2863d57`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidates_for, marked, row. Outputs/bindings: actual, ambiguous.
Calls/effect boundaries: candidates_for.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3].body[0].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[0].value::Call

Source: `infra/tests/test_catalog.py:58`; AST `4521ea5cea2983fa81d8fda7e08012dc237f1917fe850f1da0b80a7d3b868da5`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidates_for, marked, row. Outputs/bindings: (none).
Calls/effect boundaries: candidates_for.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[1]::Expr

Source: `infra/tests/test_catalog.py:59`; AST `ab6e95f0f68b7fbd97426b93db77b15a753278233b9209a5af3efd46adce4460`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[1].value::Call

Source: `infra/tests/test_catalog.py:59`; AST `6eca5ad23551af6bc0c8144eae4935402ff8067ab853bd95a66c39c6dc6c34c7`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[2]::Expr

Source: `infra/tests/test_catalog.py:60`; AST `f33668ca8930fc61269663cca9bddb7e588090980740632fc980d734ae1afe0a`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ambiguous, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[2].value::Call

Source: `infra/tests/test_catalog.py:60`; AST `f70a134a313f042b4008c6b4b268ea5a8ac425e9afe036146ccc274566c06683`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ambiguous, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[8].body[2].value.args[0]::Call

Source: `infra/tests/test_catalog.py:60`; AST `df5a71fe2829835d927c36b60456350bf639b72415c1634b83b2ca86671195d9`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ambiguous, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[8].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[9]::With

Source: `infra/tests/test_catalog.py:61`; AST `b03d050f70445f490cfe38b91339fbf1d32496270be669f5faf7e10f1ddf632a`.

Rust module: `infra::tests::test_catalog`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, inventory, qualify, root, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, qualify, self.assertRaisesRegex.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[8].body[3].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[9].items[0].context_expr::Call

Source: `infra/tests/test_catalog.py:61`; AST `e81b5727a77630ccbc077b22362697e55bf7a8b3916ff4074395f5ae64a2bf7e`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[9].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[9].body[0]::Expr

Source: `infra/tests/test_catalog.py:62`; AST `33766350d33c6c69d4e59dbc2fca8b5fe74f0167d80be09dc9b27472e9875063`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, qualify, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory, qualify.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3].body[0].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[9].body[0].value::Call

Source: `infra/tests/test_catalog.py:62`; AST `656105d09e931247a822fcf90ff247efc0776155eb313e74cb7e576a0c3f62fd`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, qualify, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory, qualify.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[9].body[0].value.args[0]::Call

Source: `infra/tests/test_catalog.py:62`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].body[0].body[9].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_catalog_preserves_repeated_entries::root.body[8].body[3].body[0].body[9].body[0].value.args[1]::Lambda

Source: `infra/tests/test_catalog.py:62`; AST `0d081c005137a7088dd15c7dc0a0c6d975396ec7003c482ba2ad8f84dea84200`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[3].body[0].body[9].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4]::FunctionDef

Source: `infra/tests/test_catalog.py:64`; AST `8d9cebfe0c076ae744fba922e67781a7fb12b357d092cce54c7cced8488a4665`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: cpp_case, second, self, text, value. Outputs/bindings: second, text, value.
Calls/effect boundaries: cpp_case, self.assertEqual, self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[0]::Assign

Source: `infra/tests/test_catalog.py:65`; AST `a81ebfef4728662f8f45d9ea6c5892546855df18521be26326040dd38088b2e3`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: text.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[1]::Assign

Source: `infra/tests/test_catalog.py:66`; AST `7cf17f57c612bd4392052be4de251f5169e968776c36b5a8c2bce2250bbe51a1`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cpp_case, text. Outputs/bindings: value.
Calls/effect boundaries: cpp_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[1].value::Call

Source: `infra/tests/test_catalog.py:66`; AST `1179dabae10816eeceb5f97d1527d38388a0181f6145a75bd57f6c877ab635a4`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cpp_case, text. Outputs/bindings: (none).
Calls/effect boundaries: cpp_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[1].value.args[3]::Lambda

Source: `infra/tests/test_catalog.py:66`; AST `39dfe9cacf4bffc0abfe597ce9710f9451753edf089bb6a30a4efb127a5e0eb8`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[4].body[1].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[2]::Expr

Source: `infra/tests/test_catalog.py:67`; AST `73199e6d582cf614162bc832fb59e8c98ef6cc64cafd036da86c9799ea4d78c4`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[2].value::Call

Source: `infra/tests/test_catalog.py:67`; AST `db4e23302304959f0fad5ea8188df1704a3f2cb2c471722801e1c52885b0567f`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[3]::Expr

Source: `infra/tests/test_catalog.py:68`; AST `409cda7f0190efd83a4f0699fc8d440b62fcd3d62d023a2a3b0b1bcd8b52603f`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[3].value::Call

Source: `infra/tests/test_catalog.py:68`; AST `d50975f55e94896a5bf0b62cd03ed14d6fbf3b5a9ceab3427412f220e00ecf04`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[4]::Expr

Source: `infra/tests/test_catalog.py:69`; AST `e9dffcadc161e55fe17f237bbf995d94ac8d1a75f5204155d9240ead9cb6f801`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[4].value::Call

Source: `infra/tests/test_catalog.py:69`; AST `002da38c5779b69bfe8f6b310b7b85ab3eb3ed1c258ca0ebb46ec064cbb653bb`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[5]::Assign

Source: `infra/tests/test_catalog.py:70`; AST `a159ebc5f845d93cf8a3e2638a8fdd97161894c1a017afeebaf2dd354e981aeb`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cpp_case, text. Outputs/bindings: second.
Calls/effect boundaries: cpp_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[5].value::Call

Source: `infra/tests/test_catalog.py:70`; AST `e32201c9a70db1b62d856be944bb3044d38a9928dc399edc920d301e059a150f`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cpp_case, text. Outputs/bindings: (none).
Calls/effect boundaries: cpp_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[5].value.args[3]::Lambda

Source: `infra/tests/test_catalog.py:70`; AST `39dfe9cacf4bffc0abfe597ce9710f9451753edf089bb6a30a4efb127a5e0eb8`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[4].body[5].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[6]::Expr

Source: `infra/tests/test_catalog.py:71`; AST `930c2b2ed55440a91a4e52623ac07db504c25564b82a436065c25ef673041224`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_preserves_setup_assertions_and_ignores_comment_braces::root.body[8].body[4].body[6].value::Call

Source: `infra/tests/test_catalog.py:71`; AST `6fea7e79ca65b7272c6765c65aca9d4a240a46686a633989a900d79ec9024e44`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5]::FunctionDef

Source: `infra/tests/test_catalog.py:73`; AST `4e9a199ec09f1bff1c042491dd483b56856e5c17669b2641e942d0e3fcaa9109`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: python_case, self, value. Outputs/bindings: value.
Calls/effect boundaries: python_case, self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[0]::Assign

Source: `infra/tests/test_catalog.py:74`; AST `3309f88be120218ce0ffac353c56ddbe4db4cfdc7bce10a32b2fbefc52564468`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: python_case. Outputs/bindings: value.
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[0].value::Call

Source: `infra/tests/test_catalog.py:74`; AST `01faefa62f2513b8afafbb823aa3fc4699fb96a09c7a7692e6e149801a07f511`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python_case. Outputs/bindings: (none).
Calls/effect boundaries: python_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[0].value.args[3]::Lambda

Source: `infra/tests/test_catalog.py:74`; AST `453bffb14f4720d9044025b99e95cc1ade7a1f2c09bf6c4fcb9b9ae84bcbb25b`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[5].body[0].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[1]::Expr

Source: `infra/tests/test_catalog.py:75`; AST `6836819a7033c9819dfb741f9adff3536a2e6562a6cf7eeb5d6c546ad1d42e0b`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[1].value::Call

Source: `infra/tests/test_catalog.py:75`; AST `c5163ae4dc51c13fdc0fa5e009847154abaf55048446d9f7f97bf80782c79b5c`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[2]::Expr

Source: `infra/tests/test_catalog.py:76`; AST `99586a27535b0015ffdb5cdf118fb9d349aeb9778fc350940d8b25f9348fba48`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_missing_original_case_never_invents_a_fixture::root.body[8].body[5].body[2].value::Call

Source: `infra/tests/test_catalog.py:76`; AST `9a6299327f70480ec1fa14102a1089289ca561d89364a402bc1848bbb3bf2365`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6]::FunctionDef

Source: `infra/tests/test_catalog.py:78`; AST `1aef37a08a40283aa441a9198b1e55ae73bd224ec2ce93add00ad98da13d4442`.

Rust module: `infra::tests::test_catalog`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: cpp_case, s, self, text, value. Outputs/bindings: s, text, value.
Calls/effect boundaries: '\n'.join, cpp_case, self.assertEqual, self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[0]::Assign

Source: `infra/tests/test_catalog.py:79`; AST `f08ac4ff5a647b543a3e796a9b6394ecda76b935f2b6029bb7b6de507dc5ad94`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: text.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[1]::Assign

Source: `infra/tests/test_catalog.py:80`; AST `52b06f667cfe4da7ba8b2e9bcd49d026b27f710d3bf2b272d25535cc82f6c39d`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cpp_case, text. Outputs/bindings: value.
Calls/effect boundaries: cpp_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[1].value::Call

Source: `infra/tests/test_catalog.py:80`; AST `366015e7a0e3e2d892c6004353338c076003d8b276a5590562a1ea9a23002d77`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cpp_case, text. Outputs/bindings: (none).
Calls/effect boundaries: cpp_case.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[1].value.args[3]::Lambda

Source: `infra/tests/test_catalog.py:80`; AST `39dfe9cacf4bffc0abfe597ce9710f9451753edf089bb6a30a4efb127a5e0eb8`.

Rust module: `infra::tests::test_catalog`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[6].body[1].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[2]::Expr

Source: `infra/tests/test_catalog.py:81`; AST `6b7c9b7b0a47a080dc366e3777ca92fb503dd624152d9e77ffe82acccaf58b3a`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[2].value::Call

Source: `infra/tests/test_catalog.py:81`; AST `9f8e14a32db9d794c7fb7659c4b3fc8aace1a1eb4910c85d6cb035e19a0ae0ed`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[3]::Expr

Source: `infra/tests/test_catalog.py:82`; AST `2ea98d3c535727f5a0111a51d0141e63f60154e8fa5beb02cf5c69d77ef9b507`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: s, self, value. Outputs/bindings: s.
Calls/effect boundaries: '\n'.join, self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[3].value::Call

Source: `infra/tests/test_catalog.py:82`; AST `4d949c82d4929bab3727a4e0cea7f2b7b10f6d5d11844e13a058b6c5a9666d29`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s, self, value. Outputs/bindings: s.
Calls/effect boundaries: '\n'.join, self.assertIn.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[3].value.args[1]::Call

Source: `infra/tests/test_catalog.py:82`; AST `d395d59ded764667a3ad2732d9bdb4d4b5992325d221202535273e5072c7f2d8`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s, value. Outputs/bindings: s.
Calls/effect boundaries: '\n'.join.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::TestCatalogExtraction::test_cpp_selected_fixture_can_be_declared_after_other_tests::root.body[8].body[6].body[3].value.args[1].args[0]::GeneratorExp

Source: `infra/tests/test_catalog.py:82`; AST `d6223d8a6d0915cbf82f20917708bb9d108918f7ad0f01d0436437ca18d92d69`.

Rust module: `infra::tests::test_catalog`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: s, value. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[6].body[3].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[9]::If

Source: `infra/tests/test_catalog.py:85`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_catalog`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[9]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[9].body[0]::Expr

Source: `infra/tests/test_catalog.py:86`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_catalog`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_catalog.py::module::root.body[9].body[0].value::Call

Source: `infra/tests/test_catalog.py:86`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_catalog`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.catalog, argparse, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
