# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 197. Inventory digest: `2cf6566e24d526aa9cdcb69eee170bc4572251659e88105e44da5a3700e722b8`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_evidence.py::module::root::Module

Source: `infra/tests/test_evidence.py:1`; AST `c3eb196fc440243d89b027e8b6e74fb6c74e7a876eed3a69f82337cf795e56fe`.

Rust module: `infra::tests::test_evidence`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AUTHORITY, CASE, OUTPUT, Path, SimpleNamespace, ValueError, __file__, __name__, bad, before, classified, copy, current_receipt, differential_cases, digest, json, kani_properties, len, load_profile, mapping, matches_version, mutations, name, output, patch, path, proof_identity, proof_output, property_location, property_name, receipt, result, scenario, self, str, sys, tempfile, text, unittest, validate_plan, version. Outputs/bindings: CASE, OUTPUT, bad, before, mapping, mutations, name, output, path, receipt, result, scenario, text, version.
Calls/effect boundaries: (self.root / 'mapping.json').write_text, (self.root / 'verification/kani/src/proofs.rs').write_text, AUTHORITY.read_bytes, OUTPUT.replace, Path, Path(__file__).resolve, SimpleNamespace, classified, copy.deepcopy, current_receipt, differential_cases, digest, json.dumps, kani_properties, len, load_profile, matches_version, patch, path.parent.mkdir, path.write_text, proof_identity, proof_output, property_location, property_name, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIsNone, self.assertNotEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.output, self.plan, self.subTest, str, sys.path.insert, tempfile.TemporaryDirectory, unittest.main, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[0]::Expr

Source: `infra/tests/test_evidence.py:1`; AST `9b367e7495d1f99a9ad8e9c43418a3b3d375471a218130106530494275d52231`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[1]::Import

Source: `infra/tests/test_evidence.py:2`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[2]::Import

Source: `infra/tests/test_evidence.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[3]::ImportFrom

Source: `infra/tests/test_evidence.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[4]::Import

Source: `infra/tests/test_evidence.py:5`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[5]::Import

Source: `infra/tests/test_evidence.py:6`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_evidence.py:7`; AST `271cd8a5819453f6952690fd43e9ce152386df249c8de9a1999907454b0006b7`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[7]::Import

Source: `infra/tests/test_evidence.py:8`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_evidence.py:9`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[9]::Expr

Source: `infra/tests/test_evidence.py:11`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[9].value::Call

Source: `infra/tests/test_evidence.py:11`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[9].value.args[1]::Call

Source: `infra/tests/test_evidence.py:11`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[9].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[9].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_evidence.py:11`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[9].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[9].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_evidence.py:11`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[9].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_evidence.py:12`; AST `777b1cedc265eb54ab9edd0c92e850a460d0888c30256976272941780ed5eaf5`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_evidence.py:13`; AST `8f134c69cfbdf3492eed71a176562b2ed576ffcc2cd5b08c09d4964542974fc0`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[12]::ImportFrom

Source: `infra/tests/test_evidence.py:14`; AST `6999405573afece86fe12b52087707f3be5ddc2b44c37bc64fd352ac8cf7ff1e`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_evidence.py:15`; AST `b036376c7c82869e84ef7a7025b7cd445b77d318572840d220242772da11da1b`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[14]::Assign

Source: `infra/tests/test_evidence.py:17`; AST `eb080c24d41e2653ebc2d9d5b1483f8f871fdf854cfd3b848b8565a21e112cc3`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: CASE.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[15]::Assign

Source: `infra/tests/test_evidence.py:18`; AST `1e9f57a6cfb3d055dad64aa8cf268683fbe597981243da783e42e2012177f498`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: OUTPUT.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::root.body[16]::ClassDef

Source: `infra/tests/test_evidence.py:32`; AST `9f0d5fa1912ffcdebef29d320efdf30cc1e51ff1cda51b5ebee4eebf28951391`.

Rust module: `infra::tests::test_evidence`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: AUTHORITY, CASE, OUTPUT, Path, SimpleNamespace, ValueError, bad, before, classified, copy, current_receipt, differential_cases, digest, json, kani_properties, len, load_profile, mapping, matches_version, mutations, name, output, patch, path, proof_identity, proof_output, property_location, property_name, receipt, result, scenario, self, tempfile, text, unittest, validate_plan, version. Outputs/bindings: bad, before, mapping, mutations, name, output, path, receipt, result, scenario, text, version.
Calls/effect boundaries: (self.root / 'mapping.json').write_text, (self.root / 'verification/kani/src/proofs.rs').write_text, AUTHORITY.read_bytes, OUTPUT.replace, Path, SimpleNamespace, classified, copy.deepcopy, current_receipt, differential_cases, digest, json.dumps, kani_properties, len, load_profile, matches_version, patch, path.parent.mkdir, path.write_text, proof_identity, proof_output, property_location, property_name, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIsNone, self.assertNotEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.output, self.plan, self.subTest, tempfile.TemporaryDirectory, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0]::FunctionDef

Source: `infra/tests/test_evidence.py:33`; AST `2849ec5885160a45a902341bc601c70b1a91b30a353774bc40283e89437a2b9f`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: name, property_name, self. Outputs/bindings: name.
Calls/effect boundaries: property_name, self.assertFalse, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[0]::For

Source: `infra/tests/test_evidence.py:34`; AST `13f6b0358d9e4f3beb522aebeb1c3c18fb91c75d2da136b9cf3e777b2158e5d7`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: name, property_name, self. Outputs/bindings: name.
Calls/effect boundaries: property_name, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[0].body[0]; no call, error or mutation may be omitted. Iteration: name in ('proofs::compare::<f64, 8>.assertion.1', '<f64 as std::cmp::PartialEq>::eq.assertion.1')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_evidence.py:35`; AST `c2314c2cfd1b5d1075af764322b98da548f99f77ca48fe282c8c85d47468f079`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, property_name, self. Outputs/bindings: (none).
Calls/effect boundaries: property_name, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_evidence.py:35`; AST `e0248dc3d2c4d871dd08c47be33ea52438d7875453397b0a93e6bb96f47d111c`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, property_name, self. Outputs/bindings: (none).
Calls/effect boundaries: property_name, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:35`; AST `85af025e9528a51636a6fb5f08cea8c796f4b61e2333720941d686a3b674ce4e`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, property_name. Outputs/bindings: (none).
Calls/effect boundaries: property_name.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[1]::For

Source: `infra/tests/test_evidence.py:36`; AST `c432704c4a83d3e576ca114795bb9e5d8e5c9e2ae54e80a6e1a2c1e555d7a63e`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: name, property_name, self. Outputs/bindings: name.
Calls/effect boundaries: property_name, self.assertFalse.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[0].body[1]; no call, error or mutation may be omitted. Iteration: name in ('x.assertion.1\n', ' x.assertion.1', 'x\t.assertion.1', 'x.cover.1')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[1].body[0]::Expr

Source: `infra/tests/test_evidence.py:37`; AST `aad97c8d716c88bb01e9adc998a513d5fa3c282cccbd3e1b7ccf6fe9c743ab7d`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, property_name, self. Outputs/bindings: (none).
Calls/effect boundaries: property_name, self.assertFalse.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[1].body[0].value::Call

Source: `infra/tests/test_evidence.py:37`; AST `6305a827b7260aee39ab8e5ee9d3ac271bdaf79ab350a95cc3805f77762b017c`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, property_name, self. Outputs/bindings: (none).
Calls/effect boundaries: property_name, self.assertFalse.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_helper_and_trait_property_names_preserve_spaces::root.body[16].body[0].body[1].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:37`; AST `85af025e9528a51636a6fb5f08cea8c796f4b61e2333720941d686a3b674ce4e`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, property_name. Outputs/bindings: (none).
Calls/effect boundaries: property_name.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1]::FunctionDef

Source: `infra/tests/test_evidence.py:39`; AST `52804ad0d8dacfa732a594720106a2c7d1e181b6c20694081082679a2b446a44`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'verification/kani/src/proofs.rs').write_text, property_location, self.assertEqual, self.assertIsNone.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[0]::Expr

Source: `infra/tests/test_evidence.py:40`; AST `8b4491be117ae8e3fa32fe46794f0a389d09904a47ccc7f5203a74b3773abe69`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'verification/kani/src/proofs.rs').write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[0].value::Call

Source: `infra/tests/test_evidence.py:40`; AST `b8bd6cad6031cdb24b68d2e8d885d3767694f553b5cc364380437acdc0d36d04`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'verification/kani/src/proofs.rs').write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[1]::Expr

Source: `infra/tests/test_evidence.py:41`; AST `2e74185b8c8e9b941c08f59be6ad3b898672f1cbac57703f697288f49a777e13`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: property_location, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[1].value::Call

Source: `infra/tests/test_evidence.py:41`; AST `f992ea6735118ecb16d382ce1fc3cea2ca5089bbe764c36661f2b3c0d3569cef`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: property_location, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[1].value.args[0]::Call

Source: `infra/tests/test_evidence.py:41`; AST `d8de3943c25b346f9e89d54686d76fe440e5e55b4c0903832cb22f459aaa263a`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: property_location.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[2]::Expr

Source: `infra/tests/test_evidence.py:44`; AST `c1d3218ac01a713d5fc49f0b06076601c1750b0913fbaf9bb75503def26e12a7`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: property_location, self.assertIsNone.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[2].value::Call

Source: `infra/tests/test_evidence.py:44`; AST `95953fc8e3c677b15b6ffc8b01d9b83fc64ceb4ced8ef94419da0e614308a912`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: property_location, self.assertIsNone.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_assertion_location_is_bound_to_the_actual_manifest_source::root.body[16].body[1].body[2].value.args[0]::Call

Source: `infra/tests/test_evidence.py:44`; AST `39b3bb9a6dee61736ea44e0cf6f39512bfbe2b0f9e6e60e1494f62c8d7b5be8d`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_location, self. Outputs/bindings: (none).
Calls/effect boundaries: property_location.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2]::FunctionDef

Source: `infra/tests/test_evidence.py:47`; AST `4b96ba9ad7e78398d9af93461cbce334998ad6d170a7b9974e5e8844a8155e53`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OUTPUT, kani_properties, name, output, proof_output, self. Outputs/bindings: name, output.
Calls/effect boundaries: OUTPUT.replace, kani_properties, proof_output, self.assertEqual, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[0]::Assign

Source: `infra/tests/test_evidence.py:48`; AST `4a40cbf5397e960e9b6f180e64b61797fa7564c0ac07cd5890a457c3a456e7ab`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: name.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[1]::Assign

Source: `infra/tests/test_evidence.py:49`; AST `b7a21591cb675dd1c31f20dd31de4bca56dba60c194e8f1db2a9402ab1636c2f`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OUTPUT, name. Outputs/bindings: output.
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[1].value::Call

Source: `infra/tests/test_evidence.py:49`; AST `2a0b704beb94d9375e6940b3a6008436b51399fabe4da0ca31a59fdd3ad9b449`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT, name. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[2]::Expr

Source: `infra/tests/test_evidence.py:50`; AST `69a5a5b254cc9e6f84a76ef95756d092b238647fb948c65ecd9618784cceda91`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kani_properties, name, output, self. Outputs/bindings: (none).
Calls/effect boundaries: kani_properties, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[2].value::Call

Source: `infra/tests/test_evidence.py:50`; AST `ad73f0ef26f2509e1faaba8fcb6bc65ebc2d13bf14982025bba6da8bdefeccf7`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kani_properties, name, output, self. Outputs/bindings: (none).
Calls/effect boundaries: kani_properties, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[2].value.args[0].value.value::Call

Source: `infra/tests/test_evidence.py:50`; AST `7c0f943fd80f660c8b177905e7707e92f5191eeaf4ac11ad9d8383985b39439f`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kani_properties, output. Outputs/bindings: (none).
Calls/effect boundaries: kani_properties.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[2].value.args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[3]::Expr

Source: `infra/tests/test_evidence.py:51`; AST `436652292cb6959314ac9072df83ee2779db0c6dd28b926814cc35e3fbba8b23`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[3].value::Call

Source: `infra/tests/test_evidence.py:51`; AST `5e425f1e6977f99157151c2ba85d9bf17bf41c14193c02c1156f47b239970f30`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[3].value.args[0]::Call

Source: `infra/tests/test_evidence.py:51`; AST `e6700bc9f52dcadcfc932c72fe6ae74ea2220352f6e799cdee635c204ebd5611`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_property_names_with_rust_type_spaces_are_never_dropped::root.body[16].body[2].body[3].value.args[0].args[1]::Call

Source: `infra/tests/test_evidence.py:51`; AST `9f725a377b470ce141117b776e04efe2d21329f9b87446a50e3d1be2eaa9ccf5`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, self. Outputs/bindings: (none).
Calls/effect boundaries: self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3]::FunctionDef

Source: `infra/tests/test_evidence.py:53`; AST `9636b3a2b38b907c523379a8c62fe4582f133516485a61c26ff834f79d7a2214`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OUTPUT, output, proof_output, self. Outputs/bindings: output.
Calls/effect boundaries: OUTPUT.replace, proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0]::For

Source: `infra/tests/test_evidence.py:54`; AST `1b0ab1f1f7eefee166a978ceacd794b1bb2ac11ff70da34e96a098eda51893dd`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OUTPUT, output, proof_output, self. Outputs/bindings: output.
Calls/effect boundaries: OUTPUT.replace, proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[3].body[0]; no call, error or mutation may be omitted. Iteration: output in (OUTPUT.replace('Check 2:', 'Check 3:'), OUTPUT.replace(' - Status: SATISFIED\n', ''))
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0].iter.elts[0]::Call

Source: `infra/tests/test_evidence.py:54`; AST `cabe083cdc6a1ce5f077f099814976638cf1483b51728973f0a3e54c0dc828c3`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0].iter.elts[1]::Call

Source: `infra/tests/test_evidence.py:55`; AST `8d81a64873168b8736ab009b3e89d74c13552186f6de33e9f2aa2c86f193f776`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0].body[0]::Expr

Source: `infra/tests/test_evidence.py:56`; AST `436652292cb6959314ac9072df83ee2779db0c6dd28b926814cc35e3fbba8b23`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_evidence.py:56`; AST `5e425f1e6977f99157151c2ba85d9bf17bf41c14193c02c1156f47b239970f30`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:56`; AST `e6700bc9f52dcadcfc932c72fe6ae74ea2220352f6e799cdee635c204ebd5611`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_incomplete_property_inventory_is_rejected::root.body[16].body[3].body[0].body[0].value.args[0].args[1]::Call

Source: `infra/tests/test_evidence.py:56`; AST `9f725a377b470ce141117b776e04efe2d21329f9b87446a50e3d1be2eaa9ccf5`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, self. Outputs/bindings: (none).
Calls/effect boundaries: self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4]::FunctionDef

Source: `infra/tests/test_evidence.py:58`; AST `78fe63ba9ad293efa565bdc0733f4218f4bf93d539ea9a62041b6add69798a06`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OUTPUT, classified, receipt, self. Outputs/bindings: receipt.
Calls/effect boundaries: OUTPUT.replace, classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4].body[0]::Assign

Source: `infra/tests/test_evidence.py:59`; AST `854441d40f19bd74c216175f2bcd9179a4e297387806b58ab8f5d91245e41316`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4].body[1]::Assign

Source: `infra/tests/test_evidence.py:60`; AST `80438f8dc7649726d16fa81232d25e6ae2245de9059fe21cb2436b0c03ca1857`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OUTPUT. Outputs/bindings: receipt.
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4].body[1].value.values[0].elts[0].values[0]::Call

Source: `infra/tests/test_evidence.py:60`; AST `07cf0b7d761cbbd1f3491809319afd116c6a5ab6efdb857607593941909d9893`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].value.values[0].elts[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4].body[2]::Expr

Source: `infra/tests/test_evidence.py:61`; AST `06a3a4833b7f807b60cbe0c2440f796fb7f928ee319a7adb6dab5f52234b6f70`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4].body[2].value::Call

Source: `infra/tests/test_evidence.py:61`; AST `cfbb9734ef1758180afe2efb4d82d8a2962e0e07e9c4e742df4b54103138a467`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_manifest_relative_cover_locations_resolve_to_the_bound_source::root.body[16].body[4].body[2].value.args[0]::Call

Source: `infra/tests/test_evidence.py:61`; AST `2ff91e3b48d4cf382fffefde71e6c38210b8199ab253397eab45b9d25f6ec973`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5]::FunctionDef

Source: `infra/tests/test_evidence.py:62`; AST `cd8ec54686d0bf861d6046cfc35a4238d2f90d783c95b82ffb46ba744ebfcfea`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CASE, Path, name, path, self, tempfile. Outputs/bindings: name, path.
Calls/effect boundaries: Path, path.parent.mkdir, path.write_text, self.addCleanup, tempfile.TemporaryDirectory.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[0]::Assign

Source: `infra/tests/test_evidence.py:63`; AST `76bde1458ae912172e4121d6d32a40d02cf372c4db6ead9b5af171facc2865c2`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[0].value::Call

Source: `infra/tests/test_evidence.py:63`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[1]::Expr

Source: `infra/tests/test_evidence.py:64`; AST `9136d3f8186e6b1cc86fd1969468d3111706e262f63ee76b6597810ec3073f13`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[1].value::Call

Source: `infra/tests/test_evidence.py:64`; AST `e659ac5a3f01e7994826bd72f68d4724068e6acade4de2c4992b16eb0f99b918`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[2]::Assign

Source: `infra/tests/test_evidence.py:65`; AST `3fd62e96028b079a923df6e9a7c1c1df8b3ae2536d55ba9d4f31f162d4d5ddb5`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[2].value::Call

Source: `infra/tests/test_evidence.py:65`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[3]::For

Source: `infra/tests/test_evidence.py:66`; AST `4819a6569ea786a207f6b79cd0e708666cf68c1ca1b91aa4852004f5d15a1fb3`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: name, path, self. Outputs/bindings: name, path.
Calls/effect boundaries: path.parent.mkdir, path.write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[5].body[3]; no call, error or mutation may be omitted. Iteration: name in ('src/runtime.rs', 'verification/spec/src/spec.rs', 'verification/kani/src/proofs.rs', 'verification/kani/Cargo.toml')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[3].body[0]::Assign

Source: `infra/tests/test_evidence.py:67`; AST `16c8e9194cc4e905a83d3c71092388e0be89d88461647b1e485eaa9b22d71c6b`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[3].body[1]::Expr

Source: `infra/tests/test_evidence.py:68`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[3].body[1].value::Call

Source: `infra/tests/test_evidence.py:68`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[3].body[2]::Expr

Source: `infra/tests/test_evidence.py:69`; AST `c71909ca115c6aea87c79b7037e9899f1c277ad64aba649df278e9125dc6c9fe`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[3].body[2].value::Call

Source: `infra/tests/test_evidence.py:69`; AST `d320fd53af77cc0b53e02c8c5e6f4372011967863a29915d213d5a0b267c30d8`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[4]::Assign

Source: `infra/tests/test_evidence.py:70`; AST `d840d9dcf29bb32d77075b36e777c2d3b5a7e272d142b119b13932dc5b321530`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::setUp::root.body[16].body[5].body[5]::Assign

Source: `infra/tests/test_evidence.py:74`; AST `68547ac2bd4cd6a7b84a8afb1a720253bea5d1fbdae9e83affe8da3c3dffd1e5`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: CASE, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::output::root.body[16].body[6]::FunctionDef

Source: `infra/tests/test_evidence.py:80`; AST `d26283cf093eb0138288b67e067ea29b09e09e444240e0f3d6613f785d232655`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: SimpleNamespace, text. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::output::root.body[16].body[6].body[0]::Return

Source: `infra/tests/test_evidence.py:81`; AST `f705dd72d0169a0b4fd78d5ba45764bee6b160997f06ba5f8924118951794adc`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SimpleNamespace, text. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::output::root.body[16].body[6].body[0].value::Call

Source: `infra/tests/test_evidence.py:81`; AST `8501888d3ec681936a82ae634a978e83f2e49865186f630f577f85e798ee3a33`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, text. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::plan::root.body[16].body[7]::FunctionDef

Source: `infra/tests/test_evidence.py:83`; AST `809dd60f2454c38aebd99e50341cea0ab9c3cb818d797c17833db24f4520a225`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AUTHORITY, digest, self. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes, digest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::plan::root.body[16].body[7].body[0]::Return

Source: `infra/tests/test_evidence.py:84`; AST `e7710308ddb1dfc33b58a98a6660b485b9506469cc2fe0b3913cee12bd4b9efd`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AUTHORITY, digest, self. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes, digest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[16].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::plan::root.body[16].body[7].body[0].value.values[2]::Call

Source: `infra/tests/test_evidence.py:84`; AST `6e82c214c870a2d99c759bc7f0f9ca53a1cf98bccb7c7a8429fe6b380861b9ea`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AUTHORITY, digest. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes, digest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::plan::root.body[16].body[7].body[0].value.values[2].args[0]::Call

Source: `infra/tests/test_evidence.py:84`; AST `357d0bc218c0b02201bc2aff9908fb9de431cd99cfa3beeb2659a5edfb327eec`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AUTHORITY. Outputs/bindings: (none).
Calls/effect boundaries: AUTHORITY.read_bytes.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8]::FunctionDef

Source: `infra/tests/test_evidence.py:88`; AST `0ba69c77217b9b2f140fa6eef8b6cd16afdfeae2ee60e1c80e9eb5da6b564641`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: matches_version, self, version. Outputs/bindings: version.
Calls/effect boundaries: matches_version, self.assertFalse, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[0]::Expr

Source: `infra/tests/test_evidence.py:89`; AST `c4903bcdc1c1bc57f22720ea4069b2a0fbf920d4bb532b23f79ddcd7c7028405`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches_version, self. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[0].value::Call

Source: `infra/tests/test_evidence.py:89`; AST `d3389401fe2c4a9f443e080e4cf0b405dbdce132d0714ba9b92794acb771f2bc`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches_version, self. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, self.assertTrue.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:89`; AST `36021f1645b116235eb9d4b33c2d988654149cec42f479c4667874c1943b8c9e`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches_version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[1]::For

Source: `infra/tests/test_evidence.py:90`; AST `e5104318781ae912ba13fdb9d935d7c9e645687e53ce88cd6c636e5bfef54a8d`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: matches_version, self, version. Outputs/bindings: version.
Calls/effect boundaries: matches_version, self.assertFalse.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[8].body[1]; no call, error or mutation may be omitted. Iteration: version in ('0.68.01', '0.68.0-dev', '0.67.0', 'v0.68.0')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[1].body[0]::Expr

Source: `infra/tests/test_evidence.py:91`; AST `a829494c69fe1e7226af0181a02dc1edd1fa811cd266bf235c8dce534a026041`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches_version, self, version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, self.assertFalse.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[1].body[0].value::Call

Source: `infra/tests/test_evidence.py:91`; AST `df3fbb8edf16de62828b54fbd2c5d09c0a42ffdb8720b56688fa0ce938bd474f`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches_version, self, version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, self.assertFalse.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_pinned_version_has_no_prefix_or_prerelease_alias::root.body[16].body[8].body[1].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:91`; AST `10d365ab1f932c083eea89ed183cb17be5e07259c70325a793daced1a806ff79`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches_version, version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[8].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9]::FunctionDef

Source: `infra/tests/test_evidence.py:93`; AST `130c87c4640b543291489222ee4562a9299ed20b893bc728fbfd357bb935b209`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OUTPUT, mutations, proof_output, self, text. Outputs/bindings: mutations, text.
Calls/effect boundaries: OUTPUT.replace, proof_output, self.assertFalse, self.assertTrue, self.output, self.subTest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[0]::Expr

Source: `infra/tests/test_evidence.py:94`; AST `1ed2634a281f27a7ed122457188c971fa6f6ad1de75e7d3fb993344a1d7b12ca`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OUTPUT, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertTrue, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[0].value::Call

Source: `infra/tests/test_evidence.py:94`; AST `8d2d8447e3531f858c6b67bb1067b8fb006ec076dcaef771dad50b12e455fb84`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertTrue, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:94`; AST `da7c21d00747a157be4979a649b5a24617bccf7f909df863f0c6c18545699b1e`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT, proof_output, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[0].value.args[0].args[1]::Call

Source: `infra/tests/test_evidence.py:94`; AST `4b39d2b08185d90adb4439be9c5560a0bc38f29b89d64369b8d937a8c7126bfd`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT, self. Outputs/bindings: (none).
Calls/effect boundaries: self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1]::Assign

Source: `infra/tests/test_evidence.py:95`; AST `a4ed599bb2b71ee98e62ce205c30f2e41558b32f4d7996752e0ae8c4b259f1f7`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OUTPUT. Outputs/bindings: mutations.
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[0]::Call

Source: `infra/tests/test_evidence.py:95`; AST `9d18854f930bfbc6f093b374974e6dc303d61cb09962c851863e35a1ec96c9c9`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[2]::Call

Source: `infra/tests/test_evidence.py:96`; AST `f7cc142894148ffa576a09e894f93e62b8a9710a1b44018749604bf4b83c7e16`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[3]::Call

Source: `infra/tests/test_evidence.py:96`; AST `eeedb428d28ecae4e5a52331d60dbdb0d29a6748ba3f99a4438b14c7e56a055b`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[4]::Call

Source: `infra/tests/test_evidence.py:97`; AST `c726cdfab9fcb14f5a3d39e6986b9124983d8942f903ca9209f7240c9dcf2de0`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[5]::Call

Source: `infra/tests/test_evidence.py:97`; AST `b3c74b40e640c0d8c18ae9cde73f4e7faefb4ef875452e5a67566b5181b8dbdf`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[6]::Call

Source: `infra/tests/test_evidence.py:98`; AST `710ed7f878c4cfa4b650fd015d1c33b0dc9f1059d873bdcdf4734a9ed3990e62`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[1].value.elts[7]::Call

Source: `infra/tests/test_evidence.py:98`; AST `21d49dceac6cb149129213ccadcf2c34acad208a91e864d42581edc7b7bb9ddb`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[1].value.elts[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2]::For

Source: `infra/tests/test_evidence.py:100`; AST `b72d1e0ebab8e2a09b51f607afc10090c2f93443e58e9388bb5c8dd65f7ea9c5`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: mutations, proof_output, self, text. Outputs/bindings: text.
Calls/effect boundaries: proof_output, self.assertFalse, self.output, self.subTest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[9].body[2]; no call, error or mutation may be omitted. Iteration: text in mutations
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2].body[0]::With

Source: `infra/tests/test_evidence.py:101`; AST `e6a5e98cb6bc2d3805c46fb7e07fa81e98590b15fc5bf05c3316c585680199dd`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: proof_output, self, text. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output, self.subTest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[9].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:101`; AST `628d7132e2225644f60c556b3d2a0a01b504b600586022b2d6472a6343c9b17a`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2].body[0].body[0]::Expr

Source: `infra/tests/test_evidence.py:102`; AST `dd3752fd5dea1ab895ea82308d36745d2f64bbd41ce3f9c9dc47235eb1318415`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proof_output, self, text. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_evidence.py:102`; AST `83beddb6263053ac3b926d39e8f62842a9b3e74dd6f9e8c0683d1a7689ebf5f7`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof_output, self, text. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.assertFalse, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:102`; AST `1091a268d39eb3b35a10a05a87a6c334456932d61506ca19fd69c17fa24673e2`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof_output, self, text. Outputs/bindings: (none).
Calls/effect boundaries: proof_output, self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_exact_harness_needs_behavioral_assertion_and_reachable_cover::root.body[16].body[9].body[2].body[0].body[0].value.args[0].args[1]::Call

Source: `infra/tests/test_evidence.py:102`; AST `7173dd33dfbabc32f8af8628e16b24dbe184252bc67ef3e715d0e751c15d2b78`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, text. Outputs/bindings: (none).
Calls/effect boundaries: self.output.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].body[2].body[0].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10]::FunctionDef

Source: `infra/tests/test_evidence.py:104`; AST `6aec899bd0b433d96269d5937c662ee09c7d818e94d6776c2fc22bef462e4728`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OUTPUT, ValueError, bad, classified, receipt, self. Outputs/bindings: bad, receipt.
Calls/effect boundaries: OUTPUT.replace, classified, self.assertEqual, self.assertRaises.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[0]::Assign

Source: `infra/tests/test_evidence.py:105`; AST `27494869ff040a87b7229fd2cf4b897c0de209d8c250387f4e61ac44dfdb363c`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OUTPUT. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[1]::Expr

Source: `infra/tests/test_evidence.py:106`; AST `0a60268a8c5081bb9192e5ceb550eb886f224f04752627d93ee3c8640a248bc3`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[1].value::Call

Source: `infra/tests/test_evidence.py:106`; AST `109a9920ad0ca378dbe5c857dc4026153cd7de11c6d71906a22503ec3205cdc2`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[1].value.args[0]::Call

Source: `infra/tests/test_evidence.py:106`; AST `2ff91e3b48d4cf382fffefde71e6c38210b8199ab253397eab45b9d25f6ec973`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[2]::Assign

Source: `infra/tests/test_evidence.py:107`; AST `9de68dc4f97f1ef4e866de166bcb7f536991c886fc8ad824b4c68f2725550941`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[3]::Expr

Source: `infra/tests/test_evidence.py:108`; AST `d0f5b109f6aac3ab691619dd9548f7b1d3b931a1d5b93eebb9df7388633f41cc`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[3].value::Call

Source: `infra/tests/test_evidence.py:108`; AST `d85680237e7ce938c74f489259270d09255d34d8a75e61bff91ca00afd75e183`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[3].value.args[0]::Call

Source: `infra/tests/test_evidence.py:108`; AST `2ff91e3b48d4cf382fffefde71e6c38210b8199ab253397eab45b9d25f6ec973`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[4]::Assign

Source: `infra/tests/test_evidence.py:109`; AST `854441d40f19bd74c216175f2bcd9179a4e297387806b58ab8f5d91245e41316`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[5]::Expr

Source: `infra/tests/test_evidence.py:110`; AST `06a3a4833b7f807b60cbe0c2440f796fb7f928ee319a7adb6dab5f52234b6f70`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[5].value::Call

Source: `infra/tests/test_evidence.py:110`; AST `cfbb9734ef1758180afe2efb4d82d8a2962e0e07e9c4e742df4b54103138a467`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[5].value.args[0]::Call

Source: `infra/tests/test_evidence.py:110`; AST `2ff91e3b48d4cf382fffefde71e6c38210b8199ab253397eab45b9d25f6ec973`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classified, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6]::For

Source: `infra/tests/test_evidence.py:111`; AST `fb0ef8fe156076a41ced427f2924f2b67cefeb6f3ada7aae6a5c5563ca5dc3d9`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OUTPUT, ValueError, bad, classified, self. Outputs/bindings: bad.
Calls/effect boundaries: OUTPUT.replace, classified, self.assertRaises.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[10].body[6]; no call, error or mutation may be omitted. Iteration: bad in (OUTPUT.replace('src/runtime.rs', 'verification/spec/src/spec.rs'), OUTPUT.replace('SATISFIED', 'UNREACHABLE'))
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6].iter.elts[0]::Call

Source: `infra/tests/test_evidence.py:111`; AST `93af726dcb46edeb780ddd49bcf176b1c127794cfb4e6f65f818e03bae303735`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[6].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6].iter.elts[1]::Call

Source: `infra/tests/test_evidence.py:111`; AST `eeedb428d28ecae4e5a52331d60dbdb0d29a6748ba3f99a4438b14c7e56a055b`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OUTPUT. Outputs/bindings: (none).
Calls/effect boundaries: OUTPUT.replace.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[6].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6].body[0]::With

Source: `infra/tests/test_evidence.py:112`; AST `1fb643d018e42dc1160f070e285684793c94594b2e264caee2591e5053f532f6`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, bad, classified, self. Outputs/bindings: (none).
Calls/effect boundaries: classified, self.assertRaises.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[10].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:112`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6].body[0].body[0]::Expr

Source: `infra/tests/test_evidence.py:113`; AST `505636d95c25bacd1102e3004d0a69376f0dcd11adefe7674d7412f70b40549a`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bad, classified, self. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[10].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_mapping_and_spec_success_do_not_promote_to_production::root.body[16].body[10].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_evidence.py:113`; AST `ee19c600a4da5bdcc088744751ee99bcf37e1ad45244511427b5b111477af100`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bad, classified, self. Outputs/bindings: (none).
Calls/effect boundaries: classified.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11]::FunctionDef

Source: `infra/tests/test_evidence.py:115`; AST `ed6ec7c106827cedb8738dd1417bd0fe17ab2d8934fed13696220e0cd31f46f4`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CASE, ValueError, copy, load_profile, patch, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy, load_profile, patch, self.assertRaisesRegex, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[0]::Assign

Source: `infra/tests/test_evidence.py:116`; AST `6121788deebdf8eb52b9dd2df60882e37f5e0f7e4a2f25ab6836a159c3a65390`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[0].value::Call

Source: `infra/tests/test_evidence.py:116`; AST `f90a45f27c7bda51cfbb7bbbab4f05b6399aa13d0846c4423f171f895c777bb6`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1]::With

Source: `infra/tests/test_evidence.py:117`; AST `6949548bdf4a6d1278ef6e66e5d048a99ffcbd1eeb8e8086f731ba631674da12`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: CASE, ValueError, load_profile, patch, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, patch, self.assertRaisesRegex, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:117`; AST `a6932a3d9f2d5f0a35ce3d8a7004cd4d61d937b26e5a9c904d2f0dcc678f8f76`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CASE, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[0]::Expr

Source: `infra/tests/test_evidence.py:118`; AST `7a4b09ac4d6094d70597eec0c80bfb418f8c37c3e24fcebdc4c5e8aa9cfcc760`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[0].value::Call

Source: `infra/tests/test_evidence.py:118`; AST `e8b97a9f15fad44aadddcec577be5db8e47e22df26adfa02f47ed31379558a67`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[0].value.args[1]::Call

Source: `infra/tests/test_evidence.py:118`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[0].value.args[2]::Call

Source: `infra/tests/test_evidence.py:118`; AST `fab2b664c25feaf86a8583183a1bb2a01f03f8bc168e96e3098f4b9bc22601e0`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[1]::Assign

Source: `infra/tests/test_evidence.py:119`; AST `7f50bb00265f2d470614fc09c2c72f1f5229f512fb3213c6f2c5a391f4f397e0`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[11].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[2]::With

Source: `infra/tests/test_evidence.py:120`; AST `448f884f6def8c50a9d3bc0e0b083fbea8759e2f4d78066955551e15d3cdaebf`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.assertRaisesRegex, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[11].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[2].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:120`; AST `248d4f4d2493ea604efeb5b69faae00c8f9b7c088b4f3fb4cd65b84fe05ecd80`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[2].body[0]::Expr

Source: `infra/tests/test_evidence.py:121`; AST `7a4b09ac4d6094d70597eec0c80bfb418f8c37c3e24fcebdc4c5e8aa9cfcc760`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[2].body[0].value::Call

Source: `infra/tests/test_evidence.py:121`; AST `e8b97a9f15fad44aadddcec577be5db8e47e22df26adfa02f47ed31379558a67`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[2].body[0].value.args[1]::Call

Source: `infra/tests/test_evidence.py:121`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[2].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[2].body[0].value.args[2]::Call

Source: `infra/tests/test_evidence.py:121`; AST `fab2b664c25feaf86a8583183a1bb2a01f03f8bc168e96e3098f4b9bc22601e0`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[2].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[3]::Assign

Source: `infra/tests/test_evidence.py:122`; AST `d2f5b572aa1555955a8488b279ffc65a1e31ee45c7f8a557f45cbd2ca889a81d`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[11].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[4]::With

Source: `infra/tests/test_evidence.py:123`; AST `ec1ec1c73e331f3bfef767c92e2756eee983704c2f841f3b8a501f8cb62f69fd`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.assertRaisesRegex, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[11].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[4].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:123`; AST `67b66f087ebf699d93af586c9d802aaeefec34013b2d1ed4eee34dff6bc9c0bf`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[4].body[0]::Expr

Source: `infra/tests/test_evidence.py:124`; AST `7a4b09ac4d6094d70597eec0c80bfb418f8c37c3e24fcebdc4c5e8aa9cfcc760`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[11].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[4].body[0].value::Call

Source: `infra/tests/test_evidence.py:124`; AST `e8b97a9f15fad44aadddcec577be5db8e47e22df26adfa02f47ed31379558a67`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile, self, validate_plan. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, self.plan, validate_plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[4].body[0].value.args[1]::Call

Source: `infra/tests/test_evidence.py:124`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[4].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_classification_requires_catalog_identity_and_production_witness::root.body[16].body[11].body[1].body[4].body[0].value.args[2]::Call

Source: `infra/tests/test_evidence.py:124`; AST `fab2b664c25feaf86a8583183a1bb2a01f03f8bc168e96e3098f4b9bc22601e0`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.plan.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].body[1].body[4].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12]::FunctionDef

Source: `infra/tests/test_evidence.py:126`; AST `89203f6c4ea3681379a0e8f4777a61c0d782e31602b22c3f52deaa239b205cd3`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: before, proof_identity, self. Outputs/bindings: before.
Calls/effect boundaries: (self.root / 'verification/kani/src/proofs.rs').write_text, proof_identity, self.assertNotEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[0]::Assign

Source: `infra/tests/test_evidence.py:127`; AST `bc48271ce935a52af05bfe1bca5552ac6000c2fa9205a540a0442f9a327d6bc7`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proof_identity, self. Outputs/bindings: before.
Calls/effect boundaries: proof_identity.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[0].value::Call

Source: `infra/tests/test_evidence.py:127`; AST `2c1a2d6e59c63420e16ee444da2acc304e2a23f0fb975f67c5b8625627a806c4`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof_identity, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[1]::Expr

Source: `infra/tests/test_evidence.py:128`; AST `fc7b08e5da81573d554fad094ff88e2ad522346478082fe33f4533a2839a2c80`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'verification/kani/src/proofs.rs').write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[1].value::Call

Source: `infra/tests/test_evidence.py:128`; AST `76336203a38948a54a75672e9f5bb0f29575fb968ab9e0a1bb9ebf978be300b6`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'verification/kani/src/proofs.rs').write_text.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[2]::Expr

Source: `infra/tests/test_evidence.py:129`; AST `98b801bfc2154367f63758a74f622ecbccd2c5318bc3a605842becec5eb92f81`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, proof_identity, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity, self.assertNotEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[2].value::Call

Source: `infra/tests/test_evidence.py:129`; AST `a6f5555c3750ba19eea2fbe34701285d7d6a00f5f14f6006f84e3e7840f5f9bf`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, proof_identity, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity, self.assertNotEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_harness_digest_changes_even_without_a_git_commit::root.body[16].body[12].body[2].value.args[1]::Call

Source: `infra/tests/test_evidence.py:129`; AST `2c1a2d6e59c63420e16ee444da2acc304e2a23f0fb975f67c5b8625627a806c4`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof_identity, self. Outputs/bindings: (none).
Calls/effect boundaries: proof_identity.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[12].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13]::FunctionDef

Source: `infra/tests/test_evidence.py:131`; AST `ebe36814160987b8e4bbf0c46c06114176c808771374b04355e8a82f7779abd3`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, current_receipt, load_profile, result, self. Outputs/bindings: result.
Calls/effect boundaries: current_receipt, load_profile, self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13].body[0]::For

Source: `infra/tests/test_evidence.py:132`; AST `efc8aaf573096fd06b2b0bd4c411d88a36e111e2d92c767c48d869c6786de492`.

Rust module: `infra::tests::test_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, current_receipt, load_profile, result, self. Outputs/bindings: result.
Calls/effect boundaries: current_receipt, load_profile, self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[16].body[13].body[0]; no call, error or mutation may be omitted. Iteration: result in ({'executed': False, 'status': 'REUSED'}, {'status': 'OBSERVED_SUCCESS'}, {'executed': True, 'status': 'UNAVAILABLE'})
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13].body[0].body[0]::With

Source: `infra/tests/test_evidence.py:133`; AST `3ab9ce5ef7611543465c7e46a0c5841d50f57611f370f84288356553ac2466b1`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, current_receipt, load_profile, result, self. Outputs/bindings: (none).
Calls/effect boundaries: current_receipt, load_profile, self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:133`; AST `a418bacc6a430026f49ab8918ac9d5ed134fd15fe2c106efbf20cfd5acb64fbf`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_evidence.py:134`; AST `593f29891e335c30c08e89b9a30edd69a1e3fbcabd8c17dd61035fdc03977184`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_receipt, load_profile, result, self. Outputs/bindings: (none).
Calls/effect boundaries: current_receipt, load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_evidence.py:134`; AST `79b16b6079e430aac64d049b7576acb2c5512ab3a1d5184877abb8793e97c114`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_receipt, load_profile, result, self. Outputs/bindings: (none).
Calls/effect boundaries: current_receipt, load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_cached_or_missing_execution_is_not_evidence::root.body[16].body[13].body[0].body[0].body[0].value.args[1]::Call

Source: `infra/tests/test_evidence.py:134`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[0].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14]::FunctionDef

Source: `infra/tests/test_evidence.py:136`; AST `a5f5f78e7cc15ab25d4f2deb13f491f7adffda18ec31b866ec75445493e03d01`.

Rust module: `infra::tests::test_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CASE, ValueError, differential_cases, json, len, load_profile, mapping, patch, receipt, scenario, self. Outputs/bindings: mapping, receipt, scenario.
Calls/effect boundaries: (self.root / 'mapping.json').write_text, differential_cases, json.dumps, len, load_profile, patch, self.assertEqual, self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[0]::Assign

Source: `infra/tests/test_evidence.py:137`; AST `abb93e96c1fbd682a7f9b66ecd6921a09c97487512895eb14785369eee47d33c`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: scenario.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[1]::Assign

Source: `infra/tests/test_evidence.py:138`; AST `37952499776c57e8eabd52eaede8a7d23e22c9b5401e791db19b433b074e54fb`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: CASE, scenario. Outputs/bindings: mapping.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[2]::Expr

Source: `infra/tests/test_evidence.py:140`; AST `e1fbe4b3c2a805537794fac28db5c6abb97fdce2f334d2e61094f35ea1c6797a`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, mapping, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'mapping.json').write_text, json.dumps.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[2].value::Call

Source: `infra/tests/test_evidence.py:140`; AST `c6db8438ca845d375bc16262ae9bfd1b61feb3ae82fcebd8e5cab538a0a33bd4`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, mapping, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'mapping.json').write_text, json.dumps.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[2].value.args[0]::Call

Source: `infra/tests/test_evidence.py:140`; AST `b46e9b44482d36ab991144d9f26b29b94a47d049a6167234b813566d47b91378`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, mapping. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[3]::Assign

Source: `infra/tests/test_evidence.py:141`; AST `32e04560aa6be5c29a82eb68f217d2c6f92a38a0ce8f02f1dfab3793624ccc0e`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: scenario. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4]::With

Source: `infra/tests/test_evidence.py:143`; AST `a9a72751abda5750328c4fed2b6145d6e99e09bd605b3301fe3ca8554567c2e7`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, differential_cases, len, load_profile, patch, receipt, scenario, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, len, load_profile, patch, self.assertEqual, self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:143`; AST `a842d8b4d7d90325ab5d82ee3868cf80181584baa2b7bdb0a46746293b5e640c`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, receipt. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[0]::Expr

Source: `infra/tests/test_evidence.py:144`; AST `b4247ef120cbf7ed6d29ae77b0acc4324116972b72b05a07147bd9ddccdfe9f5`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: differential_cases, len, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, len, load_profile, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[14].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[0].value::Call

Source: `infra/tests/test_evidence.py:144`; AST `c52ad841dd5f664ec993d46669242d8d89291471921c5469ebe1f6e5380d1c3e`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: differential_cases, len, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, len, load_profile, self.assertEqual.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[0].value.args[0]::Call

Source: `infra/tests/test_evidence.py:144`; AST `23319f9a21067b658cbb68b8298673d916dd93600ecfe023c177c9d3cb35cb92`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: differential_cases, len, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, len, load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[0].value.args[0].args[0]::Call

Source: `infra/tests/test_evidence.py:144`; AST `5f9e6b6230099587ff375a6efc652b012f23bf6122b73d4f3dc73eba3936b5bf`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: differential_cases, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[0].value.args[0].args[0].args[1]::Call

Source: `infra/tests/test_evidence.py:144`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[0].value.args[0].args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[1]::Assign

Source: `infra/tests/test_evidence.py:145`; AST `cd01d808cc6abff587e86baf726c52e94df39477146da2943a8ecac84707c47d`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, scenario. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[14].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[2]::With

Source: `infra/tests/test_evidence.py:146`; AST `1802952dea7d8357a54480405e27872d726e8c7ce0896a890f064450ff91a651`.

Rust module: `infra::tests::test_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, differential_cases, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, load_profile, self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[16].body[14].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[2].items[0].context_expr::Call

Source: `infra/tests/test_evidence.py:146`; AST `a387b59f603aae921a21caf5a1779e8e58e865ade29079deb4b0e0981b68fdcd`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[2].body[0]::Expr

Source: `infra/tests/test_evidence.py:147`; AST `08646c8b3f04d59acd234ca8213defe78701deb30dbe1c8a8f066bb03a34cce6`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: differential_cases, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[14].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[2].body[0].value::Call

Source: `infra/tests/test_evidence.py:147`; AST `5f9e6b6230099587ff375a6efc652b012f23bf6122b73d4f3dc73eba3936b5bf`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: differential_cases, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: differential_cases, load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::TestEvidence::test_differential_evidence_requires_real_executed_scenario_inventory::root.body[16].body[14].body[4].body[2].body[0].value.args[1]::Call

Source: `infra/tests/test_evidence.py:147`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[16].body[14].body[4].body[2].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[17]::If

Source: `infra/tests/test_evidence.py:150`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[17]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[17].body[0]::Expr

Source: `infra/tests/test_evidence.py:151`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_evidence.py::module::root.body[17].body[0].value::Call

Source: `infra/tests/test_evidence.py:151`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.evidence, agentinfra.formal, copy, json, pathlib, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
