# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 207. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_formal_workflow.py::module::root::Module

Source: `infra/tests/test_formal_workflow.py:1`; AST `f7bf468e2679513d5b6a89d56d550d63075c83f498b39249051570f0738f1e1d`.

Rust module: `infra::tests::test_formal_workflow`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: DestinyFixture, FRAMEWORK, Path, __name__, copy, denied, exhausted, extra, first, hashlib, invalid, json, obligations, original, os, output, patch, path, result, second, self, solver, str, super, sys, tool, unittest, version. Outputs/bindings: denied, exhausted, first, invalid, obligations, original, path, result, second, solver, tool.
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes, (self.root / '.aegis/destiny/receipts').exists, Path, Path(tool).read_text, Path(tool).write_text, copy.deepcopy, hashlib.sha256, hashlib.sha256((FRAMEWORK / 'contracts/destiny.json').read_bytes()).hexdigest, json.dumps, patch.dict, path.chmod, path.write_text, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertTrue, self.bind, self.call, self.save, self.skipTest, self.verifier, self.write, solver.write_text, str, super, super().setUp, unittest.main.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:1`; AST `ffe0a8c5749af495d01186eccc102dedd2e54a693bd8033ad8c578a79827572a`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[1]::Import

Source: `infra/tests/test_formal_workflow.py:2`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[2]::Import

Source: `infra/tests/test_formal_workflow.py:3`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[3]::Import

Source: `infra/tests/test_formal_workflow.py:4`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[4]::Import

Source: `infra/tests/test_formal_workflow.py:5`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_formal_workflow.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[6]::Import

Source: `infra/tests/test_formal_workflow.py:7`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[7]::Import

Source: `infra/tests/test_formal_workflow.py:8`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_formal_workflow.py:9`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_formal_workflow.py:11`; AST `ca1bdbb4eee459c2ccd55d68d33269bd628fba273ebc41a0012f627f106ac974`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::root.body[10]::ClassDef

Source: `infra/tests/test_formal_workflow.py:14`; AST `7a6a2db24dac879df247721d226298123ba863313d6e0954b1ac1f67588e9655`.

Rust module: `infra::tests::test_formal_workflow`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: DestinyFixture, FRAMEWORK, Path, copy, denied, exhausted, extra, first, hashlib, invalid, json, obligations, original, os, output, patch, path, result, second, self, solver, str, super, sys, tool, version. Outputs/bindings: denied, exhausted, first, invalid, obligations, original, path, result, second, solver, tool.
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes, (self.root / '.aegis/destiny/receipts').exists, Path, Path(tool).read_text, Path(tool).write_text, copy.deepcopy, hashlib.sha256, hashlib.sha256((FRAMEWORK / 'contracts/destiny.json').read_bytes()).hexdigest, json.dumps, patch.dict, path.chmod, path.write_text, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertTrue, self.bind, self.call, self.save, self.skipTest, self.verifier, self.write, solver.write_text, str, super, super().setUp.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:15`; AST `bda1d8a4f7fed06e8d2c6e07a12eedf1a038db5934e8e459f5d9c668aae1211f`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FRAMEWORK, hashlib, self, super. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes, hashlib.sha256, hashlib.sha256((FRAMEWORK / 'contracts/destiny.json').read_bytes()).hexdigest, self.write, super, super().setUp.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:16`; AST `a3c53ff6d49abe054f55c7ea156ee15aff3d12bb15e930844a2f91a5b8f6b8d3`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().setUp.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:16`; AST `5cb5af0cb7fe67f5a156cbe98e294cb7eba50327997f668490e6d9b239c1310e`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().setUp.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[0].value.func.value::Call

Source: `infra/tests/test_formal_workflow.py:16`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:17`; AST `8199f0dc2038cbb88c35b5376b1f8702d77c95219c89a5713d0f8a6ab943e00a`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:17`; AST `411b12d0295e924f6659519f502b4d66ce104d1902bb950b73ffb58637eba75e`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[2]::Assign

Source: `infra/tests/test_formal_workflow.py:18`; AST `4d269a88c53f340611eb970d00768c779ae7a8c612702975d7c85402ac22815b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FRAMEWORK, hashlib, self. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes, hashlib.sha256, hashlib.sha256((FRAMEWORK / 'contracts/destiny.json').read_bytes()).hexdigest.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[2].value.values[2]::Call

Source: `infra/tests/test_formal_workflow.py:20`; AST `aa94dadbd28f5eaa1ade243852a486bcf76a63453372c2e9f60685382eb81bf9`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes, hashlib.sha256, hashlib.sha256((FRAMEWORK / 'contracts/destiny.json').read_bytes()).hexdigest.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[2].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[2].value.values[2].func.value::Call

Source: `infra/tests/test_formal_workflow.py:20`; AST `2c9109cae8cf766d3a058dc81b2ef40489e0541f38be3973d938eeeb4bae1dda`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes, hashlib.sha256.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[2].value.values[2].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::setUp::root.body[10].body[0].body[2].value.values[2].func.value.args[0]::Call

Source: `infra/tests/test_formal_workflow.py:20`; AST `9bc44f840006bcf61adea441fd7c7aa585d3d3dca20f9c7c707b7f6f996aee5d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK. Outputs/bindings: (none).
Calls/effect boundaries: (FRAMEWORK / 'contracts/destiny.json').read_bytes.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[2].value.values[2].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::save::root.body[10].body[1]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:31`; AST `ff4a117bb9b76cb227021ac92287191af0ce0349154595459f47bd11ba5192a5`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::save::root.body[10].body[1].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:32`; AST `6d0995d967293298a6149b570872e8135d5ac976ecc542899ad30cf37490a80b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::save::root.body[10].body[1].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:32`; AST `66fec05247b5da518809c8d3b81328b2fb9ee9ae1b0b92176c368aa22c9bbf39`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::save::root.body[10].body[1].body[0].value.args[1]::Call

Source: `infra/tests/test_formal_workflow.py:32`; AST `a83235b018d4212a2fa9ceb50b4119ba1097ab1e9c8fae0c5644f4f646e56f3a`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::bind::root.body[10].body[2]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:34`; AST `19e333661fc5246feb332e6ab60f51141a6ee4356f0293e7fc4ccce2748777a5`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call, self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::bind::root.body[10].body[2].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:35`; AST `5b63971998709a22375fdd3e0d8ad9a2a7b731c63b4788c3ca3f76acf191897c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::bind::root.body[10].body[2].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:35`; AST `ad5f9d68373e57cd4d8f52cc8ff964706876674212a70aaa0b55df190c2343ec`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::bind::root.body[10].body[2].body[1]::Return

Source: `infra/tests/test_formal_workflow.py:36`; AST `b0e5169e538d92992735f2ad94ea5464d5445a64d4676b099fe97be2d18affe8`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::bind::root.body[10].body[2].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:36`; AST `1ef33a92f4cc3a6c4830c2d6a924a0c73f43f6aca9151473c7fb343e7328de41`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:38`; AST `34a5a192e8cf024d5946b30b51c9c37484775ffa8905c1d27baea884dd4b99b3`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, extra, os, output, path, self, str, sys, version. Outputs/bindings: path.
Calls/effect boundaries: Path, path.chmod, path.write_text, self.skipTest, str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[0]::If

Source: `infra/tests/test_formal_workflow.py:39`; AST `3dbd1822ea898ef731b977f4f3feb032d1a47d4854fdebd75778d51b3f511c2c`.

Rust module: `infra::tests::test_formal_workflow`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: os, self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[10].body[3].body[0]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[0].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:40`; AST `d7b9e911c190d4bca0876787ddaf9dff88ce36006e5f8c21593a6f6432cba791`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:40`; AST `e3cd2715478e1ba9b6b9d9089562b42c8791c8a6801d76e6f68c71ce4264204f`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[1]::Assign

Source: `infra/tests/test_formal_workflow.py:41`; AST `00c510c19be7d46d26780244d9827ab2ac42cc70fb9d41c57639da15eeeb77d1`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: path.
Calls/effect boundaries: Path.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[1].value.left::Call

Source: `infra/tests/test_formal_workflow.py:41`; AST `350af0ef58dfeabf82fa371e4d1a0525efa6d4376cbcb9b8ead747bbdeb7de21`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:42`; AST `adce33386e95785919a1dff0d9779e45a6be25684675298e2b396cf336b756cc`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: extra, output, path, sys, version. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:42`; AST `076d6d3448d0ca86642a513a7026873557bd90d1323139681385f029d01dfa88`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: extra, output, path, sys, version. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:43`; AST `c1da955b8ef2a5b79b7afbd0650ecc12ddd2cf1b08bec4f3927d2f8059fbd901`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.chmod.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:43`; AST `aee9c39309c0e51c3a2e4b3f570d465e210261be4d23f8c8f12ffd40aba34ac1`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.chmod.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[4]::Return

Source: `infra/tests/test_formal_workflow.py:44`; AST `f4ac91e8a6d0817b930e2b772faed20d4c0d8fcb6c5bcd61d983a0cbec797177`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::verifier::root.body[10].body[3].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:44`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:46`; AST `34b1597fba307441273b3d0e4ff8964cddec2949f1abc3fb6712310171fd0cc1`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/receipts').exists, self.assertEqual, self.assertFalse, self.assertIn, self.bind, self.call, self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:47`; AST `48a31e2bc66141dc0a19a4375a9502689ed6828276687cff44688f7ca6e2c727`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:47`; AST `bdcd6a211c01fb91b3b3d2675c1dd7566925d22dca5845b21ff8f1fee25da148`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[0].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:47`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:48`; AST `8b3660aefe64250f5df0a41550d80ee5399915d93eee75243a35bda4ee10f2a9`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:48`; AST `84163c49eb28747ec85b10f14369795f2e08f7b2870baf9663d57db8ec287f00`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[1].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:48`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:49`; AST `d4788f040f1ece2f70ecaf176ccd14e9e0875244c259109a0320e4f57c8b878c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:49`; AST `df2d3aa7ee8ddacd0a9f370dfbeff91302bf99f7ae174c1bea5c2030c10c3fc4`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:50`; AST `fae720ca2894fe76b1e45388f4778fc732faa2409c8c50762e325f5d90eb1fa6`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:50`; AST `6e0754b973aec147ce2f76c9231461d996979a12836b9d1a9206e6c7dfe3f8d9`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[3].value.args[1].value::Call

Source: `infra/tests/test_formal_workflow.py:50`; AST `2fa2b7d1bb3693d93ff460ecbb7f7aeac679a2ee78e78b780c49c568f502bde4`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[4]::Expr

Source: `infra/tests/test_formal_workflow.py:51`; AST `d28ac68719a7a41737a49017d52051433457e79556da40d115d425ce9a548ead`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/receipts').exists, self.assertFalse.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:51`; AST `8fcfa757405412f3c887c575e826cbe1ab83231fe12d05b04b208e3795818a92`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/receipts').exists, self.assertFalse.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_binding_is_not_completion_and_source_edits_invalidate_it::root.body[10].body[4].body[4].value.args[0]::Call

Source: `infra/tests/test_formal_workflow.py:51`; AST `41767118fd744fc60b410f982e54d97eb52297457515aaea4d3c69f7394bf42c`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/receipts').exists.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:53`; AST `2202097db26b5a189552a7df0099ea64c5a9f95710487d7eacead019ca4b8066`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: copy, invalid, obligations, original, self. Outputs/bindings: invalid, obligations, original.
Calls/effect boundaries: copy.deepcopy, self.assertEqual, self.call, self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:54`; AST `e285634595a434322b08ca834b23a40f6df2355791b2b7454ac35406ed0fc693`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: original.
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:54`; AST `d7a0b9a566e8ae0a5665eb6c5955b5fe97f8e4074f53c7f85ef820a5b6fbe64b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[1]::Assign

Source: `infra/tests/test_formal_workflow.py:55`; AST `66b622e745fba057f09fad4be388e7b4b58887f50511d7056d1833136912aca1`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original. Outputs/bindings: invalid.
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2]::For

Source: `infra/tests/test_formal_workflow.py:56`; AST `de3df7aeec0e29590adb6b03ac30b7196f3b8c910303fdf4cfd3af4e61ffdd03`.

Rust module: `infra::tests::test_formal_workflow`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: copy, invalid, obligations, original, self. Outputs/bindings: obligations.
Calls/effect boundaries: copy.deepcopy, self.assertEqual, self.call, self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[10].body[5].body[2]; no call, error or mutation may be omitted. Iteration: obligations in invalid
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:57`; AST `201813af317d75e871f6f9093dc69d6a39c7dc9a8d755009a172d7acf07347cd`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, original, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:57`; AST `58dbe9858bb7ae5357f0eb8a891c20bcb06bea19387f8aac5280129333f24983`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, original. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[1]::Assign

Source: `infra/tests/test_formal_workflow.py:58`; AST `40ad9ee8802480a8eb59d3f02e8e16d9acbd0495bf47eff74703a6073901adee`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligations, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:59`; AST `5b63971998709a22375fdd3e0d8ad9a2a7b731c63b4788c3ca3f76acf191897c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:59`; AST `ad5f9d68373e57cd4d8f52cc8ff964706876674212a70aaa0b55df190c2343ec`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:60`; AST `dcbc88b1491b8b38811fbb0a230d2383bc5b9f56dd7cf0cc2bc3f2217fe43a89`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:60`; AST `f70b3c94fc6cb32dbbd49e5107d3653da45160988b253bdde2e4fb8e5e9c3039`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[2].body[3].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:60`; AST `3379b7f6759e8477c1d10fc882c7d6049d172a9937825c3fd63b9c1b99d627bc`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[3]::Assign

Source: `infra/tests/test_formal_workflow.py:61`; AST `201813af317d75e871f6f9093dc69d6a39c7dc9a8d755009a172d7acf07347cd`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, original, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:61`; AST `58dbe9858bb7ae5357f0eb8a891c20bcb06bea19387f8aac5280129333f24983`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, original. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[4]::Assign

Source: `infra/tests/test_formal_workflow.py:62`; AST `901298557d9ec4db2aa81811d4663cdcca7591767a343712c6bf59461edb2276`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[5]::Expr

Source: `infra/tests/test_formal_workflow.py:63`; AST `5b63971998709a22375fdd3e0d8ad9a2a7b731c63b4788c3ca3f76acf191897c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[5].value::Call

Source: `infra/tests/test_formal_workflow.py:63`; AST `ad5f9d68373e57cd4d8f52cc8ff964706876674212a70aaa0b55df190c2343ec`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[6]::Expr

Source: `infra/tests/test_formal_workflow.py:64`; AST `7fca5a2cddb6f9d5b7e8fd80b854540860f0a9230807ba593939c8bf3000122e`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[6].value::Call

Source: `infra/tests/test_formal_workflow.py:64`; AST `3379b7f6759e8477c1d10fc882c7d6049d172a9937825c3fd63b9c1b99d627bc`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[7]::Assign

Source: `infra/tests/test_formal_workflow.py:65`; AST `201813af317d75e871f6f9093dc69d6a39c7dc9a8d755009a172d7acf07347cd`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, original, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[7].value::Call

Source: `infra/tests/test_formal_workflow.py:65`; AST `58dbe9858bb7ae5357f0eb8a891c20bcb06bea19387f8aac5280129333f24983`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, original. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[8]::Assign

Source: `infra/tests/test_formal_workflow.py:66`; AST `f08f6d64eb80e300ec2a836601747bc950c31663ee8dc0ce1ee2031733c8d502`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[9]::Expr

Source: `infra/tests/test_formal_workflow.py:67`; AST `5b63971998709a22375fdd3e0d8ad9a2a7b731c63b4788c3ca3f76acf191897c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[9].value::Call

Source: `infra/tests/test_formal_workflow.py:67`; AST `ad5f9d68373e57cd4d8f52cc8ff964706876674212a70aaa0b55df190c2343ec`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[10]::Expr

Source: `infra/tests/test_formal_workflow.py:68`; AST `7fca5a2cddb6f9d5b7e8fd80b854540860f0a9230807ba593939c8bf3000122e`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_vacuous_duplicate_and_placeholder_contracts_are_rejected::root.body[10].body[5].body[10].value::Call

Source: `infra/tests/test_formal_workflow.py:68`; AST `3379b7f6759e8477c1d10fc882c7d6049d172a9937825c3fd63b9c1b99d627bc`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:70`; AST `ef32f7e98471f01c63028e90d197679585d828b42111fa956dc4fe2bc6c9b569`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, result, self, tool. Outputs/bindings: result, tool.
Calls/effect boundaries: Path, Path(tool).read_text, Path(tool).write_text, self.assertEqual, self.assertTrue, self.bind, self.call, self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:71`; AST `1f63c7e672b19c76a8569c33956fce72a626b810766fcc52b348724deba8a82d`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:71`; AST `551d090b4465eed836a5e228e2f7e3e616e4e211d7fd6ae3d14b1aa25946cead`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:72`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:72`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[2]::Assign

Source: `infra/tests/test_formal_workflow.py:73`; AST `14a09f1b6a38dd8d13f78cfae7ea9de75e10f48652b0ad7662006f438c99369e`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: result.
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:73`; AST `e4fe34a4063f4921d5cb8c7eb88b60bd90a9b0c44ea59eb2ae32b8d3451081a3`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:74`; AST `5b8d55bbae8035107d77205ea7efdc9425695cab4dfc576107caae37f83913c0`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:74`; AST `5b8fe76e0560ab9d53cb755c59654bac5d2ff410aa75d80fc59290c6a9e5be7a`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[4]::Expr

Source: `infra/tests/test_formal_workflow.py:75`; AST `75671656c2aa69dc1b9abde538261406cb1695eba043481c09ffdf7f7da16125`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:75`; AST `0e4b3d14ee5ec6bb4c4fefd3fd43866e3f23a3bfe5397430b855d31e4d9fd5e0`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[5]::Expr

Source: `infra/tests/test_formal_workflow.py:76`; AST `840946193bbf76f119272a841c851b712f8eada4ef9aed644a4a2ddc7b2a6d0e`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[5].value::Call

Source: `infra/tests/test_formal_workflow.py:76`; AST `1ce0a84adebb4ed63a470942ca378df7c31deded704ded90d654e031eca2a8ab`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[5].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:76`; AST `29b3ee6104b7a306f03de19402b21fdfae2b2914b0e8ce1d599be12184527e45`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[6]::Expr

Source: `infra/tests/test_formal_workflow.py:77`; AST `3981c28304884cc4f69bda8267d7df2eb1b400d603db533b09df72a6b067d49b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(tool).read_text, Path(tool).write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[6].value::Call

Source: `infra/tests/test_formal_workflow.py:77`; AST `845deed7d6a7523e429c7b3622d3781d8a5bab639c028f9119bc9425ce03a84d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(tool).read_text, Path(tool).write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[6].value.func.value::Call

Source: `infra/tests/test_formal_workflow.py:77`; AST `3ea79040f315c6637dc16546fcb32731826f1bbf7cf5bda63388327f48ffccca`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[6].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[6].value.args[0].left::Call

Source: `infra/tests/test_formal_workflow.py:77`; AST `79dad3e485f0084d35656e0e3d023d5b33ededbe82f3a8ada45f8c2a3820c529`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(tool).read_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[6].value.args[0].left.func.value::Call

Source: `infra/tests/test_formal_workflow.py:77`; AST `3ea79040f315c6637dc16546fcb32731826f1bbf7cf5bda63388327f48ffccca`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[6].value.args[0].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[7]::Expr

Source: `infra/tests/test_formal_workflow.py:78`; AST `64ceba765f067d7d929025877c534671e2a1ff7b3524c35e43f07966d8912a35`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[7].value::Call

Source: `infra/tests/test_formal_workflow.py:78`; AST `6fadbf52269bc8ab2b636362196dbf0e6599a899605668f80460aae5664e7cd8`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_exact_fresh_observation_audits_and_changed_tool_is_stale::root.body[10].body[6].body[7].value.args[0].value.value.value::Call

Source: `infra/tests/test_formal_workflow.py:78`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[7].value.args[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:80`; AST `e17de2a3c76318f99cd09a70736f63012b5d3071b9cbb3cd3bca5c6de2afc4fc`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self, tool. Outputs/bindings: tool.
Calls/effect boundaries: self.assertEqual, self.bind, self.call, self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:81`; AST `5dda217385d1606b9b71f1906bfec086b488fe197b4910d85fd450e808cec10a`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:81`; AST `a6fa3876b0447a863897495d1b1085e70fde500f92eac53b39768b546d6b6ecf`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:82`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:82`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:83`; AST `b4fde6dbd05aeacb4f862b4032cb9ab5174a93e80237b8b8ca85473f056ac057`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:83`; AST `72d12ae377752e8a1248533531f519706e69d3cbb8638b7c847442e05a1dda23`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[2].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:83`; AST `d41e6e26bdf9ba9ffff86e59ad5bd8fc40359f7b1d7055a379583710b763f227`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:84`; AST `8b3660aefe64250f5df0a41550d80ee5399915d93eee75243a35bda4ee10f2a9`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:84`; AST `84163c49eb28747ec85b10f14369795f2e08f7b2870baf9663d57db8ec287f00`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[3].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:84`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[4]::Assign

Source: `infra/tests/test_formal_workflow.py:85`; AST `6e733fafe73c6d7e12cc2a5d766571ea8c70427a229102638e66fd7b5b5d1084`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:85`; AST `9055882788e6bd67fa43cf034d5b19dbeef1649e9773eaa7072ec77596e23a70`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[5]::Expr

Source: `infra/tests/test_formal_workflow.py:86`; AST `a424ab0a067eec0695e6cdaea6214d993a9e7c03aa08814c53f3dda75e2332e0`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[5].value::Call

Source: `infra/tests/test_formal_workflow.py:86`; AST `c5c70ead057c7ee087618897f68630abfe75fa206c8dbbe72d7ade35bf1be66a`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[5].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:86`; AST `d41e6e26bdf9ba9ffff86e59ad5bd8fc40359f7b1d7055a379583710b763f227`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[6]::Assign

Source: `infra/tests/test_formal_workflow.py:87`; AST `728f581d0c80b800ead8e4bd010819b4eb1bef8e679c64bdb40b7ce5292ddab2`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[6].value::Call

Source: `infra/tests/test_formal_workflow.py:87`; AST `5d024c3fd60a0526c17284e7e3ab480b5abf843696fb0359b0e00cd15fac8ec9`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[7]::Expr

Source: `infra/tests/test_formal_workflow.py:88`; AST `a424ab0a067eec0695e6cdaea6214d993a9e7c03aa08814c53f3dda75e2332e0`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[7].value::Call

Source: `infra/tests/test_formal_workflow.py:88`; AST `c5c70ead057c7ee087618897f68630abfe75fa206c8dbbe72d7ade35bf1be66a`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[7].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:88`; AST `d41e6e26bdf9ba9ffff86e59ad5bd8fc40359f7b1d7055a379583710b763f227`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[7].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[8]::Expr

Source: `infra/tests/test_formal_workflow.py:89`; AST `8b3660aefe64250f5df0a41550d80ee5399915d93eee75243a35bda4ee10f2a9`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[8].value::Call

Source: `infra/tests/test_formal_workflow.py:89`; AST `84163c49eb28747ec85b10f14369795f2e08f7b2870baf9663d57db8ec287f00`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_wrong_count_and_mismatched_version_are_incomplete::root.body[10].body[7].body[8].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:89`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[8].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:91`; AST `0229389280ec578392c82402ff538a35273754117727d0d80f5d0da2f40e2f89`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, self, solver, tool. Outputs/bindings: solver, tool.
Calls/effect boundaries: Path, self.assertEqual, self.bind, self.call, self.verifier, solver.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:92`; AST `1f63c7e672b19c76a8569c33956fce72a626b810766fcc52b348724deba8a82d`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:92`; AST `551d090b4465eed836a5e228e2f7e3e616e4e211d7fd6ae3d14b1aa25946cead`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[1]::Assign

Source: `infra/tests/test_formal_workflow.py:93`; AST `f8cfb3797b12d8a395853555c4f282668a2ef27ccf585f4d4afcef2e83f15509`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, tool. Outputs/bindings: solver.
Calls/effect boundaries: Path.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[1].value.left.value::Call

Source: `infra/tests/test_formal_workflow.py:93`; AST `3ea79040f315c6637dc16546fcb32731826f1bbf7cf5bda63388327f48ffccca`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[1].value.left.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:94`; AST `600e9ffccef07129e5e544ee4ed82e4b6b76060647957caefe689074ce601bc1`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: solver. Outputs/bindings: (none).
Calls/effect boundaries: solver.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:94`; AST `cbe08a84503050e87153df0e96f4ae0f420f3fc5b83697bb642b649df3778741`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: solver. Outputs/bindings: (none).
Calls/effect boundaries: solver.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:95`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:95`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[4]::Expr

Source: `infra/tests/test_formal_workflow.py:96`; AST `b7597f104c6163f362016addb9233fa6a7e9766007e26813fe74c7026c6bb77c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:96`; AST `e4fe34a4063f4921d5cb8c7eb88b60bd90a9b0c44ea59eb2ae32b8d3451081a3`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[5]::Expr

Source: `infra/tests/test_formal_workflow.py:97`; AST `beca1f070f5d6dd0ccc22bf51e5801c31c3364e55b54705b7a8405a694a94530`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: solver. Outputs/bindings: (none).
Calls/effect boundaries: solver.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[5].value::Call

Source: `infra/tests/test_formal_workflow.py:97`; AST `374f5f1a995ecb724121d99bf3df0d389e118f66b0536c93ea992ce5f55ba428`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: solver. Outputs/bindings: (none).
Calls/effect boundaries: solver.write_text.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[6]::Expr

Source: `infra/tests/test_formal_workflow.py:98`; AST `91b5bd59703b7a716d5df12ec03ac3c79f8a7f02d152b683caa689bb948679bd`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[6].value::Call

Source: `infra/tests/test_formal_workflow.py:98`; AST `c6872b544e39f3b05af4034ff446ef4c95053e2246bb22b1c82fba1594cc7721`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_solver_behind_unchanged_verifier_is_stale::root.body[10].body[8].body[6].value.args[0].value.value.value::Call

Source: `infra/tests/test_formal_workflow.py:98`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[8].body[6].value.args[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:100`; AST `702f7b93de3c524aa316a3262ef90c65343c3700cb60a0d9b81069da5db143f0`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.bind, self.call, self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:101`; AST `100ca64b8aefc347ca12dfe031ff39eca37b2f0f6202f68475cf369e7c966570`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:101`; AST `57f6234076222574a08caee69de978f4cd6b1dd1122798aa09eb5aead356ccf8`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:102`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:102`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:103`; AST `4876f9709ab6b788563201a0aae7f427251ea215ef29c88c463cffa98afabbe6`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:103`; AST `725b5cc45a62f4212fd0c4edb37bc07125c108b03c977a3acbf7036674e3b009`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:104`; AST `e3afb580bf4c969f6a0c95d9d519a41c6f4528ba2ac699f15ab11a136aeebb5d`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:104`; AST `6ee3b4ce418a54dea40b15e0c87c9ac36d485a9be36ea3e6ea632a59d8f637f1`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_ignored_declared_proof_changes_invalidate_binding::root.body[10].body[9].body[3].value.args[1].value::Call

Source: `infra/tests/test_formal_workflow.py:104`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].body[3].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:106`; AST `2ddf2a2c416e55aafdd9ec6f5df50bed0b82e0c0b2ede335f9cc131a3b8e4753`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: os, patch, result, self, tool. Outputs/bindings: result, tool.
Calls/effect boundaries: patch.dict, self.assertEqual, self.bind, self.call, self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:107`; AST `1f63c7e672b19c76a8569c33956fce72a626b810766fcc52b348724deba8a82d`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:107`; AST `551d090b4465eed836a5e228e2f7e3e616e4e211d7fd6ae3d14b1aa25946cead`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:108`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:108`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:109`; AST `b7597f104c6163f362016addb9233fa6a7e9766007e26813fe74c7026c6bb77c`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:109`; AST `e4fe34a4063f4921d5cb8c7eb88b60bd90a9b0c44ea59eb2ae32b8d3451081a3`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[3]::With

Source: `infra/tests/test_formal_workflow.py:110`; AST `af3a7a844fd9dcabb6bb221aeed93914b87d89bebe74c23118e419ed54217079`.

Rust module: `infra::tests::test_formal_workflow`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: os, patch, self. Outputs/bindings: result.
Calls/effect boundaries: patch.dict, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[3].items[0].context_expr::Call

Source: `infra/tests/test_formal_workflow.py:110`; AST `3a012ade6743216e739ab322012315cec7e8bfdf2082019d813084d27c62605e`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.dict.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[10].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[3].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:111`; AST `c7c8064b5ac88428371e5181611b39debed92447ae2215e73180e74ce559f337`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[3].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:111`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[4]::Expr

Source: `infra/tests/test_formal_workflow.py:112`; AST `b1fcd6bfb48c4dea6cf20afcd5f8c8d6eb926643662bdc5af6e2882b528cf610`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_changed_compilation_environment_invalidates_observation::root.body[10].body[10].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:112`; AST `e120af19300c303c702e9aba79f99755f24611c78c8b19d55d6a64227df18739`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:114`; AST `fdee0d34ef4e02de669c9a4fba4bd98add44dbe4c89da7f5e1add0b0c9c5de72`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self, str, tool. Outputs/bindings: tool.
Calls/effect boundaries: self.assertIn, self.bind, self.call, self.verifier, str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:115`; AST `3859569e510ecf2ffc9081c8f00663d17b025b3a83453fca57558fd9af8e9ca9`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, str. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier, str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:115`; AST `a3063dc7412db85999d27cb5ee3b9f57a8729c10fda6566c4ec5088539e5935f`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier, str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[0].value.keywords[0].value.values[1].value::Call

Source: `infra/tests/test_formal_workflow.py:115`; AST `d484a53f6d8b3171b49d84a6e35e2cb3806cf4f5131a3101c0599b3111bbb823`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[0].value.keywords[0].value.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:116`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:116`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[2]::Expr

Source: `infra/tests/test_formal_workflow.py:117`; AST `bcbf65d891271a97b23a2d16bb1044bbc5fd653d4ab9609b31c2a69890c6319a`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:117`; AST `d7442a9f3af50b3159b834e790a34b569956180f0ad758a1dd9a18286e4ff32b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[2].value.args[1].value::Call

Source: `infra/tests/test_formal_workflow.py:117`; AST `d41e6e26bdf9ba9ffff86e59ad5bd8fc40359f7b1d7055a379583710b763f227`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[2].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[3]::Expr

Source: `infra/tests/test_formal_workflow.py:118`; AST `e3afb580bf4c969f6a0c95d9d519a41c6f4528ba2ac699f15ab11a136aeebb5d`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:118`; AST `6ee3b4ce418a54dea40b15e0c87c9ac36d485a9be36ea3e6ea632a59d8f637f1`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_success_output_does_not_hide_input_change_during_execution::root.body[10].body[11].body[3].value.args[1].value::Call

Source: `infra/tests/test_formal_workflow.py:118`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].body[3].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12]::FunctionDef

Source: `infra/tests/test_formal_workflow.py:120`; AST `862e8c4d0b8660cfdd23b4172e63e54b8079726842952e4dfe1eed76da55ec7e`.

Rust module: `infra::tests::test_formal_workflow`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: denied, exhausted, first, second, self, tool. Outputs/bindings: denied, exhausted, first, second, tool.
Calls/effect boundaries: self.assertEqual, self.assertIn, self.assertNotEqual, self.bind, self.call, self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[0]::Assign

Source: `infra/tests/test_formal_workflow.py:121`; AST `1f63c7e672b19c76a8569c33956fce72a626b810766fcc52b348724deba8a82d`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: tool.
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:121`; AST `551d090b4465eed836a5e228e2f7e3e616e4e211d7fd6ae3d14b1aa25946cead`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.verifier.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[1]::Expr

Source: `infra/tests/test_formal_workflow.py:122`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[1].value::Call

Source: `infra/tests/test_formal_workflow.py:122`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[2]::Assign

Source: `infra/tests/test_formal_workflow.py:123`; AST `b387e713b610aed29581df0393e9a480ea36a95004f154500be78410aec4e756`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: first.
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[2].value::Call

Source: `infra/tests/test_formal_workflow.py:123`; AST `e4fe34a4063f4921d5cb8c7eb88b60bd90a9b0c44ea59eb2ae32b8d3451081a3`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[3]::Assign

Source: `infra/tests/test_formal_workflow.py:124`; AST `79467a078fed037a5e4e10f6a5c38d0f12b240b4202ea842adeff0c2b0f3fd44`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: denied.
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[3].value::Call

Source: `infra/tests/test_formal_workflow.py:124`; AST `d41e6e26bdf9ba9ffff86e59ad5bd8fc40359f7b1d7055a379583710b763f227`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[4]::Expr

Source: `infra/tests/test_formal_workflow.py:125`; AST `40613ea76a677b078fa7db369349ed727f9150364f6fe70134f04b90a0499d5a`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: denied, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[4].value::Call

Source: `infra/tests/test_formal_workflow.py:125`; AST `ff4dad0273dd99582f944e8efa3eace63454af44b66ff09c5299f45a803a32e0`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: denied, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[5]::Assign

Source: `infra/tests/test_formal_workflow.py:126`; AST `17de627b051b19e7660b5acd8d1b84e03318bca4506d5806e58cf7083510fc29`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: second.
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[5].value::Call

Source: `infra/tests/test_formal_workflow.py:126`; AST `cecb67b201e57c8a2cfda25693ed363e8c65e818094f539c7b3993e71a94911e`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[6]::Expr

Source: `infra/tests/test_formal_workflow.py:127`; AST `c6469b40b67bd254f05c9ead997f789bd99cbf45c9cac55af15928be670b83e1`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[6].value::Call

Source: `infra/tests/test_formal_workflow.py:127`; AST `5695ed2d2a3171d9e17ea445b05674bedb09391d4d7557d36b75dad73a73a828`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[7]::Assign

Source: `infra/tests/test_formal_workflow.py:128`; AST `c4a29d036fcbc1a1047c76cacb49f525c511666d8dd89127233d74cbfce35b25`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tool. Outputs/bindings: exhausted.
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[7].value::Call

Source: `infra/tests/test_formal_workflow.py:128`; AST `2c7c2cf9eb642ab0ba271ad7512962973a6566816f6dcc09d8238252c175d6ec`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[8]::Expr

Source: `infra/tests/test_formal_workflow.py:129`; AST `5c08a2775ea160c6f3c0662e5514976f4059b8f664b3d2b866e21fe1935879f8`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exhausted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[8].value::Call

Source: `infra/tests/test_formal_workflow.py:129`; AST `4c4a35259458834203b621d46e53af7b4f906b2450072741168e6337da52d971`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exhausted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[9]::Expr

Source: `infra/tests/test_formal_workflow.py:130`; AST `8b3660aefe64250f5df0a41550d80ee5399915d93eee75243a35bda4ee10f2a9`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[9].value::Call

Source: `infra/tests/test_formal_workflow.py:130`; AST `84163c49eb28747ec85b10f14369795f2e08f7b2870baf9663d57db8ec287f00`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::TestFormalWorkflow::test_repeating_proof_needs_diagnosis_and_never_reuses_cache::root.body[10].body[12].body[9].value.args[0].value::Call

Source: `infra/tests/test_formal_workflow.py:130`; AST `6241737803dcf2c380c554b128a85e6073e06e4245a98006545632d5e7a5b30b`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].body[9].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[11]::If

Source: `infra/tests/test_formal_workflow.py:133`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_formal_workflow`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[11]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[11].body[0]::Expr

Source: `infra/tests/test_formal_workflow.py:134`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_formal_workflow`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_formal_workflow.py::module::root.body[11].body[0].value::Call

Source: `infra/tests/test_formal_workflow.py:134`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_formal_workflow`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: copy, hashlib, json, os, pathlib, sys, test_destiny, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
