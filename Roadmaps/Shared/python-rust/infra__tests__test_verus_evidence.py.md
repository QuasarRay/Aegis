# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 149. Inventory digest: `01c73734136bb52a463a3ba6f5482c8318bee927be6ddfd5f69906939540135f`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_verus_evidence.py::module::root::Module

Source: `infra/tests/test_verus_evidence.py:1`; AST `69d5a2a99380208eadaece575444180a5b5c43b426b7cfe4405a5e974ba17302`.

Rust module: `infra::tests::test_verus_evidence`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ENTRY, Path, VIR, ValueError, assertion, authority, case, cases, catalog, changed, copy, current_inventory, d, digest, fixture, i, identity, inventory, j, len, mapped, mutate, mutation, path, r, range, self, source, source_inventory, tempfile, test, text, unittest, validate_case_map, validate_symbol_mapping, value. Outputs/bindings: ENTRY, VIR, assertion, authority, case, cases, catalog, changed, d, fixture, i, identity, j, mapped, mutate, mutation, path, r, source, source_inventory, test, text, value.
Calls/effect boundaries: (self.root / self.artifact).write_text, Path, VIR.replace, VIR.split, cases.append, catalog.append, changed['cases'].pop, copy.deepcopy, current_inventory, d.update, d['symbols'][0].update, digest, inventory, len, mapped.append, mutate, path.parent.mkdir, path.read_bytes, path.write_text, r['commands'][0].update, range, self.assertEqual, self.assertRaises, self.folder.cleanup, tempfile.TemporaryDirectory, validate_case_map, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:1`; AST `6184a2032b56c32bf51282be3686cabe97e797ec6fc84840ef4601576e7503a2`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[1]::Import

Source: `infra/tests/test_verus_evidence.py:2`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_verus_evidence.py:3`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[3]::Import

Source: `infra/tests/test_verus_evidence.py:4`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[4]::Import

Source: `infra/tests/test_verus_evidence.py:5`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_verus_evidence.py:7`; AST `8f134c69cfbdf3492eed71a176562b2ed576ffcc2cd5b08c09d4964542974fc0`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_verus_evidence.py:8`; AST `9f02857a9c61d8890803cea3397fe998cffd9d0faccb6ab5eeeecd60fe63aedd`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[7]::Assign

Source: `infra/tests/test_verus_evidence.py:10`; AST `58b1fa850a73021317c758b5de76d373c9829cc8c76b838519ad5631215a3b76`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: ENTRY.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::root.body[8]::Assign

Source: `infra/tests/test_verus_evidence.py:11`; AST `4c23d7d52ae33f6aa9516c69be6fc0fbf2381a5d334ae93d07d3635cfa3e3a05`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: VIR.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::root.body[9]::ClassDef

Source: `infra/tests/test_verus_evidence.py:19`; AST `2e058bf19d2fae5d9a01692cc16ca70308d44ccef0503dc2b0bb5e51d9e3d088`.

Rust module: `infra::tests::test_verus_evidence`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ENTRY, Path, VIR, ValueError, assertion, authority, case, cases, catalog, changed, copy, current_inventory, d, digest, fixture, i, identity, inventory, j, len, mapped, mutate, mutation, path, r, range, self, source, source_inventory, tempfile, test, text, unittest, validate_case_map, validate_symbol_mapping, value. Outputs/bindings: assertion, authority, case, cases, catalog, changed, d, fixture, i, identity, j, mapped, mutate, mutation, path, r, source, source_inventory, test, text, value.
Calls/effect boundaries: (self.root / self.artifact).write_text, Path, VIR.replace, VIR.split, cases.append, catalog.append, changed['cases'].pop, copy.deepcopy, current_inventory, d.update, d['symbols'][0].update, digest, inventory, len, mapped.append, mutate, path.parent.mkdir, path.read_bytes, path.write_text, r['commands'][0].update, range, self.assertEqual, self.assertRaises, self.folder.cleanup, tempfile.TemporaryDirectory, validate_case_map, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:20`; AST `4311879a17152da4464c9b7d7c1af9a4224aaeecaf138796c7449a205ac166a5`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ENTRY, Path, VIR, digest, inventory, path, self, tempfile. Outputs/bindings: path.
Calls/effect boundaries: Path, digest, inventory, path.parent.mkdir, path.read_bytes, path.write_text, tempfile.TemporaryDirectory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:21`; AST `842cb76111d3fc4776fbf8a802356afece653fa146934c086c1e55f7fbf1ae05`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:21`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[1]::Assign

Source: `infra/tests/test_verus_evidence.py:22`; AST `7d7064ca3c71a0b57e7723eec007d067294b6f1681100e18c4ce19a62e83ce4d`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[1].value::Call

Source: `infra/tests/test_verus_evidence.py:22`; AST `133344c2ee300ff0e5f3f8ab91558a23ae3aa67f6daf249fba4c7e7d034b7dcc`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[2]::Assign

Source: `infra/tests/test_verus_evidence.py:23`; AST `ef688fac36180c63fb02bd07a570da8e8fea8e34e51fd3082d5f3bd0b6fb165e`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[3]::Assign

Source: `infra/tests/test_verus_evidence.py:24`; AST `c89e6c4b32f5dd12c4523a3ef5833211a40f3152bbeb0ab54906d1d334292107`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[4]::Expr

Source: `infra/tests/test_verus_evidence.py:24`; AST `4a02dacfcdc4bdb0f5e882cce3190753b897fe61bcc8e2b13d0ac08a1dbc7824`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[4].value::Call

Source: `infra/tests/test_verus_evidence.py:24`; AST `994840cf9a86a7ba49bb09b92b22661abceaeff09aca1fbcfc473e1e6303e386`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[5]::Expr

Source: `infra/tests/test_verus_evidence.py:24`; AST `0c1a7ac4b2ec8ddf0de46ee63b093a63cf3f63995e9ed6851c3837b529835355`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: VIR, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[5].value::Call

Source: `infra/tests/test_verus_evidence.py:24`; AST `639b8b7e9d5c5efbed42bf3906fa2a2d758bad2b0303da2179459699adee0713`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[6]::Assign

Source: `infra/tests/test_verus_evidence.py:25`; AST `cc01b50d08ab8e7474a037a52ec3db49a52b6e676b598d8bbac5ca7c7e4efc8b`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENTRY, VIR, inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[6].value::Call

Source: `infra/tests/test_verus_evidence.py:25`; AST `fdb843d779b6c2ad2545b4d3daf82c3dcff4f68e954b3b7b01951b93a4430bca`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENTRY, VIR, inventory. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[7]::Assign

Source: `infra/tests/test_verus_evidence.py:26`; AST `91361fe7f2541ec67653ee96ff783802ef8c54cad47a84c741850aa529f883ae`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENTRY, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[8]::Assign

Source: `infra/tests/test_verus_evidence.py:27`; AST `91b8e37e6cf520a71ebb24dce67eb228fd6105fbf9555e0e902240b2f712eda1`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENTRY, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[9]::Assign

Source: `infra/tests/test_verus_evidence.py:30`; AST `a7e484f12d3b57a9262a238374c5a7cbc34cdcc960847d6f1d42e6631e85c51e`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, path, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[9].value.values[6].values[2]::Call

Source: `infra/tests/test_verus_evidence.py:33`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[9].value.values[6].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[9].value.values[6].values[2].args[0]::Call

Source: `infra/tests/test_verus_evidence.py:33`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[9].value.values[6].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::setUp::root.body[9].body[0].body[10]::Assign

Source: `infra/tests/test_verus_evidence.py:34`; AST `9749fd115fd38c9a3659e1674e487ecc63b0e3fe1e56bb259d6990e54d3cb3fc`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENTRY, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::tearDown::root.body[9].body[1]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:38`; AST `46b0595e8b7d0b509e3591fc82fa0db355591724994a30f219704a20bf6411fb`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.folder.cleanup.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::tearDown::root.body[9].body[1].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:38`; AST `31603c34a774bef20eee9112ff5d870dd963bf23481a0585813b9974e33fbb0d`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.folder.cleanup.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::tearDown::root.body[9].body[1].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:38`; AST `4c342ce1a49d647203c7e2424242b5cdf1c92882e0f16441d897d6723a3b680d`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.folder.cleanup.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:40`; AST `35cb0f8a2b06b7e0cb5fdc2cd679a851db6beaa4205e67bacb0005f4c205b493`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: current_inventory, self, validate_symbol_mapping, value. Outputs/bindings: value.
Calls/effect boundaries: current_inventory, self.assertEqual, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:41`; AST `66cb63c3e2c862b28fc2bc39c74411d4f3cb637a71f169f6467b55f5aaf8d80c`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_inventory, self. Outputs/bindings: value.
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:41`; AST `f16e03d15737a455899a9cf5d374d28a6cbfa3bf7e943604f72a0def61928cc3`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[1]::Expr

Source: `infra/tests/test_verus_evidence.py:42`; AST `218757c0dc7f074f86d1f7155125dab42a97d60ec0f9fc13e35fcc087bed5462`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, validate_symbol_mapping, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[1].value::Call

Source: `infra/tests/test_verus_evidence.py:42`; AST `57ef9319885c67b3a389edba8bba51c35186e209067fd065efa8cd99675638ea`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, validate_symbol_mapping, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[1].value.args[0]::Call

Source: `infra/tests/test_verus_evidence.py:42`; AST `9f923196ba4d0b60e9f1adcbffd5bc58eddd987ffc79622c687faac4ef40cc59`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, validate_symbol_mapping, value. Outputs/bindings: (none).
Calls/effect boundaries: validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[2]::Expr

Source: `infra/tests/test_verus_evidence.py:43`; AST `5b6c144b2b80cab02634512b86d82471ba538cac941001f2225c1fc96c1c4814`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_real_body_is_not_confused_with_a_nested_body_none::root.body[9].body[2].body[2].value::Call

Source: `infra/tests/test_verus_evidence.py:43`; AST `24cbac1ccd2288ecd53e577bccce71b559af034304afa8d4b6025af1dbc43b35`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:45`; AST `89aa5792733342bf715578a276fb9ebdddeee9e75bcca385bd92c7e1b0688143`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, copy, d, mutate, self, validate_symbol_mapping. Outputs/bindings: d, mutate.
Calls/effect boundaries: copy.deepcopy, d.update, d['symbols'][0].update, mutate, self.assertRaises, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0]::For

Source: `infra/tests/test_verus_evidence.py:46`; AST `caab9b24c21146c01d93aa2072d0b79e5da38a8925078c73083811f578af8d1e`.

Rust module: `infra::tests::test_verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, copy, d, mutate, self, validate_symbol_mapping. Outputs/bindings: d, mutate.
Calls/effect boundaries: copy.deepcopy, d.update, d['symbols'][0].update, mutate, self.assertRaises, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[9].body[3].body[0]; no call, error or mutation may be omitted. Iteration: mutate in (lambda d: d.update(symbols=[]), lambda d: d['symbols'][0].update(symbol='example::unrelated'), lambda d: d['symbols'][0].update(obligations=[]), lambda d: d['symbols'][0].update(review=''))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[0]::Lambda

Source: `infra/tests/test_verus_evidence.py:47`; AST `198efbb387533afe26a3bc498f2fe79e98342f47e628687c7e693e9e841dbb4b`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d.update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[3].body[0].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[0].body::Call

Source: `infra/tests/test_verus_evidence.py:47`; AST `ac3c33c8742575965afdc4f4d5d020be6e001c0a5b9e1cdbeb8c898c5efa7445`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d.update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].iter.elts[0].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[1]::Lambda

Source: `infra/tests/test_verus_evidence.py:48`; AST `47dbccf28097c86db1f5428b6fbae6581cfb54b64e1f5405f5db80de4f927d92`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d['symbols'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[3].body[0].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[1].body::Call

Source: `infra/tests/test_verus_evidence.py:48`; AST `9a496a875492b9e3fa03c0084ad278a53d15ab5cd932e45e7d657027a2c98fe0`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d['symbols'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].iter.elts[1].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[2]::Lambda

Source: `infra/tests/test_verus_evidence.py:49`; AST `59a1a0baad22a0f78021044ddd5f721d05c40ecd9a0e3f6e91f21ac8fbc923d1`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d['symbols'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[3].body[0].iter.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[2].body::Call

Source: `infra/tests/test_verus_evidence.py:49`; AST `74dc28458acb1bfe365c289090d48034a3d36ac86eb5b9c56cb492f56b9853de`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d['symbols'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].iter.elts[2].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[3]::Lambda

Source: `infra/tests/test_verus_evidence.py:50`; AST `86a677fb409232ec1d4a61dbab9b1a747c1d6f5fe13da825d63d6291b7d1bdd2`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d['symbols'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[3].body[0].iter.elts[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].iter.elts[3].body::Call

Source: `infra/tests/test_verus_evidence.py:50`; AST `a9e4c7e8e7435a55e5ce1b680dc38cef11ff2cdd226c724998d18f78c2559533`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d. Outputs/bindings: (none).
Calls/effect boundaries: d['symbols'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].iter.elts[3].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:52`; AST `e98a87b46386598e45f636ef22abc9dda96e4a17de66d41f82e795336abd805a`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: d.
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:52`; AST `4662fe4c3760a1e0583ec3c3f488446dac339d07cef0f3761ff30c6f252e0506`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[1]::Expr

Source: `infra/tests/test_verus_evidence.py:52`; AST `aa3432802ae858126543eadfcb6181005fce1d26c91bd0c3aba2b07616e718d8`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: d, mutate. Outputs/bindings: (none).
Calls/effect boundaries: mutate.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[1].value::Call

Source: `infra/tests/test_verus_evidence.py:52`; AST `295013e3864fb9bd4a6442a71ae3fdbe20832c4aadfa3af5593c7a24d87562ec`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d, mutate. Outputs/bindings: (none).
Calls/effect boundaries: mutate.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[2]::With

Source: `infra/tests/test_verus_evidence.py:53`; AST `58774f1a83ce200eae22aec737a6d339bd1a7ab0881a12e8a518ba42c8cfb252`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, d, self, validate_symbol_mapping. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[2].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:53`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[2].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:53`; AST `12f0429c4e1008fa475c5f34b67b27ca97b27853ee0a68027acf5312b3508a19`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: d, self, validate_symbol_mapping. Outputs/bindings: (none).
Calls/effect boundaries: validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected::root.body[9].body[3].body[0].body[2].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:53`; AST `cc16d005ce9385a9b738df2f729c856519ef3ad435a7742aa7edc2996ecf9648`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d, self, validate_symbol_mapping. Outputs/bindings: (none).
Calls/effect boundaries: validate_symbol_mapping.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:55`; AST `85929ab4de0aa7c7e0ebeda04f0ed262a2698eea3f288c005771628bafa6c057`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, copy, current_inventory, mutate, r, self. Outputs/bindings: mutate, r.
Calls/effect boundaries: copy.deepcopy, current_inventory, mutate, r['commands'][0].update, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0]::For

Source: `infra/tests/test_verus_evidence.py:56`; AST `43c104cfb98de5f309e70ef9c2ff40b4a8d3d88a5fcc3270f3db01f157108c05`.

Rust module: `infra::tests::test_verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, copy, current_inventory, mutate, r, self. Outputs/bindings: mutate, r.
Calls/effect boundaries: copy.deepcopy, current_inventory, mutate, r['commands'][0].update, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[9].body[4].body[0]; no call, error or mutation may be omitted. Iteration: mutate in (lambda r: r['commands'][0].update(stdout='verification results:: 0 verified, 0 errors\n'), lambda r: r['commands'][0].update(stdout='verification results:: 2 verified, 0 errors\n'), lambda r: r['commands'][0].update(returncode=1), lambda r: r['commands'][0].update(stdout='verification results:: 1 verified, 1 errors\n'), lambda r: r['commands'][0].update(stdout_truncated=True), lambda r: r['commands'][0].update(timed_out=True))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[0]::Lambda

Source: `infra/tests/test_verus_evidence.py:57`; AST `a164f22627f568001230fb5ff4e5a7082fc659f2f205eec19a6bb179449a38b2`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[4].body[0].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[0].body::Call

Source: `infra/tests/test_verus_evidence.py:57`; AST `c9f23f8f3936bdc18fc0260434ae7af6ed13b273a9e61a38227c9c4467798314`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].iter.elts[0].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[1]::Lambda

Source: `infra/tests/test_verus_evidence.py:58`; AST `9ace85f5d4a25ee5ed0f534231ef09dd84b860edcfbbcb1aa5c0d01f05c2b1aa`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[4].body[0].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[1].body::Call

Source: `infra/tests/test_verus_evidence.py:58`; AST `05acea88cad13f6d2947b17e806b4d2ec285ef86b9b522e980e66f90e7f92f7d`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].iter.elts[1].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[2]::Lambda

Source: `infra/tests/test_verus_evidence.py:59`; AST `ecb24cb0a20eca22854d507b45f2467952bd9dfeea4a4283a348ba8c261d4c3b`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[4].body[0].iter.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[2].body::Call

Source: `infra/tests/test_verus_evidence.py:59`; AST `96548c9798f258363aa2caf47b986758583ebf9c7a8e866f2ed483a722448f8d`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].iter.elts[2].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[3]::Lambda

Source: `infra/tests/test_verus_evidence.py:60`; AST `faca8dcb4afae125f5367b48ff10e6782613fb95b38ffe13f8be978f0c5fc69e`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[4].body[0].iter.elts[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[3].body::Call

Source: `infra/tests/test_verus_evidence.py:60`; AST `d8f731bd53571a0ba61f53525e36b106c1a1186674121e118cde247ca0a8f641`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].iter.elts[3].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[4]::Lambda

Source: `infra/tests/test_verus_evidence.py:61`; AST `0f2699a2adfec8a5fd7fea89a2c09524d2f0510c69a68a29265ff7136a9061f1`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[4].body[0].iter.elts[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[4].body::Call

Source: `infra/tests/test_verus_evidence.py:61`; AST `476e669d4a6b6c9333a17b5fcdde189e4c4b33c0696c5052b641b3091165edd9`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].iter.elts[4].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[5]::Lambda

Source: `infra/tests/test_verus_evidence.py:62`; AST `1ad23cd27538da41216adc5714b943a30bc9053f595a10370cab98e989f96f39`.

Rust module: `infra::tests::test_verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Lambda evaluation at root.body[9].body[4].body[0].iter.elts[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].iter.elts[5].body::Call

Source: `infra/tests/test_verus_evidence.py:62`; AST `863e51f66fdf7d7c193b3f359181659f998fbc6aa162cbb7925ad93052e3eb43`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['commands'][0].update.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].iter.elts[5].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:64`; AST `2e5a8f4baa799588d40ad7b2022a25cc3f70124ff906401a8173cec53e9dd206`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: r.
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:64`; AST `636419298943f19a8c47842cd6b823a6cb5c33d15c16259dcbace14d16cca9d7`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[1]::Expr

Source: `infra/tests/test_verus_evidence.py:64`; AST `fdcb74e075205071e572dbc1ce685df2335bbab59fbcfd03f6e396f8e48e9766`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mutate, r. Outputs/bindings: (none).
Calls/effect boundaries: mutate.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[1].value::Call

Source: `infra/tests/test_verus_evidence.py:64`; AST `148e2b1de478839b06a2e4c6f41289ee2ca3b4508752dc73c68db12246d46dbd`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mutate, r. Outputs/bindings: (none).
Calls/effect boundaries: mutate.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[2]::With

Source: `infra/tests/test_verus_evidence.py:65`; AST `8337bcdfe5b5ea068288c0fac18c3dacf12fda9870b6190b3c5d43ed6c66521a`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, current_inventory, r, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[2].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:65`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[2].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:65`; AST `b9ac39e8628f6a1985d9cdae4ef5988b7d24520235977de539eb9a087f1b6d4e`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_inventory, r, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected::root.body[9].body[4].body[0].body[2].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:65`; AST `0aa9c450455de2bcf099a64bff092be0118c63f9dab05c2785a0ca515b40079c`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_inventory, r, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:67`; AST `24208dd49b9b62973a54a57953ef0fe306b65ec747eef3133fc57eab9977fe65`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ENTRY, VIR, ValueError, copy, current_inventory, inventory, r, self. Outputs/bindings: r.
Calls/effect boundaries: (self.root / self.artifact).write_text, VIR.replace, VIR.split, copy.deepcopy, current_inventory, inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:68`; AST `2e5a8f4baa799588d40ad7b2022a25cc3f70124ff906401a8173cec53e9dd206`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: r.
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:68`; AST `636419298943f19a8c47842cd6b823a6cb5c33d15c16259dcbace14d16cca9d7`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[1]::Assign

Source: `infra/tests/test_verus_evidence.py:68`; AST `6a4db732f1333ec4c962ebb387a109240b398a317d61b76eeef0590869b3ecc1`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[2]::With

Source: `infra/tests/test_verus_evidence.py:69`; AST `8337bcdfe5b5ea068288c0fac18c3dacf12fda9870b6190b3c5d43ed6c66521a`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, current_inventory, r, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[2].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:69`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[2].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:69`; AST `b9ac39e8628f6a1985d9cdae4ef5988b7d24520235977de539eb9a087f1b6d4e`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_inventory, r, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:69`; AST `0aa9c450455de2bcf099a64bff092be0118c63f9dab05c2785a0ca515b40079c`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_inventory, r, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[3]::Expr

Source: `infra/tests/test_verus_evidence.py:70`; AST `231895e873c7fd84068c9973788c407d7b2f451e6b0db0a7522699bce41be2f7`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: VIR, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / self.artifact).write_text, VIR.replace.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[3].value::Call

Source: `infra/tests/test_verus_evidence.py:70`; AST `16d4aa7354d5bcae4ca29c798fbe01be07e2bed183b60dc88da424e072011d14`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / self.artifact).write_text, VIR.replace.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[3].value.args[0]::Call

Source: `infra/tests/test_verus_evidence.py:70`; AST `f517ec3e0d6af231d87ce700fdf85bb97c01bdbcc63df4c644303fb1d92b9632`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR. Outputs/bindings: (none).
Calls/effect boundaries: VIR.replace.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[4]::With

Source: `infra/tests/test_verus_evidence.py:71`; AST `79b69e67ac804059756b77fdfcdb5f66ef696f56d13ace9e699b1c179aadff7c`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, current_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[4].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:71`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[4].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:71`; AST `0a495700e43d53ffc61855206fe6e93df1dbe45a04160e08ae78f1282c894fa0`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[4].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:71`; AST `f16e03d15737a455899a9cf5d374d28a6cbfa3bf7e943604f72a0def61928cc3`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: current_inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[5]::With

Source: `infra/tests/test_verus_evidence.py:72`; AST `4851ed4b64549fc52efc64f53fb9803dd8520702b400cb9166f730886fac2ad0`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ENTRY, VIR, ValueError, inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: VIR.split, inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[5].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:72`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[5].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:72`; AST `020eb21d36720ecd0780818f1a67d8fa2b111b305573d1ef6cc00f6987796992`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENTRY, VIR, inventory. Outputs/bindings: (none).
Calls/effect boundaries: VIR.split, inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[5].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:72`; AST `6b531ee30a441ca33ec30b9dc60c719a4549a304e80775206872d9e2c4878c0a`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENTRY, VIR, inventory. Outputs/bindings: (none).
Calls/effect boundaries: VIR.split, inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_missing_changed_or_incomplete_inventory_is_rejected::root.body[9].body[5].body[5].body[0].value.args[0].value::Call

Source: `infra/tests/test_verus_evidence.py:72`; AST `48b5eeeecc4a947d4d6464a4af40cff0ca5b44337bafd9010fce2b5620aaa382`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR. Outputs/bindings: (none).
Calls/effect boundaries: VIR.split.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[5].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:74`; AST `93b44ea82fcccfd44e2354928814551a28c9441c8c6b5005879f4f5b940f7dfa`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ENTRY, VIR, ValueError, inventory, self, text. Outputs/bindings: text.
Calls/effect boundaries: VIR.replace, inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0]::For

Source: `infra/tests/test_verus_evidence.py:75`; AST `f0a4c615ed4188010e6cb24258b32c3b66f6aad06c4c42864564f5f01f6c4782`.

Rust module: `infra::tests::test_verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ENTRY, VIR, ValueError, inventory, self, text. Outputs/bindings: text.
Calls/effect boundaries: VIR.replace, inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[9].body[6].body[0]; no call, error or mutation may be omitted. Iteration: text in (VIR.replace('example::transition', 'other::transition'), VIR.replace(':is_external_body false', ':is_external_body true'), VIR.replace(':exec_assume_termination false', ':exec_assume_termination true'))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].iter.elts[0]::Call

Source: `infra/tests/test_verus_evidence.py:75`; AST `cbd36f1bacaf3a5e2f2e49e4612295134a7fec2c6708da807b8e59e7d094f0a2`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR. Outputs/bindings: (none).
Calls/effect boundaries: VIR.replace.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[0].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].iter.elts[1]::Call

Source: `infra/tests/test_verus_evidence.py:76`; AST `fefd979044caa0b294d6c7bbeaa63d4f70aa008d3b807675ac9162c2eeb66cfe`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR. Outputs/bindings: (none).
Calls/effect boundaries: VIR.replace.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[0].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].iter.elts[2]::Call

Source: `infra/tests/test_verus_evidence.py:77`; AST `a63d535b4c32b360d4ce14e94b667caf8e60987ccb8ecc86385309893e9d39de`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: VIR. Outputs/bindings: (none).
Calls/effect boundaries: VIR.replace.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[0].iter.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].body[0]::With

Source: `infra/tests/test_verus_evidence.py:78`; AST `d21701b1b35e9e79a2fa2da87996b051b338862b9d17264eda5a430ae0514a68`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ENTRY, ValueError, inventory, self, text. Outputs/bindings: (none).
Calls/effect boundaries: inventory, self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:78`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:78`; AST `e286de07f23d4d76ac03aa434aa16e20e896f44d0684dd48bb3310a69e081aa1`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENTRY, inventory, text. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_empty_external_and_unchecked_behavior_are_rejected::root.body[9].body[6].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:78`; AST `5fe7525f5989ab5538b009f229777cc10d86f34e32e017ec6ab9079c031e6d0e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENTRY, inventory, text. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7]::FunctionDef

Source: `infra/tests/test_verus_evidence.py:80`; AST `a3b526aa6472413dec3f9b0fbc6eb41aaf231ca19edee9c5de41ea2ac07a50bc`.

Rust module: `infra::tests::test_verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, assertion, authority, case, cases, catalog, changed, copy, fixture, i, identity, j, len, mapped, mutation, range, self, source, source_inventory, test, validate_case_map, value. Outputs/bindings: assertion, authority, case, cases, catalog, changed, fixture, i, identity, j, mapped, mutation, source, source_inventory, test, value.
Calls/effect boundaries: cases.append, catalog.append, changed['cases'].pop, copy.deepcopy, len, mapped.append, range, self.assertEqual, self.assertRaises, validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:81`; AST `6f036968440c35527205b934142c19b9a41999c7a4599f62cd05d5fd9e310b87`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: catalog.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[1]::Assign

Source: `infra/tests/test_verus_evidence.py:81`; AST `94b78388342bce9ce07ab9a0596bccbbeba71dfca30933684a6682ceab121dc3`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: cases.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[2]::Assign

Source: `infra/tests/test_verus_evidence.py:81`; AST `9ec61ee080ae6d2658bdb58b2fd0d03676909946b623364eb10adf6888278ba1`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: mapped.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3]::For

Source: `infra/tests/test_verus_evidence.py:82`; AST `2f6e59e72793b00d880c39d582b0bb0eb237224b1407262f4e64baeda52a49fe`.

Rust module: `infra::tests::test_verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: assertion, authority, case, cases, catalog, fixture, i, identity, j, mapped, range, source, test. Outputs/bindings: assertion, authority, case, fixture, i, identity, j, source, test.
Calls/effect boundaries: cases.append, catalog.append, mapped.append, range.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[9].body[7].body[3]; no call, error or mutation may be omitted. Iteration: i in range(531)
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].iter::Call

Source: `infra/tests/test_verus_evidence.py:82`; AST `ed5ee0a33fb2dd117f818e3f269b8441c5246ad5b10f20ceca18a0bae7450102`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:83`; AST `ef2dedbcc22178d6c5bb6cf24fccf3541a9dc9f67132cbccbd072958e74564ea`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: i. Outputs/bindings: j.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[1]::Assign

Source: `infra/tests/test_verus_evidence.py:84`; AST `2552f88fbecdb8e2543bf9e357754d4a68cae877cad6848a7ab338ecca142931`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: j. Outputs/bindings: source.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[2]::Assign

Source: `infra/tests/test_verus_evidence.py:84`; AST `926ebf2a7bf9f519fd9928e50b27f31dc11a70921b7b46bb21aa9c6b2b096651`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: j. Outputs/bindings: test.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[3]::Assign

Source: `infra/tests/test_verus_evidence.py:84`; AST `53c00e3634a14fb37e923afbee0894f6389dca0e117177b5bc66f9150192bb64`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: i. Outputs/bindings: fixture.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[4]::Assign

Source: `infra/tests/test_verus_evidence.py:85`; AST `33a71bd8fb62b3f759a7bbf06516423744be67f1e64443fcd46d3f98b546ba0c`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, source, test. Outputs/bindings: identity.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[5]::Assign

Source: `infra/tests/test_verus_evidence.py:86`; AST `13f028fd4680d64614d69ccde449e6237901fdb8e2085804f36786ea46e5dfcc`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: j, source. Outputs/bindings: assertion.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[6]::Assign

Source: `infra/tests/test_verus_evidence.py:87`; AST `1931121096fc88e177f112205fe0300f040daac369d01d4b62dacb587fd52269`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, source, test. Outputs/bindings: authority.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[7]::Expr

Source: `infra/tests/test_verus_evidence.py:88`; AST `1618086714f0781154c2bd072b8d5b1c265e59bf8c8121a1a4dea82579d5863f`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority, catalog. Outputs/bindings: (none).
Calls/effect boundaries: catalog.append.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[7].value::Call

Source: `infra/tests/test_verus_evidence.py:88`; AST `09ca9d77a71144068861a869ceca38e538c85c83ab71e05e757a19821cb82b17`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority, catalog. Outputs/bindings: (none).
Calls/effect boundaries: catalog.append.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[8]::Assign

Source: `infra/tests/test_verus_evidence.py:89`; AST `7ac344d128b3cbddfc5554940b2e77444bc4de41119645965d41ab161a8df3a6`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertion, authority. Outputs/bindings: case.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[9]::Expr

Source: `infra/tests/test_verus_evidence.py:90`; AST `e2040b5b2dcb8924b3407deefd12812f5db9e7a940a417ae607036ff839a598c`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: case, cases. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[9].value::Call

Source: `infra/tests/test_verus_evidence.py:90`; AST `9b22d69fca9466a69779e5016d3c94cab0c842ee8b8f9076a2491f8d1ad1e0a7`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: case, cases. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[10]::Expr

Source: `infra/tests/test_verus_evidence.py:91`; AST `b56baa54a9260f538f58d90e94a700749608a4b78cc3b90bc3ab60cff4de9ae4`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertion, case, mapped. Outputs/bindings: (none).
Calls/effect boundaries: mapped.append.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[3].body[10].value::Call

Source: `infra/tests/test_verus_evidence.py:91`; AST `dcadaddf1f220e9ff05de9526a3a6e8996b79078c6c13ab2ff7027e01dc60824`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion, case, mapped. Outputs/bindings: (none).
Calls/effect boundaries: mapped.append.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[3].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[4]::Assign

Source: `infra/tests/test_verus_evidence.py:95`; AST `af036f3772fd82f61c535f605b5aa3f3fbd515f88a2ee7eb0a2f8b86b1d70c90`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases. Outputs/bindings: source_inventory.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[5]::Assign

Source: `infra/tests/test_verus_evidence.py:96`; AST `7933ba0c7ceb564a293211198930b253a6cfdbef573957817910992bc402a1d5`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mapped. Outputs/bindings: value.
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[6]::Expr

Source: `infra/tests/test_verus_evidence.py:97`; AST `9b779e1a40047b3c37f6a70d36d16d031e5f4de45d08dc657e566afb5cc78165`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: catalog, len, self, source_inventory, validate_case_map, value. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual, validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[6].value::Call

Source: `infra/tests/test_verus_evidence.py:97`; AST `a4f61aa764241837949edc71d6e1f0ffb524e50c714a3918cb75a7122bb93f9e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, len, self, source_inventory, validate_case_map, value. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual, validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[6].value.args[0]::Call

Source: `infra/tests/test_verus_evidence.py:97`; AST `1996983243cd91e92a66e1fb6e598a97ad32503747a2b7ec65f6c63e9d580c93`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, len, source_inventory, validate_case_map, value. Outputs/bindings: (none).
Calls/effect boundaries: len, validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[6].value.args[0].args[0]::Call

Source: `infra/tests/test_verus_evidence.py:97`; AST `0e773188488b95a0831a4757b6c7c7de63493083e3986e9e2305f1b76d779b1c`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, source_inventory, validate_case_map, value. Outputs/bindings: (none).
Calls/effect boundaries: validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7]::For

Source: `infra/tests/test_verus_evidence.py:98`; AST `d11244f3d0fefb8fc23924aeddbd324e6a6445e428ce470f7604c81905ddd84b`.

Rust module: `infra::tests::test_verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, catalog, changed, copy, mutation, self, source_inventory, validate_case_map, value. Outputs/bindings: changed, mutation.
Calls/effect boundaries: changed['cases'].pop, copy.deepcopy, self.assertRaises, validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[9].body[7].body[7]; no call, error or mutation may be omitted. Iteration: mutation in ('omitted', 'assertion', 'ambiguous')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:99`; AST `7391d52290a25b45a2d20f4ab1590cad477164512bf2d6ac7cfeb4674e5afccb`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, value. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:99`; AST `782ae569ff5398c7ef42f0803d70989146bababd0ccf924077bb11c332dbb668`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, value. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[1]::If

Source: `infra/tests/test_verus_evidence.py:100`; AST `28f3b95eae279ce278ebfae6d50c2d8cb44dcb25ad21fd35cc450a43f5c832ef`.

Rust module: `infra::tests::test_verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: changed, mutation. Outputs/bindings: (none).
Calls/effect boundaries: changed['cases'].pop.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[9].body[7].body[7].body[1]; no call, error or mutation may be omitted. Condition: mutation == 'omitted'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[1].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:100`; AST `a0671b056fea0f115beef9d959b27fc2e3cfbf365e3780b3a4bab7a69a5ed2a6`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed['cases'].pop.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[1].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:100`; AST `e0b1d51e8c786edbef818aa29e73097265dba844cf48b26c19abb79f94853793`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed['cases'].pop.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[7].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[1].orelse[0]::If

Source: `infra/tests/test_verus_evidence.py:101`; AST `ef78efa394749bf5727b127bfeb94ea9b7cfcc74304239bc1668747491a7e783`.

Rust module: `infra::tests::test_verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: changed, mutation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[9].body[7].body[7].body[1].orelse[0]; no call, error or mutation may be omitted. Condition: mutation == 'assertion'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[1].orelse[0].body[0]::Assign

Source: `infra/tests/test_verus_evidence.py:101`; AST `fd17d5a896a1237aaad02004bb39f191c8e8fe8dcd9c5c666f14defdc809020a`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[7].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[1].orelse[0].orelse[0]::Assign

Source: `infra/tests/test_verus_evidence.py:102`; AST `b3f9c97eeb5fe8fb0c557b768ded493af98884677d714692cba6fbde22a3d2c6`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[7].body[7].body[1].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[2]::With

Source: `infra/tests/test_verus_evidence.py:103`; AST `f18212245f9f52282c49d1cfc11b28afbaba0a26653f0da9ed3cc20d198f2714`.

Rust module: `infra::tests::test_verus_evidence`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, catalog, changed, self, source_inventory, validate_case_map. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[9].body[7].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[2].items[0].context_expr::Call

Source: `infra/tests/test_verus_evidence.py:103`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[7].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[2].body[0]::Expr

Source: `infra/tests/test_verus_evidence.py:103`; AST `3e2aca1331e5e2f7b3e287a871fcaa86e6a296c30919de8579dae495bfd3ffb2`.

Rust module: `infra::tests::test_verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: catalog, changed, source_inventory, validate_case_map. Outputs/bindings: (none).
Calls/effect boundaries: validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[7].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_verus_evidence.py::module::VerusInventoryTests::test_qualified_catalog_join_rejects_omitted_case_and_assertion::root.body[9].body[7].body[7].body[2].body[0].value::Call

Source: `infra/tests/test_verus_evidence.py:103`; AST `d0139e08863f7e3168e65f4bf20a39c580e3964cc31e48b8c70d63305788a4dc`.

Rust module: `infra::tests::test_verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, changed, source_inventory, validate_case_map. Outputs/bindings: (none).
Calls/effect boundaries: validate_case_map.
Dependencies: agentinfra.destiny_reuse, agentinfra.verus_evidence, copy, pathlib, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].body[7].body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
